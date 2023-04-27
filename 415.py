class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1
        res = ''
        while i >= 0 or j >= 0 or carry > 0:
            sum = carry
            if i >= 0:
                sum += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                sum += ord(num2[j]) - ord('0')
                j -= 1
            carry = sum // 10
            res = str(sum % 10) + res
        return res
