#coding: utf-8

from flask import render_template, url_for, redirect, request, json
from ..models import Cities
from . import bp_cities

@bp_cities.route('/')
def index():
    #co powinno znaleźć się w index.html? czy on w ogóle powinien być?
    return render_template('index.html')

@bp_cities.route('/cities', methods=['GET', 'POST'])
def view_cities():
    if request.method == 'GET':
        #czy lista miast powinna być wyświetlana tylko przy metodzie GET?
        cities = {}
        for x in Cities:
            cities[x.id] = x.name
        cities_json = json.dumps(cities, sort_keys=True)

        return render_template('cities.html', cities_list=cities_json)
    else:
        try:
            city = Cities.create(name = request.form['name'])
            return render_template('cities.html')
        except:
            return render_template('cities.html', error=u'Błąd dodawania')

#w jaki sposób zaimplementować metody PUT oraz DELETE?
#czy po podaniu id w url użytkownik powinien zostać poproszony o podanie nowej nazwy?
#czy podanie id powinno znaleźć się wyłącznie w url?
''' #TBU:
@bp_cities.route('/cities/<int:city_id>', methods=['GET', 'POST'])
def edit_city(city_id):
    try:
        city = Cities.select().where(Cities.id == city_id).get()
        city.name = request.form['name']
        city.save()
        return render_template('cities.html')
    except:
        return render_template('cities.html', error=u'Błąd aktualizacji')
'''

'''
@bp_cities.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    try:
        city = Cities.delete().where(Cities.id == city_id)
        city.execute()
        return render_template('cities.html')
    except:
        return render_template('cities.html', error=u'Błąd usuwania')
'''
