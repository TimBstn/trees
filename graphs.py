class Vertex(object):
    def __init__(self, label):
        self.id = label
        self.label = label.split("_")[0]
        self.neighbors = {}
        print(f"Vertex created with label {self.label} and id {self.id}")

    def __str__(self):
        return self.label  

    def add_neighbor(self, neighbor, weight=1):
        """
        Adding a neighbor of type Vertex()
        Args:
            neighbor -- instance of Vertex()
            weight -- weight of edge between vertex and neighbor
        """
        self.neighbors[neighbor] = weight
        return

    def get_neighbors(self):
        """
        Get all the neighbors (labels) of the Vertex
        """
        return self.neighbors.keys()

    def get_label(self):
        """
        Return label of Vertex
        """
        return self.label

    def get_weight(self, neighbor):
        """
        Get weight between Vertex and neighbor
        Args:
            neighbor -- instance of Vertex()
        Output:
            Weight between Vertex and neighbor
        """
        return self.neighbors[neighbor]
    

class Graph(object):

    def __init__(self, vert_list=[]):
        """ 
        A class creating Graph-like objects with vertices and egdes
        Args:
            vert_list -- list of vertices in form labels

        """
        self.vert_dict = {}
        self.num_vertices = len(vert_list)
        self._initiate_graph(vert_list)
        

    def __iter__(self):
        """
        iterate over vertices when called in iter
        """
        return iter(self.vert_dict.values())

    def __str__(self):
        res = "vertices: "
        for k in self.vert_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self._generate_edges():
            res += str(edge) + " "
        return res

    def _initiate_graph(self, vert_list):
        """
        Initate graph when Graph() is called with default vertices
        Args:
            vert_list -- list of vertices in form labels
        """
        for vertex in vert_list:
            self.add_vertex(vertex)
        return 

    def add_vertex(self, label, class_to_instantiate=Vertex):
        """  
        Add a new vertex to the graph, if vertex not already exists. If the vertex exists, create new vertex with underscore id but same label.
        Args:
            label -- label of vertex to be created
        Output:
            Vertex() object of newly created vertex
        """
        self.num_vertices = self.num_vertices + 1
        i = 1
        while True:
            if label in self.vert_dict:
                label = label.split('_')[0] + '_' + str(i)
                i += 1
            else:
                break
        new_vertex = class_to_instantiate(label)
        self.vert_dict[label] = new_vertex
        return new_vertex

    def delete_vertex(self):
        return

    def get_vertex(self, label):
        """
        Return vertex if exists in Graph
        Args:
            label -- label of vertex
        Output:
            Vertex() object if vertex exists, None else
        """
        if label in self.vert_dict:
            return self.vert_dict[label]
        else:
            return None

    def all_vertices(self):
        """ 
        returns the vertices of a graph as a set 
        Output:
            Set of all labels of vertices in Graph
        """
        return set(self.vert_dict.keys())

    def add_edge(self, edge, weight=1):
        """ 
        Add an edge to the Graph (no multi edges possible)
        Args:
            edge -- edge in form of tuple or list with vertex labels. 
            weight -- weight of edge as float
            
        """
        for vertex in edge:
            if vertex not in self.vert_dict:
                self.add_vertex(vertex)

        self.vert_dict[edge[0]].add_neighbor(self.vert_dict[edge[1]], weight)
        self.vert_dict[edge[1]].add_neighbor(self.vert_dict[edge[0]], weight)
        return

    def delete_edge(self):
        return
        

    def get_neighbors(self, label):
        """ 
        Get all the neighbors (labels) of a Vertex in Graph
        Args:
            label -- label of vertex
        Output:
            list of all the labels of the neighbors of the vertex
        """
        assert self.vert_dict[label], "No vertex with that label in Graph."
        neighbor_vertices = self.vert_dict[label].get_neighbors()
        return [n.id for n in neighbor_vertices]
        

    def all_edges(self):
        """ 
        Returns the edges of a graph as a list. Edges are represented as sets
        Output:
            list of all edges (as set) in Graph
         """
        return self._generate_edges()


    def _generate_edges(self):
        edges = []
        for vertex in self.vert_dict:
            for neighbour in self.get_neighbors(vertex):
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges


class DirectedGraph(Graph):
    def __init__(self, vert_list=[]):
        super().__init__(vert_list)


    def add_edge(self, edge, weight=1):
        """ 
        Add an edge to the Graph (no multi edges possible)
        Args:
            edge -- edge in form of tuple or list with vertex labels. 
                    First entry signals origin, last entry signals end of edge
            weight -- weight of edge as float
            
        """
        for vertex in edge:
            if vertex not in self.vert_dict:
                self.add_vertex(vertex)

        self.vert_dict[edge[0]].add_neighbor(self.vert_dict[edge[1]], weight)
        return

    def get_children(self, label):
        """ 
        Get all the children (labels) of a Vertex in Graph
        Args:
            label -- label of vertex
        Output:
            list of all the labels of the children of the vertex
        """
        return Graph.get_neighbors(self, label)

    def _generate_edges(self):
        edges = []
        for vertex in self.vert_dict:
            for neighbour in self.get_neighbors(vertex):
                edges.append((vertex, neighbour))
        return edges


# if __name__ == '__main__':
#     g = DirectedGraph()

#     g.add_vertex('a')
#     g.add_vertex('b')
#     g.add_vertex('c')
#     g.add_vertex('d')
#     g.add_vertex('e')
#     g.add_vertex('f')
#     g.add_vertex('f')
#     g.add_vertex('f')

#     g.add_edge(('a', 'b'), 7)  
#     g.add_edge(('b', 'a'), 7) 
#     g.add_edge(('a', 'c'), 9)
#     g.add_edge(('a', 'f'), 14)
#     g.add_edge(('a', 'f_1'), 14)
#     g.add_edge(('a', 'f_5'), 14)

#     print(g.children("a"))