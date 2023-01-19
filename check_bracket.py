from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            bracket = Bracket(next, i)
            opening_brackets_stack.append(Bracket(next, i))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            else:
                top = opening_brackets_stack.pop()
                if not are_matching(top.char, next):
                    return i + 1
    if opening_brackets_stack:
        return opening_brackets_stack.pop().position + 1
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
