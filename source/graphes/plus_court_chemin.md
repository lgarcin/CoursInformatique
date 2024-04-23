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
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from sympy import Matrix
import warnings
warnings.filterwarnings("ignore")
```

```{prf:definition} Graphe étiqueté
Un graphe (orienté ou non) est dit **étiqueté** si l'on a affecté un attribut (nombre, chaîne de caractère, ...) à chacune de ses arêtes ou chacun de ses arcs.

De manière plus formelle, un graphe étiqueté est un triplet $(S,A,f)$ où $(S,A)$ est un graphe et $f$ une application de $A$ dans un ensemble $E$.
```

Par exemple, un tel graphe pourrait servir à décrire le type de lien existant entre les différents membres d'un réseau social.

```{code-cell}
:tags: ["remove-input"]
edges = [
  ('Alice', 'Bertrand'),
  ('Bertrand', 'Claire'),
  ('Bertrand', 'Denis'),
  ('Claire', 'Estelle'),
  ('Alice', 'François'),
  ('Claire', 'François')
]
G = nx.Graph()
G.add_edges_from(edges)
pos = nx.planar_layout(G)
nx.draw(
    G, pos,
    node_size=2000,
    with_labels=True,
    font_size=10
)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels={
      ('Alice', 'Bertrand'): 'Famille',
      ('Bertrand', 'Claire'): 'Travail',
      ('Bertrand', 'Denis'): 'Amitié',
      ('Claire', 'Estelle'): 'Travail',
      ('Alice', 'François'): 'Amitié',
      ('Claire', 'François'): 'Famille'
    },
)
plt.show()
```

```{prf:definition} Graphe pondéré
Un graphe **pondéré** est un graphe étiqueté par des réels positifs. On parle alors du **poids** d'une arête.

De manière plus formelle, un graphe étiqueté est un triplet $(S,A,p)$ où $(S,A)$ est un graphe et $p$ une application de $A$ dans un ensemble $\dR_+$.

```

On peut par exemple utiliser un graphe pondéré pour modéliser des distances entre des sommets.

```{code-cell}
:tags: ["remove-input"]
G = nx.Graph()

G.add_edge("Paris", "Tokyo", weight=9718)
G.add_edge("Paris", "Moscou", weight=2483)
G.add_edge("Paris", "Londres", weight=344)
G.add_edge("Paris", "Rome", weight=1105)
G.add_edge("Tokyo", "Moscou", weight=7693)
G.add_edge("Tokyo", "Londres", weight=9589)
G.add_edge("Moscou", "Londres", weight=2500)
G.add_edge("Londres", "Rome", weight=1415)

pos = nx.circular_layout(G)
labels = nx.get_edge_attributes(G,'weight')
nx.draw(G, pos, with_labels=True, node_size=2000, font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
```

## Représentation d'un graphe pondéré

On peut représenter un graphe pondéré (ou, de manière plus générale, étiqueté) de diverses manières.

```{code-cell}
:tags: ["remove-input"]
weighted_edges = [('A', 'B', 10), ('C', 'A', 20), ('C', 'B', 5),
                  ('A', 'D', 15), ('B', 'D', 30), ('E', 'C', 20),
                  ('D', 'E', 10), ('F', 'C', 10), ('E', 'F', 5)]
G = nx.Graph()
G.add_weighted_edges_from(weighted_edges)
labels = nx.get_edge_attributes(G,'weight')
pos = nx.planar_layout(G)
nx.draw(G, pos=pos, with_labels=True, font_weight="bold", font_size=20, node_size=600)
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)
plt.show()
```

### Dictionnaire de liste de couples

On peut tout d'abord utiliser un dictionnaire faisant correspondre à chaque sommet la liste des couples formés des sommets voisins et des poids des arêtes correspondantes.

```{code-cell}
:tags: ["remove-input"]
graphe_liste_tuples = {s: [(k, G[s][k]['weight']) for k in v] for (s, v) in G.adjacency()}
graphe_liste_tuples
```

### Dictionnaire de dictionnaires

De manière similaire, on peut utiliser une dictionnaire faisant correspondre à chaque sommet un dictionnaire associant à chacun de ses voisins le poids de l'arête correspondante.

```{code-cell}
:tags: ["remove-input"]
graphe_dictionnaire = {s: {k: G[s][k]['weight'] for k in v} for (s, v) in G.adjacency()}
graphe_dictionnaire
```

### Matrice

Enfin, quitte à numéroter les sommets, on peut utiliser une matrice dont le coefficient $(i,j)$ est le poids de l'arête $\{i,j\}$ si elle existe et $\infty$ sinon.

```{code-cell}
:tags: ["remove-input", "remove-stdout"]
Matrix(nx.to_numpy_array(G, dtype=float, nonedge=np.inf))
```

## Algorithme de Dijsktra

```{code-cell}
:tags: ["remove-input"]
:load: ../../_scripts/dijkstra.py
```

L'objectif de l'algorithme de Dijkstra est de déterminer un **chemin de poids minimal** entre deux sommets d'un graphe pondéré, le poids d'un chemin étant égal à la somme des poids des arêtes qui le composent. Bien souvent, le poids d'une arête représente une distance entre deux sommets : on parle alors de **plus court chemin**.

Plus précisément, en fixant un sommet de départ $s_0$ d'un graphe pondéré $(S,A,p)$, l'algorithme de Dijkstra calcule les distances minimales $d[s]$ du sommet de départ $s_0$ à chacun des sommets $s$ du graphe.

```{prf:algorithm} Dijkstra
* Initialisation :
  * On initialise les distances : $d[s]=\infty$ pour tout $s\in S\setminus\{s_0\}$, $d[s_0]=0$
  * On initialise la liste des sommets à traiter : $L\gets S$
* Tant que $L\neq\emptyset$
  * Trouver le sommet $s_m$ de $L$ telle que $d[s_m]$ est minimale
  * Pour chaque voisin $v$ de $s_m$ dans $L$, $d[v]=\min(d[v],d[s_m]+p(s_m,v))$
  * Retirer $s_m$ de $L$
```

```{code-cell}
:tags: ["remove-input"]
Dijkstra(G).get_dijkstra_animation('A')
```

```{code-cell}
from math import inf

def dijkstra(dod, deb):
    dist = {s: inf for s in dod}
    dist[deb] = 0
    sommets_non_traites = {s for s in dod}
    while len(sommets_non_traites) != 0:
        min_dist = inf
        for s in sommets_non_traites:
            if dist[s] < min_dist:
                min_dist_sommet = s
                min_dist = dist[s]
        voisins = dod[min_dist_sommet]
        for s in voisins:
            if s in sommets_non_traites:
                dist[s] = min(dist[s], min_dist+voisins[s])
        sommets_non_traites.remove(min_dist_sommet)
    return dist
```

```{code-cell}
graphe_dictionnaire
```

```{code-cell}
dijkstra(graphe_dictionnaire, 'A')
```

L'algorithme précédent fournit seulement les distances minimales d'un sommet de départ aux autres sommets du graphe. En modifiant légèrement cet algorithme, on peut également récupérer les chemins correspondants en affectant à chaque sommet le sommet qui le précède dans le chemin minimal.

```{code-cell}
def dijkstra_predecesseurs(dod, deb):
    predecesseurs = {s: (inf, None) for s in dod}
    predecesseurs[deb] = (0, None)
    sommets_non_traites = {s for s in dod}
    while len(sommets_non_traites) != 0:
        min_dist = inf
        for s in sommets_non_traites:
            dist, _ = predecesseurs[s]
            if dist < min_dist:
                min_dist_sommet = s
                min_dist = dist
        voisins = dod[min_dist_sommet]
        for s in voisins:
            if s in sommets_non_traites:
                d = min_dist+voisins[s]
                dist, _ = predecesseurs[s]
                if d < dist:
                    predecesseurs[s] = (d, min_dist_sommet)
        sommets_non_traites.remove(min_dist_sommet)
    return predecesseurs
```

```{code-cell}
dijkstra_predecesseurs(graphe_dictionnaire, 'A')
```

Si on le souhaite, on peut également récupérer pour chaque sommet la totalité du chemin minimal plutôt que son prédécesseur dans le chemin minimal.

```{code-cell}
def dijkstra_chemins(dod, deb):
    chemins = {s: (inf, None) for s in dod}
    chemins[deb] = (0, [])
    sommets_non_traites = {s for s in dod}
    while len(sommets_non_traites) != 0:
        min_dist = inf
        for s in sommets_non_traites:
            dist, _ = chemins[s]
            if dist < min_dist:
                min_dist_sommet = s
                min_dist = dist
        voisins = dod[min_dist_sommet]
        for s in voisins:
            if s in sommets_non_traites:
                d = min_dist+voisins[s]
                dist, _ = chemins[s]
                if d < dist:
                    _, chemin = chemins[min_dist_sommet]
                    chemins[s] = (d, chemin + [min_dist_sommet])
        sommets_non_traites.remove(min_dist_sommet)
    return chemins
```

```{code-cell}
dijkstra_chemins(graphe_dictionnaire, 'A')
```

Les algorithmes précédents fonctionnent toujours avec des graphes **orientés**.

```{code-cell}
:tags: ["remove-input"]
G = nx.DiGraph()
G.add_weighted_edges_from(weighted_edges)
```

```{code-cell}
:tags: ["remove-input"]
Dijkstra(G).get_dijkstra_animation('A')
```

```{code-cell}
:tags: ["remove-input"]
graphe_dictionnaire = {s: {k: G[s][k]['weight'] for k in v} for (s, v) in G.adjacency()}
```

```{code-cell}
graphe_dictionnaire
```

```{code-cell}
dijkstra_chemins(graphe_dictionnaire, 'A')
```

<!-- TODO Reprendre avec files de priorité -->

<!-- TODO Comparer avec l'algorithme A* -->