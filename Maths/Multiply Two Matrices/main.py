import numpy # --> We will use numpy.dot() to find multiplication of matrices.

def matrix(m,n): # function to get matrices.
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inputValue = int(input(f"Enter O({i}),({j}): "))
            row.append(inputValue)
        o.append(row)
    return(o)


if __name__ == "__main__":
    try:
        rows1 = int(input("Enter no of rows of first matrix: "))
        columns1 = int(input("Enter no of columns of first matrix: "))

        rows2 = int(input("Enter no of rows of second matrix: "))
        columns2 = int(input("Enter no of columns of second matrix: "))

        if columns1 == rows2: # --> Basic condition.

            print('Enter values of first matrix.') # --> Indicate user to enter value of first matrix.
            matrix1 = matrix(rows1,columns1)
            print(f'The first matrix is {matrix1}.')
            
            print('Enter values of second matrix.') # --> Indicate user to enter value of first matrix.
            matrix2 = matrix(rows2,columns2)
            print(f'The second matrix is {matrix2}.')

            multiplication = numpy.dot(matrix1,matrix2)
            print(f"The multiplication of the matrices {matrix1} and {matrix2} is {multiplication}.")
        
        else:
            print("Multiplication is not possible as no of columns of first matrix is not equal to number of rows of second matrix.")
        
    except:
        print("Invalid Entry")