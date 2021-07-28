class Node:
    def __init__(self,value):
        self.value=value 
        self.next=None
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
        elif temp1.next==None and temp1.value==value:
            previous.next=None
        else:
            previous.next=temp1.next
        

        
    

    def printlist(self):
        if self.parent!=None:
            temp1=self.parent
            while(temp1.next!=None):
                print(temp1.value,end=" ")
                temp1=temp1.next
            print(temp1.value)
    
dll=DoublyLinkedList()
import random
n=int(input("Enter number of digits  "))
for i in range(n):
    dll.insert(random.randint(1,n))
dll.printlist()
print("RANDOM DELETION:")
for i in range(n):
    val=random.randint(1,n)
    print("Deleting:",val)
    dll.delete(val)
    if i%(n//10)==0:
        print("Updated List: ")
        dll.printlist()
dll.printlist()
"""dll.insert(10)
dll.insert(50)
dll.insert(40)
dll.printlist()
dll.delete(0)
dll.printlist()
dll.delete(10)
dll.printlist()
dll.delete(40)
dll.printlist()
"""

















'''class Node:
    def __init__(self,value):
        self.value=value 
        self.next=None
        self.previous=None
class DoublyLinkedList:
    def __init__(self):
        self.parent=None
    def insert(self,value):
        if self.parent==None:
            self.parent=Node(value)
        else:
            self._insert(value,self.parent)
    def _insert(self,value,curr_node,previous_node=None):
        if curr_node.next==None:
            curr_node.next=Node(value)
            #curr_node.previous=previous_node
            curr_node.next.previous=curr_node
        else:
            self._insert(value,curr_node.next,curr_node)
    
    def delete(self,value):
        if self.parent==None:
            return False
        else:
            if self.parent==value:
                self.parent=
            self._delete(value,self.parent)
    def _delete(self,value,curr_node):
        if 

    def printlist(self):
        if self.parent!=None:
            self._printlist(self.parent)
    def _printlist(self,curr_node):
        if curr_node!=None:
            print(str(curr_node.value))
            self._printlist(curr_node.next)

DLL=DoublyLinkedList()
DLL.insert(10)
DLL.insert(50)
DLL.insert(120)
DLL.insert(103)
DLL.insert(120)
DLL.insert(130)
DLL.insert(180)
DLL.printlist()
'''