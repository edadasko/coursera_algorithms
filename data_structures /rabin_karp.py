'''
Find pattern in text
Task. In this problem your goal is to implement the Rabin–Karp’s
      algorithm for searching the given pattern in the given text.
Input Format. There are two strings in the input: the pattern P and the text T.
Output Format. Print all the positions of the occurrences of P in T in the
               ascending order. Use 0-based indexing of positions in the the text 𝑇.
'''

import random


def polinomial_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans % prime


def precompute_hashes(text, pattern_len, prime, x):
    text_len = len(text)
    hashes = [None] * (text_len - pattern_len + 1)
    hashes[text_len - pattern_len] = \
        polinomial_hash(text[text_len - pattern_len:], prime, x)
    y = 1
    for i in range(pattern_len):
        y = (y * x) % prime
    for i in range(text_len - pattern_len - 1, -1, -1):
        hashes[i] = (x * hashes[i + 1] + ord(text[i]) - \
                     y * ord(text[i + pattern_len])) % prime
    return hashes


def rabin_karp(pattern, text):
    p = 1000000007
    x = random.randrange(1, p - 1)
    result = []
    pattern_hash = polinomial_hash(pattern, p, x)
    hashes = precompute_hashes(text, len(pattern), p, x)
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash != hashes[i]:
            continue
        if text[i: i + len(pattern)] == pattern:
            result.append(i)
    return result


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


print_occurrences(rabin_karp(*read_input()))
