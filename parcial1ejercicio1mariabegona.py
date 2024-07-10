
palabra_usuario = input("Ingresa una palabra: ")

izquierda = 0
derecha = len(palabra_usuario) - 1

while izquierda < derecha:
    if palabra_usuario[izquierda] != palabra_usuario[derecha]:
        print(f"{palabra_usuario} no es un palíndromo.")
        break
    izquierda += 1
    derecha -= 1
else:
    print(f"{palabra_usuario} es un palíndromo.")
