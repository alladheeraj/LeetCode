class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // (len(arr) - 1)
        i, j = 0, len(arr) - 1
        while i < j:
            mid = (i + j) // 2
            if arr[mid+1] - arr[mid] != d:
                return arr[mid] + d
            elif arr[mid] + d != arr[mid-1]:
                j = mid - 1
            else:
                i = mid + 1
        return arr[-1] + d
