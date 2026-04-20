Exercícios de Estruturas de Dados - 2
Programação Orientada a Dados
Prof. Me. Otávio Parraga
1. Criação de Conjuntos e Operações Básicas
Crie dois conjuntos, um chamado A e outro chamado B , com os seguintes elementos:
Agora, faça o seguinte:
2. Remover Duplicatas de uma Lista
Dada a lista:
Use um conjunto para remover os elementos duplicados e retorne a lista sem repetições.
3. Conjuntos com Strings
Crie um conjunto com as seguintes palavras:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
Exiba a união entre os dois conjuntos.
Exiba a interseção entre os dois conjuntos.
Exiba a diferença entre A e B .
Verifique se A é um subconjunto de B .
numeros = [1, 2, 3, 2, 1, 4, 5, 6, 5, 4]
palavras = ["maçã", "banana", "laranja", "maçã", "uva", "banana"]
Agora, faça o seguinte:
4. Contagem de Elementos com Dicionário
Dada a lista de nomes:
Escreva um programa que conte a frequência de cada nome na lista e armazene essa
contagem em um dicionário. O resultado deve ser algo assim:
5. Dicionário de Notas
Você tem o seguinte dicionário que armazena as notas de um grupo de alunos:
Faça o seguinte:
Exiba o conjunto de palavras sem duplicatas.
Verifique se a palavra "laranja" está presente no conjunto.
Adicione a palavra "abacaxi" ao conjunto.
Remova a palavra "uva" do conjunto.
nomes = ["Ana", "Carlos", "Ana", "João", "Carlos", "Carlos", "Ana"]
{
 "Ana": 3,
 "Carlos": 3,
 "João": 1
}
notas = {
 "Alice": [8, 7, 9],
 "Bob": [6, 8, 7],
 "Carlos": [9, 9, 8],
}
Exiba a média de notas de cada aluno.
Adicione um novo aluno, "Diana", com as notas [7, 8, 6] .
Remova o aluno "Bob" do dicionário.
6. Inverter Dicionário
Dado o seguinte dicionário:
Inverta o dicionário, de forma que as cores sejam as chaves e as frutas sejam os valores,
resultando em algo como:
7. Conjuntos a partir de Tuplas
Dada a seguinte tupla de números:
Converta a tupla em um conjunto e exiba o conjunto resultante. Depois, adicione o número 7
ao conjunto e exiba novamente o conjunto.
8. Mesclar Dicionários
Dado dois dicionários:
Escreva um código que mescle os dois dicionários, de forma que os valores de chaves
duplicadas sejam somados. O resultado deve ser:
frutas = {
 "maçã": "vermelha",
 "banana": "amarela",
 "uva": "roxa",
}
{
 "vermelha": "maçã",
 "amarela": "banana",
 "roxa": "uva"
}
numeros = (1, 2, 3, 2, 1, 4, 5, 6, 5)
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"b": 3, "c": 4}
9. Operações com Dicionários de Produtos
Considere o seguinte dicionário que armazena produtos e seus respectivos preços:
Agora, faça o seguinte:
10. Intersecção de Conjuntos a partir de Listas
Dadas as seguintes listas:
Converta ambas as listas para conjuntos e exiba a interseção entre elas.
11. Dicionário com Tuplas como Valores
Crie um dicionário que armazena informações sobre diferentes cidades e suas coordenadas
(latitude e longitude):
{
 "a": 1,
 "b": 5,
 "c": 4
}
produtos = {
 "arroz": 5.99,
 "feijão": 7.99,
 "macarrão": 3.50,
}
Exiba o preço do "feijão".
Adicione um novo produto chamado "azeite" com preço 15.99 .
Atualize o preço do "macarrão" para 4.00 .
Remova o produto "arroz" do dicionário.
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
Agora, faça o seguinte:
12. Contagem de Ocorrências em uma Lista de Tuplas
Dada a lista de tuplas contendo nomes e idades:
Crie um dicionário que armazena quantas vezes cada nome aparece na lista. O resultado deve
ser algo assim:
cidades = {
 "São Paulo": (-23.5505, -46.6333),
 "Rio de Janeiro": (-22.9068, -43.1729),
 "Brasília": (-15.8267, -47.9218)
}
Adicione uma nova cidade, "Salvador", com coordenadas (-12.9714, -38.5014) .
Exiba as coordenadas de "Brasília".
Remova "Rio de Janeiro" do dicionário.
pessoas = [("Ana", 20), ("Carlos", 30), ("Ana", 25), ("João", 30),
("Carlos", 35)]
{
 "Ana": 2,
 "Carlos": 2,
 "João": 1
}
