##############################################

#A two dimensional array(matrix) that returns the transpose of the matrix

################################################

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []
    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(0)
        transpose.append(row)

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose