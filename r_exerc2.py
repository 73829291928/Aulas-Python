import os
os.system("cls")

print("usuario e senha")
print("------------")

nome_usuario = input("Digite o seu usuário: ")
senha = input("Senha: ")

while nome_usuario == senha:
    print("Erro! O nome de usuário e a senha não podem ser iguais! Tente novamente. ")

    nome_usuario = input("Digite o seu usuário: ")
    senha = input("Senha: ")

print("------------")
input("Pressione Enter para finalizar...")