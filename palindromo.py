#Receber uma palavra
#inverter a palavra
#comparar a palavra invertida com a palavra enviada

def validarPalindromo(palavra):
    palavra_invertida = palavra[::-1]
    if palavra_invertida == palavra:
        print("é um palindromo!!!!!!!!!")
    else:
        print("num é não")

palavra = input("digita ae uma palavra pfv: ")
validarPalindromo(palavra)