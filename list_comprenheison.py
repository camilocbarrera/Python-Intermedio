def run():
    # first_integers_squares = []
    # for i in range(1, 101, 1):
    #     if i % 3 != 0:
    #         first_integers_squares.append(i**2)
    #     # print(i**2)
    # # pass
    # print(len(first_integers_squares))
    # print(first_integers_squares)


# vamos a resolver el mismo problema con list comprenhension
    squares = [i**2 for i in range(1,101) if i % 3 != 0 ]
    # print(squares)

    squares_b = [i for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 ]
    print(squares_b)


if __name__ == '__main__':
    run()