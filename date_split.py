from datetime import datetime


def splitting_hairs():
    # buscar a data atual e brincar com os splits (isto pode ser realizado diretamente com o modulo datetime)
    data = datetime.now().strftime("%w %d/%m/%Y %H:%M:%S")

    # splits
    diasemana = data.split(" ")[0]
    dia = data.split(" ")[1].split("/")[0]
    mes = data.split(" ")[1].split("/")[1]
    ano = data.split(" ")[1].split("/")[2]

    hora = data.split(" ")[2].split(":")[0]
    minuto = data.split(" ")[2].split(":")[1]
    segundo = data.split(" ")[2].split(":")[2]

    # Tuple dias da semana
    diasdasemana = ("Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado")

    # tuple meses do ano
    mesesano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro",
                "Novembro", "Dezembro")

    print("Hoje é %s, dia %s de %s de %s \ne são %s horas, %s minutos e %s segundos" % (
        diasdasemana[int(diasemana)], dia, mesesano[int(mes) - 1], ano, hora, minuto, segundo))
