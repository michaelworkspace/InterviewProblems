""" A basic algorithm for creating a matrix using user inputs. """

# Get the number of rows and columns from the user
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

# Initilize the matrix
matrix = []
print("Enter the entries row-wise:\n")

# For user input
for i in range(rows):
    a = []
    for j in range(columns):
        a.append(int(input()))
    matrix.append(a)

# Printing the matrix
for i in range(rows):
    print()  # Print a new line for every row entries
    for j in range(columns):
        print(matrix[i][j], end=" ")
