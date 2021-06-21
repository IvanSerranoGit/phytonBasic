# def imprimir_mensaje():
#     print("Este es un gran mensaje: ")
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversacion(mensaje):
    print("Hola")
    print("¿Cómo estas?")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opcion (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opcion 1 ")
elif opcion == 2:
     conversacion("Elegiste la opcion 2 ")
elif opcion == 3:
     conversacion("Elegiste la opcion 3 ")
else:
    print("Elige una opcion incorrecta")