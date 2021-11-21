from Graph import Graph


# driver creating graph and run functions
if __name__ == '__main__':
    # creating Click graph order N
    # Modify your graph as you want!
    N = 7
    g = Graph()
    for i in range(N):
        g.add_node(i)

    # Adding edges
    for i in range(N):
        for j in range(N):
            if i != j:
                g.add_edge(i, j)

    # Printing the graph adjacency list
    g.print()

    print("Perform DFS on G...")
    dfs_tree = g.dfs()
    dfs_tree.print()

    print("Perform BFS on G,3...")
    bfs_tree = g.bfs(3)
    bfs_tree.print()



