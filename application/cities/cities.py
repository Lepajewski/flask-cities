#coding: utf-8

from flask import render_template, url_for, redirect, request
from ..models import Cities
from . import bp_cities

@bp_cities.route('/')
def index():
    return render_template('index.html')

@bp_cities.route('/cities', methods=['GET', 'POST'])
def view_cities():
    if request.method == 'GET':
        cities_list = {i:Cities.get(Cities.id) for i in Cities.get(Cities.name)}
        return render_template('cities.html')
    else:
        try:
            city = Cities.create(name = request.form['name'])
            return render_template('cities.html')
        except:
            return render_template('cities.html', error=u'Błąd dodawania')
