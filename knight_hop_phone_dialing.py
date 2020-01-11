"""
One of Google excercises:

Imagine you place a knight chess piece on a phone dial pad.
This chess piece moves in an uppercase "L" shape.
Two steps horizontally followed by one vertically
or one step horizontally then two vertically:

|->1| 2 | 3 |    | 1 | 2 | 3 |    | 1 | 2 | 3 |    | 1 | 2 | 3 |
| 4 | 5 | 6 | => | 4 | 5 |->6| => | 4 | 5 | 6 | => |->4| 5 | 6 | => ...
| 7 | 8 | 9 |    | 7 | 8 | 9 |    | 7 | 8 | 9 |    | 7 | 8 | 9 |
|   | 0 |   |    |   | 0 |   |    |   |->0|   |    |   | 0 |   |

      1       =>       6       =>       0       =>       4       => ...

Suppose you dial keys on the keypad using only hops a knight can make.
Every time the knight lands on a key, we dial that key and make another hop.
The starting position counts as being dialed.

How many distinct numbers can you dial in N hops from a particular
starting position?
"""

import time


try:
    xrange
except NameError:
    xrange = range


# ============ First variant ===========
# Recursion, calculation and momoization

matrix_for_recursion = {
    '1379': ((2, 4), 2),
    '28': ((1, 1), 2),
    '46': ((1, 1, 0), 3),
    '0': ((4, 4), 2),
}


def get_recursion_steps(depth=1111, step=250):
    return list(xrange(step, depth, step)) + [depth]


def count_combinations(starting_index=1, combination_length=3, memo={}):
    """Count knight hop combinations using calculation and recursion."""

    if combination_length == 1 or starting_index == 5:
        return 1
    mi = indexes[starting_index]
    starting_index_group_key = starting_index_group_keys[mi]
    if combination_length == 2:
        return matrix_for_recursion[starting_index_group_key][1]
    if starting_index not in xrange(10):
        raise ValueError('Only simple digits are allowed')
    if combination_length < 1:
        raise ValueError('Only positive combination length is allowed')

    combinations = 0
    for cur_combination_length in get_recursion_steps(combination_length):
        for i in matrix_for_recursion[starting_index_group_key][0]:
            cur_len = cur_combination_length - 1
            if (i, cur_len) not in memo:
                memo[(i, cur_len)] = count_combinations(i, cur_len)
    for i in matrix_for_recursion[starting_index_group_key][0]:
        combinations += memo[(i, cur_combination_length - 1)]
    return combinations

# ================= Second variant ==================
# Ariphemitic progression calculation and memoization

# starting_point: matrix_index, starting_sum
indexes = {1: 0, 3: 0, 7: 0, 9: 0, 2: 1, 8: 1, 4: 2, 6: 2, 0: 3}
matrix = (
    [2, 5, 10, 26],  # 1, 3, 7, 9
    [2, 4, 10, 20],  # 2, 8
    [3, 6, 16, 32],  # 4, 6
    [2, 6, 12, 32],  # 0
)
starting_index_group_keys = ('1379', '28', '46', '0')
starting_sum = (
    (
        matrix[0][0] + 0,
        matrix[1][0] + 0,
        matrix[2][0] + 1,
        matrix[3][0] + 2,
    ), (
        matrix[0][1] + 1,
        matrix[1][1] + 0,
        matrix[2][1] + 2,
        matrix[3][1] + 2,
    )
)


def count_combinations2(starting_index=1, combination_length=3, memo={}):
    """Count knight hop combinations using ariphmetic progression."""

    if combination_length == 1 or starting_index == 5:
        return 1
    if starting_index not in xrange(10):
        raise ValueError('Only simple digits are allowed')
    if combination_length < 1:
        raise ValueError('Only positive combination length is allowed')

    mi = indexes[starting_index]
    if len(matrix) + 1 >= combination_length:
        return matrix[mi][combination_length + 2]

    starting_index_group_key = starting_index_group_keys[mi]
    if (starting_index_group_key, combination_length) in memo:
        return memo[(starting_index_group_key, combination_length)][0]

    if not memo:
        for m_group_index, m_group_data in enumerate(matrix):
            sig_key = starting_index_group_keys[m_group_index]
            for i in xrange(2, len(m_group_data) + 2):
                if (sig_key, i) in memo:
                    continue
                memo[(sig_key, i)] = (
                    m_group_data[i - 2],
                    (starting_sum[i % 2][m_group_index] if i > 2 else 0),
                )

    for i in xrange(
            max(len(memo) - 10, len(matrix[0]) + 2), combination_length + 2):
        for sig_key in starting_index_group_keys:
            if (sig_key, i) in memo:
                continue
            memo[(sig_key, i)] = (
                5 * memo[(sig_key, i - 2)][0] + memo[(sig_key, i - 2)][1],
                sum(memo[(sig_key, i - 2)])
            )
    
    return memo[(starting_index_group_key, combination_length)][0]


# ==== Run both variants of knight hops combinations ====
for combinations_length in (3010, 3011):
    print("\ncombinations_length: %s" % combinations_length)
    for i in (1, 2, 4, 0):
        print("Starting_index: %s" % i)
        for run in ("First", "Second"):
            start = time.time()
            r = count_combinations(i, combinations_length)
            end = time.time()
            print("%9s run, Recursion%s: %s" % (run, " " * 13, end - start))
            start = time.time()
            a = count_combinations2(i, combinations_length)
            end = time.time()
            print("%sAriphmetic progression: %s" % (" " * 15, end - start))
            assert r == a
        print("")
