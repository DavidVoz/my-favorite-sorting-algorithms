# When the user requests an array to be sorted, it asks for an input of a correct random number in order for the sort to happen

def guessingsort(ar):
    import random
    while True:
        randomnum = random.randint(0, 100000000000)
        userInput = int(input("I'm thinking of a random number from 0 and 100000000000: "))

        if userInput == randomnum:
            break
        else:
            print("Nope! Guess again!")

    print("Correct! The array is now sorted for you <3") 
    ar.sort()


def main():
    array = [5,4,3,2,1]
    guessingsort(array)
    print(array)


if __name__ == "__main__":
    main()
