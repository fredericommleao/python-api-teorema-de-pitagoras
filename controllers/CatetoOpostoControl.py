import json

from flask import jsonify, request

from caso_uso.CatetoOpostoCalculo import CatetoOpostoCalculo


class CatetoOpostoRoute:
    def __init__(self):
        self.cateto_oposto_calculo = CatetoOpostoCalculo()

    def register2(self, app):
        @app.route("/cateto_oposto", methods=['POST'])
        def calculate2():
            data = json.loads(request.data)
            hipotenusa = data['hipotenusa']
            cateto_adjacente = data['cateto_adjacente']
            cateto_oposto = self.cateto_oposto_calculo.calculate(hipotenusa, cateto_adjacente)
            return jsonify({'cateto_oposto': cateto_oposto})