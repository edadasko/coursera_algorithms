def build_trie(patterns):
    if not patterns:
        return
    trie = {0: {patterns[0][0]: 1}}
    num_of_last_letter = 1
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            if trie.get(current_node, None) is not None and \
                trie[current_node].get(pattern[i], None) is not None:
                    current_node = trie[current_node][pattern[i]]
            else:
                while i < len(pattern):
                    if trie.get(current_node, None) is None:
                        trie[current_node] = {}
                    num_of_last_letter += 1
                    trie[current_node][pattern[i]] = num_of_last_letter
                    current_node = num_of_last_letter
                    i += 1
                break
        else:
            if len(trie) > 1:
                del trie[current_node]
    return trie


def check_patterns(text, trie):
    positions = []
    for i in range(len(text)):
        if is_matching(i, text, trie):
            positions.append(i)
    return positions


def is_matching(index, text, trie):
    current_node = 0
    while trie.get(current_node, None) is not None and index < len(text):
        current_node = trie[current_node].get(text[index], None)
        index += 1
        if not current_node:
            return False
    return trie.get(current_node, None) is None


text = input()
n = int(input())
patterns = [input() for _ in range(n)]
patterns.sort(reverse=True)
trie = build_trie(patterns)
print(' '.join(map(str, (check_patterns(text, trie)))))

