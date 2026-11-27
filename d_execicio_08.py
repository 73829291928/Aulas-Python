import os
os.system("cls")

print("Comparaçao de preços")
print("--------------------")

produto1 = input("Informe o nome do produto 1: ")
valor1 = float(input(f"Informe o valor do produto {produto1}: R$ "))
print("--------------------")
produto2 = input("Informe o nome do produto 2: ")
valor2 = float(input(f"Informe o valor do produto {produto2}: R$ "))
print("--------------------")
produto3 = input("Informe o nome do produto 3: ")
valor3 = float(input(f"Informe o valor do produto {produto3}: R$ "))
print("--------------------")

if valor1 < valor2 and valor1 < valor3:
    print(f"Menor preço: {produto1} com R$ {valor1:.2f}")
 
elif valor2 < valor1 and valor2 < valor3:
    print(f"Menor preço: {produto2} com R$ {valor2:.2f}")
 
elif valor3 < valor1 and valor3 < valor2:
    print(f"Menor preço: {produto3} com R$ {valor3:.2f}")
 
else:
    print("As propostas possuem o mesmo valor.")


print("------------------------------")
input("Aperte a tecla enter para finalizar")