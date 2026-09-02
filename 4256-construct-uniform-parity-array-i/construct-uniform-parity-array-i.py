class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        mn = min(nums1)

        for x in nums1:
            if x % 2 != mn % 2 and x < mn:
                return False

        return True