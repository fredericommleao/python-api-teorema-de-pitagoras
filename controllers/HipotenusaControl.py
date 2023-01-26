import json
from flask import jsonify, request
from caso_uso.HipotenusaCalculo import HipotenusaCalculo


class HipotenusaRoute:
    
    def __init__(self):
        self.hipotenusa_calculo = HipotenusaCalculo()

    def register3(self, app):
        @app.route("/hipotenusa", methods=['POST'])
        def calculate3():
            data = json.loads(request.data)
            cateto_oposto = data['cateto_oposto']
            cateto_adjacente = data['cateto_adjacente']
            hipotenusa = self.hipotenusa_calculo.calculate(cateto_oposto, cateto_adjacente)
            return jsonify({'hipotenusa': hipotenusa})