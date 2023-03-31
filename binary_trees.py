from trees import Node 
from trees import Tree

class Node(Node):
    def __init__(self, label, parent=None):
        super().__init__(label, parent)
    
    def add_child(self, child):
        if len(self.children) < 2:
            return super().add_child(child)
        else:
            raise RuntimeError("Parent already has two children.")


class BinaryTree(Tree):
    def __init__(self):
        super().__init__()

    def add_node(self, label, parent=None, class_to_instantiate=Node):
        return super().add_node(label, parent, class_to_instantiate)


if __name__ == '__main__':

    # a = Node('A')
    # b = Node('B', parent=a)
    # c = Node("C")
    # b.add_child(c)
    # print(a.children)

    t = BinaryTree()
    t.add_node('A')
    t.add_node("B", "A")
    t.add_node("C", "A")
    t.add_node("D", "B")
    t.add_vertex("D", "C")
    t.add_edge(("C", "D_1"), 2)
    t.add_child("C", "H")
    t.add_child("D", "J")
    t.add_child("D_1", "J")
    #t.add_child("A", "P")

    print(t)