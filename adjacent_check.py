adjacecncy_matrix = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]
  ]

def adjacent_check(node1, node2):
  y = adjacecncy_matrix[node2]
  x = y[node1]
  if x:
    r = "Nodes are adjacent!"
  else:
    r = "Nodes are not adjacent!"
  return r

Nodes = input("Please enter the two numbers you want to check adjacency of separated by a comma.\n").split(",")
print(adjacent_check(node1=int(Nodes[0]), node2=int(Nodes[1])))