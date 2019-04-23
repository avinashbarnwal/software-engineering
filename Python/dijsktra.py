import collections
import math

class Graph:

    def __init__(self):
        self.vertices    = set()
        self.edges       = collections.defaultdict(list)
        self.weights      = {}

    def add_edges(self,from_vertex,to_vertex,distance):
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex,to_vertex)] = distance

    def add_vertex(self,value):
        self.vertices.add(value)

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string

def dijkstra(graph,start):
    S=set()
    delta    = dict.fromkeys(list(graph.vertices),math.inf)
    previous = dict.fromkeys(list(graph.vertices),None)

    delta[start] = 0

    while S!=graph.vertices:
        v = min((set(delta.keys)-S),key=delta.get)
        for neighbor in set(graph.edges[v])-S:
            new_path = delta[v] + graph.weights[v,neighbor]

            if new_path < delta[neighbor]:
                # since it's optimal, update the shortest path for neighbor
                delta[neighbor] = new_path
                # set the previous vertex of neighbor to v
                previous[neighbor] = v

    return (delta, previous)

def shortest_path(graph, start, end):
    '''Uses dijkstra function in order to output the shortest path from start to end
    '''

    delta, previous = dijkstra(graph, start)
    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]

    path.reverse()
    return path

G = Graph()
G.add_vertex('a')
G.add_vertex('b')
G.add_vertex('c')
G.add_vertex('d')
G.add_vertex('e')

G.add_edge('a', 'b', 2)
G.add_edge('a', 'c', 8)
G.add_edge('a', 'd', 5)
G.add_edge('b', 'c', 1)
G.add_edge('c', 'e', 3)
G.add_edge('d', 'e', 4)

print(G)

print(dijkstra(G, 'a'))
print(shortest_path(G, 'a', 'e'))
