#!/usr/bin/python3
"""init module for property package"""

from flask import Blueprint
import os
import sys

base_path = os.path.dirname(__file__)
parent_path = os.path.abspath(os.path.join(base_path, '../../'))
sys.path.append(parent_path)

app_views_property = Blueprint("app_view_property", __name__, 
                               url_prefix="/property",
                                template_folder="templates", 
                                static_folder="../auth/static")


from property.property import *
