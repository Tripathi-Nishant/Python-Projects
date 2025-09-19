class Node:
    def _init_(self, name):
        self.name = name
        self.edges = []

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def _init_(self, source, target, relation):
        self.source = source
        self.target = target
        self.relation = relation


class KG:
    def _init_(self, name):
        self.name = name
        self.nodes = {}

    def add_node(self, node_name):
        if node_name not in self.nodes:
            self.nodes[node_name] = Node(node_name)
        return self.nodes[node_name]
    
    def add_edge(self, source_name, target_name, relation):
        self.add_node(source_name)
        self.add_node(target_name)
        source_node = self.nodes[source_name]
        target_node = self.nodes[target_name]
        edge = Edge(source_node, target_node, relation)
        source_node.add_edge(edge)
        
    def display(self):
        for node in self.nodes.values():
            for edge in node.edges:
                print(f"{edge.source.name} -[{edge.relation}]-> {edge.target.name}")

    def check_relation(self, source_name, target_name, relation):
        if source_name not in self.nodes or target_name not in self.nodes:
            return False
        source_node = self.nodes[source_name]
        for edge in source_node.edges:
            if edge.target.name == target_name and edge.relation.lower() == relation.lower():
                return True
        return False


if _name_ == "_main_":
    graph = KG("Family Tree")
    graph.add_edge("A", "B", "is father of")
    graph.add_edge("B", "C", "is sibling of")
    graph.add_edge("A", "C", "is father of")
    graph.add_edge("A", "D", "is partner of")
    graph.add_edge("D", "B", "is mother of")
    graph.add_edge("D", "C", "is mother of")

    print("Knowledge Graph")
    graph.display()

    print("\nQueries:")
    print("Is A father of B?", graph.check_relation("A", "B", "is father of"))
    print("Is B sibling of C?", graph.check_relation("B", "C", "is sibling of"))
    print("Is D father of A?", graph.check_relation("D", "A", "is mother of"))