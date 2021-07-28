

    def printlist(self):
        if self.parent!=None:
            temp1=self.parent
            while(temp1.next!=None):
                print(temp1.value,end=" ")
                temp1=temp1.next
            print(temp1.value)
    
dll=DoublyLinkedList()