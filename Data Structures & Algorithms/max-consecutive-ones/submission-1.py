class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr= 0
        max_one = 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            if curr > max_one:
                max_one = curr
        return max_one;
        