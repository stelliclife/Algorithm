class Graph:
    def __init__(self, graph):
        self._result = []
        self._graph = graph
        self._visited_nodes = {node: False for node in graph.keys()}

    @property
    def result(self):
        return self._result

    def depth_first_search(self, current_node):
        self._visited_nodes[current_node] = True
        self._result.append(current_node)
        for neighbor in self._graph[current_node]:
            if not self._visited_nodes[neighbor]:
                self.depth_first_search(neighbor)

    def breath_first_search(self, current_node):
        array = []
        self._visited_nodes[current_node] = True
        self._result.append(current_node)

        i = 0
        while len(self._result) != len(self._graph.keys()):
            length = len(self._graph[current_node])
            neighbor = self._graph[current_node][i]
            if not self._visited_nodes[neighbor]:
                self._visited_nodes[neighbor] = True
                array.append(neighbor)
            i += 1
            if i == length:
                if not array:
                    break
                current_node = array.pop(0)
                self._result.append(current_node)
                i = 0