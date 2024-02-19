class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = nums[0]
        index = 1
        while index!= len(nums):
            if nums[index] == last:
                nums.pop(index)
            else:
                last = nums[index]
                index+=1

        