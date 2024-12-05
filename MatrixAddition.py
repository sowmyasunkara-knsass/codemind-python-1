rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter the elements of the first matrix:")
matrix1 = [list(map(int, input().split())) for _ in range(rows)]

print("Enter the elements of the second matrix:")
matrix2 = [list(map(int, input().split())) for _ in range(rows)]

result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]

print("The resulting matrix after addition is:")
for row in result:
    print(' '.join(map(str, row)))
