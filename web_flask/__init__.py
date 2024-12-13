#!/usr/bin/python3
"""init module"""
import os
import sys

base_path = os.path.dirname(__file__)
parent_path = os.path.abspath(os.path.join(base_path, '../../'))
sys.path.append(parent_path)