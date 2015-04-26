# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify
from flask import Response
from model import FakeDataBase
import json

app = Flask(__name__)
data = FakeDataBase(3)

@app.route("/")
def index():    
    return  "Resm is a simple resource manager that provides resources on demand.", 200

@app.route('/list', methods=['GET'])
def get_list():
    return jsonify({"allocated": data.get_allocated(), "deallocated": data.get_deallocated()}), 200

@app.route('/list/<owner>', methods=['GET'])
def get_list_by_user(owner):
    return json.dumps(data.get_allocated_by_user(owner)), 200

@app.route('/reset', methods=['GET'])
def reset():
    data.reset()
    return Response(status=204)
   
@app.errorhandler(404)
def bad_request(error):
    return "Bad request.", 400

@app.route('/allocate/<owner>', methods=['GET'])
def allocate_res(owner):
    res_name = data.allocate(owner)
    return (res_name, 201) if res_name is not None else ("Out of resources.", 503)

@app.route('/deallocate/<res_name>', methods=['GET'])
def deallocate_res(res_name):
    return Response(status=204) if data.deallocate(res_name) else ("Not allocated.", 404)


def run(number_of_res, port=5000):
    data.rescale(number_of_res)
    app.run(port=port) 