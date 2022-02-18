def divisors(num):
    try:
        if num < 0:
            raise ValueError("The number must be positive")
        divisors = [ x for x in range(1,num+1) if num %x == 0 ]
        return divisors
    except ValueError as ve:
        print(ve)
        return ve








def run():
    
    try:
        num = int(input("Ingresa un número entero: "))
        print(divisors(num))
    except ValueError:
        print("The imput must be an integer")
    print("terminó el programa")



if __name__=='__main__':
    run()