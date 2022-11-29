def hcf():
    for i in range(1,smaller+1):
        if number1%i == 0 and number2%i == 0:
            highestCommonFactor = i
    return print(f"The hcf is {highestCommonFactor}.")


if __name__ == "__main__":

    number1 = int(input("Enter First number: "))
    number2 = int(input("Enter Second number: "))

    smaller = min(number1,number2) # --> Give Smaller Number

    hcf() # --> Function call.