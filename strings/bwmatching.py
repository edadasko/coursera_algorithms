def preprocess_BWT(bwt):
    letters = ''.join(set(bwt))
    count_of_letters = len(letters)
    len_of_bwt = len(bwt)
    counts = [dict(zip(letters, [0] * count_of_letters))]
    for i in range(1, len_of_bwt + 1):
        counts.append(counts[-1].copy())
        counts[i][bwt[i - 1]] += 1
    sorted_bwt = sorted(bwt)
    starts = {c: sorted_bwt.index(c, ) for c in letters}
    return starts, counts


def count_occurrences(pattern, bwt, starts, occ_counts_before):
    n = len(bwt)
    top, bottom = 0, n - 1
    while top <= bottom and pattern:
        letter = pattern[-1]
        pattern = pattern[:-1]
        try:
            top = starts[letter] + occ_counts_before[top][letter]
            bottom = starts[letter] + occ_counts_before[bottom + 1][letter] - 1
        except KeyError:
            return 0
    return bottom - top + 1 if not pattern and top <= bottom else 0


bwt = input()
pattern_count = int(input())
patterns = input().split()
starts, occ_counts_before = preprocess_BWT(bwt)
occurrence_counts = []
for pattern in patterns:
    occurrence_counts.append(count_occurrences(pattern, bwt, starts, occ_counts_before))
print(' '.join(map(str, occurrence_counts)))
