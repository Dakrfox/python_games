import random

max_intentos = 10

def validating(palabra, lista, user_input):
    for i in range(len(palabra)):
        if user_input == palabra[i]:
            lista[i] = user_input
    return lista


def run():
    print("""      
     ##    ##      ###      ####    ##  #########  ####      ####      ###      ####    ##
     ##    ##     ## ##     ## ##   ##  ##         ## ##    ## ##     ## ##     ## ##   ##
     ########    #######    ##  ##  ##  ##  #####  ##  ##  ##  ##    #######    ##  ##  ## 
     ##    ##   ##     ##   ##   ## ##  ##     ##  ##   ####   ##   ##     ##   ##   ## ##
     ##    ##  ##       ##  ##    ####  #########  ##    ##    ##  ##       ##  ##    ####
             """)

    with open("./files/data.txt", "r", encoding="utf-8")as f:
        word_list = f.readlines()
        # Elegir una palabra al azar, eliminar los white-spaces y llevar a mayúsculas.
        palabra = word_list[random.randint(0, len(word_list) - 1)].strip().upper()

        lista = ["_"] * len(palabra)
        # lista = ["_" for i in range(0, len(palabra) - 1)]

    for intentos in range(max_intentos, 1, -1):
        print(f"te quedan {intentos} intentos")

        user_input = input("digite una letra: ").strip().upper()

        if len(user_input) == 1:
            lista = validating(palabra, lista, user_input)
            print(" ".join(lista).upper())
            string2 = "".join(lista)

            if palabra == string2:
                print(f"HAS GANADO!!! la palabra es: {palabra}")
                break
        else:
            print("Ingresa sólo una letra")
    else:
        print("te quedaste sin intentos, GAME OVER!!!")

if __name__ == '__main__':
    run()