def isValid(s: str) -> bool:
    if len(s) == 0:
        return True

    stack = []

    for v in s:
        if v in ["[", "(", "{"]:
            stack.append(v)
        elif (
            (v == "]" and len(stack) > 0 and stack[-1] == "[")
            or (v == ")" and len(stack) > 0 and stack[-1] == "(")
            or (v == "}" and len(stack) > 0 and stack[-1] == "{")
        ):
            stack.pop()
        else:
            return False

    return len(stack) == 0
