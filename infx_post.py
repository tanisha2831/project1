def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  
    stack = [] 
    postfix = "" 

    for char in expression:
        if char.isalnum():  
            postfix += char
        elif char == '(': 
            stack.append(char)
        elif char == ')': 
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop() 
        else:  
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[char]:
                postfix += stack.pop()
            stack.append(char)  
    while stack:
        postfix += stack.pop()

    return postfix

infix_expr = "A+B/c"
print("Infix Expression:", infix_expr)
print("Postfix Expression:", infix_to_postfix(infix_expr))
