# LeetCode 5. 
# Longest Palindromic Substring
# Given a string s, return the longest palindromic substring in s.

def Palindrome(s):
    if len(s)==0 or len(s)==1: return 0
    longest_num = []
    for i in range(len(s)):
        left,right = left_right(s,i,i)
        left_e, right_e = left_right(s,i,i+1)
        longest_num.append(str(s[left:right+1]))
        longest_num.append(str(s[left_e:right_e+1]))
    return max(longest_num,key=len)

def left_right(s_str,left,right):
        while left>=0 and right<len(s_str) and s_str[left] == s_str[right]:
                left = left -1
                right = right +1
        return int(left+1), int(right-1)

#Improved
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0 or len(s)==1: return s
        start, end = 0,0
        for i in range(len(s)):
            left,right = self.left_right(s,i,i)
            left_e, right_e = self.left_right(s,i,i+1)
            if right - left > end - start:
                start,end = left,right
            if right_e - left_e > end - start:
                start,end = left_e,right_e
        return s[start:end+1]

    def left_right(self, s_str,left,right):
            while left>=0 and right<len(s_str) and s_str[left] == s_str[right]:
                    left = left -1
                    right = right +1
            return int(left+1), int(right-1)