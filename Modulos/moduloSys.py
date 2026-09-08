import sys

print(sys.version) #Exibe a versão do Python que está sendo usada para executar o código. Isso é útil para verificar a compatibilidade do código com diferentes versões do Python.
print(sys.platform) #Exibe o sistema operacional em que o código está sendo executado. Isso pode ser útil para adaptar o comportamento do código com base no sistema operacional.
print(sys.path) #Exibe a lista de diretórios onde o Python procura por módulos. Isso é importante para entender onde o Python está procurando por módulos e para garantir que os módulos personalizados estejam acessíveis.
print(sys.maxsize) #Exibe o valor máximo que um objeto pode ter em termos de tamanho. Isso é útil para entender as limitações de memória do Python e para evitar erros relacionados a objetos muito grandes.

print(type(sys.argv)) #Exibe o tipo da lista de argumentos passados para o script Python. Isso é útil para entender como o script foi executado e para acessar os argumentos fornecidos pelo usuário.
print(sys.argv) #Exibe a lista de argumentos passados para o script Python. O primeiro elemento (sys.argv[0]) é o nome do script, e os elementos subsequentes são os argumentos fornecidos pelo usuário. Isso é útil para criar scripts que podem aceitar parâmetros de entrada.
print(sys.argv[0]) #Exibe o nome do script Python que está sendo executado. Isso é útil para identificar o script em execução, especialmente quando o script é chamado a partir de outro script ou do terminal.
print(sys.argv[:1])