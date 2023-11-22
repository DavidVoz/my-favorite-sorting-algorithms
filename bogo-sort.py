# Randomly sorts an array until it's sorted
# Best O-time = 1
# Worst O-time = infinity


def checksort(ar):
    for i in range(len(ar)-1):
        if ar[i] > ar[i+1]:
            return False
    return True
    

def bogosort(ar):
    import random

    leng = len(ar)

    while True:
        n1 = random.randint(0,leng-1)
        n2 = random.randint(0,leng-1)

        temp = ar[n1]
        ar[n1] = ar[n2]
        ar[n2] = temp

        if checksort(ar):
            return False 



def main():
    array = [1,2,4,3,6,7,8,9,10]
    bogosort(array)
    print(array)


if __name__ == "__main__":
    main()