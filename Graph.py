#Adjacency Matrix representation in Python

class Graph(object):
  #Initialize the Matrix
  def __init__(self,size):
    self.adjMatrix=[]
    for i in range(size):
      self.adjMatrix.append([0 for i in range(size)])
      self.size=size
      
    
