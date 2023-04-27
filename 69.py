class Solution:
    def mySqrt(self, x: int) -> int:
        # Base case: x is 0 or 1
        if x == 0 or x == 1:
            return x
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
