'''txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))'''

'''txt = "The temperature is between {} and {} degrees celsius."
print(txt.format(-3, 7))'''

'''txt = "É de mais de {:,}!!!"

print(txt.format(8000))'''

'''txt = "Meu nick é: Pedruquis_{:_}"
print(txt.format(666999))'''

'''txt = "Código Secreto: {0:b}{1:b}{2:b}{3:b} ... Decodificando ... Senha '{0}{1}{2}{3}'."
print(txt.format(5,6,7,8))'''

'''txt = "Criptografador recebendo dados: {0}{1}{2}{3}... Codificando... Código: {0:d}{1:d}{2:d}{3:d}"
print(txt.format(0b101,0b110,0b111,0b1000))'''

x = float("nan")
txt = "Pedro {:f}."
print(txt.format(x))