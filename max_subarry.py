class Solution(object):

    def maxSubArray(self, nums):



        cur = 0

        best = max(nums)

        for n in nums:

            cur = max(cur + n, 0)

            best = max(best, cur) if cur > 0 else best



        return best
