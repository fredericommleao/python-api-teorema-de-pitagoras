"""
    Classe de teste para calcular a saída do metodo calculate da classe HipotenusaCalculo
    é utilizado o pytest para executar os testes
"""
from HipotenusaCalculo import HipotenusaCalculo

def test_calculate():
    hipotenusa = HipotenusaCalculo()
    result = hipotenusa.calculate(5,4)
    assert result == 6.4031242374328485