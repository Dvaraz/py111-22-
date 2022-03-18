from typing import Hashable, List
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    for edge in graph.edges:
        nx.draw_networkx_edges(
            graph, pos,
            edgelist=[(edge[0], edge[1])], connectionstyle="arc3,rad=0.2"
        )

    plt.show()


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    path_nodes = []
    visited_nodes = {node: False for node in g.nodes}

    def requrs(point):
        current_node = point
        visited_nodes[current_node] = True
        path_nodes.append(current_node)
        neighbors = g[current_node]
        for i in neighbors:
            if not visited_nodes[i]:
                requrs(i)

    requrs(start_node)

    return path_nodes


# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an breadth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node for search
#     :return: list of nodes in the visited order
#     """
#     draw_graph(g)
#     path_nodes = []
#     wait_deque = []
#     visited_nodes = {node: False for node in g.nodes}
#     wait_deque.append(start_node)
#     visited_nodes[start_node] = True
#
#     while wait_deque:
#         current_node = wait_deque.pop()
#         path_nodes.append(current_node)
#         neighbors = g[current_node]
#
#         for i in neighbors:
#             if not visited_nodes[i]:
#                 wait_deque.append(i)
#                 visited_nodes[i] = True
#
#
#     return path_nodes
