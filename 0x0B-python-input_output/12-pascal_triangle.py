#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents Pascal's Triange of size n.

    Args:
        n (int): Size of the pascal triangle.

    Returns:
        list: List of lists of integers representing the pascal triange.
    """

    if n <= 0:
        return ({})
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(tri[i] + tri[i + 1])
        temp.append(1)
        triangles.append(temp)
    return (triangles)
