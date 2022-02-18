def divisors(num):
    divisors = [ x for x in range(1,num+1) if num %x == 0 ]
    return divisors




def run():
    
    num = input("Ingresa un número entero: ")
    assert num.isnumeric() and int(num) > 0 , "The input must be numeric and positive"
    print(divisors(int(num)))



if __name__=='__main__':
    run()