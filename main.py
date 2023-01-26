#classe responsável pela inicialização do servidor flask, e também pela inicialização das rotas
#cria uma instância de cada rota e registra no servidor flask
#o servidor flask é inicializado na porta 5000
#o servidor flask é inicializado com o CORS habilitado para a porta 3000

from flask import Flask
from flask_cors import CORS
from controllers.CatetoAdjacenteControl import CatetoAdjacenteRote
from controllers.CatetoOpostoControl import CatetoOpostoRoute
from controllers.HipotenusaControl import HipotenusaRoute

class main:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app, resources={r"/*": {"origins": "http://localhost:3000"}},
             allow_headers=["Content-Type", "Authorization", "Access-Control-Allow-Credentials"], 
             supports_credentials=True)
        self.cateto_adjacente_route = CatetoAdjacenteRote()
        self.cateto_oposto_route = CatetoOpostoRoute()
        self.hipotenusa_route = HipotenusaRoute()
        
    def run(self):
        @self.app.route("/")
        def hello():
            return "Hello, World!"
        
        self.cateto_oposto_route.register2(self.app)
        self.hipotenusa_route.register3(self.app)
        self.cateto_adjacente_route.register1(self.app)
        self.app.run()

if __name__ == "__main__":
    main = main()
    main.run()
