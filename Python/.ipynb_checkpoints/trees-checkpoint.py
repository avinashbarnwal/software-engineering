
##Inorder Successor
# Node with two children: Get the inorder successor
# (smallest in the right subtree)

class Node:
    
    def __init__(self,key):
        self.left  = None
        self.right = None
        self.data  = key
    
#getRoot
#add
#_add
#find
#_find
#_find
#printTree


class Tree:
    
    def __init__(self):
        self.root = None
        
    def getRoot(self):
        return self.root
    
    def add(self,data):
        if(self.root == None):
            self.root = Node(data)
        else:
            self._add(data,self.root)
            
    def _add(self,data,node):
        if data < node.data:
            if node.left == None:
                node.left = Node(data)
            else:
                self._add(data,node.left)
        else:
            if node.right == None:
                node.right = Node(data)
            else:
                self._add(data,node.right)
    
    def find(self,data):
        if self.root==None:
            return None
        else :
            self._find(data,self.root)
    
    def _find(self,data,node):
        if node.data == data:
            return True
        else:
            if data < node.data and node.left != None:
                self._find(data,node.left)
            elif data < node.data and node.left == None:
                return False
            elif data > node.data and node.right != None:
                self._find(data,node.right)
            else:
                return False
     
    def deletenode(self,data):
        if self.root == None:
            return None
        else:
            self._deletenode(data,self.root)
        
    def _deletenode(self,data,node):
        if node.data == data:
            if node.left == None:
                node = node.right
            elif node.right ==None:
                node = node.left
            else:
                parent    = node
                successor = node.right
                while successor.left:
                    parent    = successor
                    successor = successor.left
                node.data   = successor.data
                parent.left = None
    
    def inorder_list(self,root):
        res = []
        if root:
            res = self.inorder_list(root.left)
            res.append(root.data)
            res = res + self.inorder_list(root.right)
        return res  
    def inorder_print(self,node):
        if node:
            self.inorder_print(node.left)
            print(node.data)
            self.inorder_print(node.right)
                
if __name__ == "__main__":    
    T1 =   Tree()
    T1.add(1)
    T1.add(10)
    T1.add(3)
    T1.inorder_print(T1.root) 
    T1.deletenode(3)

