class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        for i in range(1, n):
            for j in range(i+1, n):
                num1 = num[:i]
                num2 = num[i:j]
                if (num1.startswith('0') and num1 != '0') or (num2.startswith('0') and num2 != '0'):
                    continue
                x, y = int(num1), int(num2)
                k = j
                while k < n:
                    z = x + y
                    z_str = str(z)
                    if not num.startswith(z_str, k):
                        break
                    k += len(z_str)
                    x, y = y, z
                if k == n:
                    return True
        return False
