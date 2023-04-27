class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        b = '0' * (len(a) - len(b)) + b
        carry = 0
        result = ''
        for i in range(len(a) - 1, -1, -1):
            digit_sum = int(a[i]) + int(b[i]) + carry
            if digit_sum == 0 or digit_sum == 1:
                carry = 0
                result = str(digit_sum) + result
            elif digit_sum == 2:
                carry = 1
                result = '0' + result
            else: # digit_sum == 3
                carry = 1
                result = '1' + result
        if carry == 1:
            result = '1' + result
        
        return result
