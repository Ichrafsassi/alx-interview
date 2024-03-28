#!/usr/bin/python3
"""pascal_triangle module"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        # Create a new row with 1s at the ends
        row = [1] + [0] * (i - 1) + [1]

        # Calculate remaining elements using the previous row
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        # Add the completed row to the triangle
        triangle.append(row)

    return triangle
