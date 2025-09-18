# valid sub array = sliding window 
# best valid subarray 

def find_length(nums, k):
    left = curr = ans = 0
    for right in range(len(nums)):
        cur += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left +1)

    return ans 