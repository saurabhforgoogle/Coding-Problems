class Node:
    def __init__(self,value):
        self.value=value 
        self.next=None
        self.previous=None
class DoublyLinkedList:
    def __init__(self):
        self.parent=None
    def insert(self,value):
        temp=Node(value)
        temp1=self.parent
        if self.parent==None:
            self.parent=temp
        else:
            while(temp1.next!=None):
                temp1=temp1.next
            temp1.next=temp
            temp.previous=temp1
        temp1=None
        temp=None
        return

    
    
    def delete(self,value):
        temp1=self.parent
        while(temp1.next!=None or temp1.value==value):
            if temp1.value!=value:
                previous=temp1
                temp1=temp1.next 
            else:
                break
        else:
            print(value,"Not Found")
            return
            
        if temp1==self.parent:
            self.parent=temp1.next
            temp1.next.previous=self.parent
            
        elif temp1.next==None and temp1.value==value:
            previous.next=None
        else:
            previous.next=temp1.next
            temp1.next.previous=previous
        print("Deleted",value)

        
    

    def printlist(self):
        if self.parent!=None:
            temp1=self.parent
            while(temp1.next!=None):
                print(temp1.value,end=" ")
                temp1=temp1.next
            print(temp1.value)
    def printback(self):
        if self.parent!=None:
            temp1=self.parent
            while(temp1.next!=None):
                temp1=temp1.next
            while(temp1!=self.parent):
                print(temp1.value,end=" ")
                temp1=temp1.previous
            print(temp1.value)
    
dll=DoublyLinkedList()
import random
n=int(input("Enter number of digits  "))
for i in range(n):
    dll.insert(random.randint(1,n))
dll.printlist()
dll.printback()

dll.delete(random.randint(1,n))
dll.printlist()
"""print("RANDOM DELETION:")
for i in range(n):
    val=random.randint(1,n)
    print("Deleting:",val)
    dll.delete(val)
    if i%(n//10)==0:
        print("Updated List: ")
        dll.printlist()
dll.printlist()
"""