def build_trie(patterns):
    if not patterns:
        return
    trie = {0: {patterns[0][0]: 1}}
    num_of_last_letter = 1
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            if current_node in trie and pattern[i] in trie[current_node]:
                current_node = trie[current_node][pattern[i]]
            else:
                while i < len(pattern):
                    if current_node not in trie:
                        trie[current_node] = {}
                    num_of_last_letter += 1
                    trie[current_node][pattern[i]] = num_of_last_letter
                    current_node = num_of_last_letter
                    i += 1
                break
    return trie


n = int(input())
patterns = [input() for _ in range(n)]
trie = build_trie(patterns)
for node in trie:
    for c in trie[node]:
        print("{}->{}:{}".format(node, trie[node][c], c))
