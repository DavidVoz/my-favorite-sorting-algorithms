# Much like the Stalin sort, where if a value is out of order it will be killed, except random amounts of indexes are deleted until it's sorted
# Best O-time = 1
# Worst O-time = n

def checksort(ar):
    for i in range(len(ar)-1):
        if ar[i] > ar[i+1]:
            return False
    return True


def randomkill(ar):
    import random
    ar2 = ar

    while True:
        deaths = random.randint(0, len(ar2))
        for i in range(deaths):

            if len(ar2) == 0:
                break

            n = random.randint(0, len(ar2)-1)
            ar2.pop(n) # pop is another word for kill, but nicer

        if checksort(ar):
            break

    ar = ar2


def main():
    array = [1,7,6,2,4,6,5]
    randomkill(array)
    print(array)


if __name__ == "__main__":
    main()