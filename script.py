# Vamos utilizar as bibliotecas csv para lidar com o arquivo csv e fazer o parser apropiado
import csv
# Import datetime para lidar com as datas
from datetime import datetime
import locale

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
    if((valorContrato == valorParcela * numParcelas) and diaUtil(data)):
        return True
    else:
        return False


def qtdAcordos(listaDicionarios):
    return len(listaDicionarios)


def ehCPF(acordo):
    return len(acordo['documento']) == 11


def ehCNPJ(acordo):
    return len(acordo['documento']) == 14


def qtdCPF(listaDicionarios):
    listaCPF = [x for x in listaDicionarios if ehCPF(x)]
    return len(listaCPF)


def qtdCNPJ(listaDicionarios):
    listaCNPJ = [x for x in listaDicionarios if ehCNPJ(x)]
    return len(listaCNPJ)


def qtdAcordosInvalidos(listaDicionarios):
    qtdAcordosInvalidos = 0
    for acordo in listaDicionarios:
        if(not(acordoValido(acordo))):
            qtdAcordosInvalidos += 1
    
    return qtdAcordosInvalidos

def qtdTotalAcordos(listaDicionarios):
    qtdReais = 0
    for acordo in listaDicionarios:
        qtdReais += float(acordo['ValorContrato'])
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    qtdReais = locale.currency(qtdReais, grouping=True, symbol=None)
    return qtdReais


print("Foram gerados {qtd} acordos:".format(qtd = qtdAcordos(listaDicionarios)))
print("{qtd} de CPF's".format(qtd = qtdCPF(listaDicionarios)))
print("{qtd} de CNPJ's".format(qtd = qtdCNPJ(listaDicionarios)))
print("{qtd} acordos são inválidos!".format(qtd = qtdAcordosInvalidos(listaDicionarios)))
qtdTotalAcordos(listaDicionarios)
print("Valor total de todos os acordos gerados: R$ {valor}".format(valor = qtdTotalAcordos(listaDicionarios)))