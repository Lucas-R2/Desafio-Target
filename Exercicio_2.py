import math

def eh_quadrado_perfeito(x):
    raiz = int(math.sqrt(x))
    return raiz * raiz == x

def pertence_fibonacci(numero):
    return eh_quadrado_perfeito(5 * numero * numero + 4) or eh_quadrado_perfeito(5 * numero * numero - 4)

numero = int(input("Informe o número: "))

if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
