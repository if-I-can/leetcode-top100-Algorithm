class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        start = needle[0]
        for i in range(len(haystack)):
            if hasattr[i] == start and needle == hasattr[i:i+len(needle)]:
                return i
        return -1


