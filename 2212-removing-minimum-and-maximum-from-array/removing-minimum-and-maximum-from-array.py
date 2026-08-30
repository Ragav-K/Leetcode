class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        mn = nums.index(min(nums))
        mx = nums.index(max(nums))

        a, b = min(mn, mx), max(mn, mx)

        return min(
            b + 1,
            n - a,
            a + 1 + n - b
        )