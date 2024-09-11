# Crie um programa que receba um número do usuário e informe se ele é positivo, negativo ou zero.
numero=int(input("digite um numero"))
if numero>0:
    print("seu valor é positivo")
elif numero == 0:
    print("seu valor é zero")
elif numero < 0 :
    print ("seu valor é negativo")