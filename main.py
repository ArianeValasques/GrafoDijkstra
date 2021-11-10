
from grafo import Graph

if __name__ == "__main__":
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addVertex('g')
    G.addVertex('h')
    #print("GetVertices", G.getVertices())
    # print("G.Vertices", G.vertices)
    # print(G.vertices['a'].id)
    # print("ConnectedTo", G.vertices['a'].connectedTo)
    G.addEdge('a', 'b', 4)
    G.addEdge('a', 'c', 2)
    G.addEdge('b', 'c', 1)
    G.addEdge('b', 'd', 5)
    G.addEdge('c', 'd', 8)
    G.addEdge('c', 'e', 10)
    G.addEdge('d', 'e', 2)
    G.addEdge('d', 'f', 6)
    G.addEdge('e', 'f', 2)

    #print("GetEdges", G.getEdges())
    print("Largura:")
    print(G.bfs('a'))
    print("Profundidade:")
    print(G.dfs('a'))
    print("Caminho: ", G.dijkstra('a', 'f'))
    del G

