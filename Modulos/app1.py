from humano import * #importando tudo do módulo humano para que possamos usar as classes e exceções definidas nele sem precisar do prefixo "h." #Isso é útil para evitar a necessidade de escrever "h.Pessoa" ou "h.ErroIdadeInvalida" toda vez que quisermos usar essas classes ou exceções. No entanto, é importante ter cuidado ao usar "import *" para evitar conflitos de nomes e garantir que o código seja claro e legível.

try:
    NOME = input("Digite o nome da pessoa: ")
    IDADE = int(input("Digite a idade da pessoa: "))
    pessoa1 = Pessoa(NOME, IDADE)
except ErroIdadeInvalida:
    if IDADE < 0:
        IDADE = abs(IDADE)
    pessoa1 = Pessoa(NOME, IDADE)
print(pessoa1)