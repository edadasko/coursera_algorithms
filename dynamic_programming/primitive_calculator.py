'''
Primitive Calculator.
Task. Given an integer n, compute the minimum number of operations needed
      to obtain the number n starting from the number 1.
Input Format. The input consists of a single integer 1 ≤ n ≤ 106.
Output Format. In the first line, output the minimum number k of
               operations needed to get n from 1. In the second line output
               a sequence of intermediate numbers. That is, the second line
               should contain positive integers a0,a2,..., a(k−1) such that
               a0 = 1,a(k−1) = n and for all 0 <= i < k−1,
               a(i+1) is equal to either ai + 1, 2ai, or 3ai.
               If there are many such sequences, output any one of them.
'''
import math

def optimal_sequence(n):
    prevs = [1]
    table = [0, 0]
    for i in range(2, n + 1):
        var_1 = table[i // 3] if i % 3 == 0 else math.inf
        var_2 = table[i // 2] if i % 2 == 0 else math.inf
        var_3 = table[i - 1]
        var = min(var_1, var_2, var_3)
        if var == var_1:
            prevs.append(i // 3)
        elif var == var_2:
            prevs.append(i // 2)
        else:
            prevs.append(i - 1)
        table.append(var + 1)
    sequence = [n]
    el = prevs[-1]
    while el != 1:
        sequence.append(el)
        el = prevs[el - 1]
    if n != 1:
        sequence.append(1)
    return sequence[::-1]


n = int(input())
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
