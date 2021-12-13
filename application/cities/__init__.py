# coding: utf-8

from flask import Blueprint

bp_cities = Blueprint('cities', __name__)

from .cities import *
