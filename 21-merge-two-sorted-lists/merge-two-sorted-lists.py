# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # def linked_list_to_arr(head1, head2):
        #     arr = []
        #     temp = head1
        #     while temp:
        #         arr.append(temp.val)
        #         temp = temp.next

        #     temp = head2
        #     while temp:
        #         arr.append(temp.val)
        #         temp = temp.next
        #     return arr

        # arr = linked_list_to_arr(list1, list2)
        # arr.sort()

        # def arr_to_ll(arr):
        #     if not arr:
        #         return 
        #     head = ListNode(arr[0])
        #     current = head
        #     for i in arr[1:]:
        #         current.next = ListNode(i)
        #         current = current.next
        #     return head
        # head = arr_to_ll(arr)
        # return head
        t1 = list1
        t2 = list2
        dNode = ListNode(-1)
        temp = dNode
        while t1 is not None and t2 is not None:
            if t1.val < t2.val:
                temp.next = t1
                temp = t1
                t1 = t1.next
            else:
                temp.next = t2
                temp = t2
                t2 = t2.next
        if t1 is not None:
            temp.next = t1
        else:
            temp.next = t2
        return dNode.next

                


    





        