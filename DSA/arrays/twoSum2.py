# time: O(n)
# space: O(1)

def twoSum(nums, target):
    left = 0
    right = nums.size() -1

    while left < right:
        sum = nums[left] + nums[right]
        if  sum == target:
            return True
        elif sum > target:
            right -= 1
        else:
            left += 1 

    return False