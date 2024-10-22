def valid_parantheses(s):
    # make a dict with opening brackets as keys and closing as values
    brackets = {'{': '}', '[': ']', '(': ')'}
    stack = []

    # iterate over string, if opening brackets found, append to stack
    # else check if stack is empty or if the closing bracket matches the key in bracket

    for char in s:
        if char in brackets:
            stack.append(char)
        elif len(stack) == 0 or brackets[stack.pop()] != char:
            return False

        # in the end the stack should be empty if its valid

    return len(stack) == 0


s = "[()]"
print(valid_parantheses(s))
