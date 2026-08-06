class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height)-1
        maxh = 0
        while l <= r:
            current = min(height[l],height[r])*(r-l)
            maxh = max(maxh,current)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxh