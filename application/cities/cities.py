#coding: utf-8

from flask import render_template, url_for, redirect, request
from ..models import Cities
from . import bp_cities

@bp_cities.route('/')
def index():
    return render_template('index.html')

@bp_cities.route('/cities', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
