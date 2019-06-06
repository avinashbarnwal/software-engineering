class Stack(object):
    
    def __init__(self):
        self._item = []
        
    def is_empty(self):
        return not bool(self._item)
    
    def push(self,data):
        self._item.append(data)
        
    def pop(self):
        return self._item.pop()
    
    def peek(self):
        return self._item[-1]
    
    def size(self):
        return len(self._items)