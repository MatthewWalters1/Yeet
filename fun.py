from random import randint

n = int(input("Enter a number: "))
list = [randint(0,n) for _ in range(n)]
print(list)