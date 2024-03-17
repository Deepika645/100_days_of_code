#Given two linked list head1 and head2 with distinct elements, determine the count of all distinct pairs from both lists 
class Solution:

    def countPair(self, head1, head2, n1, n2, x):
        arr=[]
        cnt = 0
        temp=head1
     
        while temp:
            arr.append(temp.data)
            temp=temp.next
        
        set1=set(arr)
        temp2=head2
        while temp2:
            if x-temp2.data in set1:
                cnt+=1
            temp2=temp2.next
        
        return cnt