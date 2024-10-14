'''
2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

'''
def verificaString(string):
    string = string.upper()

    aparicoes = string.count('A')
    
    if aparicoes > 0:
        print(f"A letra A aparece {aparicoes} vezes.")
    else:
        print("String inserida não possui ôcorrencia de letra A.")

def main():
    print("Insira uma string para calcular a quantidade de letras A: ")
    input_string = str(input())

    verificaString(input_string)

if __name__ == "__main__":
    main()
