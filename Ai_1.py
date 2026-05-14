from collections import defaultdict, deque

class Graph:
    directed = False      

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

        # Add reverse edge v -> u
        if not self.directed:
            self.graph[v].append(u)


    def DFS(self, v, d, visitSet=None) -> bool:

        visited = visitSet or set()

        visited.add(v)
        print(v, end=" ")

        # Destination found
        if v == d:
            return True

        # Visit adjacent nodes
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                if self.DFS(neighbour, d, visited):
                    return True

        return False


    def BFS(self, s, d):

        visited = defaultdict(bool)
        queue = deque([s])

        visited[s] = True

        while queue:

            s = queue.popleft()
            print(s, end=" ")

            # Destination found
            if s == d:
                return

            # Visit adjacent nodes
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



if __name__ == '__main__':

    g = Graph()

    # Reduced edges
    g.addEdge('H', 'A')
    g.addEdge('A', 'B')
    g.addEdge('A', 'D')
    g.addEdge('B', 'C')
    g.addEdge('C', 'E')
    g.addEdge('C', 'G')
    g.addEdge('E', 'F')

    print("Following is Depth First Traversal H -> E:")
    g.DFS('H', 'F')

    print("\n\nFollowing is Breadth First Traversal H -> E:")
    g.BFS('H', 'F')