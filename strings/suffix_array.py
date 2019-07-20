def build_suffix_array(text):
    suffixes = [(i, text[i:]) for i in range(len(text))]
    suffixes.sort(key=lambda c: c[1])
    result = [c[0] for c in suffixes]
    return result


text = input()
print(" ".join(map(str, build_suffix_array(text))))
