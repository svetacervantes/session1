

# def sayhello(name):
#     print("hello " + name)

# sayhello("misha")
# sayhello("sveta")

def factorial(num):
    ans = 1
    for i in range(1, num + 1):
        ans *= i

    return ans

# print(factorial(5))

def sum():
    n = int(input('enter a number: '))
    sum = 0
    for x in range(1, n):
        sum = sum + x
    print('sum from 1 to ' + str(n) + ' is ' + str(sum))

sum()