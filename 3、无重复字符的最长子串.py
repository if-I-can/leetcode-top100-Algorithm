class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = len(char_set)
        return (char_set,max_length)

real = Solution()
print(real.lengthOfLongestSubstring("pwwkew"))
print(real)
