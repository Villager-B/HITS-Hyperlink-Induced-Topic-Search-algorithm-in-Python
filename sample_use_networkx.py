import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

G = nx.DiGraph()

G.add_edges_from([('A', 'D'), ('B', 'C'), ('B', 'E'), ('C', 'A'),
                  ('D', 'C'), ('E', 'D'), ('E', 'B'), ('E', 'F'),
                  ('E', 'C'), ('C', 'H'), ('G', 'A'),
                  ('G', 'C'), ('H', 'A'), ('F', 'B')])

plt.figure(figsize=(5, 5))
nx.draw_networkx(G, with_labels=True)
plt.savefig("img/sample_digraph.png")

hubs, authorities = nx.hits(G, max_iter=60, normalized=True)

pprint("Authority Scores")
pprint(authorities)

pprint("Hub Scores")
pprint(hubs)
