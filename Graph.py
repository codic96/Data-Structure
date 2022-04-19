#Adjacency Matrix representation in Python

class Graph(object):
  #Initialize the Matrix
  def __init__(self,size):
    self.adjMatrix=[]
    for i in range(size):
      self.adjMatrix.append([0 for i in range(size)])
      self.size=size
  #Add edges 
  def add_edge(self,v1,v2):
    if v1==v2:
      print("Some vertex %d and %d" %(v1,v2))
    self.adjMatrix[v1][v2]=1
    self.adjMatrix[v2][v1]=1
  #Remove edges 
  def remove_edge(self,v1,v2):
    if self.adjMatrix[v1][v2]==0:
      print("No edge between %d and %d" %d(v1,v2))
      return 
    self.adjMatrix[v1][v2]=0
    self.adjMatrix[v2][v1]=0
 def __len__(self):
  return self.size
#Print the matrix 
def print_matrix(self):
  for row in self.adjMatrix:
    for val in row:
      print('{:4}'.format(val))
      
    
      
    
