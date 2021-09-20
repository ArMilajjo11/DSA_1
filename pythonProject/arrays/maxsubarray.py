def maxSubArraySum(nums):
    sum = 0
    highest = nums[0]
    for i in nums:
        sum = sum + i
        if sum < 0:
            sum = 0
        elif sum > highest:
            highest = sum
    return highest

nums = list(map(int, input().split()))
print(nums)
print(maxSubArraySum(nums))
# [5,4,-1,7,8]