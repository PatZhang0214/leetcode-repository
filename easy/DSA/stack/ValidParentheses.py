from typing import List

def isValid(s: str) -> bool:
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
        elif i == ']':
            if len(stack) == 0 or stack.pop() != '[':
                return False
        elif i == '}':
            if len(stack) == 0 or stack.pop() != '{':
                return False

    return len(stack) == 0
if __name__ == '__main__':
    print(isValid("[]"))