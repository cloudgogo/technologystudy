# -*- coding: utf-8 -*-
# def power(x):
#     return x * x

# print(power(15))
def power(x,n=2):
    s=1
    t=x
    while s<n:
        s=s+1
        x=x*t
    return x

print(power(5))
print(power(5,3))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3]))


def calcchangeparm(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calcchangeparm(1, 2, 3))
print(calcchangeparm())