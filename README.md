# API feita para a calculadora do teorema de pitagoras
No desenvolvimento dessa api, eu escolhi o flask por ser mais prático e aparentemente mais tranquilo
do que o Jdango.

Na organização do projeto eu tentei seguir o primeiro principio do SOLID, estabelecendo classes com responsabilidades unicas
além do pytest para as classes de teste, os endpoints foram testados também no postman.

O projeto possui 2 pacotes principais 

1 - caso_uso // nesse pacote estão presente as classes responsáveis por fazer o calculo do teorema de pitagoras
e classes de testes unitários para validar o resultado processado pelas classes de calculo

2 - controllers // nesse pacote estão presente as classes responsáveis pelas rotas utilizadas nos endpoits

e no diretorio raiz, está presente o arquivo main.py que é responsável pela inicialização do servidor

###Endpoints:

abaixo segue exemplos de como utilizar os endpoints da aplicação:


##http://127.0.0.1:5000/hipotenusa
{
    "cateto_oposto": 25,
    "cateto_adjacente": 33
}


##http://127.0.0.1:5000/cateto_oposto
{
    "hipotenusa": 7,
    "cateto_adjacente": 6
}


##http://127.0.0.1:5000/cateto_adjacente
{
    "hipotenusa": 45,
    "cateto_oposto": 4
}
