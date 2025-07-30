


# pascal triangle.py

def generate_pascals_triangle(n):
    """Generate Pascal's Triangle up to the nth row."""
    triangle = []

    for i in range(n):
        row = [1] * (i + 1)  # Start with a row of 1s
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle 

n = 5  # Change this value to generate more rows
pascals_triangle = generate_pascals_triangle(n)
for row in pascals_triangle:
    print(row)

# You are given an n x n 2D matrix representing an image. Rotate the image by 90 degrees clockwise. The rotation should be done in-place, meaning you have to modify the input matrix directly without using any additional matrix for storage.


# Input: matrix = [[5, 1, 9, 11],
#                  [2, 4, 8, 10],
#                  [13, 3, 6, 7],
#                  [15, 14, 12, 16]]
# Output: [[15, 13, 2, 5],
#          [14, 3, 4, 1],
#          [12, 6, 8, 9],
#          [16, 7, 10, 11]]

def rotate_matrix(matrix):
    """Rotate the given n x n matrix by 90 degrees clockwise."""
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()


triangle = []

for i in range(5):
    row = [1] * (i + 1)
    for j in range(1,i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)
print(triangle)

for  i in range(len(matrix)):
    for j in range(i ,len(matrix)):
        matrix[i][j], matrix[j][i]= matrix[j][i],matrix[i][j]
for i in range(len(matrix)):
    matrix[i].reverse()


# Input: mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]], target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
# Output: True
 
# Input: mat = [[0, 1], [1, 1]], target = [[1, 0], [0, 1]]
# Output: False

# You are given two n x n binary matrices mat and target. Your task is to determine whether it is possible to make mat equal to target by rotating mat in 90-degree increments (clockwise). You can rotate mat by 90, 180, or 270 degrees, or leave it unchanged.

# def can_transform(mat, target):
#     """Check if mat can be transformed to target by rotating."""
#     def rotate(matrix):
#         n = len(matrix)
#         for i in range(n):
#             for j in range(i, n):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         for i in range(n):
#             matrix[i].reverse()

#     for _ in range(4):  # Check all 4 rotations
#         if mat == target:
#             return True
#         rotate(mat)

#     return False



# n MATLAB, there is a handy function called reshape that reshapes a matrix of dimensions m x n into a new one with a different size r x c keeping its original data in row-traversing order.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and columns of the wanted reshaped matrix. The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with the given parameters is possible and legal, output the new reshaped matrix. Otherwise, output the original matrix.



# Input Parameters:

# mat (List[List[int]]): A 2D list representing an m x n matrix.

# r (int): The number of rows for the reshaped matrix.

# c (int): The number of columns for the reshaped matrix.



# Output:

# List[List[int]]: The reshaped matrix or the original matrix if reshaping isn't possible.



# Example:

# Input: mat = [[1, 2], [3, 4]], r = 1, c = 4
# Output: [[1, 2, 3, 4]]
 
# Input: mat = [[1, 2], [3, 4]], r = 2, c = 4
# Output: [[1, 2], [3, 4]]


def reshape_matrix(mat, r, c):
    """Reshape the given matrix to r x c if possible."""
    m = len(mat)
    n = len(mat[0]) if m > 0 else 0
    
    if m * n != r * c:
        return mat  # Reshaping not possible, return original matrix
    
    flat_list = [item for row in mat for item in row]  # Flatten the matrix
    reshaped_matrix = []
    
    for i in range(r):
        reshaped_matrix.append(flat_list[i * c:(i + 1) * c])
    
    return reshaped_matrix
# Example usage
mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(reshape_matrix(mat, r, c))
