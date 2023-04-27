def twoSum(nums, target):
    complement_map = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in complement_map:
            return [complement_map[complement], i]
        complement_map[nums[i]] = i
