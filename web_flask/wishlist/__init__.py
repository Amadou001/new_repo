#!/usr/bin/python3
"""init module"""
from flask import Blueprint
import os
import sys


app_views_wishlist = Blueprint('app_views_wishlist', __name__, url_prefix='/wishlist',
                           template_folder='templates',
                           static_folder='../auth/static')
app_views_sell = Blueprint('app_views_sell', __name__, url_prefix='/wishlist',
                           template_folder='templates',
                           static_folder='../auth/static')
app_views_rent = Blueprint('app_views_rent', __name__, url_prefix='/wishlist',
                           template_folder='templates',
                           static_folder='../auth/static')

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from wishlist.wishlist import *

