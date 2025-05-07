# Task 1: Calculate Factorial Using a Function

a = input('Enter a number: ')

a = int(a)

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a - 1)


print('Factorial of', a, 'is: ', factorial(a))
