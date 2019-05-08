from __future__ import print_function
from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Resource, Api
import json


app = Flask(__name__)


nodos = {
        "nodo1":8,
        "nodo2":3,
        "nodo3":6,
        "nodo4":1,
        "nodo5":10,
        "nodo6":14,
        "nodo7":13,
        "nodo8":4,
        "nodo9":7
    }

nodosHijos = {
    "raiz":8,
    "nodo1":6,
    "nodo2":1
}
#Decorador
@app.route('/', methods=['GET'])
def get_nodos():
    return jsonify(nodos)

#Decorador
@app.route('/nodosancestro', methods=['GET'])
def get_hijos():
    return jsonify(nodosHijos)

#Correr la aplicación

if __name__ == '__main__':
    app.run(debug=True)

