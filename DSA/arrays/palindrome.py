# time: O(n)
# spcae: O(1)

def checkIfPalindrome(s):
    left = 0
    right = s.size() -1

    while left < right:
        if s[left] != s[right]:
            return False
        right -= 1
        left += 1

    return True