class Sulotion:
    def searchRange(self, nums, target):
        range_list = []
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                range_list.append(mid)
            if target < nums[mid]:
                hi = mid - 1
            else :
                lo = mid + 1
        if range_list is None:
            return [-1,-1]
        else:
            return range_list
c = Sulotion()
kis = c.searchRange([5,7,7,8,8,10],8)
print(kis)
