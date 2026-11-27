import os
os.system("cls")

print("Media")
print("------------")
nome= input("Informe o nome do(a) aluno(a)")
serie=input("Informe serie do(a) aluno(a)")
nota_1= int(input("Informe a nota do 1º Bimestre"))
nota_2= int(input("Informe a nota do 2º Bimestre"))
nota_3= int(input("Informe a nota do 3º Bimestre"))
nota_4= int(input("Informe a nota do 4º Bimestre"))


media= nota_1 + nota_2 + nota_3 + nota_4 



print("---------")
print(f"O(A) aluno(a) {nome}, da {serie}, fechou o 1º Bimestre com media final: {nota_1} ")
print(f"O(A) aluno(a) {nome}, da {serie}, fechou o 2º Bimestre com media final: {nota_2} ")
print(f"O(A) aluno(a) {nome}, da {serie}, fechou o 3º Bimestre com media final: {nota_3} ")
print(f"O(A) aluno(a) {nome}, da {serie}, fechou o 4º Bimestre com media final: {nota_4} ")

print("------------")
input("Pressione Enter para finalizar...")
