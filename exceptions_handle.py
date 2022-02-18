


def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("The string can't be empty")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False

# print(palindrome('olos'))


def run():
    text = input("Ingresa la palabra")
    print("Your word is: " , text)
    print(palindrome(text))
    # print("Sorry, you can input only strings")





if __name__ == '__main__':
    run()