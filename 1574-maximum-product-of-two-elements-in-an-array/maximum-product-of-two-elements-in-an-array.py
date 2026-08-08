class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for l in range(len(nums)):
            prod = 1
            r = l+1
            while r < len(nums):
                prod = (nums[l]-1) * (nums[r]-1)
                if prod > ans:
                    ans = prod
                r += 1
            r = l+1
        return ans