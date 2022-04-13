#Tree traveral in Python

class Node:
  def __init__(self,val):
    self.left=None
    self.right=None
    self.val =item
def inorder(root):
  if root:
    #Traverse left
    inorder(root.left)
    #Traverse right
    print(str(root.val)+ "->",end='')
    #Traverse right
    inorder(root.right)
    
    
    
    
