# a fixed length k
# static window size, find the largest sum 

def fidn_best_subarray(nums, k):
    left = right = curr = ans = size = 0

    for right in range(len(nums)):
        while size <= k:
            curr += nums[right]
            right += 1
            size += 1
            ans += nums[right]
        curr -= nums[left]
        left += 1
        right += 1
        curr += nums[right]
        ans = max(curr, ans)
    return ans 

def find_best_subarray2(nums, k):
    curr = 0
    # curr only needs to be added up to max len of subarray
    for i in range(k):
        curr += nums[i]

    ans = curr
    # going from k (where we stopped) to the end 
    for i in range(k, len(nums)):
        curr += nums[i] - nums[i-k]
        ans = max(ans, curr)

    return ans 

