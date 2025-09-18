def find_length(s):
    left = curr = ans = 0
    # curr will hold how many zeros we have 
    for right in range (len(s)):
        # keep moving the left until there is only 1 0 left 
        while curr > 1:
            if s[right] == '0':
                curr -= 1
            left += 1
        # update the curr because there can onlly be 1 0 
        if s[right] == '0':
            curr += 1
        ans = max(ans, right - left + 1)
    
    return ans
