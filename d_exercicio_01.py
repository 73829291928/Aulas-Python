import os
os.system ("cls")

print ("Qual é o maior número? ")
print ("---------------------------------")

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))

if num1 >= num2:
    print(f"Maior número: {num1}")

else:
    print(f"Maior número: {num2}")

print("------------------------------")
input("Aperte a tecla enter para finalizar")