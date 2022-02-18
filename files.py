import encodings
from opcode import opname


def read():
    
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:

        numbers = [ int(lines) for lines in f  ]
        # for line in f:
            # numbers.append(int(line))

    print(numbers)



def write():
    names = ["Cristian", "Pepe", "Facundo", "José"]

    # with open("./files/names.txt", "w", encoding="utf-8") as f:
    with open("./files/names.txt", "a", encoding="utf-8") as f:
        for n in names:
            f.write(n) 
            f.write("\n")
            




def run():

    # read()
    write()


if __name__ == '__main__':
    run()