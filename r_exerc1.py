import os
os.system("cls")

print("Valor válido")
print("------------")

parar = False

while parar == False:
    nota = int(input("Digite uma nota entre 0 e 10: "))
    if nota > 0 and nota <= 10:
        parar = True
    
    print("Opção inválida, digite uma nota entre 0 e 10! ")

print("------------")
input("Pressione Enter para finalizar...")