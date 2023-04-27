class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes
        if x < 0:
            return False
        
        # Reverse the integer
        reversed_int = 0
        temp = x
        while temp > 0:
            reversed_int = reversed_int * 10 + temp % 10
            temp //= 10
        
        # Check if the original and reversed integers are the same
        return x == reversed_int
