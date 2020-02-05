from flask import Blueprint, Response, jsonify
from flask import render_template
from analysis import house as house_

house = Blueprint('house', __name__, url_prefix='/house')

@house.route('/')
def index():
    return render_template('house/index.html')

@house.route('/count_top10')
def count_top10():
    return render_template('house/count_top10.html', query=house_.count_top10())

@house.route('/type')
def type():
    return render_template('house/type.html', query=house_.type())

@house.route('/type.json')
def type_json():
    return jsonify(house_.type())

@house.route('/area')
def area():
    return render_template('house/area.html', query=house_.area())

@house.route('/area.json')
def area_json():
    return jsonify(house_.area())

@house.route('/rent')
def rent():
    return render_template('house/rent.html', query=house_.rent())
@house.route('/rent.json')
def rent_json():
    return jsonify(house_.rent())
