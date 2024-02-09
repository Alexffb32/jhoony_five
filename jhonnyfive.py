import time
import webbrowser

def dar_dica_nome(tentativas_restantes):
    if tentativas_restantes == 2:
        print("Dica: O nome começa com a letra 'J'.")
    elif tentativas_restantes == 1:
        print("Dica: O nome possui um 'h' e dois 'n'.")

def dar_dica_conta(tentativas_restantes):
    if tentativas_restantes == 2:
        print("Dica: Tente usar uma operação de adição.")
    elif tentativas_restantes == 1:
        print("Dica: A soma dos números deve ser igual a 5.")

def desafio_jhonny_five():
    max_tentativas_nome = 3
    max_tentativas_conta = 3
    
    while True:
        nome_correto = "Jhonny"
        resultado_esperado = 5
        
        tentativas_nome = 0
        tentativas_conta = 0

        while tentativas_nome < max_tentativas_nome:
            nome_usuario = input("Digite o nome corretamente: ")

            if nome_usuario.lower() == nome_correto.lower():
                print("Nome correto! Agora vamos para o próximo desafio.")
                break
            else:
                print("Nome incorreto.")
                tentativas_nome += 1
                if tentativas_nome < max_tentativas_nome:
                    print(f"Tentativas restantes para o nome: {max_tentativas_nome - tentativas_nome}")
                    if input("Deseja uma dica para o nome? (S/N): ").upper() == "S":
                        dar_dica_nome(max_tentativas_nome - tentativas_nome)
                else:
                    print("Número máximo de tentativas atingido para o nome.")
                    break

        if tentativas_nome == max_tentativas_nome:
            continuar_jogo = input("Deseja jogar novamente? (S/N): ").upper()
            if continuar_jogo != "S":
                break
            else:
                continue

        print("Você tem 10 segundos para responder à próxima pergunta.")
        start_time = time.time()
        num1 = int(input("Digite o primeiro número: "))
        operador = input("Digite o operador matemático (+, -, *, /): ")
        num2 = int(input("Digite o segundo número: "))
        end_time = time.time()

        tempo_restante = 10 - (end_time - start_time)
        if tempo_restante <= 0:
            print("Tempo esgotado! Desafio incompleto.")
            continuar_jogo = input("Deseja jogar novamente? (S/N): ").upper()
            if continuar_jogo != "S":
                break
            else:
                continue

        while tentativas_conta < max_tentativas_conta:
            if operador == "+":
                resultado = num1 + num2
            elif operador == "-":
                resultado = num1 - num2
            elif operador == "*":
                resultado = num1 * num2
            elif operador == "/":
                if num2 == 0:
                    print("Divisão por zero não é permitida.")
                    tentativas_conta += 1
                    if tentativas_conta < max_tentativas_conta:
                        print(f"Tentativas restantes para a conta: {max_tentativas_conta - tentativas_conta}")
                        if input("Deseja uma dica para a conta? (S/N): ").upper() == "S":
                            dar_dica_conta(max_tentativas_conta - tentativas_conta)
                    else:
                        print("Número máximo de tentativas atingido para a conta.")
                    continue
                else:
                    resultado = num1 / num2
            else:
                print("Operador inválido.")
                tentativas_conta += 1
                if tentativas_conta < max_tentativas_conta:
                    print(f"Tentativas restantes para a conta: {max_tentativas_conta - tentativas_conta}")
                    if input("Deseja uma dica para a conta? (S/N): ").upper() == "S":
                        dar_dica_conta(max_tentativas_conta - tentativas_conta)
                else:
                    print("Número máximo de tentativas atingido para a conta.")
                    break

            if resultado == resultado_esperado:
                print(f"Parabéns! Descobriste o Jhonny Five {resultado_esperado}!")
                break
            else:
                print("Resultado incorreto.")
                tentativas_conta += 1
                if tentativas_conta < max_tentativas_conta:
                    print(f"Tentativas restantes para a conta: {max_tentativas_conta - tentativas_conta}")
                else:
                    print("Número máximo de tentativas atingido para a conta.")
                    break

        continuar_jogo = input("Deseja jogar novamente? (S/N): ").upper()
        if continuar_jogo != "S":
            break

    conhecer_jhonny_five = input("Gostarias de conhecer o Jhonny Five? (S/N): ").upper()
    if conhecer_jhonny_five == "S":
        webbrowser.open("https://johnny-five.io/")

    conhecer_criador = input("Gostarias de conhecer o criador deste jogo? (S/N): ").upper()
    if conhecer_criador == "S":
        webbrowser.open("https://github.com/Alexffb32/jhoony_five")

    print("Obrigado por jogar! Até a próxima!")

desafio_jhonny_five()
