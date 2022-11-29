import time
from plyer import notification
from datetime import datetime


if __name__ == '__main__':
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    name = input ("Enter Your Name: ")

    print(f"Greetings! {name}.Your notification schedule is started. Don't forget to tell whether you have done the task or not after notification arrives.")

    time.sleep(60)
    
    while True:
        notification.notify (
            title = "Time to drink water.",
            message ='''Drinking Water Helps keeping you healthy. Don't Forget to tell have you drank or not..''',
            timeout= 10
        )

        num = 'valid' 


        while num == 'valid':
            value = input ("Please tell have you drank water or not (Yes or No): ")
            value = value.lower()
            

            if value == 'yes':
                with open(f"{name} Record.txt",'a') as f:
                    f.write (f"Drank water at {current_time}\n")
                num = "invalid"

            elif value == 'no':
                with open(f"{name} Record.txt",'a') as f:
                        f.write (f"Didn't drink water at {current_time}\n")
                num = "invalid"

            else:
                print("invalid number..Try Again.")



        time.sleep(60*15)
        
        notification.notify(
            title = "Time for some Eyes Exercise",
            message ='''Exercising your Eyes will prevent Lower eyesight. Don't Forget to tell have you done or not..''',
            timeout= 10
            )

        num1 = 'valid' 


        while num1 == 'valid':
            value = input ("Please tell have you done your eye exercise (Yes or No): ")
            value = value.lower()
            

            if value == 'yes':
                with open(f"{name} Record.txt",'a') as f:
                    f.write (f"Did eye exeercise at {current_time}\n")
                num1 = "invalid"

            elif value == 'no':
                with open(f"{name} Record.txt",'a') as f:
                        f.write (f"Didn't do eye exercise at {current_time}\n")
                num1 = "invalid"

            else:
                print("invalid number..Try Again.")


        time.sleep(60*30)

        notification.notify(
            title = "Time for some Physical Exercise",
            message ='''Exercise will keep you healthy.Don't Forget to tell have you done or not..''',
            timeout= 10
            )

        num3 = 'valid' 


        while num3 == 'valid':
            value = input ("Please tell have you physical exercise or not (Yes or No): ")
            value = value.lower()
            

            if value == 'yes':
                with open(f"{name} Record.txt",'a') as f:
                    f.write (f"Did Physical Exercise at {current_time}\n")
                num3 = "invalid"

            elif value == 'no':
                with open(f"{name} Record.txt",'a') as f:
                        f.write (f"Didn't do Physical Exercise at {current_time}\n")
                num3 = "invalid"

            else:
                print("invalid number..Try Again.")

        time.sleep(60*15)