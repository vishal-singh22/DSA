def spiralOrder(matrix):
    result = []
    if not matrix:  # Check if the matrix is empty
        return result

    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right on the topmost row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1  # Move the top boundary down

        # Traverse from top to bottom on the rightmost column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1  # Move the right boundary left

        if top <= bottom:
            # Traverse from right to left on the bottommost row
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1  # Move the bottom boundary up

        if left <= right:
            # Traverse from bottom to top on the leftmost column
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1  # Move the left boundary right

    return result
