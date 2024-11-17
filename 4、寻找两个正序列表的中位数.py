class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        record = []
        for j in nums2:
            record.append(j)
        for i in nums1:
            record.append(i)
        record.sort()
        index_med = len(record) % 2
        if index_med != 0 :
            med = record[index_med]
        else:
            a = int(len(record)/2)
            b = int(len(record)/2-1)
            med = (record[a]+record[b])/2
        return med


res = Solution()
print(res.findMedianSortedArrays(nums1=[1,2],nums2 =[3,4]))



