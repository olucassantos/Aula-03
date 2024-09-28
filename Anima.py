import time
import os

espaco = 0
operacao = 1
while True:
    print(" " * espaco, end="")
    if espaco == 15:
        print("\O/")
    elif espaco == 14:
        print("__O__")
    else:
        print(" O")

    print(" " * espaco, end="")

    if espaco == 15:
        print(" |")
    elif espaco == 14:
        print("  |")
    else:
        print("/|\\")
        
    print(" " * espaco, end="")
    
    if espaco % 2 == 0:
        print("/ |")
    else:
        print("| \\")

    # Espera 0.5 segundos
    time.sleep(0.3)

    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')

    if espaco == 15:
        operacao = -1
    if espaco == 0:
        operacao = 1

    espaco = espaco + operacao        