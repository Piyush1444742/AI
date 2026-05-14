def astaralgo(start_node, stop_node):
    open_set = set(start_node)
    closed_set = set()

    g = {}
    parents = {}
    g[start_node] = 0
    parents[start_node] = start_node

    # Loop until open set becomes empty
    while len(open_set) > 0:
        n = None

        for v in open_set:

            if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        # If goal node reached or node has no neighbors
        if n == stop_node or Graph_nodes[n] == None:
            pass

        else:

            # Explore neighbors of current node
            for (m, weight) in get_neighbors(n):

                # If neighbor is not visited
                if m not in open_set and m not in closed_set:

                    # Add neighbor to open set
                    open_set.add(m)

                    # Set current node as parent
                    parents[m] = n

                    # Calculate path cost
                    g[m] = g[n] + weight

                else:

                    # Check if shorter path exists
                    if g[m] > g[n] + weight:

                        # Update distance
                        g[m] = g[n] + weight

                        # Update parent node
                        parents[m] = n

                        # Move node back to open set
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n == None:
            print("path does not exist!")
            return None

        if n == stop_node:

            # Store final path
            path = []

            # Backtrack path using parent nodes
            while parents[n] != n:

                path.append(n)
                n = parents[n]

            path.append(start_node)

            # Reverse path to get correct order
            path.reverse()

            # Print final shortest path
            print("Path found: {}".format(path))

            return path

        # Remove current node from open set
        open_set.remove(n)

        # Add current node to closed set
        closed_set.add(n)

    print("Path does not exist!")

    return None

def get_neighbors(v):

    if v in Graph_nodes:
        return Graph_nodes[v]

    else:
        return None


def heuristic(n):
    H_dist = {

        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }

    return H_dist[n]

Graph_nodes = {

    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}


astaralgo('A', 'G')