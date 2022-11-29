def FibonacciSeries(number):
    previousNumber = 0
    currentNumber = 1
    for i in range (1,number):
        prepreviousNumber = previousNumber
        previousNumber = currentNumber
        currentNumber = prepreviousNumber + previousNumber
    return currentNumber

# def FibonacciSeriesRecursive(number): --> It takes much time as it performs same operation for multiple times.

#     if number == 0 or number == 1:
#         return number

#     else:
#         return FibonacciSeriesRecursive(number-1) + FibonacciSeriesRecursive(number-2)
    

if __name__ == "__main__":
    number = int(input("Enter any number to find Fibonacci Series: "))
    results = FibonacciSeries(number)
    print (f"Fibonacci Series of the number {number} is {results}.")
