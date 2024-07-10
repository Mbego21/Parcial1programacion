
# Solicitar una palabra al usuario
palabra_usuario = input("Ingresa una palabra: ")


# Inicializar los índices para recorrer la palabra
izquierda = 0
derecha = len(palabra_usuario) - 1

# Verificar si la palabra es un palíndromo
while izquierda < derecha:
    if palabra_usuario[izquierda] != palabra_usuario[derecha]:
        print(f"{palabra_usuario} no es un palíndromo.")
        break
    izquierda += 1
    derecha -= 1
else:
    print(f"{palabra_usuario} es un palíndromo.")