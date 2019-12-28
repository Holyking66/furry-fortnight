class ListNode:
    def __init__(self,val=0):
        self.value=val
        self.next = None
class List:
    def __init__(self):
        self.head = ListNode()
    def add(self,num):
        last = self.head
        while(last.next!=None):
            last=last.next
        last.next=ListNode(num)
    def reverse(self,head):
            #head = self.head.next
        if((head.next== None)or(head==None)):
            return head
        result = self.reverse(head.next)
        head.next.next=head
        head.next=None
        self.next=result
        return result
    def print(self):
        head = self.head
        i=0
        while(head):
            print(head.value)
            head = head.next
            i+=1
        print(i)


l = ListNode(3)
print(l.value)
L1 = List()
for i in range(1,10):
    L1.add(i)
L1.print()
L = L1.reverse(L1.head)
while(L.next!=None):
    print(L.value)
    L = L.next
