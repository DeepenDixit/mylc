# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = list()
        list2 = list()
        
        while True:
            list1.append(l1.val)
            if l1.next!= None:
                l1 = l1.next
            else:
                break
        
        while True:
            list2.append(l2.val)
            if l2.next!= None:
                l2 = l2.next
            else:
                break
        
        carry = 0
        
        if len(list1) >= len(list2):
            for i in range(len(list1)):
                try:
                    s = list1[i] + list2[i] + carry
                except IndexError as e:
                    s = list1[i] + carry
                r = s % 10
                carry = s // 10
                if i == 0:
                    ln = ListNode(r)
                    lnrs = ln
                else:
                    lnrs.next = ListNode(r)
                    lnrs = lnrs.next
                
                
        else:
            for i in range(len(list2)):
                try:
                    s = list1[i] + list2[i] + carry
                except IndexError as e:
                    s = list2[i] + carry
                r = s % 10
                carry = s // 10
                
                if i == 0:
                    ln = ListNode(r)
                    lnrs = ln
                else:
                    lnrs.next = ListNode(r)
                    lnrs = lnrs.next
        
        if carry != 0:
            j = [int(x) for x in str(carry)]
            for i in j:
                lnrs.next = ListNode(i)
                lnrs = lnrs.next

        return ln