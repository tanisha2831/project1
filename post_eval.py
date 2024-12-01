def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            a, b = stack.pop(), stack.pop()
            stack.append(eval(f"{b}{token}{a}"))
    return stack[0]

expr = "2 3 1 * + 9 -"
result = evaluate_postfix(expr)
print(f"The result of the postfix expression '{expr}' \n= {result}")
