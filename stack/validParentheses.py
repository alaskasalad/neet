# time: O(n)
# space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # keys are the closing one 
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
                
# time: O(n^2)
# space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('[]', '')
            s = s.replace('{}', '')

        return s == ''