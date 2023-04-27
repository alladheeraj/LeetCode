class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i = 0       
        while i < n:
            s[i:i+k] = s[i:i+k][::-1]
            i += 2*k
        return ''.join(s)
