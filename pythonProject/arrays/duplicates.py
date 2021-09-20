def removeDuplicates(nums):
    j = 0
    count = 0
    l = len(nums)
    for i in range(l - 1):
        if nums[i] != nums[i + 1]:
            nums[j] = nums[i]
            j += 1
            count += 1
        else:
            continue
    nums[j] = nums[l - 1]
    count += 1
    return nums, count

def findDuplicate(nums):
    count = 0
    nums = sorted(nums)
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return nums[i]
        else:
            count += 1
            continue
    if nums[len(nums)-1] == nums[len(nums)-2]:
        return nums[len(nums)-1]


nums = list(map(int, input("Enter elements: ").split()))
print(nums)
print(findDuplicate(nums))


# def removeDuplicates(self, nums):
#     len_ = 1
#     if len(nums) == 0:
#         return 0
#     for i in range(1, len(nums)):
#         if nums[i] != nums[i - 1]:
#             nums[len_] = nums[i]
#             len_ += 1
#     return len_

