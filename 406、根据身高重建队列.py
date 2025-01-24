class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sort_people = sorted(people,key=lambda x:(-x[0],x[1]))
        queue = []

        for p in sort_people:
            queue.append(p[1],p)

        return queue

        