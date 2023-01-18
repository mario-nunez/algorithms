"""Implementation of a graph using an adjacency list"""


class Graph:
    """
    A class to represent a graph using an adjacency list
    """
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2, bidirectional=True):
        """Add an edge to the graph. Accept bidirectional creation"""
        if (   v1 not in self.adj_list.keys()
            or v1 not in self.adj_list.keys()
            or v1 == v2
           ):
                return False
        if v2 not in self.adj_list[v1]:
            self.adj_list[v1].append(v2)
        if (    bidirectional is True
            and v1 not in self.adj_list[v2]
           ):
                self.adj_list[v2].append(v1)
        return True

    def remove_edge(self, v1, v2, bidirectional=True):
        """Remove certain edge from the graph. Accept bidirectional delete"""
        if (   v1 not in self.adj_list.keys()
            or v1 not in self.adj_list.keys()
            or v1 == v2):
                return False
        if v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
        if (    bidirectional is True
            and v1 in self.adj_list[v2]
           ):
            self.adj_list[v2].remove(v1)
        return True

    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges"""
        if vertex not in self.adj_list:
            return False
        for other_vertex in self.adj_list[vertex]:
            if vertex in self.adj_list[other_vertex]:
                self.adj_list[other_vertex].remove(vertex)
        del self.adj_list[vertex]
        return True

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])


if __name__ == '__main__':
    my_graph = Graph()

    my_graph.add_vertex('A')
    my_graph.add_vertex('B')
    my_graph.add_vertex('C')

    my_graph.add_edge('A', 'B')
    my_graph.add_edge('A', 'C')
    my_graph.add_edge('C', 'B')
    print('adding edge to same vertex:', my_graph.add_edge('A', 'A'))

    # test remove_edge
    print('\nBefore deleting A->C vertex')
    my_graph.print_graph()
    my_graph.remove_edge('A', 'C', False)
    print('\nAfter deleting A->C vertex')
    my_graph.print_graph()
    print('removing edge to same vertex:', my_graph.add_edge('A', 'A'))
    print('removing edge from vertex doesnt exist:', my_graph.remove_edge('N', 'A'))

    # test remove_vertex
    my_graph = Graph()

    my_graph.add_vertex('A')
    my_graph.add_vertex('B')
    my_graph.add_vertex('C')
    my_graph.add_vertex('D')

    my_graph.add_edge('A', 'B')
    my_graph.add_edge('A', 'C')
    my_graph.add_edge('A', 'D')
    my_graph.add_edge('B', 'D')
    my_graph.add_edge('C', 'D')

    print('\nBefore deleting D vertex')
    my_graph.print_graph()
    my_graph.remove_vertex('D')

    print('\nAfter deleting D vertex')
    my_graph.print_graph()

    print('removing vertex doesnt exist:', my_graph.remove_vertex('N'))
