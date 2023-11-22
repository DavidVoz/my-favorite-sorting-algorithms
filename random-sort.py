# Randomly sorts an array once per function call
# Best O-time = 1
# Worst O-time = ??

def randomsort(ar):
    import random

    leng = len(ar)
    loop = random.randint(0,leng)
    
    for i in range(loop):
        n1 = random.randint(0,leng-1)
        n2 = random.randint(0,leng-1)

        temp = ar[n1]
        ar[n1] = ar[n2]
        ar[n2] = temp


def main():
    array = [1,2,3,4,5]
    randomsort(array)
    print(array)


if __name__ == "__main__":
    main()