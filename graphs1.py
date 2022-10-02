##graphst
class Graph:
    def __init__(self,num_nodes,is_directed=True):
        self.num_nodes = num_nodes
        self.is_directed = is_directed
        self.adj_matrix = [[0 for column in range(num_nodes)]for row in range(num_nodes)]
        self.adj_list = {node:list() for node in range(num_nodes)}
    def add_edge_matrix(self,node1,node2,weight=1):
        self.adj_matrix[node1][node2] = weight
        if(self.is_directed==False):
            self.adj_matrix[node2][node1] = weight 
    def add_edge_list(self,node1,node2,weight=1):
        self.adj_list[node1].append([node2,weight])
        if(self.is_directed==False):
            self.adj_list[node2].add((node1,weight))
    def print(self):
        print("adj_matrix is ",self.adj_matrix)
        print("adj_list is ", self.adj_list)

if __name__=="__main__":
    g1 = Graph(5)
    g1.add_edge_matrix(0,0,25)
    g1.add_edge_list(0,0,25)
    g1.print()
    print((g1.adj_list[0][0][0]))


    
