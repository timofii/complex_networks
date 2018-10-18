""" CR15 graph library """
class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object """
        if graph_dict:
            self.__graph_dict = graph_dict
        else:
            self.__graph_dict = dict()

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If vertex is not in self.__graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary. Otherwise nothing has to be 
        done. To complete."""
        if not vertex in self.vertices():
            self.__graph_dict[vertex] = []
        
    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list. No loops or 
        multiple edges. To complete."""
        for vertex in edge:
            if not vertex in self.vertices():
                return False
        vertex_1,vertex_2 = edge
        if not vertex_2 in self.__graph_dict[vertex_1]:# forget to check this condition
            self.__graph_dict[vertex_1].append(vertex_2)
            self.__graph_dict[vertex_2].append(vertex_1)

    def __generate_edges(self):
        """ A static method generating the edges of the graph "graph". Edges 
        are represented as sets two vertices, with no loops. To complete."""
        edges = []
        for vertex_1 in self.__graph_dict.keys():
            for vertex_2 in self.__graph_dict[vertex_1]:
                if not set([vertex_1, vertex_2]) in edges:
                    edges.append(set([vertex_1, vertex_2]))
        return edges
    
    def vertex_degree(self, vertex=None):
        """Outputs the degree of each vertex of the graph in a format of your choosing"""
        if vertex == None:
            degrees = []
            for vertex in self.__graph_dict.keys():
                degrees.append((vertex, len(self.__graph_dict[vertex])))
            return degrees
        else:
            return len(self.__graph_dict[vertex])

        
    def find_isolated_vertices(self):
        """Outputs the list of isolated vertices in a graph degree = 0"""
        degrees = self.vertex_degree()
        isolated_vertices = []
        for vertex in degrees:
            if vertex[1] == 0:
                isolated_vertices.append(vertex)
        return isolated_vertices
       
    def density(self):
        """density = #edges/#fully_conected_graph"""
        number_of_edges = len(self.__generate_edges())
        number_of_vertecies = len(list(self.__graph_dict.keys()))
        fully_conected_graph = number_of_vertecies*(number_of_vertecies - 1)/2
        if fully_conected_graph == 0:
            return 0.0
        else:
            return number_of_edges/fully_conected_graph
    
        
        
if __name__ == "__main__":

    G = {
      "a": ["c", "d", "g"],
      "b": ["c", "f"],
      "c": ["a", "b", "d", "f"],
      "d": ["a", "c", "e", "g"],
      "e": ["d"],
      "f": ["b", "c"],
      "g": ["a", "d"]
    }
    graph = Graph(G)   
    