from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        len_s,len_p = len(s),len(p)

        if len_s < len_p:
            return []
        p_counter=  Counter(p)
        s_counter = Counter(s[:len(p)-1])

        result = []

        for i in range(len_p-1,len_s):
            s_counter[s[i]] += 1
            if s_counter == p_counter:
                result.append(i-len_p+1)

            s_counter[s[i-len_p+1]] -= 1
            if s_counter[s[i-len_p+1]] == 0:
                del s_counter[s[i-len_p+1]]
           

        return result









# Test the function
tp = Solution()
print(tp.findAnagrams("abcab", "ab"))
