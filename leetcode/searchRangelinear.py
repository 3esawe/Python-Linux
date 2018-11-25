def searchRange(self, nums, target):
        first = -1
        last = -1
        for i in range(0,len(nums)):
            if nums[i] != target:
                continue
            if  first == -1:
                first = i
            last = i
        return [first, last]  