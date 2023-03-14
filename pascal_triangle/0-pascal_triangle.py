#!/usr/bin/python3
"""
Generates Pascal's Triangle up to a given index.
"""

def generate_pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []
    triangle = [[1], [1, 1]]
    for i in range(2, n):
        prev_row = [0] + triangle[i - 1] + [0]
        row = []
        for j in range(0, len(prev_row) - 1):
            row.append(prev_row[j] + prev_row[j + 1])
        triangle.append(row)
    return triangle[:n]
