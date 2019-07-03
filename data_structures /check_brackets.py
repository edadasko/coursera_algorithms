"""
Check brackets in the code
Task. Your friend is making a text editor for programmers. He is currently working
      on a feature that will find errors in the usage of different types of brackets.
      Code can contain any brackets from the set []{}(). For convenience, the text editor
      should not only inform the user that there is an error in the usage of brackets,
      but also point to the exact place in the code with the problematic bracket.
      First priority is to find the first unmatched closing bracket which either doesn’t
      have an opening bracket before it, like ] in ](), or closes the wrong opening bracket,
      like } in ()[}. If there are no such mistakes, then it should find the first unmatched
      opening bracket without the corresponding closing bracket after it, like ( in {}([].
      If there are no mistakes, text editor should inform the user that the usage
      of brackets is correct. Apart from the brackets, code can contain big and small
      latin letters, digits and punctuation marks.
Input Format. Input contains one string S which consists of big and small latin letters,
              digits, punctuation marks and brackets from the set []{}().
Output Format. If the code in S uses brackets correctly, output “Success". Otherwise,
               output the 1-based index of the first unmatched closing bracket,
               and if there are no unmatched closing brackets, output the 1-based index
               of the first unmatched opening bracket.
"""

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_symbol in enumerate(text):
        if next_symbol in "([{":
            opening_brackets_stack.append(Bracket(next_symbol, i))
        elif next_symbol in ")]}":
            if not opening_brackets_stack:
                return i + 1
            opening_bracket = opening_brackets_stack.pop()
            if not are_matching(opening_bracket.char, next_symbol):
                return i + 1
    return opening_brackets_stack[0].position + 1 if opening_brackets_stack else None


text = input()
mismatch = find_mismatch(text)
print("Success" if not mismatch else mismatch)
