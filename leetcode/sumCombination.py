class Solution:
    # for the duplicate nums if the nums[i] is divisable by the target we check to see how many times needed to get the target
    def sumComb(self, nums, target):
        #nums are set
        
        combination_set = []
        sum_list = []

        for i in range(len(nums)):
            sum_list= []
            if target % nums[i] == 0:
                multi_value = target // nums[i]
                for v in range(multi_value):
                    sum_list.append(nums[i])
                combination_set.append(sum_list)
            elif target % nums[i] > 0:
                sum_list = []
                multi_value = target // nums[i]
                for v in range(multi_value):
                    sum_list.append(nums[i])
                rm_valaue = target - (multi_value * nums[i])
                sum_list.append(rm_valaue)
                combination_set.append(sum_list)
        return combination_set
c = Solution()
v = c.sumComb([2,3,5], 8)
print(v)
