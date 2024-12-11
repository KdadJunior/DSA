#################################

#Sum the diagonals of a 3D array. 
#Return 0 if the submatrix is not perfect. thus 3x3 or 2x2 or 4x4 etc

##################################

def sum_of_diagonals(matrix):
    total_sum = 0

    for sub_matrix in matrix:
        ROWS = len(sub_matrix)
        COLS = len(sub_matrix[0])

        if ROWS != COLS:
            return 0
        
        for i in range(ROWS):
            total_sum += sub_matrix[i][i]
            
    return total_sum