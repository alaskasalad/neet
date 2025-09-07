def reserveString(s):
    i = s.size() - 1
    j = 0
    char = ''

    while j < i:
        char = s[i]
        s[i] = s[j]
        s[j] = char
        i -= 1
        j += 1