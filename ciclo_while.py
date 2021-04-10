def run():
    # cONSTANTE EN MAYUSCULAS
    LIMITE = 1000000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
      print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))  
      contador = contador +1
      potencia_2 = 2**contador

if __name__ == '__main__':
    run()


contador = 1
print(contador)
while contador < 1000:
    contador += 1
    print(contador)

