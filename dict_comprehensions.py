
def run():
    my_dic = {i: i**3 for i in range(1,101,1) if i % 3 != 0}

    dictionary_challenge = {i: round(i**(1/2),2) for i in range(1,1001,1) if True }

    print(dictionary_challenge)

    # for i in range(1,101,1):
        # if i % 3 != 0:
            # my_dic[i] = i**3
            
    print(my_dic)
    # for k,v in my_dic.items():
        # print(k,' : ', v)



if __name__ == '__main__':
    run()