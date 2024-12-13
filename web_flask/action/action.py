#!/usr/bin/python3

"""Action module"""

from action import app_views_action
from flask import render_template, url_for, request, redirect, flash
import os
from werkzeug.utils import secure_filename
from flask import current_app
from models.property import Property
from models.property_image import Property_image
from flask_login import login_required, current_user
from models.user import User
from models import storage


@login_required
@app_views_action.route('/upload_property', methods=['POST'])
def upload_property():
    """upload a property"""

    upload_folder = current_app.config['UPLOAD_FOLDER']
    os.makedirs(upload_folder, exist_ok=True)

    # Collecting basic property data
    new_property = Property()
    new_property.user_id = current_user.id # current user
    new_property.title = request.form.get('title')
    new_property.description = request.form.get('description')
    new_property.property_type = request.form.get('propertyType')
    new_property.price = request.form.get('price', type=float)
    if new_property.price < 0 or new_property.price is None:
        new_property.price = 0
    new_property.listing_type = request.form.get('listing_type')
    new_property.address = request.form.get('address')
    new_property.city = request.form.get('city')
    new_property.state = request.form.get('state')
    new_property.country = request.form.get('country')
    new_property.zip_code = request.form.get('zipCode')
    new_property.bedrooms = request.form.get('bedrooms', type=int)
    if new_property.bedrooms < 0 or new_property.bedrooms is None:
        new_property.bedrooms = 0
    new_property.bathrooms = request.form.get('bathrooms', type=int)
    if new_property.bathrooms < 0 or new_property.bathrooms is None:
        new_property.bathrooms = 0
    new_property.area = request.form.get('area', type=float)
    if new_property.area < 0 or new_property.area is None:
        new_property.area = 0
    
    new_property.save()

    # Collect additional images and descriptions
    main_image = request.files.get('mainImage')
    additional_images = request.files.getlist('additionalImages')
    additional_descriptions = request.form.getlist('additionalDescriptions')

    # Save the main image
    if main_image:
        new_image = Property_image()

        image_extension = os.path.splitext(main_image.filename)[1]
        main_image_filename = secure_filename(f"{new_property.id}_Main_image{image_extension}")
        main_image_path = os.path.join(upload_folder, main_image_filename)
        main_image.save(main_image_path)

        new_image.image_type = "Main_image"
        new_image.image_url = main_image_path
        new_image.property_id = new_property.id
        new_image.save()

    # Ensure additional_images and additional_descriptions have matching lengths
    if len(additional_images) == len(additional_descriptions):
        # Save each additional image with its description
        for i in range(len(additional_images)):
            image = additional_images[i]
            if image and image.filename:  # Ensure the image is not empty
                #get the image extension
                image_extension = os.path.splitext(image.filename)[1]
                description_safe = secure_filename(additional_descriptions[i])
                image_filename = f"{new_property.id}_{description_safe}{image_extension}"
                image_path = os.path.join(upload_folder, image_filename)
                image.save(image_path)

                # Save the additional image data
                new_image = Property_image()
                new_image.image_type = additional_descriptions[i]
                new_image.image_url = image_path
                new_image.property_id = new_property.id
                new_image.save()
    else:
        # Handle mismatch between image and description counts if necessary
        flash("Mismatch between additional images and descriptions!", 'error')

    flash("Property added successfully!", 'success')
    return redirect(url_for('app_view_action.my_properties', listing_type="featured"))

@login_required
@app_views_action.route('/my_properties/<listing_type>')
def my_properties(listing_type):
    """View properties of current user(supplier)"""

    feature = ""
    property_objs = None
    if listing_type == "sell":
        property_objs = storage.get_property_by_user_id(current_user.id, "sell")  #Current user
        feature = "sell"
    elif listing_type == "rent":
        feature = "rent"
        property_objs = storage.get_property_by_user_id(current_user.id, "rent")
    else:
        property_objs = storage.get_property_by_user_id(current_user.id)
        feature ="featured"
    property_list = []
    
    for obj in property_objs:
    
        Main_image_obj = storage.get_image(obj.id, "Main_image")

        property_list.append({"id": obj.id, "title": obj.title, 
                              "property_type": obj.property_type, 
                              "price": obj.price, "listing_type": obj.listing_type,
                              "address": obj.address, "city": obj.city, 
                              "country": obj.country, "bedrooms": obj.bedrooms, 
                              "bathrooms": obj.bathrooms, "area": obj.area, 
                              "Main_image_url": Main_image_obj.image_url})
        print(len(property_list))

    return render_template('my_properties.html', properties=property_list, feature=feature, window="action")

@login_required
@app_views_action.route("/delete_property/<property_id>")
def delete_property(property_id):
    """
    Delete property in my properties
    """
    storage.delete_property_by_id(property_id)

    upload_folder = current_app.config['UPLOAD_FOLDER']
    try:
        # Loop through all files in the folder
        for filename in os.listdir(upload_folder):
            if filename.startswith(property_id):  # Match files starting with the property_id
                file_path = os.path.join(upload_folder, filename)  # Build the full file path
                os.remove(file_path)  # Delete the file
        flash("Property deleted successfully!", "success")
    except Exception as e:
        flash("Error occurred during deletion!", "error")
        print(f"An error occurred: {e}")
    return redirect(url_for('app_view_action.my_properties', listing_type="featured"))
