# Vamos utilizar as bibliotecas csv para lidar com o arquivo csv e fazer o parser apropiado
import csv
# Import datetime para lidar com as datas
from datetime import datetime

# Funcao que le o csv e converte em funcao lista de dicionarios, onde cada dicionario representa um acordo
with open('teste.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in  reader:
        listaDicionarios = list(reader)
        print(listaDicionarios[0])

def diaUtil(stringData):
    date = datetime.strptime(stringData, '%Y-%m-%d').date()
    if(date.weekday() == 6 or date.weekday() == 7):
        return False
    else:
        return True

def acordoValido(acordo):
    valorContrato = float(acordo['ValorContrato'])
    valorParcela =  float(acordo['ValorParcela'])
    numParcelas = float(acordo['ContratoPlano'])
    data = acordo['DataVencimento']
    if(valorContrato == valorParcela * numParcelas and diaUtil(data)): 
        return True
    else:
        return False

if(acordoValido(listaDicionarios[0])):
    print('Acordo Valido!')
else:
    print('Acordo inválido')