#Adjasency List representation in Python

class AdjNode:
  def __init__(self,vales):
    self.vertices = vales
    self.next = None
class Graph:
  def __init__(self,num):
    self.v = num
    self.graph=[None]*self.v
  #Add edges
  
  def add_edges(self,s,d):
    node = AdjNode(d)
    node.next = self.graph[s]
    self.graph[s]=node
    node = AdjNode(s)
    node.next = self.graph[d]
    self.graph[d]=node 
 
#Print the edges 

def print_agraph(self):
  for i in range(self.v):
    print("vertex"+str(i)+":",end="")
    temp = self.graph(i)
    while temp:
      print("->{}".format(temp.vertex),end='')
      temp = temp.next
      print('\n')
 
if __name__ == '__main__':
  V = 5
  #Create graph and edges 
  graph = Graph(5)
  graph.add_edges(0,1)
  graph.add_edges(0,2)
  graph.add_edges(0,3)
  graph.add_edges(1,2)
  graph.print_agraph()
  
      
    
