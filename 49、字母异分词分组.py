class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for s in strs:
            s_modify = "".join(sorted(s))
            if s_modify not in dict:
               dict[s_modify] = []
            dict[s_modify].append(s)
        return list[dict.values]
    
    














