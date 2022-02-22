import random

from sympy import O




GAME_LIST = [
'PERRO',
'GATOss',
'ARROZs',
'AVESTRUZ',
'POLLOMAX',
'CARNEPARRILLA'

]

def random_word():
   return random.choice(GAME_LIST)

def list_to_str(list):
    word = ''
    for x in list:
        word+=x
    return word


def check_word(word_input, word_ch,place_holder):
    
    for i in range(len(word_ch)):
        if word_input.lower() == word_ch[i].lower():
            place_holder[i] = word_ch[i]
        # else:
            # print("Sorry esa palabra no está: ")
    
def print_ahorcado():
    pass

def  run():

    word_challenge = random_word()

    print(word_challenge)
    place_holder = [ '_' for w in range(len(word_challenge)) ]

    flag  = True
    while flag:
        word = input("Por favor ingresa una letra ")
        check_word(word, word_challenge, place_holder)
        print(list_to_str(place_holder))

        if '_' not in place_holder:
            flag = False
            print("¡Ganaste!")




#   O
#  -|-
#  / \


if __name__ == '__main__':
    run()