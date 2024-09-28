# 1 - Crie um programa que escreva os numeros de 0 a 100

# contador = 0
# while contador <= 100:
#     print(contador)
#     contador = contador + 1

# 2 - Crie um programa que escreva apenas os numeros pares de 0 a 1000

# contador = 0
# while contador <= 1000:
#     print(contador)
#     contador += 2

# 3 - Crie um programa que escreva a tabuada do 2:
# 2 x 0 = 0
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# ...

# contador = 0
# while contador <= 10:
#     print(f"2 x {contador} = {contador * 2}")
#     contador += 1

# 4 - Crie um programa que solicite ao usuário qual a tabuada desejada e escreva a tabuada correspondente.
continuar = "s"
while continuar == "s":
    tabuada = int(input("Digite a tabuada desejada: "))
    contador = 0
    while contador <= 10:
        print(f"{tabuada} x {contador} = {contador * tabuada}")
        contador += 1

    continuar = input("Deseja continuar? (s/n): ")

# Imprime numeros de 0 a 4
for i in range(10):
    print(i)

# Imprime numeros de 5 a 9
for i in range(5, 10):
    print(i)

# Imprime numeros de 0 a 100 de 2 em 2
for i in range(0, 101, 2):
    print(i)

# Imprime numeros de 1 a 100 de 2 em 2
for i in range(1, 101, 2):
    print(i)

# Cria uma lista de nomes
nomes = [
    "João Cleber",
    "Maria das Graças",
    "Goreti Milagres",
    "Claudia Orrana",
    "Umberlinda Zulene"
]

# len() é uma função que retorna o tamanho de uma lista
print(len(nomes)) # Imprime o tamanho da lista

# Imprime os nomes da lista
for nome in nomes:
    print(f"O nome da vez é: {nome}")

print("*" * 40)

# Imprime os nomes da lista COM O ÍNDICE
for i in range(len(nomes)):
    print(f"{i + 1} - {nomes[i]}")


nomes = [] # Cria uma lista vazia
continua = "s"
while continua == "s":
    nome = input("Digite um nome: ")
    nomes.append(nome) # Adiciona o nome na lista de nomes

    continua = input("Deseja continuar? (s/n): ")

# Imprime os nomes da lista que o usuário digitou
for nome in nomes:
    print(f"O nome da vez é: {nome}")


# Atividades

# 5 - Crie um programa que solicite ao usuário 5 números e ao final imprima a soma de todos eles.

# 6 - Crie um programa que solicite ao usuário o nome e o salário de seus funcionários. Ao final imprima o nome e o salário de todos os funcionários, bem como a média salarial da empresa, o maior salário e o menor salário e o total gasto com salários.

# 7 - Crie um programa que solicite o nome e 4 notas de um aluno. Ao final imprima o nome do aluno, a média das notas e se ele foi aprovado ou reprovado. A média para aprovação é 7.