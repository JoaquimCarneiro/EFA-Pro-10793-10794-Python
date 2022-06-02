import verify_input


def classifica_aluno():
    print("Classificar o aluno")
    classifica = ("Mau", "Insuficiente", "Suficiente", "Bom", "Excelente")

    nota = -1

    while nota < 0 or nota > 20:
        nota = verify_input.checkint("digite a nota ", "Tem que digitar um numero")

    if 0 <= nota < 8:
        notaverbo = classifica[0]
    elif 8 <= nota < 10:
        notaverbo = classifica[1]
    elif 10 <= nota < 14:
        notaverbo = classifica[2]
    elif 14 <= nota < 18:
        notaverbo = classifica[3]
    else:
        notaverbo = classifica[4]

    print("O aluno teve um desempenho " + notaverbo)
