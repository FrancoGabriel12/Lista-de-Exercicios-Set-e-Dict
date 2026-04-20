#Exercicios de Set e Dicionário

#Criação de conjuntos e operações básicas

#Crie dois conjuntos, um chamado A e outro chamado B , com os seguintes elementos:
#A = {1, 2, 3, 4, 5}
#B = {4, 5, 6, 7, 8}
#Realize as seguintes operações e imprima os resultados:
#União de A e B
#Interseção de A e B
#Diferença de A e B (elementos que estão em A mas não em B
#Diferença de B e A (elementos que estão em B mas não em A)
#Verificar se A é um subconjunto de B
#Verificar se B é um subconjunto de A

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("União de A e B:", a | b) # União de A e B
print("Interseção de A e B:", a & b) # Interseção de A e B
print("Diferença de A e B:", a - b) # Diferença de A e B
print("Diferença de B e A:", b - a) # Diferença de B e A
print("A é subconjunto de B?", a.issubset(b)) # Verificar se A é um subconjunto de B
print("B é subconjunto de A?", b.issubset(a)) # Verificar se B é um subconjunto de A

#Remover duplicatas de uma lista usando conjuntos

#Crie uma lista com elementos duplicados, por exemplo:
#lista = [1, 2, 2, 3, 4, 4, 5]
#Use um conjunto para remover os elementos duplicados e imprima a nova lista sem duplicatas.

lista = [1, 2, 2, 3, 4, 4, 5]
conjunto = set(lista) # Converte a lista em um conjunto para remover duplicatas
nova_lista = list(conjunto) # Converte o conjunto de volta para uma lista
print("Lista sem duplicatas:", nova_lista)

#Conjunto com Strings
#Crie um conjunto de strings com os seguintes elementos:
#frutas = {"maçã", "banana", "laranja", "uva", "maçã"}
#Exiba o conjunto de palavras sem duplicatas.
#Verifique se a palavra "laranja" está presente no conjunto.
#Adicione a palavra "abacaxi" ao conjunto.
#Remova a palavra "uva" do conjunto.

frutas = {"maçã", "banana", "laranja", "uva", "maçã"} # Cria um conjunto de strings, onde a palavra "maçã" é duplicada, mas o conjunto irá armazenar apenas uma ocorrência, conjunto não guarda as posições dos elementos, ou seja, não mantém a ordem de inserção. Portanto, a ordem dos elementos no conjunto pode ser diferente da ordem em que foram adicionados.
print("Conjunto de frutas sem duplicatas:", frutas) # Exibe o conjunto de palavras sem duplicatas
print("A palavra 'laranja' está presente?", "laranja" in frutas) # Verifica se a palavra "laranja" está presente no conjunto
frutas.add("abacaxi") # Adiciona a palavra "abacaxi" ao conjunto
print("Conjunto de frutas após adicionar 'abacaxi':", frutas) # Exibe o conjunto após adicionar "abacaxi"
frutas.remove("uva") # Remove a palavra "uva"
print("Conjunto de frutas após remover 'uva':", frutas) # Exibe o conjunto após remover "uva"

#Contagem de elementos com dicionário
# Dada uma lista de nomes
#nomes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]

#Escreva um programa que conte a frequência de cada nome na lista e armazene essa
#contagem em um dicionário. O resultado deve ser algo assim:

#{
# "Ana": 3,
# "Carlos": 3,
# "João": 1
#}

nomes = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
contagem = {} # Cria um dicionário vazio para armazenar a contagem de nomes
for nome in nomes: # Itera sobre cada nome na lista de nomes
    if nome in contagem: # Verifica se o nome já está no dicionário de contagem
        contagem[nome] += 1 # Se estiver, incrementa a contagem do nome
    else:
        contagem[nome] = 1 # Se não estiver, adiciona o nome ao dicionário com contagem inicial de 1
print("Contagem de nomes:", contagem) # Exibe o dicionário com a contagem de cada nome

#Dicionario de notas
#Temos um dicionario que armazena as notas de um grupo de alunos

#notas = {
# "Alice": [85, 90, 78],
# "Bob": [92, 88, 95],
# "Charlie": [78, 82, 80],
# "Diana": [90, 85, 92]
#}

#Exiba a média de notas de cada aluno.
#Adicione um novo aluno, "Diana", com as notas [7, 8, 6] .
#Remova o aluno "Bob" do dicionário.

notas = {
 "Alice": [85, 90, 78],
 "Bob": [92, 88, 95],
 "Charlie": [78, 82, 80]
}

for aluno, notas_aluno in notas.items(): # Itera sobre cada aluno e suas respectivas notas no dicionário de notas
    media = sum(notas_aluno) / len(notas_aluno) # Calcula a média das notas do aluno
    print(f"Média de {aluno}: {media:.2f}") # Exibe a média de cada aluno formatada com 2 casas decimais
notas["Diana"] = [7, 8, 6] # Adiciona um novo aluno "Diana" com as notas [7, 8, 6]
print("Dicionário de notas após adicionar Diana:", notas) # Exibe o dicionário de notas após adicionar Diana
del notas["Bob"] # Remove o aluno "Bob" do dicionário
print("Dicionário de notas após remover Bob:", notas) # Exibe o dicionário de notas após remover Bob

#Inverso de dicionário
#Dado o seguinte dicionário

#frutas = {
# "maçã": "vermelha",
# "banana": "amarela",
# "laranja": "laranja",
# "uva": "roxa"
#}

#Crie um novo dicionário onde as chaves sejam as cores e os valores sejam as frutas correspondentes. O resultado deve ser algo assim:   
#{
# "vermelha": "maçã",
# "amarela": "banana",
# "laranja": "laranja",
# "roxa": "uva"
#}

frutas = {
 "maçã": "vermelha",
 "banana": "amarela",
 "laranja": "laranja",
 "uva": "roxa"
}

inverso = {cor: fruta for fruta, cor in frutas.items()} # Cria um novo dicionário usando compreensão de dicionário, onde as chaves são as cores e os valores são as frutas correspondentes
print("Dicionário inverso (cores como chaves):", inverso) # Exibe o dicionário inverso com as cores como chaves e as frutas como valores

#Conjunto a partir de uma tupla
#Dada a seguinte tupla
#numeros = (1, 2, 3, 4, 5, 2, 3, 1)
#Converta a tupla em um conjunto e exiba o conjunto resultante. Depois, adicione o número 7 ao conjunto e exiba novamente o conjunto.
numeros = (1, 2, 3, 4, 5, 2, 3, 1)
conjunto_numeros = set(numeros) # Converte a tupla em um conjunto para remover os números duplicados
print("Conjunto resultante:", conjunto_numeros) # Exibe o conjunto resultante
conjunto_numeros.add(7) # Adiciona o número 7 ao conjunto
print("Conjunto após adicionar o número 7:", conjunto_numeros) # Exibe o conjunto após adicionar o número 7

#Mesclar dicionários
#Dado os seguintes dicionários
#dict1 = {"a": 1, "b": 2, "c": 3}
#dict2 = {"b": 4, "e": 5, "f": 6}
#Escreva um código que mescle os dois dicionários, de forma que os valores de chaves duplicadas sejam somados. O resultado deve ser:
#{
# "a": 1,
# "b": 6,
# "c": 3,
# "e": 5,
# "f": 6 
#}
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "e": 5, "f": 6}
mesclado = dict1.copy() # Cria uma cópia do primeiro dicionário para começar a mesclagem
for chave, valor in dict2.items(): # Itera sobre cada chave e valor do segundo dicionário
    if chave in mesclado: # Verifica se a chave já existe no dicionário mesclado
        mesclado[chave] += valor # Se existir, soma o valor ao valor existente
    else:
        mesclado[chave] = valor # Se não existir, adiciona a chave e o valor ao dicionário mesclado
print("Dicionário mesclado:", mesclado) # Exibe o dicionário resultante da mesclagem, onde os valores de chaves duplicadas foram somados

#Operações com dicionarios de produtos
#Consire o seguinte dicionário de produtos e seus preços
#produtos = {
# "arroz": 5.99,
# "feijão": 7.99,
# "macarrão": 3.50,
#}

#Exiba o preço do "feijão".
#Adicione um novo produto chamado "azeite" com preço 15.99 .
#Atualize o preço do "macarrão" para 4.00 .
#Remova o produto "arroz" do dicionário.

produtos = {
 "arroz": 5.99,
 "feijão": 7.99,
 "macarrão": 3.50,
}
print("Preço do feijão:", produtos["feijão"]) # Exibe o preço do "feijão"
produtos["azeite"] = 15.99 # Adiciona um novo produto "azeite" com preço 15.99
print("Dicionário de produtos após adicionar azeite:", produtos) # Exibe o dicionário de produtos após adicionar azeite
produtos["macarrão"] = 4.00 # Atualiza o preço do "macarrão" para 4.00
print("Dicionário de produtos após atualizar o preço do macarrão:", produtos) # Exibe o dicionário de produtos após atualizar o preço do macarrão
del produtos["arroz"] # Remove o produto "arroz" do dicionário
print("Dicionário de produtos após remover arroz:", produtos) # Exibe o dicionário de produtos após remover arroz

#Intersecção de conjuntos a partir de listas
#Dadas as seguintes listas de números
#lista1 = [1, 2, 3, 4, 5]
#lista2 = [4, 5, 6, 7, 8]

#Converta ambas as listas para conjuntos e exiba a interseção entre elas.

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
conjunto1 = set(lista1) # Converte a primeira lista em um conjunto
conjunto2 = set(lista2) # Converte a segunda lista em um conjunto
intersecao = conjunto1 & conjunto2 # Calcula a interseção entre os dois conjuntos
print("Interseção entre os conjuntos:", intersecao) # Exibe a interseção entre os conjuntos, que contém os elementos comuns a ambos os conjuntos (neste caso, 4 e 5)

#Dicinario com tuplas como valores

#Crie um dicionário que armazena informações sobre diferentes cidades e suas coordenadas(latitude e longitude):

#cidades = {
# "São Paulo": (-23.5505, -46.6333),
# "Rio de Janeiro": (-22.9068, -43.1729),
# "Brasília": (-15.8267, -47.9218)
#}

#Adicione uma nova cidade, "Salvador", com coordenadas (-12.9714, -38.5014) .
#Exiba as coordenadas de "Brasília".
#Remova "Rio de Janeiro" do dicionário.

cidades = {
 "São Paulo": (-23.5505, -46.6333),
 "Rio de Janeiro": (-22.9068, -43.1729),
 "Brasília": (-15.8267, -47.9218)
}
cidades["Salvador"] = (-12.9714, -38.5014) # Adiciona uma nova cidade "Salvador" com coordenadas (-12.9714, -38.5014)
print("Dicionário de cidades após adicionar Salvador:", cidades) # Exibe o dicionário de cidades após adicionar Salvador
print("Coordenadas de Brasília:", cidades["Brasília"]) # Exibe as coordenadas de "Brasília"
del cidades["Rio de Janeiro"] # Remove "Rio de Janeiro" do dicionário
print("Dicionário de cidades após remover Rio de Janeiro:", cidades) # Exibe o dicionário de cidades após remover Rio de Janeiro

#Contagem de ocorrencias em uma lista de tuplas

#Dada a lista de tuplas contendo nomes e idades:

#pessoas = [("Ana", 20), ("Carlos", 30), ("Ana", 25), ("João", 30), ("Carlos", 35)]

#Crie um dicionário que armazena quantas vezes cada nome aparece na lista. O resultado deve ser algo assim:

#{
# "Ana": 2,
# "Carlos": 2,
# "João": 1
#}

pessoas = [("Ana", 20), ("Carlos", 30), ("Ana", 25), ("João", 30), ("Carlos", 35)]
contagem_nomes = {} # Cria um dicionário vazio para armazenar a contagem de nomes
for nome, idade in pessoas: # Itera sobre cada tupla na lista de pessoas, onde nome e idade são os elementos da tupla
    if nome in contagem_nomes: # Verifica se o nome já está no dicionário de contagem
        contagem_nomes[nome] += 1 # Se estiver, incrementa a contagem do nome
    else:
        contagem_nomes[nome] = 1 # Se não estiver, adiciona o nome ao dicionário com contagem inicial de 1
print("Contagem de nomes:", contagem_nomes) # Exibe o dicionário com a contagem de cada nome, onde as chaves são os nomes e os valores são a quantidade de vezes que cada nome aparece na lista de tuplas
