import math
from functools import reduce


def vector_add(v, w):
    """adds corresponding elements"""
    return [vi + wi for vi, wi in zip(v, w)]

def vector_subtract(v, w):
    """subtracts corresponding elements"""
    return [vi - wi for vi, wi in zip(v, w)]

def vector_sum(vectors):
    """sums all corresponding elements"""
    return reduce(vector_add, vectors)

def scalar_multiply(c, v):
    """c is a number, v is a vector"""
    return [c * vi for vi in v]

def vector_mean(vectors):
    """compute the vector whose ith element is the mean of the
        ith elements of the input vectors"""
    return scalar_multiply(1/ len(vectors), vector_sum(vectors))

def dot(v, w):
    """v1 * w1 + ... + vn * wn"""
    return sum(vi * wi for vi, wi in zip(v, w))

def sum_of_squares(v):
    """v1 * v1 + ... + vn * vn"""
    return dot(v, v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v, w):
    """(v1 - w1) ** 2 + ... + (vn - wn) ** 2"""
    return sum_of_squares(vector_subtract(v, w))

def distance(v, w):
#     return math.sqrt(squared_distance(v, w))
    return magnitude(vector_subtract(v, w))

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return (num_rows, num_cols)

def get_row(A, i):
    return A[i]

def get_col(A, j):
    return [Ai[j] for Ai in A]

def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix
        whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

def is_diagonal(i, j):
    """1's on the 'diagonal', 0's everywhere else"""
    return 1 if i == j else 0

