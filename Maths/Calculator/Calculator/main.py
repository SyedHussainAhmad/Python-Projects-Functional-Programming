class Calculator:

    def __init__(self):
        self.name = input('Enter your name: ')
        return    print (f"\nGreetings! {self.name}.")
        
    def add(self,num1,num2):
        return num1 + num2 

    def subtract(self,num1,num2):
        return num1 - num2 

    def multiply(self,num1,num2):
        return num1 * num2 

    def divide(self,num1,num2):
        return num1 / num2 

    def modulus (self,num1,num2):
        return num1 % num2 
    

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
            print (f'The division of {val1} and {val2} is {number.modulus(val1,val2)}.')
        

        elif value == 6:
            print("ThankYou! For using this calculator...")
            exit()

        else:
            print('Invalid Number..')
