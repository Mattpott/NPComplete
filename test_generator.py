"""
    name:  Matthew Potter
"""

import matplotlib.pyplot as plt
import networkx as nx
import random


def dfs(adj_list, vertex) -> list:
    visited = set()
    stack = [vertex]
    while len(stack) > 0:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for w in adj_list[v]:
                stack.append(w)
    return list(visited)


def main():
    # make a random graph with around vertex_count vertices
    # and around edge_count edges
    vertex_count = int(input())
    vertices = list(range(1, vertex_count + 1))
    edge_count = int(input())
    graph = nx.Graph()
    adj_list = {}
    edges = set()
    for _ in range(edge_count):
        u = random.choice(vertices)
        v = random.choice(vertices)
        while v == u:
            v = random.choice(vertices)
        if u not in adj_list:
            adj_list[u] = set()
            graph.add_node(u)
        if v not in adj_list:
            adj_list[v] = set()
            graph.add_node(v)
        adj_list[u].add(v)
        adj_list[v].add(u)
        edges.add((u, v))
        graph.add_edge(u, v)
    # add edges to make the graph connected if it is
    component = dfs(adj_list, random.choice(list(adj_list.keys())))
    other_comp = [u for u in adj_list.keys() if u not in component]
    while len(other_comp) > 0:
        # add edge between two random vertices in the components
        u = random.choice(component)
        v = random.choice(other_comp)
        adj_list[u].add(v)
        adj_list[v].add(u)
        edges.add((u, v))
        graph.add_edge(u, v)
        # connect any other unconnected components
        component = dfs(adj_list, random.choice(component))
        other_comp = [x for x in adj_list.keys() if x not in component]
    print(len(edges))
    for (u, v) in edges:
        print(u, v)
    pos = nx.spring_layout(graph)
    nx.draw(graph, with_labels=True, pos=pos)
    plt.show()


if __name__ == "__main__":
    main()
