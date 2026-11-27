import os
os.system ("cls")

print ("Vogal ou consoante")
print ("---------------------------------")

letra = input("Digite a letra que você deseja: ")

vogais = ("a", "e", "i", "o", "u")


if letra in vogais:
    print(f"A letra {letra} é uma vogal! ")

else:
    print(f"A letra {letra} é uma consoante! ")

print("--------------------------")
input("Aperte a tecla enter para finalizar")