# 1- Crie um programa que simule um sistema básico de reserva de voos. O programa deve permitir que o usuário adicione reservas de voos enquanto desejar. Cada reserva deve incluir o nome do passageiro e o destino. Ao final, o programa deve listar todas as reservas feitas.

import os

listaNomes = []
listaDestinos = []

desejaContinuar = "S"
while desejaContinuar.upper() != "N":
    nome = input("Digite o nome do passageiro: ")
    listaNomes.append(nome)

    destino = input("Digite o destino do voo: ")
    listaDestinos.append(destino)

    desejaContinuar = input("Deseja continuar? (S/N) \n")

    while desejaContinuar.upper() != "N" and desejaContinuar.upper() != "S":
        os.system("cls") # Limpa a tela
        print("Opção inválida!")
        desejaContinuar = input("Deseja continuar? (S/N) \n")

    os.system("cls") # Limpa a tela

print("Reservas feitas")
print("=" * 14)
print("")

for i in range(len(listaDestinos)):
    print(f"Passageiro: {listaNomes[i]} | Destino: {listaDestinos[i]}")

