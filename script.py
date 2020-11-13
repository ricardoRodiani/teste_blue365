# Vamos utilizar a biblioteca csv para lidar com o arquivo csv e fazer o parser apropiado
import csv

# Import datetime para lidar com as datas
from datetime import datetime

# Import local para lidar com moeda em Reais
import locale

# Trecho que le o csv e converte em uma lista de dicionarios, onde cada dicionario representa um acordo
with open('teste.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter="|")
    listaDicionarios = []
    for row in reader:
        listaDicionarios.append(row)

# Recebe uma stringData e retorna se o dia da mesma é util ou não
def diaUtil(stringData):
    date = datetime.strptime(stringData, '%Y-%m-%d').date()
    if(date.weekday() == 5 or date.weekday() == 6):
        return False
    else:
        return True


def valorAcordoValido(acordo):
    valorContrato = float(acordo['ValorContrato'])
    valorParcela = float(acordo['ValorParcela'])
    numParcelas = float(acordo['ContratoPlano'])
    if(valorContrato == (valorParcela * numParcelas)):
        return True
    else:
        return False


def acordoValido(acordo):
    data = acordo['DataVencimento']
    if(valorAcordoValido(acordo) and diaUtil(data)):
        return True
    else:
        return False


def qtdAcordos(listaDicionarios):
    return len(listaDicionarios)


def ehCPF(acordo):
    return len(acordo['documento']) == 11


def ehCNPJ(acordo):
    return len(acordo['documento']) == 14

# Pega cada acordo da lista e verifica se os valores que estao na coluna de "documento" representam um cpf, retorna essa nova lista no final
def qtdCPF(listaDicionarios):
    listaCPF = [x for x in listaDicionarios if ehCPF(x)]
    return len(listaCPF)


# Pega cada acordo da lista e verifica se os valores que estao na coluna de "documento" representam um cnpj, retorna essa nova lista no final
def qtdCNPJ(listaDicionarios):
    listaCNPJ = [x for x in listaDicionarios if ehCNPJ(x)]
    return len(listaCNPJ)


def qtdAcordosInvalidos(listaDicionarios):
    qtdAcordosInvalidos = 0
    for acordo in listaDicionarios:
        if(not(acordoValido(acordo))):
            qtdAcordosInvalidos += 1

    return qtdAcordosInvalidos


# Usa biblioteca locale para transfomar um valor em uma string formatada para Reais
def qtdTotalAcordos(listaDicionarios):
    qtdReais = 0
    for acordo in listaDicionarios:
        qtdReais += float(acordo['ValorContrato'])

    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    qtdReais = locale.currency(qtdReais, grouping=True, symbol=None)
    return qtdReais


def invalidoPeloValor(listaDicionarios):
    invalidos = 0
    for acordo in listaDicionarios:
        if(not(valorAcordoValido(acordo))):
            invalidos += 1
    return invalidos


def invalidoPeloDia(listaDicionarios):
    invalidos = 0
    for acordo in listaDicionarios:
        data = acordo['DataVencimento']
        if(not(diaUtil(data))):
            invalidos += 1
    return invalidos


print("Foram gerados {qtd} acordos:".format(qtd=qtdAcordos(listaDicionarios)))
print("{qtd} de CPF's".format(qtd=qtdCPF(listaDicionarios)))
print("{qtd} de CNPJ's".format(qtd=qtdCNPJ(listaDicionarios)))
print("{qtd} acordos são inválidos!".format(
    qtd=qtdAcordosInvalidos(listaDicionarios)))
qtdTotalAcordos(listaDicionarios)
print("Acordos inválidos porque os valores estão incorretos: {qtd}".format(
    qtd=invalidoPeloValor(listaDicionarios)))
print("Acordos inválidos porque o dia da data de vencimento não é útil: {qtd}".format(
    qtd=invalidoPeloDia(listaDicionarios)))
print("Valor total de todos os acordos gerados: R$ {valor}".format(
    valor=qtdTotalAcordos(listaDicionarios)))