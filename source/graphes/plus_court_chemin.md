---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Recherche d'un plus court chemin

## Graphe pondéré

```{code-cell}
:tags: ["remove-input"]
import warnings
warnings.filterwarnings("ignore")
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from sympy import Matrix
weighted_edges=[('A','B',10.), ('C','A',20.), ('B','C',5.), ('A','D',15.), ('B','D',30.), ('C','C',10.), ('E','C',20.)]
```

```{code-cell}
:tags: ["remove-input"]
G = nx.Graph()
G.add_weighted_edges_from(weighted_edges)
labels = nx.get_edge_attributes(G,'weight')
pos = nx.circular_layout(G)
nx.draw(G, pos=pos, with_labels=True, font_weight="bold", font_size=20, node_size=600)
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)
plt.show()
```

```{code-cell}
:tags: ["remove-input"]
{s: [(k, G[s][k]['weight']) for k in v] for (s, v) in G.adjacency()}
```

```{code-cell}
:tags: ["remove-input"]
{s: {k: G[s][k]['weight'] for k in v} for (s, v) in G.adjacency()}
```

```{code-cell}
:tags: ["remove-input", "remove-stdout"]
Matrix(nx.to_numpy_array(G, dtype=float, nonedge=np.inf))
```
