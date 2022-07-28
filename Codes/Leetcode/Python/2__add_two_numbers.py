# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    
    def getOutputNumStr(self, l):
        num_list = []
        while l:
            num_list.append(l.val)
            l = l.next
        num_list.reverse()
        num_list_str = [str(item) for item in num_list]
        return int("".join(num_list_str))
        

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_nums = str(self.getOutputNumStr(l1) + self.getOutputNumStr(l2))
        sum_nums = sum_nums[::-1]
        root = ListNode()
        curr = root
        for item in sum_nums:
            curr.next = ListNode(int(item))
            curr = curr.next
        return root.next
        
       
                
        

            
        

            
        