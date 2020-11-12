# Vamos utilizar as bibliotecas csv para lidar com o arquivo csv e fazer o parser apropiado
import csv
# Import datetime para lidar com as datas
from datetime import datetime

# Funcao que le o csv e converte em funcao lista de dicionarios, onde cada dicionario representa um acordo
with open('teste.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    for row in reader:
        listaDicionarios = list(reader)


def diaUtil(stringData):
    date = datetime.strptime(stringData, '%Y-%m-%d').date()
    if(date.weekday() == 6 or date.weekday() == 7):
        return False
    else:
        return True


def acordoValido(acordo):
    valorContrato = float(acordo['ValorContrato'])
    valorParcela = float(acordo['ValorParcela'])
    numParcelas = float(acordo['ContratoPlano'])
    data = acordo['DataVencimento']
    if(valorContrato == valorParcela * numParcelas and diaUtil(data)):
        return True
    else:
        return False

def qtdAcordos(listaDicionarios):
    return len(listaDicionarios)

def ehCPF(acordo):
    return len(acordo['documento']) == 11

def ehCNPJ(acordo):
    return len(acordo['documento']) == 14

listaCPF = [x for x in listaDicionarios if ehCPF(x)]
print(len(listaCPF))
listaCNPJ = [x for x in listaDicionarios if ehCNPJ(x)]
print(len(listaCNPJ))
print(qtdAcordos(listaDicionarios))