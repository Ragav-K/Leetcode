class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def sets(index,sub,nums):
            if index == len(nums):
                ans.append(sub[:])
                return ans
            sub.append(nums[index])
            sets(index+1,sub,nums)
            sub.remove(nums[index])
            sets(index+1,sub,nums)
        sets(0,[],nums)
        return ans