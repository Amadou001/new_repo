#!/usr/bin/python3
"""Initiation of the home package"""

from flask import Blueprint
import os
import sys


base_path = os.path.dirname(__file__)
parent_path = os.path.abspath(os.path.join(base_path, '../../'))
sys.path.append(parent_path)

app_views_home = Blueprint('app_view_home', __name__,
                           url_prefix="/home",
                         template_folder='templates',
                         static_folder='../auth/static')

from home.home import *
