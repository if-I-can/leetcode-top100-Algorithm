###这里可以记一下 就是字典的dict.values() 转list，然后列表的list.count(element)的用啊
### 以及要计入一个公式，对于解决带有冷却器的任务调度问题：最短时间为 （最高任务频率-1）* （n-1）+最高任务频率数量+1

from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count_tasks = Counter(tasks)
        max_frq = max(count_tasks.values())
        max_frq_number = list(count_tasks.values()).count(max_frq)

        ###这里有个公式：记住就好了， 最短时间 = (最高频率-1) * (冷却时间+1) + 最高频率任务的个数
        min_time = (max_frq-1)*(n+1)+max_frq_number   #计算的是需要空闲时间中和的情况

        return min(min_time,len(tasks))  #len(tasks) 任务数量足够多，不会空出空闲时间n





tp = Solution()
print(tp.leastInterval(["A","A","A","B","B","B"],1))