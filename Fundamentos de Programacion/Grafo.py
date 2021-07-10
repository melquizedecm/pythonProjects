from collections import deque


class Graph(object):
    def __init__(self):
        self.relations = {}

    def __str__(self):
        return str(self.relations)

    def addVertice(graph, element):
        graph.relations.update({element: []})

    def addRelations(graph, element1, element2):
        graph.addOneRelation(element1, element2)
        graph.addOneRelation(element2, element1)

    def addOneRelation(graph, origin, destination):
        graph.relations[origin].append(destination)

    def printElement(graph, element):
        print(element)

    def dfs(graph, first_element, function, toured_elements=None):
        if toured_elements is None:
            toured_elements = []
        if first_element in toured_elements:
            return True
        function(first_element)
        toured_elements.append(first_element)
        for neighbour in graph.relations[first_element]:
            graph.dfs(neighbour, function, toured_elements)

    def bfs(graph, first_element, function, queue=deque(), toured_elements=None):
        if toured_elements is None:
            toured_elements = []
        if not first_element in toured_elements:
            function(first_element)
            toured_elements.append(first_element)
            if len(graph.relations[first_element]) > 0:
                queue.extend(graph.relations[first_element])
        if len(queue) != 0:
            graph.bfs(queue.popleft(), function, queue, toured_elements)



grafo = Graph()
grafo.addVertice("A")
grafo.addVertice("B")
grafo.addVertice("C")
grafo.addVertice("D")

grafo.addRelations("A", "B")
grafo.addRelations("A", "C")
grafo.addRelations("A", "D")
grafo.addRelations("B", "C")
print("------------------------------------------------------------------------------")
print(grafo)
print("------------------------------------------------------------------------------")

