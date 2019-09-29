# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = head
        stack = []
        while pre:
            stack.append(pre)
            pre = pre.next
        
        head = stack[-1]
        stack.pop()
        temp = head
        while len(stack) != 0:
            temp.next = stack[-1]
            stack.pop()
            temp = temp.next
        
        return head