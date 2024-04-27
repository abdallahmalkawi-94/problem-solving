def add(*nums):
    return sum(nums)

def subtract(*nums):
    sub = nums[0]
    for num in nums[1:]:
        sub -= num
    return sub

def multiply(*nums):
    multi = 1
    for num in nums:
        multi *= num
    return multi

