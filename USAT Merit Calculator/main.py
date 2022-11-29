# Program to calculate the merit percentage of USAT test.

def calculateMerit(matricMarks, interMarks, usatMarks):
    calculation = (((matricMarks/1100)*0.25) +
                   ((interMarks/1100) * 0.45) + ((usatMarks/100)*0.30))*100
    return calculation


if __name__ == "__main__":
    matricMarks = int(input("Enter your matric marks: "))
    interMarks = int(input("Enter your intermediate marks: "))
    usatMarks = int(input("Enter your usat marks: "))
    result = calculateMerit(matricMarks, interMarks, usatMarks)
    print(f"The result is {result}")
