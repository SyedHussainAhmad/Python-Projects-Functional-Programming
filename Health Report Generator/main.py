from datetime import datetime


now = datetime.now()
time = now.strftime("%d/%m/%Y %H:%M:%S")

name = input ("Enter Your Name: ")

while (True):
    welcomeMsg = '''\n~~~~ Welcome to the Health Report Generator ~~~~
    Please select an option:
    1: Write about exercise.
    2: Write about Diet.
    3: Retrieve Exercise Report.
    4: Retrieve Exercise Diet.
    5: Exit  \n
    '''

    print (welcomeMsg)

    value = int(input('Enter your choice: '))

    if value == 1:
        exercise = input("Enter Exercise: ")
        
        with open (f"Exerise Report of {name}.txt","a") as f:
            f.write (f"{exercise}   {time}\n")
    elif value == 2:
        diet = input("Enter Diet: ")
        
        with open (f"Diet Report of {name}.txt","a") as f:
            f.write (f"{diet},   {time}\n")
    
    elif value == 3:
        try:
            with open (f"Exerise Report of {name}.txt") as f:
                data = f.read()
                print (data)
        except:
            print("You are a new user or you have not input any of your Exercise. Please write about exercise first.")

    elif value == 4:
        try:
            with open (f"Diet Report of {name}.txt") as f:
                data = f.read()
                print (data)
        except:
            print("You are a new user or you have not input any of your diet. Please write about diet first.")


    elif value == 5:
        print("ThankYou! For using our services..")
        exit()

    else:
        print("Invalid Input..")