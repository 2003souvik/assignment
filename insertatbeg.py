
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def printlist(self):
       t=self.head
       while(t!=None):
          print(t.data)
          t=t.next
    def insert(self, data):
       newNode = Node(data)
       if(self.head!=None):
         current = self.head
         while(current.next!=None):
           current = current.next
         current.next = newNode
       else:
          self.head = newNode
    def insertbeg(self,data):
        n=Node(data)
        if(self.head==None):
            self.head=n
        else:
            n.next=self.head
            self.head=n
    def afternode(self,a,data):
        n=Node(data)
        if(self.head==None):
            self.head=n
            return
        t=self.head
        while(t!=None and t.data!=a):
            t=t.next
        n.next=t.next
        t.next=n



llist=LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(6)
#llist.insertbeg(4)
llist.afternode(3,5)
llist.printlist()

