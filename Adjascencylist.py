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
    
    
