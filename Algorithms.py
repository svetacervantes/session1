import random

def sequentialsearch(haystack, needle):
    for i in range(0, len(haystack)):
        if (haystack[i] == needle):
            return i
def main():
    numbers = []
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    target = random.randrange(0,2000)
    location = sequentialsearch(numbers, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))


if __name__ == '__main__':
    main()

def binarysearch(haystack, needle):
    start = 0
    end = len(haystack)

    while start <= end:
        i = start + (end-start)//2
        if haystack[i] < needle:
            start = i+1
        elif haystack[i] > needle:
            end = i-1
        else:
            return i

def main():
    numbers = []
    for i in range(0, 1000):
        numbers.append(random.randrange(0,2000))

    numbers.sort()
    target = random.randrange(0,2000)
    location = binarysearch(numbers, target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + " at location " + str(location))

