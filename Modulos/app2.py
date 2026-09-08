from humano import Pessoa
from humano import ErroIdadeInvalida

try:
    NOME = input("Digite o nome da pessoa: ")
    IDADE = int(input("Digite a idade da pessoa: "))
    pessoa1 = Pessoa(NOME, IDADE) #Criando um objeto da classe Pessoa utilizando o módulo humano (h) e passando os valores de nome e idade fornecidos pelo usuário
except ErroIdadeInvalida: #Capturando a exceção personalizada ErroIdadeInvalida que pode ser lançada se a idade fornecida for inválida
    if IDADE < 0:
        IDADE = abs(IDADE)
    pessoa1 = Pessoa(NOME, IDADE)
print(pessoa1)
del pessoa1