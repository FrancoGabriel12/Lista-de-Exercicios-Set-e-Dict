import humano as h #importando o módulo humano e dando a ele o apelido de h para facilitar a escrita do código

try:
    NOME = input("Digite o nome da pessoa: ")
    IDADE = int(input("Digite a idade da pessoa: "))
    pessoa1 = h.Pessoa(NOME, IDADE) #Criando um objeto da classe Pessoa utilizando o módulo humano (h) e passando os valores de nome e idade fornecidos pelo usuário
except h.ErroIdadeInvalida: #Capturando a exceção personalizada ErroIdadeInvalida que pode ser lançada se a idade fornecida for inválida
    if IDADE < 0:
        IDADE = abs(IDADE)
    pessoa1 = h.Pessoa(NOME, IDADE)
print(pessoa1)
del pessoa1
#print(h._MAX_IDADE) #Acessando a variável _MAX_IDADE do módulo humano (h) para exibir o valor máximo permitido para a idade. Isso demonstra como podemos acessar variáveis definidas em um módulo usando o prefixo do módulo.