from typing import Hashable, List
from collections import deque

import networkx as nx


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    path_nodes = []
    wait_deque = []
    visited_nodes = {node: False for node in g.nodes}
    wait_deque.append(start_node)
    visited_nodes[start_node] = True

    while wait_deque:
        current_node = wait_deque.pop()
        path_nodes.append(current_node)
        neighbors = g[current_node]

        for i in neighbors:
            if not visited_nodes[i]:
                wait_deque.append(i)
                visited_nodes[i] = True


    return path_nodes
    # while wait_deque:
    #     current_node = wait_deque.popleft()
    #
    #     neighbors = g[current_node]
    #     path_nodes.append(current_node)
    #     for i in neighbors:
    #         if not visited_nodes[i]:
    #             wait_deque.append(i)
    #             visited_nodes[i] = True
    #
    #
    # print(g, start_node)
    # return path_nodes



#
# if __name__ == '__main__':
#     graph = nx.Graph()
#     graph.add_nodes_from("ABCDEFGHIJ")
#     graph.add_edges_from([
#         ('A', 'B'),
#         ('A', 'F'),
#         ('B', 'G'),
#         ('F', 'G'),
#         ('G', 'C'),
#         ('G', 'H'),
#         ('G', 'I'),
#         ('C', 'H'),
#         ('I', 'H'),
#         ('H', 'D'),
#         ('H', 'E'),
#         ('H', 'J'),
#         ('E', 'D'),
#     ])
#
#     print(graph["A"])
#
#     visited_nodes2 = {node: False for node in graph.nodes}
#     print(visited_nodes2)
#     wd = []
#     wd.append(graph["A"])
#     print(wd)
#     for i in graph["A"]:
#         print(i)