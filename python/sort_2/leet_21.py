# 리트코드 21. 두 개의 정렬된 목록 병합
# https://leetcode.com/problems/merge-two-sorted-lists/
# 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None

        elif not list1 or not list2:
            return list1 or list2

        else:
            Node = newList = ListNode()
            print(Node, newList)
            while list1 and list2:
                if list1.val <= list2.val:
                    Node.next = list1
                    list1 = list1.next
                else:
                    Node.next = list2
                    list2 = list2.next
                Node = Node.next
            Node.next = list1 or list2
        print(Node, newList)
        return newList.next















# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class LinkedList:
#     def __init__(self):
#         self.head = None
#     def append(self, val):
#         if not self.head:
#             self.head = ListNode(val, None)
#             return
#         node = self.head
#         while node.next:
#             node = node.next
#         node.next = ListNode(val, None)
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         newList = LinkedList()
#         arr = []
#         i = 0
#         while list1:
#             arr.append(list1.val)
#             list1 = list1.next
#         while list2:
#             arr.append(list2.val)
#             list2 = list2.next
#         arr.sort()
#         while i < len(arr):
#             newList.append(arr[i])
#             i += 1
#         return newList.head

