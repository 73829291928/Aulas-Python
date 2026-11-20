import os 
os.system ("cls")

nomes= ["Joaquim", "Maria" , "Ana"] 

print(nomes[0])
print(nomes[1])
print(nomes[2])

print("--------------------------")

nomes[0] = "João"

print(nomes[0])
print(nomes[1])
print(nomes[2])

print("--------------------------")

aleatoriedade= [1, "dois" , 3.0 , True]

print(aleatoriedade[0])
print(aleatoriedade[1])
print(aleatoriedade[2])
print(aleatoriedade[3])

print("--------------------------")

nomes= ["Joaquim", "Maria" , "Ana"] 

print(nomes[0])
print(nomes[1])
print(nomes[2])

print("--------------------------")

nomes.append("Joana")

print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])

#print("Após append":, nomes) p/ add no final

print("--------------------------")

nomes.insert(4, "Mario")
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])


#print("Após insert:", nomes) p/ add elemento na localização desejada 

print("--------------------------")

nomes[3] = "Pedro"
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])
print(nomes[4])


#print("Após insert:", nomes) p/ add elemento na localização desejada 

print("--------------------------")

del nomes [2]
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(nomes[3])

#print("Após del:", nomes) p/ remover elemento na  localização desejada

print("--------------------------")

removido = nomes.pop (1)
print(nomes[0])
print(nomes[1])
print(nomes[2])
print(f"Após pop (removido: '{removido}')")

# p/ remover elemento na  localização desejada

print("--------------------------")

nomes.remove("Mario")
print(nomes[0])
print(nomes[1])
print(f"Após remove (permanece: '{nomes}')")

# p/ remover elemento na  localização desejada

print("--------------------------")

nomes.clear()
print(f"Após clear", nomes)

# p/ esvasiar a lista