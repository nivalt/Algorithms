class Graph:
    # init empty graph
    def __init__(self):
        self.adj_list = dict()

    # add new node to graph
    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    # add new edge to graph (node1,node2) as node1-->node2
    # def weight between nodes will be 1
    def add_edge(self, node1, node2, weight=1):
        if node1 in self.adj_list and node2 in self.adj_list:
            if (node2, weight) not in self.adj_list[node1]:
                self.adj_list[node1].append((node2, weight))
            else:
                print("node2 is already neighbor of " + str(node1) + ", the edge in node 1 are: " +
                      str(self.adj_list.get(node1)))
        else:
            print("One or more of nodes are not in graph")

    def dfs(self):
        tree = Graph()
        visited_list = [0] * len(self.adj_list)
        for v in self.adj_list:
            if visited_list[v] == 0:
                visited_list[v] = 1
                tree.add_node(v)
                self.dfs_visit(v, visited_list, tree)
        return tree

    def dfs_visit(self, v, visited_list, tree):
        for u in self.adj_list[v]:
            if visited_list[u[0]] == 0:
                visited_list[u[0]] = 1
                tree.add_node(u[0])
                tree.add_edge(v, u[0])
                self.dfs_visit(u[0], visited_list, tree)

    def bfs(self, v=0):
        que = []
        visited_list = [0] * len(self.adj_list)
        tree = Graph()
        tree.add_node(v)
        que.append(v)
        visited_list[v] = 1
        while len(que) != 0:
            u = que.pop(0)
            for w in self.adj_list[u]:
                w = w[0]
                if visited_list[w] == 0:
                    tree.add_node(w)
                    tree.add_edge(u,w)
                    visited_list[w] = 1
                    que.append(w)
        return tree

    def print(self):
        for node in self.adj_list:
            print(node, " ---> ", [i for i in self.adj_list[node]])
