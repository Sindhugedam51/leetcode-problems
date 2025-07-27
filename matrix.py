
'''import numpy as np 
matrix1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
result =  matrix1 + matrix2
print("matrix1 :")
print(matrix1)
print("\n matrix2: ")
print(matrix2)
print("\n result of the matrix addition:")
print(result)
'''
'''
def generate_sprial_matrix(n):
    matrix = [[0] * n for k in range(n)]
    start_row, end_row = 0, n - 1
    start_col, end_col = 0, n - 1
    counter = 1
    while start_row <= end_row and start_col <= end_col:
        
        for i in range(start_col,end_col + 1):
            matrix[start_row][i] = counter
            counter +=1
        start_row += 1
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = counter
            counter += 1
        end_col -= 1
        if start_row <=end_row:
            for i in range(end_col,start_col - 1, -1):
                matrix[end_row][i] = counter
                counter += 1
            end_row -= 1
        if start_col <= end_col:
            for i in range(end_row,start_row - 1, -1):
                matrix[i][start_col] = counter
                counter += 1
            start_col += 1
    return matrix
n = int(input("enter the size of the sprial:"))
sprial_matrix = generate_sprial_matrix(n)
print("sprial matrix: ")
for row in sprial_matrix:
    print(row)              '''
 #user will give the elements   
 
def sprial_traversal(matrix, n):
   
    start_row, end_row = 0, n - 1
    start_col, end_col = 0, n - 1
    result = []
    while start_row <= end_row and start_col <= end_col:
        
        for i in range(start_col,end_col + 1):
            
            result.append(matrix[start_row][i])
        start_row += 1
        for i in range(start_row, end_row + 1):
            
            result.append(matrix[i][end_col])
        end_col -= 1
        if start_row <=end_row:
            for i in range(end_col,start_col - 1, -1):
                
                result.append(matrix[i][start_row])
            end_row -= 1
        if start_col <= end_col:
            for i in range(end_row,start_row - 1, -1):
                result.append(matrix[i][start_col]) 
                
            start_col += 1
    return result
n = int(input("enter the size of the matrix:"))
matrix = []
print("enter the matrix row-size:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
sprial_order = sprial_traversal(matrix,n)
print("\nsprial Order Trversal: ")
print(sprial_order)


