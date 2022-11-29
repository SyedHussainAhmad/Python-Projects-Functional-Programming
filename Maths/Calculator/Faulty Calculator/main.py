# This is a faulty Calculator to avoid cheating..

# Faults are:
# 56 * random number
# 77 + random number
# 8 % random number
# 99 - random number

import random

class Calculator:

    randomNo = random.randint(1,100)

    def __init__(self):
        self.name = input('Enter your name: ')
        return    print (f"\nGreetings! {self.name}.")
        

    def add(self,num1,num2):
        self.a = num1
        self.b = num2

        if num1 == 77 or num2 == 77:
            return self.a+self.randomNo
        else:
            return self.a + self.b
    
    def subtract(self,num1,num2):
        self.a = num1
        self.b = num2

        if num1 == 99 or num2 == 99:
            return self.a - self.randomNo
        else:
            return self.a - self.b
    
    def multiply(self,num1,num2):
        self.a = num1
        self.b = num2

        if num1 == 56 or num2 == 56:
            return self.a*self.randomNo
        else:
            return self.a * self.b

    def divide(self,num1,num2):
        self.a = num1
        self.b = num2

        if num1 == 7 or num2 == 7:
            return self.b/self.randomNo
        else:
            return self.a / self.b
    
    def modulus(self,num1,num2):
        self.a = num1
        self.b = num2

        if num1 == 8 or num2 == 8:
            return self.a%self.randomNo
        else:
            return self.a % self.b

if __name__ == "__main__":

    number = Calculator()

    while True:
        welcomeMessage = ''' 
        ~~~ Welcome to the Calcutor. ~~~ 

        Please choose an action:
        1: Addition.
        2: Subtraction.
        3: Multiplication.
        4: Division. 
        5: Modulus/Remainder.
        6: Exit.
        \n'''

        print(welcomeMessage)
        
        value = int(input("Enter your choice: "))

        if value ==1:
            val1 = int(input('Enter First Number: '))
            val2 = int(input('Enter Second Number: '))
            print (f'The sum of {val1} and {val2} is {number.add(val1,val2)}.')

        elif value == 2:
            val1 = int(input('Enter First Number: '))
            val2 = int(input('Enter Second Number: '))
            print (f'The difference of {val1} and {val2} is {number.subtract(val1,val2)}.')

            
        elif value == 3:
            val1 = int(input('Enter First Number: '))
            val2 = int(input('Enter Second Number: '))
            print (f'The product of {val1} and {val2} is {number.multiply(val1,val2)}.')

        elif value == 4:
            val1 = int(input('Enter First Number: '))
            val2 = int(input('Enter Second Number: '))
            print (f'The division of {val1} and {val2} is {number.divide(val1,val2)}.')

        
        elif value == 5:
            val1 = int(input('Enter First Number: '))
            val2 = int(input('Enter Second Number: '))
            print (f'The Modulus/Remainder of {val1} and {val2} is {number.modulus(val1,val2)}.')
        

        elif value == 6:
            print("ThankYou! For using this calculator...")
            exit()

        else:
            print('Invalid Number..')
