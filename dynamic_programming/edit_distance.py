'''
Edit Distance
Task. The goal of this problem is to implement the algorithm for computing
      the edit distance between two strings.
Input Format. Each of the two lines of the input contains a string consisting
              of lower case latin letters.
Output Format. Output the edit distance between the given two strings.
'''

def edit_distance(s, t):
    l1 = len(s)
    l2 = len(t)
    table = [[i] for i in range(l1 + 1)]
    for j in range(1, l2 + 1):
        table[0].append(j)
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            var_1 = table[i - 1][j] + 1
            var_2 = table[i][j - 1] + 1
            var_3 = table[i - 1][j - 1]
            if s[i - 1] != t[j - 1]:
                var_3 += 1
            var = min(var_1, var_2, var_3)
            table[i].append(var)
    return table[l1][l2]

print(edit_distance(input(), input()))
