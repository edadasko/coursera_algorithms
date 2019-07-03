'''
Longest Common Subsequence of Two Sequences
Task. Given two sequences A = (a1, a2, ..., an) and B = (b1, b2, ..., bm),
      find the length of their longest common subsequence, i.e.,
      the largest non-negative integer p such that there exist indices
      1 ≤ i1 < i2 < ··· < ip ≤ n and 1 ≤ j1 < j2 < ··· < jp ≤ m, such that
      ai1 = bj1, ..., aip = bjp.
Input Format. First line: n. Second line: a1, a2, ..., an. Third line: m.
              Fourth line: b1, b2, ..., bm. Constraints. 1 ≤ n, m ≤ 100;
              −109 < ai, bi < 109.
Output Format. Output p.
'''

def lcs(a, b):
    l1 = len(a)
    l2 = len(b)
    table = [[0] for i in range(l1 + 1)]
    for j in range(1, l2 + 1):
        table[0].append(0)
    
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            if a[i - 1] == b[j - 1]:
                lcs = table[i - 1][j - 1] + 1
            else:
                lcs = max(table[i - 1][j], table[i][j - 1])
            table[i].append(lcs)
    return table[l1][l2]


n = input()
a = list(map(int, input().split()))
m = input()
b = list(map(int, input().split()))

print(lcs(a, b))
