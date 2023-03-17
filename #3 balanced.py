def is_balanced(expression):
    stack = []
    for char in expression:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return not stack

# Testing the program with sample expressions
expression1 = "((a+b)"
expression2 = "(((a+b)+c)+d)+e"

print(is_balanced(expression1)) # Output: False
print(is_balanced(expression2)) # Output: True
