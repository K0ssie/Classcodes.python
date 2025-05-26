from collections import deque

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def push_character(self, ch):
        self.stack.append(ch)  

    def enqueue_character(self, ch):
        self.queue.append(ch)  

    def pop_character(self):
        return self.stack.pop() 

    def dequeue_character(self):
        return self.queue.popleft()  



s = input("Enter a word: ")


obj = Solution()


for char in s:
    obj.push_character(char)
    obj.enqueue_character(char)

is_palindrome = True


for i in range(len(s) // 2):
    if obj.pop_character() != obj.dequeue_character():
        is_palindrome = False
        break

# Output
if is_palindrome:
    print(f"The word, {s}, is a palindrome.")
else:
    print(f"The word, {s}, is not a palindrome.")
