def divisors(num):
    divisors = [ x for x in range(1,num,1) if num %x == 1 ]
    return divisors









def run():
    num = int(input("Ingresa un número entero: "))
    print(divisors(num))
    print("terminó el programa")



if __name__=='__main__':
    run()