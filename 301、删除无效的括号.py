from collections import deque
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isvalid(curr):
            count = 0
            for i in curr:
                if i == '(':
                    count += 1
                elif i == ')':
                    count -= 1
                if count < 0:
                    return False
            if count == 0:
                return True

            
        queue  = deque([s])
        seen = set([s])
        result = []
        found =False

        while queue:
            new_char = queue.popleft()

            if isvalid(new_char):
                result.append(new_char)
                found =True

            if found:
                continue

            for i in range(len(new_char)):
                if new_char[i] in ('(',')'):
                    next_char = new_char[:i]+new_char[i+1:]
                    if next_char not in seen:
                        seen.add(next_char)
                        queue.append(next_char)

        return result