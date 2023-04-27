class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(': ')', '[': ']', '{': '}'}
        for c in s:
            if c in parentheses:
                stack.append(c)
            elif stack and parentheses.get(stack[-1]) == c:
                stack.pop()
            else:
                return False
        return not stack
