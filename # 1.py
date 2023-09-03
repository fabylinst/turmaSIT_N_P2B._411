# 1. Faça um programa que calcule a média de três números inseridos pelo usuário.

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3

print("A média dos números é:", media)

# 2.Crie um programa que determine se um número inserido pelo usuário é par ou ímpar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#3.Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número.

numero = int(input("Digite um número: "))

for i in range(2, numero + 1, 2):
    print(i)

# 4.Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

numeros = [int(x) for x in input("Digite a lista de números separados por espaço: ").split()]

maior = max(numeros)
menor = min(numeros)

print("Maior valor:", maior)
print("Menor valor:", menor)

# 5.	Faça um programa que leia uma lista de números e retorne a média dos números pares.

numeros = [int(x) for x in input("Digite a lista de números separados por espaço: ").split()]

numeros_pares = [num for num in numeros if num % 2 == 0]

if len(numeros_pares) > 0:
    media_pares = sum(numeros_pares) / len(numeros_pares)
    print("Média dos números pares:", media_pares)
else:
    print("Não há números pares na lista.")

# 6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número.

def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n-1)

numero = int(input("Digite um número inteiro positivo: "))
if numero < 0:
    print("Número deve ser positivo.")
else:
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")

#  7. Crie um programa que imprima a sequência de Fibonacci até um valor inserido pelo usuário. 

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < n:
            next_num = fib[-1] + fib[-2]
            fib.append(next_num)
        return fib

valor = int(input("Digite um valor para a sequência de Fibonacci: "))
if valor <= 0:
    print("O valor deve ser maior que zero.")
else:
    sequencia = fibonacci(valor)
    print(f"A sequência de Fibonacci até {valor} é {sequencia}")

#  8. Faça um programa que determine se um número é primo ou não.

def is_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

numero = int(input("Digite um número para verificar se é primo: "))
if is_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")

# 9. Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começaram com a letra 'A'. 

def nomes_com_a(lista_nomes):
    return [nome for nome in lista_nomes if nome.startswith('A') or nome.startswith('a')]

    nomes = input("Digite uma lista de nomes separados por vírgula: ").split(',')
nomes_filtrados = nomes_com_a(nomes)
print(f"Nomes que começam com 'A': {', '.join(nomes_filtrados)}")

# 10. Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O programa deve solicitar uma escolha do usuário e, em seguida, escolher aleatoriamente a escolha do computador e determinar o vencedor.

import random

def jogo_pedra_papel_tesoura(escolha_usuario):
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)
    
    print(f"Você escolheu: {escolha_usuario}")
    print(f"Computador escolheu: {escolha_computador}")
    
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (
        (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or
        (escolha_usuario == 'papel' and escolha_computador == 'pedra') or
        (escolha_usuario == 'tesoura' and escolha_computador == 'papel')
    ):
        return "Você ganhou!"
    else:
        return "Computador ganhou!"

escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
    print("Escolha inválida.")
else:
    resultado = jogo_pedra_papel_tesoura(escolha_usuario)
    print(resultado)
import random

def jogo_pedra_papel_tesoura(escolha_usuario):
    opcoes = ['pedra', 'papel', 'tesoura']
    escolha_computador = random.choice(opcoes)
    
    print(f"Você escolheu: {escolha_usuario}")
    print(f"Computador escolheu: {escolha_computador}")
    
    if escolha_usuario == escolha_computador:
        return "Empate!"
    elif (
        (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or
        (escolha_usuario == 'papel' and escolha_computador == 'pedra') or
        (escolha_usuario == 'tesoura' and escolha_computador == 'papel')
    ):
        return "Você ganhou!"
    else:
        return "Computador ganhou!"

escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
    print("Escolha inválida.")
else:
    resultado = jogo_pedra_papel_tesoura(escolha_usuario)
    print(resultado)
