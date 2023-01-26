import json
from flask import jsonify, request
from caso_uso.CatetoAdjacenteCalculo import CatetoAdjacenteCalculo


class CatetoAdjacenteRote:
    def __init__(self):
        self.cateto_adjacente_calculo = CatetoAdjacenteCalculo()

    def register1(self, app):
        @app.route("/cateto_adjacente", methods=['POST'])
        def calculate1():
            
            data = json.loads(request.data)
            hipotenusa = data['hipotenusa']
            cateto_oposto = data['cateto_oposto']
            cateto_adjacente = self.cateto_adjacente_calculo.calculate(hipotenusa, cateto_oposto)
            return jsonify({'cateto_adjacente': cateto_adjacente})