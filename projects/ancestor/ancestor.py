from collections import deque


def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)
    earliestAncestor = (starting_node, 0)
    stack = deque()
    stack.append((starting_node, 0))
    visited = set()
    while len(stack) > 0:
        curr = stack.pop()
        currNode, distance = curr[0], curr[1]
        visited.add(curr)

        if currNode not in graph:
            if distance > earliestAncestor[1]:
                earliestAncestor = curr
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                earliestAncestor = curr
        else:
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1))

    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1


def createGraph(edges):

    store = {}
    for edge in edges:
        parent, child = edge[0], edge[1]
        if child in store:
            store[child].add(parent)
        else:
            store[child] = set()
            store[child].add(parent)

    return store


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))
