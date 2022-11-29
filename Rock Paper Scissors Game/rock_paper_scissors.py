import random


def game(computer,you):
    if (comp=='r' and you == 'w') or (comp=='p' and you=='r') or (comp=='s' and you=='r'):
        print ('Computer wins')
    elif(you=='r' and comp == 's') or (you=='p' and comp=='r') or (you=='s' and comp=='p'):
        print ('Congratulations! You are a winner.')
    elif comp==you or you == None:
        print ('This is a tie')
    else:
        print ('Invalid')
    
random_no = random.randint(1,3)

if random_no==1:
    comp="r"
elif random_no==2:
    comp="p"
elif random_no==3:
    comp="s"

print("'Here's the computer turn.. ")
you = input('Your: Rock(r),Paper(p),Scissors(s):\n')

print (f"Computer choose {comp}")
print (f"You choose {you}")

result= game(comp,you)
print(result)