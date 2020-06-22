# Given a string s, eliminate consecutive duplicate characters from the string and return it.
# That is, if a list contains repeated characters, they should be replaced with a single copy 
# of the character. The order of the elements should not be changed.
class Solution:
    def solve(self, s):
        letters = ""
        x = ""
        if(len(s)==1):
            return s
        else: 
            for i in range(len(s)):
                if i <= len(s):
                    if(s[i]!=x):
                        letters+=(s[i])
                        x = s[i]
            return letters