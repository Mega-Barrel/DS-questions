from typing import List

class Solution:

    # Time: O(n^2)
    # Space: O(1)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    
    # Time: O(n)
    # Space: O(n)
    def optimizeTwoSum(self, nums: List[int], target: int) -> List[int]:
        ndict = {}  # val: idx
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in ndict:
                return [ndict[diff], idx]
            ndict[num] = idx
        return

sol = Solution()
nums = [2,7,11,15]
target = 18
res = sol.optimizeTwoSum(nums, target)
print(res)