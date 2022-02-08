from functools import reduce
def run():
    # pass
    # numbers = [1, 4, 5, 6, 9, 13, 19, 21]

# Solución con List comprenhension
# Un número es impar sólo si al dividirlo entre dos es diferente de cero.
    # resp = [i for i in numbers if i%2 !=0]
    # print(resp)

#Ahora vamos a resolverlo con filter
# vamos a leer esto
# ¿Que hace la función labda?
# Recibe cómo parametro una x
#  y retorna el resultado x%2 !=0 
# Filter es una función de orden superior
# Recibe una función (lambda funtion) y un iterable, (cualquier elemento de Python que pueda iterarse)
# Esto retorna  un iterador
# El List de afuera es para pasar el iterador en una lista

    # odd = list(filter(lambda x: x%2 !=0, numbers))

    # print(odd)



# Map
    numbers = [1,2,3,4,5]
    resp = [i**2 for i in numbers]
    # print(resp)

#Esto mismo se puede resover con map

    squares = list(map(lambda x: x**2, numbers))

    # print(squares)

#Reduce
    numb = [2, 2, 2, 2, 2]
    # all_mult = 1

    # for i in numb:
        # all_mult = all_mult * i

    # print(all_mult)

    all_mult = reduce(lambda a,b : a * b, numb)
    print(all_mult)


if __name__ == '__main__':
    run()