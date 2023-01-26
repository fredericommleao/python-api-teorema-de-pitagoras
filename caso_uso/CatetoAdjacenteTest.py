"""
    Classe de teste para calcular a saída do metodo calculate da classe CatetoAdjacenteCalculo
    é utilizado o pytest para executar os testes
"""
from CatetoAdjacenteCalculo import CatetoAdjacenteCalculo


def test_calculate():
    cateto_adjacente = CatetoAdjacenteCalculo()
    result = cateto_adjacente.calculate(5,4)
    assert result == 3
