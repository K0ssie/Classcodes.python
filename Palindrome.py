from collections import deque
import re

def is_palindrome(s):
    
    
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

    stack = []
    queue = deque()

    for char in s:
        stack.append(char)

        queue.append(char)

    for i in range(len(s) // 2):
        if stack.pop() != queue.popleft():
            return False
        




    return True