from graphs import Vertex
from graphs import DirectedGraph 
import pptree

class Node(Vertex):
    def __init__(self, label, parent=None):
        super().__init__(label)
        self.children = self.neighbors
        self.parent = None
        self._initiate_parent(parent)    

    def _initiate_parent(self, parent):
        """
        Add parent to Node and child to parent
        Args:
            parent -- parent Node()
        """
        if not parent is None:
            parent.add_child(self)
        return

    def is_root(self):
        """
        Check if Node is root of Tree
        Output:
            Boolean
        """
        if self.parent is None:
            return True
        else:
            return False

    def is_leaf(self):
        """
        Check if Node is leaf of Tree
        Output:
            Boolean
        """
        if self.children:
            return False
        else:
            return True
    
    
    def depth(self):
        """
        Check the depth of the Node in Tree
        Output:
            Integer with depth
        """   
        if self.is_root():
            return 0
        else:
            return 1 + self.parent.depth()

    def add_child(self, child):
        """
        Adding a child to the node while updating the parent attribute of the child.
        Args:
            child -- child of type Node
            weight -- weight of edge between Node and child
        """
        Vertex.add_neighbor(self, child, 1)
        child.parent = self
        return

    def add_weight(self, child, weight):
        self.children[child]=weight
        return


class Tree(DirectedGraph):
    def __init__(self):
        """ 
        A class creating Tree-like objects with parents and children.
        Use add_node to build the tree.
        """
        super().__init__([])
        self.height=0
        self.root=None

    def __str__(self):
        pptree.print_tree(self.root,'children','name')
        return ""

    def add_node(self, label, parent=None, class_to_instantiate=Node):
        """
        Add node to the tree. If the node exists, create new node with underscore id but same label.
        First added node will be made root. Every other node must be declared with existing node as parent.
        If you want to add a weight to the edge, please use add_edge after creating the node.
        Args:
            label -- label of node to be created
            parent -- label of parent node
        Output:
            Node() object of newly created node
        """
        self.num_vertices = self.num_vertices + 1
        i = 1
        while True:
            if label in self.vert_dict:
                label = label.split('_')[0] + '_' + str(i)
                i += 1
            else:
                break

        if self.root is None:
            new_node = class_to_instantiate(label)
            self.root=new_node
        else:
            if parent is None:
                raise ValueError("Please specify parent id")
            assert parent in self.vert_dict, "Please specify existing parent"


            parent=self.vert_dict[parent]
            new_node = class_to_instantiate(label, parent)

        self.vert_dict[label] = new_node
        
        return new_node

    def add_child(self, parent, child, class_to_instantiate=Node):
        """
        Add a child to an  existing node
        Args:
            parent -- existing label of Node in Tree
            child -- label of new Node to be created
        Output:
            Node() object of newly created node
        """
        return self.add_node(label=child, parent=parent, class_to_instantiate=class_to_instantiate)

    def add_vertex(self, label, parent=None, class_to_instantiate=Node):
        """
        Please use add_node()
        """
        return self.add_node(label, parent, class_to_instantiate)

    def get_node(self, label):
        """
        Return node if exists in Graph
        Args:
            label -- label of node
        Output:
            Node() object if node exists, None else
        """
        return self.get_vertex(label)

    def all_nodes(self):
        """ 
        returns the nodes of a tree as a set 
        Output:
            Set of all labels of nodes in Tree
        """
        return self.all_vertices()

    def add_edge(self, edge, weight):
        """
        Adds a weight to an existing parent-child pair.
        Args:
            edge -- edge in form of tuple or list with node labels (parent, child)
            weight -- weight of edge as float
        """
        for vertex in edge:
            if vertex not in self.vert_dict:
                raise ValueError("Choose existing nodes")

        if self.vert_dict[edge[1]] in self.vert_dict[edge[0]].children:
            self.vert_dict[edge[0]].add_weight(self.vert_dict[edge[1]], weight)
        else:
            raise ValueError("Choose existing parent-child combination")
        return

    def get_root(self):
        """
        Get the root of the Tree. Use .label to the label if the root.
        Output:
            Node object of the root of the tree
        """
        return self.root

if __name__ == '__main__':

    # a = Node('A')
    # b = Node('B', parent=a)
    # c = Node("C")
    # b.add_child(c)
    # print(a.children)

    t = Tree()
    t.add_node('A')
    t.add_node("B", "A")
    t.add_node("C", "A")
    t.add_node("D", "B")
    t.add_vertex("D", "C")
    t.add_edge(("C", "D_1"), 2)
    t.add_child("C", "H")
    t.add_child("D", "J")
    t.add_child("D_1", "J")
    t.add_child("A", "P")

    print(t)



