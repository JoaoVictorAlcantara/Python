numero = int(input("digite um número"))

if not (numero % 3) and (numero % 5):
    print("FizzBuzz")
else:
    print(numero)