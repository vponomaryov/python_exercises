"""
We have NxM matrix.
Need to be able to turn it for either left or right.

 1 2 3   _   7 4 1   _   9 8 7    _   7 4 1
 4 5 6  / \  8 5 2  / \  6 5 4   / \  8 5 2
 7 8 9   </  9 6 3   </  3 2 1   \>   9 6 3
"""

m = [
    ['a',  1,   2,   3,  4],
    [ 5, 'b',   6,   7,  8],
    [ 9,  10, 'c',  11, 12],
    [13,  14,  15, 'd', 16],
]
m_right = [
    [ 13,   9,   5, 'a'],
    [ 14,  10, 'b',   1],
    [ 15, 'c',   6,   2],
    ['d',  11,   7,   3],
    [ 16,  12,   8,   4],
]


def turn_matrix(m, to_right=True):
    new_m = [[] for i in range(len(m[0]))]
    if to_right:
        j_start, j_stop, j_step = 0, len(m[0]), 1
    else:
        j_start, j_stop, j_step = len(m[0]) - 1, -1, -1
    for i in range(len(m)):
        for j in range(j_start, j_stop, j_step):
            if to_right:
                new_m[j].insert(0, m[i][j])
            else:
                new_m[j_stop - j].append(m[i][j])
    return new_m


print(m)
print(turn_matrix(m))
print(turn_matrix(m_right, False))
assert turn_matrix(m) == m_right
assert turn_matrix(m_right, False) == m
