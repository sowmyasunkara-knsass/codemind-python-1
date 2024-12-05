rows1 = int(input("Enter the number of rows for the first matrix: "))
cols1 = int(input("Enter the number of columns for the first matrix: "))
print("Enter the elements of the first matrix:")
matrix1 = [list(map(int, input().split())) for _ in range(rows1)]

rows2 = int(input("Enter the number of rows for the second matrix: "))
cols2 = int(input("Enter the number of columns for the second matrix: "))
print("Enter the elements of the second matrix:")
matrix2 = [list(map(int, input().split())) for _ in range(rows2)]

if cols1 != rows2:
    print("Matrix multiplication not possible.")
else:
    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(cols1)) for j in range(cols2)] for i in range(rows1)]
    print("The resulting matrix after multiplication is:")
    for row in result:
        print(' '.join(map(str, row)))
