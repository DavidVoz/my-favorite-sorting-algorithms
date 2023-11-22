# Create a second array where a random index is inputted from the original, check if it's sorted, then continue
# If at any point the second array is not sorted, everything will restart from the beginning
# same index can be used many times
# Best O-time = n^n
# Worst O-time = infinity

def cleararray(ar):
    for i in range(len(ar)):
        ar.pop(0)


def checksort(ar):
    for i in range(len(ar)-1):
        if ar[i] > ar[i+1]:
            return False
    return True


def randombogosort(ar):
    import random
    ar2 = []

    leng = len(ar)
    while True:
        n = random.randint(0,leng-1)
        ar2.append(ar[n])
        if not checksort(ar2):
            cleararray(ar2)
        else:
            if checksort(ar2) and leng == len(ar2):
                print(ar2)
                break

    ar = ar2


def main():
    array = [5,4,3,2,1,6,7,8]
    randombogosort(array)






if __name__ == "__main__":
    main()