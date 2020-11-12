# Leitura e conversão do arquivo CSV para um dicionario iterativo, usando a funcionalidade DictReader
import csv
with open('teste.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in  reader:
        listaDicionarios = list(reader)
        print(listaDicionarios[0])