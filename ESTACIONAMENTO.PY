import os
os.system("cls")
 
# ==================================
# SISTEMA DE ESTACIONAMENTO
# ==================================
 
# Constantes
quantidade_maxima = 20
 
# Controle do estacionamento
veiculos = {}
faturamento = 0.0
 
 
# ==================================
# REGISTRAR ENTRADA
# ==================================
 
def registrar_entrada():
 
    print("\n=== REGISTRO DE ENTRADA ===")
 
    if len(veiculos) >= quantidade_maxima:
        print("Estacionamento lotado!")
        return
 
    nome_cliente = input("Nome do cliente: ")
    placa = input("Placa do veículo: ").upper()
 
    if placa in veiculos:
        print("Este veículo já está estacionado!")
        return
 
    print("\nTipos de veículos:")
    print("[1] - Moto  | R$ 5,00/h")
    print("[2] - Carro | R$ 8,00/h")
    print("[3] - SUV   | R$ 12,00/h")
 
    tipo = input("Selecione o tipo de veículo: ")
 
    if tipo == "1":
        veiculo = "Moto"
        valor_hora = 5
 
    elif tipo == "2":
        veiculo = "Carro"
        valor_hora = 8
 
    elif tipo == "3":
        veiculo = "SUV"
        valor_hora = 12
 
    else:
        print("Tipo de veículo inválido!")
        return
 
    veiculos[placa] = {
        "cliente": nome_cliente,
        "tipo": veiculo,
        "valor_hora": valor_hora
    }
 
    print("\nVeículo registrado com sucesso!")
    print(f"Cliente: {nome_cliente}")
    print(f"Placa: {placa}")
    print(f"Veículo: {veiculo}")
    print(f"Veículos estacionados: {len(veiculos)}")
    print(f"Vagas disponíveis: {quantidade_maxima - len(veiculos)}")
 
 
# ==================================
# REGISTRAR SAÍDA E COBRANÇA
# ==================================
 
def registrar_saida():
 
    global faturamento
 
    print("\n=== REGISTRO DE SAÍDA ===")
 
    if len(veiculos) == 0:
        print("Estacionamento vazio!")
        return
 
    placa = input("Placa do veículo: ").upper()
 
    if placa not in veiculos:
        print("Veículo não encontrado!")
        return
 
    nome_cliente = veiculos[placa]["cliente"]
    veiculo = veiculos[placa]["tipo"]
    valor_hora = veiculos[placa]["valor_hora"]
 
    horas = float(input("Horas estacionado: "))
 
    if horas <= 0:
        print("Quantidade de horas inválida!")
        return
 
    valor_permanencia = valor_hora * horas
 
    if horas > 10:
        taxa = valor_permanencia * 0.10
 
    elif horas > 5:
        taxa = valor_permanencia * 0.05
 
    else:
        taxa = 0
 
    total_a_pagar = valor_permanencia + taxa
    media_hora = total_a_pagar / horas
 
    print("\n========== NOTA DE PAGAMENTO ==========")
 
    print(f"Cliente: {nome_cliente}")
    print(f"Placa: {placa}")
    print(f"Veículo: {veiculo}")
    print(f"Horas estacionado: {horas:g}")
    print(f"Valor por hora: R$ {valor_hora:.2f}")
    print(f"Permanência: R$ {valor_permanencia:.2f}")
    print(f"Taxa adicional: R$ {taxa:.2f}")
    print("---------------------------------------")
    print(f"TOTAL A PAGAR: R$ {total_a_pagar:.2f}")
    print(f"Valor médio por hora: R$ {media_hora:.2f}")
    print("=======================================")
 
    faturamento += total_a_pagar
 
    del veiculos[placa]
 
    print("\nSaída registrada com sucesso!")
    print("Obrigado pela preferência!")
 
 
# ==================================
# CONSULTAR VAGAS
# ==================================
 
def consultar_vagas():
 
    vagas_disponiveis = quantidade_maxima - len(veiculos)
 
    print("\n=== VAGAS DISPONÍVEIS ===")
 
    print(f"Capacidade total: {quantidade_maxima}")
    print(f"Vagas ocupadas: {len(veiculos)}")
    print(f"Vagas disponíveis: {vagas_disponiveis}")
 
 
# ==================================
# CONSULTAR FATURAMENTO
# ==================================
 
def consultar_faturamento():
 
    print("\n=== FATURAMENTO ===")
 
    print(f"Valor arrecadado: R$ {faturamento:.2f}")
 
 
# ==================================
# CONSULTAR VEÍCULOS
# ==================================
 
def consultar_veiculos():
 
    print("\n=== VEÍCULOS ESTACIONADOS ===")
 
    if len(veiculos) == 0:
        print("Nenhum veículo estacionado!")
 
    else:
        for placa in veiculos:
 
            print("----------------------------")
            print(f"Placa: {placa}")
            print(f"Cliente: {veiculos[placa]['cliente']}")
            print(f"Veículo: {veiculos[placa]['tipo']}")
 
 
# ==================================
# PROGRAMA PRINCIPAL
# ==================================
 
opcao = ""
 
while opcao != "0":
 
    print("\n========= ESTACIONAMENTO =========")
    print("======== SEJA BEM-VINDO ==========")
 
    print("[1] - Registrar entrada de veículo")
    print("[2] - Registrar saída e cobrança")
    print("[3] - Consultar vagas disponíveis")
    print("[4] - Consultar faturamento")
    print("[5] - Consultar veículos estacionados")
    print("[0] - Sair do sistema")
 
    opcao = input("\nSelecione uma opção: ")
 
    if opcao == "1":
        registrar_entrada()
 
    elif opcao == "2":
        registrar_saida()
 
    elif opcao == "3":
        consultar_vagas()
 
    elif opcao == "4":
        consultar_faturamento()
 
    elif opcao == "5":
        consultar_veiculos()
 
    elif opcao == "0":
        print("\nSistema encerrado!")
 
    else:
        print("\nOpção inválida. Tente novamente!")
 
    if opcao != "0":
        input("\nPressione ENTER para continuar...")
        os.system("cls")