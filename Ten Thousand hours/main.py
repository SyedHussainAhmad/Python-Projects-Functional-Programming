'''Program to calculate years equal to 10,000 hours based on hours per day.'''

hours = int(input("Enter hours per day: "))
DAYS = 7
WEEK = 52.1429 #Weeks in a year.
VALUE = 10000

calc = VALUE/(hours*DAYS*WEEK)
print(f'If you work {hours} hourse per day then you will complete {VALUE} hours in {calc} years.')
