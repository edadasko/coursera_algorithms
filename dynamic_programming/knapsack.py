'''
Task. Given n gold bars, find the maximum weight of gold that fits
      into a bag of capacity W .
Input Format. The first line of the input contains the capacity W of a knapsack and
              the number n of bars of gold. The next line contains n integers w0, w1, ...,
              wn − 1 defining the weights of the bars of gold.
Output Format. Output the maximum weight of gold that fits into a knapsack of capacity W.
'''

def optimal_weight(W, w):
    quantity = len(w)
    table = [[0] for i in range(quantity)]
    for j in range(1, W + 1):
        table[0].append(0 if j < w[0] else w[0])
    for i in range(1, quantity):
        for j in range(1, W + 1):
            if j >= w[i]:
                best = max(table[i - 1][j], table[i - 1][j - w[i]] + w[i])
            else:
                best = table[i - 1][j]
            table[i].append(best)
    return table[quantity - 1][W]


input = sys.stdin.read()
W, n, *w = list(map(int, input.split()))
print(optimal_weight(W, w))
