class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums == []:
            return []
        ans = []
        s = set(nums)
        for i in range(min(nums)+1,max(nums)):
            if i not in s:
                ans.append(i)
        return ans