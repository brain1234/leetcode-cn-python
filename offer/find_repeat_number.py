from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        num_set=set()
        for num in nums:
            if num in num_set:
                return num
            else:
                num_set.add(num)