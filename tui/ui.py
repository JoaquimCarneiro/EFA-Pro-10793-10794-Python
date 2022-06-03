import os
from tui.verify_input import checkint


def clearconsole():
    cmd = "clear"
    if os.name in ("nt", "dos"):
        cmd = "cls"
    os.system(cmd)


def separador(caracter, tamanholinha):
    for i in range(tamanholinha):
        if i < tamanholinha-1:
            print(caracter, end="")
        else:
            print(caracter)


def titulo(titulostr, caracter, tamanholinha):
    separador(caracter, tamanholinha)
    centrastring(titulostr, caracter, tamanholinha)
    separador(caracter, tamanholinha)


def centrastring(titulostr, caracter, tamanholinha):
    print(caracter, end="")
    qtd = tamanholinha - len(titulostr) - 2
    for i in range(int(qtd/2)):
        print(" ", end="")
    print(titulostr, end="")
    for j in range(int(qtd/2)):
        print(" ", end="")
    if qtd % 2 == 0:
        print(caracter)
    else:
        print(" " + caracter)


def menu(titulostr, caracter, tamanholinha, items, msg_opcao_invalida):

    titulo(titulostr, caracter, tamanholinha)

    separador("-", tamanholinha)
    for i in range(len(items)):
        print("\t[%i] - %s" % (i+1, items[i]))
    separador("-", tamanholinha)
    print("\t[0] - Sair")
    separador("-", tamanholinha)
    separador(caracter, tamanholinha)
    opcao = -1
    controle = False
    while opcao < 0 or opcao > len(items):
        if controle:
            print(msg_opcao_invalida)
        opcao = checkint("Escolha uma opção: ", msg_opcao_invalida)
        controle = True
    return opcao


def repetir(pergunta, verdadeiro, falso, msgerro):
    opcao = ""
    controle = False
    while opcao not in (verdadeiro, falso):
        if controle:
            print(msgerro)
        opcao = input("%s (%s/%s) " % (pergunta, verdadeiro, falso))
        controle = True

    if opcao == verdadeiro:
        return True
    else:
        return False
