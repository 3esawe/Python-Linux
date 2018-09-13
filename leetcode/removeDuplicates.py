class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
    		return
    	if len(nums) == 1:
    		return len(nums)

    	smallest_pointer = 0
    	largest_pointer = len(nums)

    	while smallest_pointer < largest_pointer - 1:
    		if nums[smallest_pointer] == nums[smallest_pointer + 1]:
    			del nums[smallest_pointer]
    			largest_pointer -= 1
    		else:
    			smallest_pointer += 1
    	return len(nums)
