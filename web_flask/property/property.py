#!/usr/bin/python3
"""Property module"""

from property  import app_views_property
from flask import render_template, abort, request, jsonify
from models import storage
from models.property import Property
from models.property_image import Property_image
from flask_login import  current_user


@app_views_property.route("/description/<property_id>", methods = ["GET"])
def property_onclick(property_id):
    """When property clicked"""
    show_modal= request.args.get('show_modal')
    print(request.path)
    the_property = storage.get_property_by_id(property_id)
    if not the_property:
        abort(404, description="Bad request: Property not found")

    the_property_images = storage.get_image(property_id)
    property_dict = {}
    for image in the_property_images:
        property_dict[image.image_type] = image.image_url
    property_dict["title"] = the_property.title
    property_dict["description"] = the_property.description
    property_dict["price"] = the_property.price
    property_dict["listing_type"] = the_property.listing_type
    property_dict["id"] = property_id
    property_dict["property_owner"] = the_property.user_id
    property_dict["current_user"] = current_user.id

    return render_template("property.html", property=property_dict, window="property", show_modal=show_modal)



@app_views_property.route("/property_list")
def property_list():
    """Lists properties with pagination"""

    per_page = 3  # Number of properties per page
    property_type = request.args.get('type', None)
    if property_type not in ["apartment", "studio", "house", "villa"]:
        property_type = None
    country = request.args.get('country', None)
    city = request.args.get('city', None)
    max_price = request.args.get('max_price', None)
    min_price = request.args.get('min_price', None)
    feature = request.args.get('feature', None)
    total_properties = 0
    if country and city and property_type and max_price and min_price:
        # Get the total number of properties
        total_properties = storage.count(Property, property_type,
                                          country, city, max_price, min_price)
    
    elif feature == "rent":
        total_properties = storage.count(Property, listing_type="rent")
        print(total_properties)
    elif feature == "sell":
        total_properties = storage.count(Property, listing_type="sell")
        print(total_properties)
    else:
        # Get the total number of properties
        total_properties = storage.count(Property, property_type) 
    if per_page > total_properties:
        per_page = total_properties
    
    total_pages = 0
    if per_page != 0:
        total_pages = (total_properties + per_page - 1) // per_page  # Total pages required

    countries = storage.get_countries()

    return render_template('property_listing.html', 
                            countries=countries,
                            total_pages=total_pages, 
                            property_type=property_type, 
                            per_page=per_page, country=country,
                            city=city, max_price=max_price, 
                            min_price=min_price, feature=feature,
                            window="property", window2="list")
  

@app_views_property.route("/page_generation")
def page_generation():
    """ Returns a json of properties corresponding to the current request or page"""

    per_page = int(request.args['per_page'])  # Number of properties per page
    page = int(request.args.get('page', 1))  # Get current page from query parameters
    offset = (page - 1) * per_page
    property_type = request.args.get('property_type', None)
    country = request.args.get('country', None)
    city = request.args.get('city', None)
    max_price = request.args.get('max_price', None)
    min_price = request.args.get('min_price', None)
    feature = request.args.get('feature', None)
    if country == 'None':
        country = None
    if city == 'None':
        city = None
    if max_price == 'None':
        max_price = None
    if min_price == 'None':
        min_price = None
    if property_type not in ["apartment", "studio", "house", "villa"] or property_type == 'None':
        property_type = None
    if feature == 'None':
        feature = None

    # Query properties with limit and offset
    property_objs = storage.property_objs(per_page, offset, property_type, 
                                          country, city, max_price, 
                                          min_price, feature)

    property_list = []
    for obj in property_objs:
        # Retrieve property images and select the main image URL
        main_image_obj = storage.get_image(obj.id, "Main_image")
    
        
        # Append property details to the list
        property_list.append({
            "id": obj.id,
            "title": obj.title,
            "property_type": obj.property_type,
            "price": obj.price,
            "listing_type": obj.listing_type,
            "address": obj.address,
            "city": obj.city,
            "country": obj.country,
            "bedrooms": obj.bedrooms,
            "bathrooms": obj.bathrooms,
            "area": obj.area,
            "Main_image_url": main_image_obj.image_url
        })

    return jsonify({"properties": property_list}) 


@app_views_property.route("/property_types")
def property_types():
    """Property types"""

    Number_per_type ={"apartment": storage.count(Property, "apartment"), 
                      "villa": storage.count(Property, "villa"), 
                      "studio": storage.count(Property, "studio"),
                      "house":storage.count(Property, "house") }
    return render_template('property-type.html', Number_per_type=Number_per_type,
                            window="property", window2="type")


@app_views_property.route("/property_agents")
def property_agents():
    """Property agents"""
    agents = storage.get_agents()
    agents_list =[]
    for agent in agents:

        agents_list.append({"name": agent.agent_name, "image_url":agent.image_url.split('/')[3]}) # to improve
        print(agent.image_url.split('/')[3])

    return render_template("property-agent.html", agents=agents_list, window="property", window2="agent")


@app_views_property.route("/about")
def about():
    """About Page"""

    return render_template('about.html', window="about")
