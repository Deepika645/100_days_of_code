#Given a linked list of N nodes such that it may contain a loop.
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        slow = head
        fast = head.next
        while fast!=slow:
             if fast is None or fast.next is None:
                return
             fast = fast.next.next
             slow = slow.next
        size=1
        fast=fast.next
        while fast!=slow:
            fast=fast.next
            size+=1
        slow=head
        fast=head
        for i in range(size-1):
            fast=fast.next
        while fast.next!=slow:
            fast=fast.next
            slow=slow.next
        fast.next=None   
