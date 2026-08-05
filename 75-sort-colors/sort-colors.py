class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        point = 0
        while point <len(nums):
            if nums[point] == min(nums):
                point += 1
            else:
                minIndex = point
                minValue = nums[point]
                for i in range(point+1,len(nums)):
                    if nums[i] < minValue:
                        minValue = nums[i]
                        minIndex = i
                """temp = nums[point]
                nums[point] = nums[minIndex]
                nums[minIndex] = temp"""
                nums[point] , nums[minIndex] = nums[minIndex] , nums[point]
                point += 1
            

        """low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1"""