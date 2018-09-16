class Sulotion:
    def searchRange(self, nums, target):

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
                return [self.first(nums, 0, mid, target), self.last(nums, mid + 1, len(nums)- 1, target)]
        return [-1, -1]


    def first(self, nums, lo, hi, target):
        while lo <= hi:
            mid = (hi + lo)// 2
            if  target > nums[mid]:
                lo = mid +1
            elif target > nums[mid - 1]:
                return mid
            else:
                hi = mid - 1
        return lo


    def last(self, nums, lo, hi, target):
        while lo <= hi:
            mid = (hi + lo) // 2
            if target < nums[mid]:
                hi = mid + 1
            elif target < nums[mid + 1]:
                return mid
            else:
                lo = mid - 1
        return hi
c = Sulotion()
kis = c.searchRange([5,7,7,8,8,10],8)
print(kis)
