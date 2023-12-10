"""
    name:  Matthew Potter
"""

import matplotlib.pyplot as plt
import networkx as nx
from timeit import default_timer as timer


# Exact Algorithm:
# Uses Branch-and-Bound/Backtracking Approach by adapting pseudocode from:
# *****************************************************************************
# Title: An Exact Algorithm for Minimum Vertex Cover Problem
# Authors: Luzhi Wang, Shuli Hu, Mingyang Li, and Junping Zhou
# Date: Published 6 July, 2019
# Version: Published in Mathematics volume 7(7), page 603
# Source: https://www.mdpi.com/2227-7390/7/7/603
# Formal citation:
#   Wang, L. et al. 2019. An Exact Algorithm for Minimum Vertex Cover Problem.
#   Mathematics. 7, 7 (Jul. 2019), 603. DOI:https://doi.org/10.3390/math7070603.
# *****************************************************************************
# *****************************************************************************
# Title: Choosing the Efficient Algorithm for Vertex Cover Problem
# Authors: K.V.R.Kumar, supervised by Dr. Deepak Garg
# Date: June 2009
# Version: CIIT International Journal of Software
#          Engineering and Technology May 2009 issue
# Source:https://gdeepak.com/thesisme/thesis-Choosing%20the%20Efficient%20Algorithm%20for%20Vertex%20Cover%20problem.pdf
# Formal citation:
#   K.V.R Kumar, Deepak Garg, Complete Algorithms on Minimum Vertex Cover
#   CIIT International Journal of Software Engineering and Technology, Issue
#   May 2009 ISSN 0974 – 9748 & Online: ISSN 0974 – 9632.
# ****************************************************************************
def mvc(adj_list: dict[str, set]) -> set:
    # N(v) denotes the neighborhood of v (does not include v) [N(v) = {u in V | (u, v) is in E}]
    # N*(v) denotes the closed neighborhood of v (includes v) [N(v) including v]
    # Input: a graph G = (V, E), an upper bound UB = |V|, and a growing partial vertex cover C = Empty Set
    # Output: the size of the minimum vertex cover Smin of G
    def mvc_recur(subgraph: set, upper_bound: int, cover: set) -> set:
        """
        | Branch and Bound recursive approach to find the
        | optimal solution of the vertex cover problem.
        | Essentially the knapsack problem
        |
        | Args:
        | subgraph -- a set of vertices which define the
        | vertices in the subgraph this branch iterates on
        | upper_bound -- the upper bound of the number of
        | vertices which can be in the cover set
        | cover -- the set of vertices which define the
        | current vertex cover
        |
        | Returns:
        | the minimum vertex cover for the passed subgraph
        """
        # base cases
        # if |C| + max (DegLB(G), ClqLB(G), SatLB(G)) >= UB
        # if len(cover) >= upper_bound:
        #    return cover  # return upper bound
        if len(subgraph) == 0:
            return cover
        # Select a vertex v from V with the maximum degree
        max_v = list(subgraph)
        max_v.sort(key=lambda v: len(adj_list[v]), reverse=True)
        max_v = max_v[0]
        #   [recursive step]
        # |C1| <-- EMVC(G \ N*(v), UB, C union N(V));
        # the exclusive and inclusive neighborhoods of max_v for the subgraph
        excl_neighbors = {u for u in adj_list[max_v] if u in subgraph}
        incl_neighbors = excl_neighbors.union({max_v})
        # recur without including this vertex, so add all its neighbors to
        # the cover in order to cover its edges and remove the inclusive
        # neighborhood from the subgraph
        cover_without = mvc_recur(subgraph.difference(incl_neighbors),
                                  upper_bound, cover.union(excl_neighbors))
        # |C2| <-- EMVC(G \ v, min(UB, |C1|), C union v);
        # recur including this vertex, so do not include its neighbors
        # in the cover as its edges are covered and remove v from the subgraph
        cover_with = mvc_recur(subgraph.difference({max_v}),
                               min(upper_bound, len(cover_without)),
                               cover.union({max_v}))
        # return the smallest cover for this subgraph
        smallest_cover = cover_without
        if len(cover_without) > len(cover_with):
            smallest_cover = cover_with
        return smallest_cover

    if len(adj_list) == 0:
        return set()
    else:
        return mvc_recur(set(adj_list.keys()), len(adj_list.keys()), set())


# All modules for CS 412 must include a main method that allows it
# to be imported and invoked from other python scripts
def main():
    # build the graph using an adjacency list
    edge_count = int(input())
    graph = nx.Graph()
    adj_list = {}
    for _ in range(edge_count):
        edge = input().split()
        u = edge[0]
        v = edge[1]
        if u not in adj_list:
            adj_list[u] = set()
            graph.add_node(u)
        if v not in adj_list:
            adj_list[v] = set()
            graph.add_node(v)
        adj_list[u].add(v)
        adj_list[v].add(u)
        graph.add_edge(u, v)
    test_name = input()  # used for outputting graph images
    start_time = timer()
    cover = mvc(adj_list)
    end_time = timer()
    for vertex in sorted(cover):  # write out vertices as text
        print(vertex)
    print(f"Time taken: {end_time - start_time} seconds")  # write out runtime
    # all under this is code to save the necessary graphs
    # draw the initial graph
    plt.subplot(121)
    pos = nx.spring_layout(graph)
    nx.draw(graph, with_labels=True, pos=pos)
    plt.subplot(122)
    # draw covered nodes red and other nodes stay normal color
    nx.draw_networkx_nodes(graph, pos, nodelist=list(cover),
                           node_color="tab:red")
    uncovered = [u for u in adj_list.keys() if u not in cover]
    nx.draw_networkx_nodes(graph, pos, nodelist=uncovered)
    # draw the covered edges (should be all edges, but make sure)
    covered_edges = set()
    uncovered_edges = set()
    for u in adj_list:
        if u in cover:
            for v in adj_list[u]:
                covered_edges.add((u, v))  # should be all edges
        else:
            for v in adj_list[u]:
                if v not in cover:
                    uncovered_edges.add((u, v))  # should be empty
    # draw covered edges with red highlight, uncovered stay normal
    nx.draw_networkx_edges(graph, pos, edgelist=covered_edges,
                           edge_color="tab:red", width=8, alpha=0.5)
    nx.draw_networkx_edges(graph, pos, edgelist=uncovered_edges)
    # draw labels as the graph should
    nx.draw_networkx_labels(graph, pos)
    plt.savefig(f"./test_cases/outputs/{test_name}_graphs.png")  # save graphs


if __name__ == "__main__":
    main()
