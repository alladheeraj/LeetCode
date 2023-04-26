class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        
        for num in nums:
            i, j = 0, size
            
            while i != j:
                mid = (i + j) // 2
                
                if tails[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            
            tails[i] = num
            size = max(i + 1, size)
        
        return size
