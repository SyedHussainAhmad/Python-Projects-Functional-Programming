def matrix(m,n):
    o = []
    for i in range(m):
        row = []
        for j in range(n):
            inputValue = int(input(f"Enter O({i}),({j}): "))
            row.append(inputValue)
        o.append(row)
    return(o)

def sum(matrix1,matrix2):
    output = []
    for i in range(len(matrix1)): # number of rows
        row = []
        for j in range(len(matrix1[0])): # number of columns
            row.append(matrix1[i][j] + matrix2[i][j])
        output.append(row)
    return output


if __name__ == "__main__":
    try:
        m = int(input("Enter no of rows : "))
        n = int(input("Enter no of columns : "))

        print('Enter values of first matrix.') # --> Indicate user to enter value of first matrix.
        matrix1 = matrix(m,n)
        print(f'The first matrix is {matrix1}.')
        
        print('Enter values of second matrix.') # --> Indicate user to enter value of first matrix.
        matrix2 = matrix(m,n)
        print(f'The second matrix is {matrix1}.')

        addition = sum(matrix1,matrix2)
        print(f"The addition of the matrices {matrix1} and {matrix2} is {addition}.")
    
    except:
        print("Invalid Entry")