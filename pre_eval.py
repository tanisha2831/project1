def evaluate_prefix(expression):
    stack = []
    for token in expression.split()[::-1]:
        if token.isdigit():
            stack.append(int(token))
        else:
            b, a = stack.pop(), stack.pop()
            stack.append(eval(f"{b}{token}{a}"))
    return stack[0]


expr = "- + 8 / 6 3 2"
result = evaluate_prefix(expr)
print(f"The result of the prefix expression '{expr}' \n= {result}")
