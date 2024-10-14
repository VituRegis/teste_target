"""

1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
 (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci
 e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

"""

def pertence_fibonacci(numero):
    a, b = 0, 1
    
    if numero == 0 or numero == 1:
        return True
    
    while b <= numero:
        
        if b == numero:
            return True
        
        a, b = b, a + b
    
    return False

def main():
    numero = int(input("Digite um número: "))

    if pertence_fibonacci(numero):
        print(f"{numero} pertence a sequência de Fibonacci.")
    else:
        print(f"{numero} não pertence a sequência de Fibonacci.")

if __name__ == "__main__":
    main()
