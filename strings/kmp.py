def compute_prefix_function(string):
    p_function = [0]
    border = 0
    for i in range(1, len(string)):
        while border > 0 and string[border] != string[i]:
            border = p_function[border - 1]
        border = border + 1 if string[border] == string[i] else 0
        p_function.append(border)
    return p_function


def find_pattern(pattern, text):
    pattern_length = len(pattern)
    if pattern_length > len(text):
        return []
    indexes_of_overlaps = []
    str_for_kmp = pattern + '$' + text
    prefix_function = compute_prefix_function(str_for_kmp)
    for i in range(len(str_for_kmp)):
        if prefix_function[i] == pattern_length:
            indexes_of_overlaps.append(i - 2 * pattern_length)
    return indexes_of_overlaps


pattern = input()
text = input()
result = find_pattern(pattern, text)
print(" ".join(map(str, result)))
