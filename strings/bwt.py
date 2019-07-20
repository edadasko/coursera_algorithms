def BWT(text):
    cycle_strings = [text]
    text_len = len(text)
    for i in range(1, text_len):
        cycle_strings.append(text[-i:] + text[:text_len - i])
    cycle_strings.sort()
    return ''.join([c[-1] for c in cycle_strings])


text = input()
print(BWT(text))
