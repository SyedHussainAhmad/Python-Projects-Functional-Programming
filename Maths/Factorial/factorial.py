# Recursion offen produces memory error when manupulating large numbers..

def fact():
    multiply = 1
    try:
        number = int(input('Enter any number: '))
        for i in range(1,number+1):
            multiply = multiply*i
        print (f'The facorial of the given number is {multiply}.')

    except:
        print('Invalid number..')

def recursiveFactorial(number):
    try:

        if number == 0 or number == 1:
            return 1

        else:
            return number * recursiveFactorial (number -1)

    except:
        print("Invalid Number..")

def factTrailingZeros(number):
    count = 0
    prime = 5

    while (number // prime != 0):
        count += int (number /prime)
        prime = prime*5
    return count


if __name__ == '__main__':

    num = int (input("Enter any number: "))
    factor = factTrailingZeros(num)

    if factor == 1:
        print (f'The number of trailing zeros in the factorial is {factor}.')
    else:
        print (f'The number of trailing zeros in the factorial are {factor}.')
