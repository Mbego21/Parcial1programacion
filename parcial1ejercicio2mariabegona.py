
palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

for i in range(len(palabra1)):
    for j in range(len(palabra1) - 1):
        if palabra1[j] > palabra1[j + 1]:
            palabra1 = palabra1[:j] + palabra1[j + 1] + palabra1[j] + palabra1[j + 2:]

for i in range(len(palabra2)):
    for j in range(len(palabra2) - 1):
        if palabra2[j] > palabra2[j + 1]:
            palabra2 = palabra2[:j] + palabra2[j + 1] + palabra2[j] + palabra2[j + 2:]

if palabra1 == palabra2:
    print(f"{palabra1} y {palabra2} son anagramas.")
else:
    print(f"{palabra1} y {palabra2} no son anagramas.")
    
    
