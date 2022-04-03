class Node:
  #Creating a Node 
  def __init__(self,item):
    self.item = item 
    self.next = None 
class LinkedList:
  def __init__(self):
    self.head = None

 if __name__ == '__main__':
  linkedlist = LinkedList()
  #Assign item values
  linked_list.head = Node(1)
  second = Node(2)
  third = Node(3)
  
  #Connect Nodes
  linked_list.head.next = second
  second.next = third
  
  #Print the linkedlist item
  while linked_list.head !=None:
    print(linked_list.head.item,end='')
    linked_list.head = linked_list.head.next
    
    
    #Second Example 
    #create a node
    class Node:
      def __init__(self,data):
        self.data=data
        self.next=None
    class LinkedList:
      def __init__(self):
        self.head = None
      #Insert at the beginning 
      
      def insertAtBeginning(self,new_data):
        new_node=Node(new_data)
        new_node.next =self.head
        self.head = new_node 
     #Insert after a node
      
      def insertAtAfter(self,prev_node,new_data):
        if prev_node is None:
          print("The given previous node must linkedlist")
          return 
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next =  new_node
        
        
        
    
  
    
