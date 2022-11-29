if __name__ == "__main__":

    # Input numbers.
    firstNumber = int(input('Enter First number: '))
    secondNumber = int(input('EnterSecond number: '))

    maximumNumber = max(firstNumber,secondNumber) # --> Returns maximum number.
    
    # LCM is always greater or equal to the maximum number.
    while True:
        if maximumNumber%firstNumber==0 and maximumNumber%secondNumber==0:
            break
        maximumNumber += 1

    print (f'The LCM of {firstNumber} and {secondNumber} is {maximumNumber}.')