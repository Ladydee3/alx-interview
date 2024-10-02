#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of intergers representing the pascal's triangle of n:
    Returns an empty list if n <= 0
    You can assume n will be always an integer

    """


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to n rows.
    
    Args:
    n (int): The number of rows of the triangle.

    Returns:
    list of lists: Pascal's triangle with n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the triangle with the first row
    
    for row_num in range(1, n):
        prev_row = triangle[-1]  # Get the last row of the current triangle
        new_row = [1]  # Start each row with 1
        
        # Calculate the in-between values
        for i in range(1, row_num):
            new_row.append(prev_row[i-1] + prev_row[i])

        new_row.append(1)  # End each row with 1
        triangle.append(new_row)
    
    return triangle

# Test the function using the provided script
def print_triangle(triangle):
    """
    Print the triangle in the required format.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

