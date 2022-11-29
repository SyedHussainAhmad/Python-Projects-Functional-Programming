def armstrong(number):
    copyNumber = number
    sum = 0
    power = len(str(number))

    while number > 0:
        digit = number % 10
        sum += digit ** power
        number = number // 10

    if sum == copyNumber:
        return True
    else:
        return False

if __name__ == "__main__":
    
    number = int(input('Enter any number: '))
    check = armstrong(number)

    if check:
        print(f"{number} is an armstrong number.")
    else:
        print(f"{number} is not an armstrong number.")