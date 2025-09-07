# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

def sub(s, t):
    if len(s) > len(t):
        return False 
    i = j = 0

    while j < len(t) and i < len(s):
        if t[j] == s[i]:
            i += 1
        j += 1

    return i == len(s)
        
        