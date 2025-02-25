def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}
    for token in expression.split():
        if token not in operators:
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
    return stack[0]

def evaluate_prefix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}
    for token in reversed(expression.split()):
        if token not in operators:
            stack.append(int(token))
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
    return stack[0]

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_operator(operators, operands):
    operator = operators.pop()
    operand2 = operands.pop()
    operand1 = operands.pop()
    if operator == '+':
        operands.append(operand1 + operand2)
    elif operator == '-':
        operands.append(operand1 - operand2)
    elif operator == '*':
        operands.append(operand1 * operand2)
    elif operator == '/':
        if operand2 == 0:
            raise ValueError("Division by zero!")
        operands.append(operand1 / operand2)

expression = input("Enter an expression: ")
operators = {'+', '-', '*', '/'}
if any(op in expression for op in operators):
    # Postfix expression
    result_postfix = evaluate_postfix(expression)
    print("Result of Postfix Expression:", result_postfix)
else:
    # Prefix expression
    result_prefix = evaluate_prefix(expression)
    print("Result of Prefix Expression:", result_prefix)
