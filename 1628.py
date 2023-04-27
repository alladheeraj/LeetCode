class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        if self.val.isdigit():
            return int(self.val)
        left_val = self.left.evaluate()
        right_val = self.right.evaluate()
        if self.val == '+':
            return left_val + right_val
        elif self.val == '-':
            return left_val - right_val
        elif self.val == '*':
            return left_val * right_val
        else:
            return left_val // right_val

class Solution:
    def buildTree(self, postfix: List[str]) -> 'Node':
        stack = []
        for c in postfix:
            if c.isdigit():
                stack.append(Node(c))
            else:
                right = stack.pop()
                left = stack.pop()
                stack.append(Node(c, left, right))
        return stack[0].evaluate()
