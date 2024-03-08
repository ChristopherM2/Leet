class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        index = 1
        while index!= len(nums):
            if nums[index] == nums[index-1]:
                nums.pop(index)
            else:
                
                index+=1

        