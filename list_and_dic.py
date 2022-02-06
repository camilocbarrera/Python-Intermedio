

def run():
    my_list = [1, 2,'hellow', True, 4.5]
    my_dict = {'firstname': 'Cristian Camilo','lastname': 'Correa Barrera'}
    super_list = [
        {'firstname': 'Cristian Camilo','lastname': 'Correa Barrera'},
        {'firstname': 'Pepe','lastname': 'Torres'},
        {'firstname': 'Susana','lastname': 'Martinez'},
        {'firstname': 'José','lastname': 'García'},
        {'firstname': 'Amanda','lastname': 'Silva'}
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums':[-1, -2, 0, 1, 2],
        'floating_nums':[1.1, 4.5, 6.43]
    }


    for key, value in super_dict.items():
        print(key,' : ',value)

    for dicti in super_list:
        print(dicti['firstname'],' : ',dicti['lastname'])



if __name__ == '__main__':
    run()