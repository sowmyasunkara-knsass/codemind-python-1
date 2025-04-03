def added(A,B):
    return[[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
def main():
    A = [[1,2,3],[4,5,6]]
    B = [[3,2,1],[7,5,3],[1,2,3]]
    add = added(A,transpose(B))
    for row in add:
        print(row)
if __name__=="-main-":
    main()
