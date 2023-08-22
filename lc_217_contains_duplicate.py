from typing import List

class Solution:
    # Time: O(n)
    # Space: O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                return num, True
            else:
                num_dict[num] = 1
        return

sol = Solution()

nums = [1, 2, 3, 3, 4, 5]
res = sol.containsDuplicate(nums=nums)
print(res)