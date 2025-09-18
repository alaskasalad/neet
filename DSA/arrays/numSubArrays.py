# getting the product of each element 

def numSubArrayProductLessThan(nums, k):
    if k <= 1:
        return 0
    
    ans = left = 0
    curr = 1 # doing multiplicaiton so it cant be 0

    for right in range(len(nums)):
        curr *= nums[right]
        while curr >= k:
            curr //= nums[left]
            left += 1

        ans += right - left + 1

    return ans 