def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    ROWS = len(matrix)
    COLS = len(matrix[0])

    top_row = 0
    bot_row = ROWS - 1
    while top_row <= bot_row:
        mid_row = (top_row + bot_row) // 2
        if target > matrix[mid_row][-1]:
            top_row = mid_row + 1
        elif target < matrix[mid_row][0]:
            bot_row = mid_row - 1
        else:
            break

    if not (top_row <= bot_row):
        return False
    left = 0
    right = COLS - 1     #Assuming it's a perfect matrix, thus 3x3, 2x2, 4x4
    mid = (left + right) // 2
    while left <= right:
        if target > mid:
            left = mid + 1
        elif target < mid:
            right = mid - 1
        else:
            return True
    return False