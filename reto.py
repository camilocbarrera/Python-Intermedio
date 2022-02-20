import random


GAME_LIST = [
'PERRO',
'GATO',
'ARROZ'

]

def random_word():
   return random.choice(GAME_LIST)


def check_word(word_input, word_ch):
    if word_input in word_ch:
        print("Si está")
    else:
        print("-1 ahorcado")
    





def  run():
    pass

word_challenge = random_word()


word = input("Por favor ingresa una palabra")
check_word(word)


if __name__ == '__main__':
    run()