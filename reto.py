import random


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


def check_word(word_input, word_ch):
    
    for word in word_challenge:
        if word.lower() ==  word_input.lower():
            print("Si está")


        else:
            print("No está")

    # for word in range(0,len(word_challenge)):
    #     if word_input.lower() in word_ch.lower():
    #         print("Si está", )
    #     else:
    #         print("-1 ahorcado")
        





def  run():
    pass

word_challenge = random_word()


# word = input("Por favor ingresa una letra ")
# print("La palabra es: --> ",word_challenge)
# print("La palabra es: --> ",word_challenge.replace())

# check_word(word,word_challenge)
# print(len(word_challenge))


# empty_holder = ''

for i in range(len(word_challenge)):
    print(i, ' ', word_challenge[i])

# print(empty_holder)




if __name__ == '__main__':
    run()