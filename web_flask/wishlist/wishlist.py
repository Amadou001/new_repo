#!/usr/bin/python3
"""
WISHLIST module
"""

from wishlist import app_views_wishlist
from wishlist import app_views_sell
from wishlist import app_views_rent
from flask import render_template, jsonify, request, flash, redirect, url_for
from flask_login import login_required, current_user
from models import storage
from models.user import User
from models.property import Property
from models.whishlist import Whishlist
import os


@login_required
@app_views_wishlist.route("/", methods=['GET'])
@app_views_sell.route("sell/", methods=['GET'])
@app_views_rent.route("rent/", methods=['GET'])
def wishlist():
    """Wishlist function"""

    property_attributes = []
    active_button = "wishlist"
    wishlist_type = ""

    if current_user.is_authenticated:
        user = storage.get_object(User, id=current_user.id)
        all_properties = []

        for property in user.whishlists:
            query = storage.get_object(Property,
                                       id=property.property_id)
            if request.path == "/wishlist/sell/":
                query = storage.get_object(Property,
                                           id=property.property_id,
                                           listing_type="sell")
                active_button = wishlist_type = "sell"
            elif request.path == "/wishlist/rent/":
                query = storage.get_object(Property,
                                           id=property.property_id,
                                           listing_type="rent")
                active_button = wishlist_type = "rent"
            if query is not None:
                all_properties.append(query)

        for property in all_properties:
            values = {
                'id': property.id,
                'title': property.title,
                'listing_type': property.listing_type,
                'address': f"""{property.address}, {property.city},
                {property.country}""",
                'price': property.price,
                'area': property.area,
                'bedrooms': property.bedrooms,
                'bathrooms': property.bathrooms,
                'picture_link': storage.get_image(property.id, "Main_image").image_url
                # find_image_path(property.id)
            }
            property_attributes.append(values)

        return render_template('wishlist.html',
                               property_attributes=property_attributes,
                               active_button=active_button,
                               wishlist_type=wishlist_type)
    else:
        return render_template('404.html')


def find_image_path(image_id):  # NO need
    """find image_path"""
    file_names = os.listdir("property/static/img/")
    extensions = [".png", ".jpg", ".jpeg", ".gif"]
    matching_files = [
        f for f in file_names
        if f.startswith(str(image_id) + '_p') and
        any(f.endswith(ext) for ext in extensions)
    ]
    if matching_files:
        return matching_files[0]


@app_views_wishlist.route('/delete_property/<string:property_id>',
                          methods=['DELETE'])
def delete_property(property_id):
    """Property deletion"""
    wishlist_property = storage.get_object(Whishlist, property_id=property_id)
    storage.delete(wishlist_property)
    storage.save()
    return jsonify({'success': 'Property correctly deleted'})


# Newly added
@app_views_wishlist.route('/add_to_wishlist/<property_id>')
def add_to_wishlist(property_id):
    """ Add a property to the wishlist"""
    new_record = Whishlist()
    new_record.user_id = current_user.id #Current User
    inside =  any(property_id in item for item in storage.all_wishlist_for_user(current_user.id))
    if not inside:
        new_record.property_id = property_id
        new_record.save()
        flash("Property successfully added to wishlist!", "success")
    else:
        flash("Property already in wishlist!", "error")
    return redirect(url_for('app_view_property.property_onclick', property_id=property_id))
