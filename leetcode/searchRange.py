class Sulotion:
    def searchRange(self, nums, target):
        indicies = []
        while len(indicies) < 2:
            position = self.positions(nums, target)
            if type(position) is list:
                if -1 in position:
                    return [-1, -1]
                else:
                    return [0, 0]
            indicies.append(position)
        indicies.sort()
        return indicies


    def positions(self, nums, target):
        if len(nums) == 1 and target in nums:
            return [0, 0]
        range_list = []
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                del nums[mid]
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else :
                lo = mid + 1
        return [-1, -1]
c = Sulotion()
kis = c.searchRange([1],1)
print(kis)
