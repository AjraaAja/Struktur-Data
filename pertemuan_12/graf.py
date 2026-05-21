#membuat logic untuk visualisasi streamlit
import networkx as nx
class Graf:
    def __init__(self):
        self.graph = nx.Graph()
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph.add_node(vertex)
        return True
        return False    

    def add_edge(self, v1, v2, w):
        if self.graph.has_node(v1) and self.graph.has_node(v2):
            self.graph.add_edge (v1, v2, weight=w)
        return False
    
    def get_graph(self):
        return self.graph
    
    def get_all_vertex(self):
        return self.graph.nodes()
    
    def get_edge_(self)
        return self.graph.edges()
    
    def get_all_vertex_with_weight(self):
        return self.graph.edges(data=True)
