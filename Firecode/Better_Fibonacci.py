def better_fibonacci(n):
    if n == 0:
        return 0
    nums = []
    a, b = 0, 1
    while len(nums) < n:
        nums.append(b)
        a, b = b, a+b
    return nums[n-1]
print(better_fibonacci(3))
