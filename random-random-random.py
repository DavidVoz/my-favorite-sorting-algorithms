# When user calls a function, an array of random length and random values is now the array
# 

def randomrandomsort(ar):
    import random

    for i in range(len(ar)-1):
        ar.pop(0)
    
    
    leng = random.randint(0,10000)

    for i in range(leng-1):
        n = random.randint(0,100000000)
        ar.append(n)


def main():
    array = [1,2,3,4,5]
    randomrandomsort(array)
    print(array)


if __name__ == "__main__":
    main()
