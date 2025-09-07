# time: O(n)
# space: O(1)

def twoSum(NA, target):
    left = 0
    right = NA.size() -1

    while left < right:
        sum = NA[left] + NA[right]
        if  sum == target:
            return True
        elif sum > target:
            right -= 1
        else:
            left += 1 

    return False