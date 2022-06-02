import verify_input as verifica
import date_split
import ui
from nota_aluno import classifica_aluno

opcao = -1
while opcao != 0:

    ui.clearconsole()
    items = ["Comparar numeros inteiros", "Somar numeros reais", "Data e hora atual", "Classificar aluno"]
    opcao = ui.menu("Exercícios de Python", "#", 70, items, "Opcao inválida!")

    match opcao:
        case 1:
            continuar = True
            while continuar:
                ui.clearconsole()
                ui.titulo(items[0], "#", 70)
                numero1 = verifica.checkint("\tIntroduza o primeiro numero: ", "Necessário numero inteiro.")
                numero2 = verifica.checkint("\tIntroduza o segundo numero: ", "Necessário numero inteiro.")
                if numero1 > numero2:
                    print("O primeiro numero é maior do que o segundo")
                elif numero2 > numero1:
                    print("O segundo numero é maior do que o primeiro")
                else:
                    print("Os numeros são iguais")
                ui.separador("#", 70)
                continuar = ui.repetir("Comparar outros numeros? ", "s", "n", "Opção inválida")

        case 2:
            continuar = True
            while continuar:
                ui.clearconsole()
                ui.titulo(items[1], "#", 70)

                float1 = verifica.checkfloat("\tIntroduza o primeiro numero real: ")
                float2 = verifica.checkfloat("\tIntroduza o segundo numero real: ")
                print("A soma dos numeros %f e %f é %.2f " % (float1, float2, (float1 + float2)))
                ui.separador("#", 70)
                continuar = ui.repetir("Somar outros numeros reais? ", "s", "n", "Opção inválida")

        case 3:
            continuar = True
            while continuar:
                ui.clearconsole()
                ui.titulo(items[2], "#", 70)

                date_split.splitting_hairs()
                ui.separador("#", 70)
                continuar = ui.repetir("Atualizar data hora? ", "s", "n", "Opção inválida")

        case 4:
            continuar = True
            while continuar:
                ui.clearconsole()
                ui.titulo(items[3], "#", 70)

                classifica_aluno()
                ui.separador("#", 70)
                continuar = ui.repetir("Atualizar data hora? ", "s", "n", "Opção inválida")

        case 0:
            print("... a sair ...")

        case _:  # necessário?
            print("A opção não existe")
