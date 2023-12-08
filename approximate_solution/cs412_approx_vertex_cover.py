"""
    name:  Matthew Potter
"""


# Approximation Algorithm:
# https://tandy.cs.illinois.edu/dartmouth-cs-approx.pdf
# https://cpsc.yale.edu/sites/default/files/files/tr404.pdf this one is bad tbh
# *****************************************************************************
# Title: Optimal Algorithm for Solving Vertex Cover Problem in Polynomial Time
# Authors: Sharad Singh, Gaurav Singh, and Neeraj Kushwah
# Date: August 2018
# Version: International Journal of Scientific & Engineering Research
#          Volume 9, Issue 8
# Source: https://www.ijser.org/researchpaper/Optimal-Algorithm-for-Solving-Vertex-Cover-Problem-in-Polynomial-Time.pdf
# Formal citation:
#   Sharad Singh, Gaurav Singh, and Neeraj Kushwah, Optimal Algorithm for Solving
#   Vertex Cover Problem in Polynomial Time, International Journal of Scientific &
#   Engineering Research Volume 9, Issue 8, August 2018, ISSN 2229-5518.
# ****************************************************************************
def approx_mvc(adj_list: dict[str, set]) -> set:
    """
    | Vertex cover approximation based on the algorithm by
    | Sharad Singh, Gaurav Singh, and Neeraj Kushwah in their paper
    | "Optimal Algorithm for Solving Vertex Cover Problem in Polynomial Time",
    | which was published in International Journal of Scientific &
    | Engineering Research Volume 9, Issue 8, August-2018,
    | ISSN 2229-5518 (See above citation)
    | Uses a somewhat heuristic, somewhat greedy algorithm to
    | find the approximate minimum vertex cover of the passed
    | graph in O(n^2) time.
    |
    | Args:
    | adj_list -- the adjacency list defining the connected, unweighted graph
    |
    | Returns:
    | the minimum vertex cover for the passed graph
    """
    if len(adj_list) == 0:
        return set()
    # Step 1: Input all the vertices in the list V[N]
    #         Where N is Total number of vertices.
    # v_list is a list of vertices sorted by degree that has "unfit" vertices removed
    # until the minimum vertex cover is approximated well
    v_list = list(adj_list.keys())
    # Step 2: Sort the list V[N] according to degree of vertices.
    v_list.sort(key=lambda vertex: len(adj_list[vertex]))
    # Step 3: For each vertex u € V [N]
    # ind keep track of the offset from kept vertices
    # and list_size keeps track of the current list size
    # so that removals may be iterated properly (for loops don't like mutation)
    ind = 0
    list_size = len(v_list)
    while ind < list_size:
        u = v_list[ind]
        # a) Delete the vertex u from the list V [N] if all the adjacent
        #    vertices from the u exist in list V [N].
        delete = True
        for v in adj_list[u]:
            if v not in v_list:
                delete = False
                break
        # b) If vertex deleted then
        if delete:
            # N=N-1 (remove it from v_list)
            list_size = list_size - 1
            v_list.remove(u)
        else:
            ind = ind + 1
    # Step 4: Return V [N].
    return set(v_list)


# All modules for CS 412 must include a main method that allows it
# to be imported and invoked from other python scripts
def main():
    # build the graph using an adjacency list
    edge_count = int(input())
    adj_list = {}
    for _ in range(edge_count):
        edge = input().split()
        u = edge[0]
        v = edge[1]
        if u not in adj_list:
            adj_list[u] = set()
        if v not in adj_list:
            adj_list[v] = set()
        adj_list[u].add(v)
        adj_list[v].add(u)
    cover = approx_mvc(adj_list)
    print(cover)


if __name__ == "__main__":
    main()
