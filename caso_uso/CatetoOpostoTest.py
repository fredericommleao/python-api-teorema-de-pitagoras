"""
    Classe de teste para calcular a saída do metodo calculate da classe CatetoOpostoCalculo
    é utilizado o pytest para executar os testes
"""
from CatetoOpostoCalculo import CatetoOpostoCalculo

def test_calculate():
    cateto_oposto = CatetoOpostoCalculo()
    result = cateto_oposto.calculate(5,4)
    assert result == 3