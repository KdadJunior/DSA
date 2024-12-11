###################################################

#You are given a 3D matrix of size 𝑁×𝑁×𝑁 representing a cube.
# Write a function to rotate the cube 90 degrees clockwise along the Z-axis.
# The rotation should be performed layer by layer, with each 2D layer being rotated independently.

#####################################################

def rotate_2D_matrix(matrix_2D):
    N = len(matrix_2D)
    rotated = []
    for i in range(N):
        row = [0] * N
        rotated.append(row)

    for i in range(N):
        for j in range(N):
            rotated[j][N - i -1] = matrix_2D[i][j]

    return rotated

def rotated_3D_matrix(matrix_3D):
    N = len(matrix_3D)
    for i in range(N):
        matrix_3D[i] = rotate_2D_matrix(matrix_3D[i])

    return matrix_3D