"""
    name:  Matthew Potter
"""


# Approximation Algorithm:
# https://tandy.cs.illinois.edu/dartmouth-cs-approx.pdf
# https://www.ijser.org/researchpaper/Optimal-Algorithm-for-Solving-Vertex-Cover-Problem-in-Polynomial-Time.pdf
# https://cpsc.yale.edu/sites/default/files/files/tr404.pdf this one is bad tbh
def approx_mvc(adj_list: dict[str, set]) -> set:
    pass


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
