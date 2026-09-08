class ErroIdadeInvalida(Exception):
    """"Classe de erro pra idade invalida"""
    def __init__(self, dado):
        self.__valor = dado
    def __str__(self):
        return "ErroIdadeInvalida: (" + str(self.__valor) + ") Idade deve ser um número inteiro entre 0 e 120"
_MAX_IDADE = 120

#Utilizando Property
class Pessoa:
    """
    Exemplo de classe que armazena
    nome de pessoas e idade
    """

    def __init__(self, nome, idade): #nome do argumento do método
        self.nome = nome #atributo
        self.idade = idade

    def __str__(self):
        return self.nome + " possui " + str(self.idade) + " anos"
    
    @property
    def nome(self):
        print("getter")
        return self.__nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor
        print("setter")
    @nome.deleter
    def nome(self):
        print("deleter")
        del self.__nome
    
    def set_idade(self, valor):
        if isinstance(valor, int) and (valor > 0) and (valor < _MAX_IDADE): #Usando a função MAX_IDADE para validar a idade, garantindo que seja um número inteiro positivo e menor que 120. Isso ajuda a evitar erros e garantir que os dados sejam consistentes.
            self.__idade = valor
            print("setter")
        else:
            raise ErroIdadeInvalida(valor) #Lança a exceção personalizada ErroIdadeInvalida, passando o valor inválido como argumento. Isso permitirá que a mensagem de erro personalizada seja exibida quando a exceção for capturada.

    def get_idade(self):
        print("getter")
        return self.__idade
    
    idade = property(get_idade, set_idade, doc = "Propriedade para o atributo idade")
    
    def aniversario(self):
        self.idade+=1

try:
    NOME = input("Digite o nome da pessoa: ")
    IDADE = int(input("Digite a idade da pessoa: "))
    pessoa1 = Pessoa(NOME, IDADE)
except ErroIdadeInvalida:
    if IDADE < 0:
        IDADE = abs(IDADE)
    pessoa1 = Pessoa(NOME, IDADE)
print(pessoa1)

