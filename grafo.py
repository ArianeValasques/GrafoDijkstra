from vertex import Vertex
from queue import Queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.vertices[key] = newVertex
        return newVertex

    def getVertex(self, key):
        return self.vertices[key]

    def addEdge(self, f, t, cost):
        if f not in self.vertices:
            v1 = Vertex(f)
            self.vertices[f] = v1
        if t not in self.vertices:
            v2 = Vertex(t)
            self.vertices[t] = v2
        self.vertices[f].addNeighbor(self.vertices[t], cost)
        self.vertices[t].addNeighbor(self.vertices[f], cost)

    def getVertices(self):
        return self.vertices.keys()

    def getEdges(self):
        edges = set()
        for name, vertex in self.vertices.items():
            for nbr in vertex.connectedTo:
                edges.add((name, nbr.id, vertex.getWeight(nbr)))
        return list(edges)

    def bfs(self, start):
        fila = Queue()
        fila.put(start)
        visitado = [start]
        while fila.qsize() > 0:
            vert = fila.get()
            for nbr in self.vertices[vert].getConnections():
                if nbr.id not in visitado:
                    visitado.append(nbr.id)
                    fila.put(nbr.id)
        return visitado

    def dfs(self, start):
        pilha = [start]
        visit = []
        while pilha:
            vertic = pilha.pop()
            if vertic not in visit:
                visit.append(vertic)
                for nbr in self.vertices[vertic].getConnections():
                    if nbr.id not in visit:
                        pilha.append(nbr.id)
        return visit

    def dijkstra(self, start, end):
        info = {}
        path = []
        naoVisitados = []
        predecessor = {}
        infinito = 1e309
        info[start] = 0

        for key in self.vertices.keys():  # Inicializa todos como não visitados
            if key != start:
                info[key] = infinito
            naoVisitados.append(key)

        iteracao = 0

        while naoVisitados:

            if iteracao == 0:
                vertice = start
                iteracao = 1

            else:
                vertice = None

            for node in naoVisitados:
                if vertice is None:
                    vertice = node
                elif info[node] < info[vertice]:
                    vertice = node

            for neighbor in self.vertices[vertice].getConnections():
                nbr = neighbor.id
                cost = self.vertices[vertice].connectedTo.get(neighbor)
                total = info[vertice] + cost

                if total < info[nbr]:
                    info[nbr] = total
                    predecessor[nbr] = vertice
            naoVisitados.remove(vertice)

        node = end

        while node != start:
            try:
                path.insert(0, node)
                node = predecessor[node]
            except KeyError:
                print("Caminho inacessível")
                break
        path.insert(0, start)

        if info[end] != infinito:
            print("Menor distancia: " + str(info[end]))
            # print("Caminho: " + str(path))
            return path
