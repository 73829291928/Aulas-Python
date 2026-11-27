import os
os.system("cls")

print("Converter arquivos de Gigabytes em Megabytes e em Kilobytes")
print("------------")

Giga = float(input("Informe o tamanho do arquivo em Gigabytes"))

Megabytes= Giga * 1024
Kilobytes= Giga * 1024 * 1024

print("------------")
print (f"O tamnho do arquivo em Gigabytes   {Giga}, convertido em Megabytes é {Megabytes}.") 
print (f"O tamanho do arquivo em Gigabytes  {Giga}, convertido em Kilobytes é {Kilobytes}.")

