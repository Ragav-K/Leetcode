class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            if nums[right] == val:
                right -= 1
            elif nums[left] == val:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                right -= 1
            else:
                left += 1
        """nums.remove(val)"""
        """nums = nums[:left+1]
        print(nums)"""

        return left

        """count = 0
        for i in nums:
            if i == val:
                count += 1
        return len(nums)-count"""