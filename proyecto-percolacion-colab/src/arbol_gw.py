import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def sample_pk():
    r = np.random.rand()
    k = 0
    while r > 1 / (2 ** (k + 1)):
        r -= 1 / (2 ** (k + 1))
        k += 1
    return k

def sample_rhok():
    while True:
        k = np.random.geometric(p=0.5)
        if k > 0 and np.random.rand() < (k / (2 ** (k + 1))) / (1 / (2 ** k)):
            return k

def generate_gw_tree_with_spine(max_depth=10):
    G = nx.DiGraph()
    root = 0
    G.add_node(root, depth=0)
    current_node = root
    node_counter = 1
    for depth in range(max_depth):
        spine_children = sample_rhok()
        spine_child_ids = list(range(node_counter, node_counter + spine_children))
        G.add_edges_from([(current_node, c) for c in spine_child_ids])
        G.nodes[current_node]['spine'] = True
        next_root = np.random.choice(spine_child_ids)
        for c in spine_child_ids:
            if c != next_root:
                n_children = sample_pk()
                for i in range(n_children):
                    child = node_counter + spine_children + i
                    G.add_edge(c, child)
                node_counter += n_children
        current_node = next_root
        node_counter += spine_children
    return G

def draw_tree(G):
    pos = nx.spring_layout(G, seed=42)
    colors = ['red' if G.nodes[n].get('spine', False) else 'skyblue' for n in G.nodes]
    nx.draw(G, pos, node_color=colors, with_labels=True, node_size=500, arrows=True)
    plt.title("Árbol de Galton-Watson condicionado (espina en rojo)")
    plt.show()

if __name__ == "__main__":
    tree = generate_gw_tree_with_spine(max_depth=6)
    draw_tree(tree)
