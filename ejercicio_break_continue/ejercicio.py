def run():

    # ejercicio con break y continie

    print("""
        seleciona la letra faltante

        G to
    
    """)
    palabra = input('Escribe la letra faltante: ')
    for letra in palabra:
        if letra != 'a':
            print('Incorrecto la palabra no es G' + palabra + "to")    
            continue
        if letra == 'a':
            print('correcto la palabra es gato')
            break

if __name__ == '__main__':
    run()



