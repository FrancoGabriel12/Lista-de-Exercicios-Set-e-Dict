import os

pwd = os.getcwd() #Obtém o diretório de trabalho atual usando a função getcwd() do módulo os e armazena o resultado na variável pwd.
print(pwd) #Exibe o diretório de trabalho atual armazenado na variável pwd.

PASTA = "NOVApasta" #Define uma variável chamada PASTA com o valor "NOVApasta", que representa o nome da pasta a ser criada.
os.mkdir(PASTA) #Cria uma nova pasta com o nome especificado na variável PASTA usando a função mkdir() do módulo os.

ls=os.listdir('.')
print(ls) #Exibe a lista de arquivos e pastas presentes no diretório atual ('.') usando a função listdir() do módulo os e armazena o resultado na variável ls.

os.chdir('..') #Altera o diretório de trabalho atual para o diretório pai usando a função chdir() do módulo os e passando '..' como argumento.


os.rmdir(PASTA) #Remove a pasta criada anteriormente usando a função rmdir() do módulo os e passando o nome da pasta armazenado na variável PASTA.