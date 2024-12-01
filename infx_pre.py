def infix_to_prefix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  
    stack = []  
    prefix = []  
    expression = expression[::-1] 

    for char in expression:
        if char.isalnum(): 
            prefix.append(char)
        elif char == ')':  
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            stack.pop()  
        else: 
            while stack and stack[-1] != ')' and precedence[stack[-1]] > precedence[char]:
                prefix.append(stack.pop())
            stack.append(char)

    while stack:  
    return ''.join(prefix[::-1]) 

infix_expr = "A+B/c"
print("Infix Expression:", infix_expr)
print("Prefix Expression:", infix_to_prefix(infix_expr))
