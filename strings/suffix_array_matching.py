size_of_alphabet = 5

from_char_to_int = {'$': 0, 'A': 1, 'C': 2, 'G': 3, 'T': 4}
from_int_to_char = {v: k for k, v in from_char_to_int.items()}


def check_patterns(text, suffix_array, patterns):
    answer = set()
    for pattern in patterns:
        answer |= set(find_pattern(text, pattern, suffix_array))
    return list(answer)


def find_pattern(text, pattern, suffix_array):
    min_index = 0
    max_index = len(text)
    pattern_len = len(pattern)
    while min_index < max_index:
        mid_index = (min_index + max_index) // 2
        if pattern > text[suffix_array[mid_index]:suffix_array[mid_index] + pattern_len]:
            min_index = mid_index + 1
        else:
            max_index = mid_index
    start = min_index
    max_index = len(text)
    while min_index < max_index:
        mid_index = (min_index + max_index) // 2
        if pattern < text[suffix_array[mid_index]:suffix_array[mid_index] + pattern_len]:
            max_index = mid_index
        else:
            min_index = mid_index + 1
    end = max_index
    return suffix_array[start:end]


def build_suffix_array(text):
    order = sort_chars(text)
    classes = compute_char_classes(text, order)
    L = 1
    while L < len(text):
        order = sort_doubled(text, L, order, classes)
        classes = update_classes(order, classes, L)
        L *= 2
    return order


def sort_chars(s):
    order = [0] * len(s)
    count = [0] * size_of_alphabet
    for c in s:
        count[from_char_to_int[c]] += 1
    for i in range(1, size_of_alphabet):
        count[i] += count[i - 1]
    for i in range(len(s) - 1, -1, -1):
        c = s[i]
        count[from_char_to_int[c]] -= 1
        order[count[from_char_to_int[c]]] = i
    return order


def compute_char_classes(s, order):
    len_s = len(s)
    classes = [0] * len_s
    for i in range(1, len_s):
        classes[order[i]] = classes[order[i - 1]] if s[order[i]] == s[order[i - 1]] \
            else classes[order[i - 1]] + 1
    return classes


def sort_doubled(s, L, order, classes):
    len_s = len(s)
    count = [0] * len_s
    new_order = [0] * len_s
    for cl in classes:
        count[cl] += 1
    for i in range(1, len_s):
        count[i] += count[i - 1]
    for i in range(len_s - 1, -1, -1):
        start = (order[i] - L + len_s) % len_s
        cl = classes[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def update_classes(new_order, classes, L):
    len_s = len(new_order)
    new_classes = [0] * len_s
    for i in range(1, len_s):
        cur, prev = new_order[i], new_order[i - 1]
        mid, prev_mid = (cur + L) % len_s, (prev + L) % len_s
        if classes[cur] != classes[prev] or classes[mid] != classes[prev_mid]:
            new_classes[cur] = new_classes[prev] + 1
        else:
            new_classes[cur] = new_classes[prev]
    return new_classes


text = input()
text += '$'
suffix_array = build_suffix_array(text)
n = input()
patterns = input().split()
print(" ".join(map(str, check_patterns(text, suffix_array, patterns))))
