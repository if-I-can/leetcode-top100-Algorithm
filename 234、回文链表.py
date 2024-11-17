class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        first1 = head
        second1 = head
        first2 = head
        second2 = head
        count = 0
        while head:
            count += 1
            head = head.next
        if count == 1:
            return True
        number = count // 2# 偶数
        jishu1 = 0
        b = []
        if count % 2 != 0:
            for i in range(number+1):
                second1 = second1.next
            for j in range(number):
                b.append(second1.val)
                second1= second1.next
            b = b[::-1]
            for k in b:
                if first1.val == k:
                    jishu1 += 1
                    first1 = first1.next
            if jishu1 == number:
                return True
            else:
                return False

        for i in range(number):
            second2 = second2.next
        a = []
        for i in range(number):
            a.append(second2.val)
            second2 = second2.next
        a = a[::-1]
        jishu2 = 0
        for i in range(number):
            if first2.val == a[i]:
                jishu2 += 1
            first2 = first2.next
        if jishu2 == number:
            return True
        else:
            return False


