def insertandserch(nums, target):
	lo = 0 
	hi = len(nums) - 1 
	while lo <= hi: 
		mid = (hi-lo) // 2 + lo
		if nums[mid] == target:
			return mid
		elif target > nums[mid]:
			lo = mid + 1

		else:
			hi = mid - 1 

	return lo

print(insertandserch([1,2,3,4,5,7], 6))