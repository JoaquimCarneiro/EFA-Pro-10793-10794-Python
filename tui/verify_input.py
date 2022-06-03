def checkint(pergunta, erro):
    controle = False
    valor = ""  # so para remover um "warning"
    while not controle:
        valor = input(pergunta)
        controle = valor.isdigit()
        if not controle:
            print(erro)
        else:
            valor = int(valor)
    return valor


def checkfloat(pergunta):
    controle = False
    valor = ""  # so para remover um "warning"
    while not controle:
        valor = input(pergunta)
        try:
            valor = float(valor)
            controle = True
        except ValueError:
            print("O valor introduzido não é um numero real")
            controle = False
    return valor
