# When user calls a function, an array of random values is now the array

def randomrandom(ar):
    import random

    leng = len(ar)
    for i in range(leng):
        n = random.randint(0,100000000)
        ar[i] = n


def main():
    array = [1,2,3,4,5]
    randomrandom(array)
    print(array)


if __name__ == "__main__":
    main()