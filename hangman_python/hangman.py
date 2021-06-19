import random
import os

def formats():
    os.system("cls")
    print("""      
        ##    ##      ###      ####    ##  #########  ####      ####      ###      ####    ##
        ##    ##     ## ##     ## ##   ##  ##         ## ##    ## ##     ## ##     ## ##   ##
        ########    #######    ##  ##  ##  ##  #####  ##  ##  ##  ##    #######    ##  ##  ## 
        ##    ##   ##     ##   ##   ## ##  ##     ##  ##   ####   ##   ##     ##   ##   ## ##
        ##    ##  ##       ##  ##    ####  #########  ##    ##    ##  ##       ##  ##    ####
                """ )

def comparation(word, palabra):
    word = word+"\n"
    if word==palabra:
        print("HAS GANADO!!! la palabra es: " + palabra)
        return True
    return False
    

def validating(palabra, lista, user_input):
    cont = 0
    for i in palabra:
        if(user_input == i):
            lista.pop(cont)
            lista.insert(cont, user_input)
        cont+=1
    return lista 

def run():
    with open("./files/data.txt", "r", encoding="utf-8")as f:
        word_list = [word for word in f]
        palabra = word_list[random.randint(0,9)]
    lista = ["_" for i in range(0,len(palabra)-1)]

    for i in range(0,10):
        formats()
        print("te quedan", 10-(i), " intentos")

        print(" ".join(lista).upper())
        string2 = "".join(lista)

        if comparation(string2, palabra):
                break

        user_input = input("digite una letra: ")
        assert user_input!="", "HAS PERDIDO!!!, no puede estar vacio"  
        if i==9:
            print("te quedaste sin intentos, GAME OVER!!!")
            break

        if len(user_input)==1:
            lista = validating(palabra, lista, user_input)

        elif comparation(user_input, palabra):
                break
        
        else: 
            print("HAS PERDIDO!!!")
            break
            
if __name__ == '__main__':
    run()