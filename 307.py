class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        self.tree = [0] * (2 * n)
        for i in range(n, 2*n):
            self.tree[i] = nums[i-n]
        for i in range(n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index: int, val: int) -> None:
        n = len(self.tree) // 2
        index += n
        self.tree[index] = val
        while index > 0:
            left = index
            right = index
            if index % 2 == 0:
                right += 1
            else:
                left -= 1
            parent = index // 2
            self.tree[parent] = self.tree[left] + self.tree[right]
            index = parent

    def sumRange(self, left: int, right: int) -> int:
        n = len(self.tree) // 2
        left += n
        right += n
        sum_ = 0
        while left <= right:
            if left % 2 == 1:
                sum_ += self.tree[left]
                left += 1
            if right % 2 == 0:
                sum_ += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return sum_

      
