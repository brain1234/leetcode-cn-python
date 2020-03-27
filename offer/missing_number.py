from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n+1)*n//2 - sum(nums)


if __name__ == '__main__':
    num = Solution().missingNumber([0])
    print(num)
