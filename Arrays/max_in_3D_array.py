def max_in_3D_array(matrix):
    max_value = float('-inf')

    for layer in matrix:
        for row in layer:
            for element in row:
                if element > max_value:
                    max_value = element
    return max_value