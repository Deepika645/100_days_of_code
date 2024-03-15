#You are given a Linked list of size n. The list is in alternating ascending and descending orders. 
#Sort the given linked list in non-decreasing order.
def merge_sorted(self,h1,h2):
    res=Node(None)
    curr=res
    while h1 and h2:
        if h1.data<h2.data:
            curr.next=h1
            curr=h1
            h1=h1.next
        else:
            curr.next=h2
            curr=h2
            h2=h2.next
    if h1:
        curr.next=h1
    if h2:
        curr.next=h2
    return res.next

def sort(self, h1):
    curr=h1
    desc=None
    while curr and curr.next:
        temp=desc
        desc=curr.next
        temp2=desc.next
        desc.next=temp
        curr.next=temp2
        curr=curr.next
    h1=self.merge_sorted(h1,desc)
    return h1