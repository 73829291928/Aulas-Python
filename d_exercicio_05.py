import os
os.system ("cls")

print("Nota dos alunos")
print("------------")
nome= input("Informe seu nome: ")
trabalho = float(input("Informe a nota do trabalho: "))
prova = float(input("Informe a nota da prova: "))

media = (trabalho + prova) /2

print(f"Sua média  é: {media:.2f}")

if media == 10:
    print(f"{nome}, você foi Aprovado com Distinção!")
 
elif media >= 7:
    print(f"{nome}, você foi aprovado!")
 
else:
    print(f"{nome}, você foi reprovado.")
 

print("--------------------------")
input("Aperte a tecla enter para finalizar")