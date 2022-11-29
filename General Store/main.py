sum = 0

welcomeMsg = '''~~~Welcome to the Calculator~~~'''    
print (welcomeMsg)

while True:

    numbers = input("Enter the price or Press q to quit: ")

    if numbers != 'q':

        sum = sum + int(numbers)
        print(f'Order total so far {sum}.')

    if numbers == 'q':

        print(f'Your Total Bill is Rs\{sum}.')
        print ('ThankYou! for shopping with us..')
        exit()