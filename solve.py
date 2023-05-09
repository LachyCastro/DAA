import networkx as nx
import matplotlib.pyplot as plt


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
    print('\n')


def painting_matrix(n, k):
    matrix = [[0 for _ in range(n+1)]for _ in range(n+1)]
    for tuple in k:
        for i in range(tuple[0], tuple[2] + 1):
            for j in range(tuple[1], tuple[3] + 1):
                matrix[i][j] = 1
    print_matrix(matrix=matrix)
    return matrix


def build_graph(matrix):
    set_A = set(['A'+str(i) for i in range(len(matrix))])
    set_B = set(['B'+str(j) for j in range(len(matrix[0]))])

    # crear el grafo y añadir los nodos
    G = nx.DiGraph()
    G.add_nodes_from(set_A)
    G.add_nodes_from(set_B)

    # añadir las aristas del grafo
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                G.add_edge('A'+str(i), 'B'+str(j))
    return G


def max_flow_min_cut(graph: nx.Graph):
    # calculate max flow in the graph

    # add source and fountain node
    graph.add_node('s')
    graph.add_node('t')
    # add edges from source to A nodes
    # add edges from B to fountain node
    for node in graph.nodes():
        if node[0] == 'A':
            graph.add_edge('s', node)
        elif node[0] == 'B':
            graph.add_edge(node, 't')
    # add weight to the edges
    for edge in graph.edges():
        graph[edge[0]][edge[1]]['capacity'] = 1
    # print de grafo
    # print(graph.edges(data=True))

    max_flow = nx.maximum_flow(graph, 's', 't')
    return max_flow


n = 200
k = [(84, 113, 191, 187), (52, 68, 74, 83), (63, 46, 158, 68),
     (38, 15, 170, 81), (38, 81, 164, 183), (109, 52, 141, 156),
     (117, 151, 126, 155), (21, 25, 128, 197), (111, 30, 163, 59),
     (138, 62, 154, 73), (83, 161, 143, 189), (26, 56, 77, 196),
     (19, 56, 66, 150)]
# n = 10
# k = [
#     (3, 2, 10, 5),
#     (8, 2, 10, 2),
#     (5, 4, 5, 6),
#     (5, 1, 8, 7),
#     (10, 4, 10, 10)
# ]

# n = 10
# k = [
#     (4, 8, 6, 9),
#     (2, 3, 4, 4),
#     (6, 5, 6, 6)]
# n = 1000000000
# k = [
#     (755312705, 208314772, 979816776, 413350061),
#     (504975947, 580545612, 742993862, 822481605),
#     (71081030, 302221415, 777045906, 760955957),
#     (59005620, 71441769, 579437611, 173761068),
#     (108290992, 135681316, 130173981, 423327924),
#     (730854196, 342245706, 987367869, 746156573),
#     (549592180, 299075961, 851728078, 759898613),
#     (767765094, 416880160, 988884730, 602444576),
#     (132601847, 887575854, 837539482, 977191979)]
matrix = painting_matrix(n, k)
bipartite_graph = build_graph(matrix=matrix)
max_f = max_flow_min_cut(bipartite_graph)
print(max_f[0])
