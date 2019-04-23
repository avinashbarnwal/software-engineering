
# coding: utf-8

# In[5]:

class Node:
    
    def __init__(self,weight):
        self.data = weight
        self.next = None 
        
    def getData(self):
        return self.data
    
    def setNext(self,new):
        self.next = new
        
    def getNext(self):
        return self.next

class Unorderedlist:
    
    def __init__(self):
        self.head = None
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count = count +1
            current = current.getNext()
        return count        
    
    def search(self,item):
        current = self.head
        found = False
        
        while current != None:
            if current.getData() == item :
                found =True
                break
            else:
                current = current.getNext()
        return found
     
if __name__ == '__main__':
    
    mylist = Unorderedlist()
    mylist.add(1)
    mylist.add(8)
    mylist.add(6)
    mylist.add(3)
    mylist.add(6)
    mylist.size()
    
    
  
    
    
        

