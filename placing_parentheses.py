"""
Maximum Value of an Arithmetic Expression
Task: Find the maximum value of an arithmetic expression by specifying
      the order of applying its arithmetic operations using additional parentheses.
Input Format: The only line of the input contains a string s of length 2n + 1 for some n,
               with symbols s0, s1,..., s2n. Each symbol at an even position of s is a digit.
               (that is, an integer from 0 to 9) while each symbol at an odd position is one
               of three operations from {+ , — , *}.
Output Format: Output the maximum possible value of the given aritlnnetic expression among
               different orders of applying arithmetic operations.
"""
import math

max_table = []
min_table = []


def do_operation(a, b, operation):
    if operation == '*':
        return a * b
    elif operation == '+':
        return a + b
    else:
        return a - b


def get_max_and_min_of_subexpression(i, j, digits, operations):
    if i == j:
        return digits[i], digits[i]
    max_value = -math.inf
    min_value = math.inf
    for k in range(i, j):
        var_1 = do_operation(max_table[i][k], max_table[k + 1][j], operations[k])
        var_2 = do_operation(max_table[i][k], min_table[k + 1][j], operations[k])
        var_3 = do_operation(min_table[i][k], max_table[k + 1][j], operations[k])
        var_4 = do_operation(min_table[i][k], min_table[k + 1][j], operations[k])
        max_value = max(max_value, var_1, var_2, var_3, var_4)
        min_value = min(min_value, var_1, var_2, var_3, var_4)
    return max_value, min_value


def get_maximum_value(digits, operations):
    num_of_digits = len(digits)
    global max_table, min_table
    max_table = [[0 for j in range(num_of_digits)] for i in range(num_of_digits)]
    min_table = [[0 for j in range(num_of_digits)] for i in range(num_of_digits)]
    
    for size in range(num_of_digits):
        for i in range(num_of_digits - size):
            j = i + size
            max_table[i][j], min_table[i][j] = get_max_and_min_of_subexpression(i, j, digits, operations)

    return max_table[0][num_of_digits - 1]


s = input()
operations = [s[i] for i in range(1, len(s), 2)]
digits = [int(s[i]) for i in range(0, len(s), 2)]
print(get_maximum_value(digits, operations))
