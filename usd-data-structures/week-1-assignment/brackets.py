# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]
def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # add opening bracket to stack
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # closing bracket with no opening bracket
            if len(opening_brackets_stack) == 0:
                return i + 1
            else:
                top = opening_brackets_stack[-1]
                if are_matching(top.char,next):
                    opening_brackets_stack.pop()
                else:
                    return i + 1
                
    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0].position
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
