from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @classmethod
    def build_node_list(cls, l: List[int]):
        """
        The method was added for debug purposes
        """
        r = cls()
        current_node = r
        previous_node = None
        for el in l:
            current_node.val = el
            if previous_node:
                previous_node.next = current_node
            previous_node = current_node
            current_node = cls()
        return r



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        finished = False

        r = ListNode()
        m = 0
        current_node = r
        previous_node = None

        while not finished:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            s = num1 + num2 + m
            current_node.val = s % 10
            m = s // 10

            if previous_node:
                previous_node.next = current_node

            previous_node = current_node
            current_node = ListNode()
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 is None and l2 is None and m == 0:
                finished = True
        return r
