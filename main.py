import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx
import heapq

# definice grafu - uzel: [(sousedni_uzel, vaha)]
graph = {
    'A': [('B', 10), ('D', 3)],
    'B': [('C', 2)],
    'C': [('F', 4)],
    'D': [('E', 3)],
    'E': [('C', 8), ('F', 4)],
    'F': [('E', 1)]
}

# implementace dijkstry
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}  # vzdalenost = nekonecno
    distances[start] = 0  # vzdalenost startovniho uzlu = 0
    predecessors = {node: None for node in graph}  # predchudci pro rekonstrukci cesty
    queue = [(0, start)]  # prioritni fronta

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # preskocime, pokud jsme nasli lepsi cestu uz drive
        if current_distance > distances[current_node]:
            continue

        # projdeme vsechny sousedy aktualniho uzlu
        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            # pokud najdeme kratsi cestu, aktualizujeme
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, predecessors

# rekonstrukce cesty z predchudcu
def reconstruct_path(predecessors, target):
    path = []
    while target is not None:
        path.insert(0, target)  # pridavame na zacatek, abychom meli cestu od startu k cili
        target = predecessors[target]
    return path

# vykresleni grafu s vyznacenim nejkratsi cesty (pokud je zadan)
def draw_graph(graph, shortest_path=None):
    G = nx.DiGraph()

    # graficke vytvoreni grafu - networkx
    for node in graph:
        for neighbor, weight in graph[node]:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)  # pozice uzlu
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # vykresleni vah hran

    # vykresleni nejkratsi cesty cervenou barvou
    if shortest_path and len(shortest_path) > 1:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title("Graf s nejkratší cestou")
    plt.axis('off')
    plt.show()

# funkce volana po stisknuti tlacitka - spocita a vykresli cestu
def calculate_and_draw():
    start_node = start_combobox.get()
    target_node = target_combobox.get()
    if not start_node or not target_node:
        return

    distances, predecessors = dijkstra(graph, start_node)
    path = reconstruct_path(predecessors, target_node)
    print(f"Vzdalenosti: {distances}")
    print(f"Nejkratsi cesta k {target_node}: {path}")
    draw_graph(graph, shortest_path=path)

# vytvoreni gui
root = tk.Tk()
root.title("Výběr vrcholů")

nodes = list(graph.keys())

# startovni uzel
tk.Label(root, text="Startovní vrchol:").grid(row=0, column=0, padx=10, pady=5)
start_combobox = ttk.Combobox(root, values=nodes, state="readonly")
start_combobox.grid(row=0, column=1, padx=10, pady=5)
start_combobox.set(nodes[0])

# cilovy uzel
tk.Label(root, text="Cílový vrchol:").grid(row=1, column=0, padx=10, pady=5)
target_combobox = ttk.Combobox(root, values=nodes, state="readonly")
target_combobox.grid(row=1, column=1, padx=10, pady=5)
target_combobox.set(nodes[-1])

# tlacitko pro vypocet
submit_btn = tk.Button(root, text="Spočítat nejkratší cestu", command=calculate_and_draw)
submit_btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()