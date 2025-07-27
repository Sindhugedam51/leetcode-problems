class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for n in range(num_vertices)]
        self.adj_list = {i: [] for i in range(num_vertices)}
    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        self.adj_list[u].append(v)
        self.adj_list[u].append(u)
    def display_adj_matrix(self):
        print("Adjacency Matrix: ")
        for row in self.adj_matrix:
            print(row)
    def display_adj_list(self):
        print("Adjacency list: ")
        for vertex, neighbours in self.adj_list.items():
            print(f"{vertex}: {neighbours}") 
graph = Graph(4)
graph.add_edge(0, 1) 
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 3) 
graph.display_adj_matrix()
graph.display_adj_list() 