import pytest

from dsa.graph import Graph


def test_graph_initialization():
    """Test graph initializacion"""
    expected_result = {}
    graph = Graph()
    result = graph.adj_list
    assert result == expected_result


@pytest.mark.xfail
def test_graph_wrong_initialization_list():
    """Test graph wrong initializacion using a list"""
    Graph([1, 2, 3])


def test_graph_add_vertex():
    """Test graph add vertex method"""
    expected_result_add_vertex = True
    expected_result_wrong = False
    expected_result = {'A': [], 'B': []}
    graph = Graph()
    result_add_vertex1 = graph.add_vertex('A')
    result_add_vertex2 = graph.add_vertex('B')
    result_wrong = graph.add_vertex('A')
    result = graph.adj_list
    assert result_add_vertex1 == expected_result_add_vertex
    assert result_add_vertex2 == expected_result_add_vertex
    assert result_wrong == expected_result_wrong
    assert result == expected_result


def test_graph_add_edge():
    """Test graph add edge method"""
    expected_result_add_edge = True
    expected_result_wrong = False
    expected_result = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B']}
    graph = Graph()
    print(graph.adj_list)
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    result_add_edge1 = graph.add_edge('A', 'B')
    result_add_edge2 = graph.add_edge('B', 'C', False)
    result_add_edge3 = graph.add_edge('C', 'B')
    result_wrong = graph.add_edge('D', 'A')
    result = graph.adj_list
    assert result_add_edge1 == expected_result_add_edge
    assert result_add_edge2 == expected_result_add_edge
    assert result_add_edge3 == expected_result_add_edge
    assert result_wrong == expected_result_wrong
    assert result == expected_result


def test_graph_remove_edge():
    """Test graph remove edge method"""
    expected_result_remove_edge = True
    expected_result_wrong = False
    expected_result = {'A': [], 'B': [], 'C': ['B']}
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    result_remove_edge1 = graph.remove_edge('A', 'B')
    result_remove_edge2 = graph.remove_edge('B', 'C', False)
    result_wrong = graph.remove_edge('D', 'A')
    result = graph.adj_list
    assert result_remove_edge1 == expected_result_remove_edge
    assert result_remove_edge2 == expected_result_remove_edge
    assert result_wrong == expected_result_wrong
    assert result == expected_result


def test_graph_remove_vertex():
    """Test graph remove vertex method"""
    expected_result_remove_vertex = True
    expected_result_wrong = False
    expected_result = {'B': ['C'], 'C': ['B']}
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    result_remove_vertex1 = graph.remove_vertex('A')
    result_remove_vertex2 = graph.remove_vertex('D')
    result_wrong = graph.remove_vertex('E')
    result = graph.adj_list
    assert result_remove_vertex1 == expected_result_remove_vertex
    assert result_remove_vertex2 == expected_result_remove_vertex
    assert result_wrong == expected_result_wrong
    assert result == expected_result


def test_graph_print():
    """Test graph print method"""
    expected_vertex_exist = True
    expected_result = {'A': ['B'], 'B': ['A', 'C'], 'C': ['B'], 'D': []}
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C', False)
    graph.add_edge('C', 'B')
    graph.print_graph()
    for vertex in graph.adj_list:
        vertex_exist = vertex in expected_result
        assert vertex_exist == expected_vertex_exist
        assert graph.adj_list[vertex] == expected_result[vertex]
