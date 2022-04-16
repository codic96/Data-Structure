class Node:
  def __init__(self,key):
    self.left=None
    self.right = None
    self.val = key
#Traverse preorder 

def traversePreOrder(self):
  print(self.val,end='')
  if self.left:
    self.left.traversePreorder()
  if self.right:
    self.right.traversePreOrder()
 
#Traverse Order

def traverseInorder(self):
  if self.left:
    self.left.traverseInorder()
  print(self.val,end='')
  if self.right:
    self.right.traverseInorder()

#Traverse postorder

def traversePostOrder(self):
  if self.left:
    self.left.traversePostOrder()
  if self.right:
    self.right.traversePostOrder()
  print(self.val,end='')
  
    
    
    
