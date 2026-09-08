import datetime

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.month)
print(x.day)

print(x.strftime("%A")) #Exibe o nome do dia da semana correspondente à data atual usando a função strftime() do módulo datetime e o formato "%A" para obter o nome completo do dia da semana.
print(x.strftime("%B")) #Exibe o nome do mês correspondente à data atual usando a função strftime() do módulo datetime e o formato "%B" para obter o nome completo do mês
    