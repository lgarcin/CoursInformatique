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

# Graphe non orienté

```{code-cell}
:tags: ["remove-input"]
import networkx as nx
from IPython.display import Latex
edges = [(1,2), (3,1), (2,3), (1,4), (2,4), (3,3), (5,3)]
```

```{prf:definition} Graphe
:label: def_graphe
Un **graphe** est la donnée de **sommets** (ou **noeuds**) et d\\'**arêtes** reliant ces sommets.
```

On peut représenter visuellement un graphe de la manière suivante :

```{code-cell}
:tags: ["remove-input"]
G = nx.Graph()
G.add_edges_from(edges)
nx.draw_circular(G, with_labels=True, font_weight="bold", font_size=20, node_size=600)
```

La liste des sommets de ce graphe est :

```{code-cell}
:tags: ["remove-input"]
Latex(r",\;".join([str(n) for n in G.nodes]))
```

et la liste des arêtes est :

```{code-cell}
:tags: ["remove-input"]
Latex(r",\;".join([str(e[0])+"-"+str(e[1]) for e in G.edges]))
```

```{prf:definition} Boucle
:label: def_boucle
C'est une arête reliant un sommet à lui-même.
```

Dans l'exemple précédent $3-3$ est une boucle.

```{prf:definition} Définition formelle d'un graphe non orienté
:label: def_graphe_formel
On appelle graphe tout couple $G=(S,A)$ où $S$ est un ensemble et

$$
A\subset\left\{\{x,y\},\;(x,y)\in S^2\right\}
$$

$S$ désigne l'ensemble des sommets tandis que $A$ désigne l'ensemble des arêtes.
```

```{note}
On s'autorise des "paires" de la forme $\{x,x\}$ pour représenter les boucles. Plus précisément, $\{x,x\}$ désigne la boucle reliant $x$ à lui-même.
```

Dans l'exemple précédent, on a donc :

```{code-cell}
:tags: ["remove-input"]
Latex(r"S=\left\{"+r",\;".join([str(n) for n in G.nodes])+r"\right\}")
```

```{code-cell}
:tags: ["remove-input"]
Latex(r"A=\left\{"+r",\;".join([r"\{"+str(e[0])+","+str(e[1])+r"\}" for e in G.edges])+r"\right\}")
```

```{exercise}
:label: complet
Un graphe est dit **complet** si deux sommets quelconques distincts sont reliés par une arête et qu'il ne comporte pas de boucle. Combien existe-t-il de graphes complets à $n$ sommets ?
```

```{prf:definition} Degré d'un sommet
:label: def_degre
Le degré d'un sommet $s$ est le nombre $d(s)$ d'arêtes dont une extrémité est $s$.
```

```{note}
Les boucles d'un graphe non orienté sont comptées deux fois dans le calcul du degré.
```

Dans l'exemple précédent, les degrés des différents sommets sont les suivants :

```{code-cell}
:tags: ["remove-input"]
Latex(r",\;".join(["d("+str(s)+")="+str(d) for (s,d) in G.degree()]))
```

```{prf:definition} Chemin
:label: def_chemin
On appelle **chemin** d'un sommet $s_1$ à un sommet $s_2$ une suite finie d'arêtes consécutives reliant les sommets $s_1$ et $s_2$.
```

```{note}
Un chemin peut être de longueur nulle.
```

Dans l'exemple précédent, $1-2-4$ et $5-3-2-1$ sont deux chemins.

```{exercise}
:label: rel-equiv
Montrer que la relation binaire : "il existe un chemin reliant le sommet $s_1$ au sommet $s_2$" est une relation d'équivalence sur l'ensemble des sommets d'un graphe.
```

```{prf:definition} Cycle
:label: def_cycle
Un **cycle** est un chemin dont le sommet initial et le sommet terminal sont identiques.
```

Dans l'exemple précédent, $1-2-4-1$ est un cycle.

```{prf:definition} Connexité
:label: def_connexite
Un graphe est dit **connexe** si pour tout couple $(s_1,s_2)$ de sommets, il existe un chemin menant de $s_1$ à $s_2$.
```

```{note}
Un graphe $G$ est connexe si la relation d'équivalence définie dans {ref}`rel-equiv` admet une seule classe d'équivalence. Sinon chaque classe d'équivalence forme un sous-graphe connexe de $G$.
```

```{exercise}
:label: exo_connexe
1. Quel est le nombre minimal d'arêtes d'un graphe connexe à $n$ sommets ?
2. Montrer qu'un graphe sans boucle à $n$ sommets et strictement plus de $\frac{(n-1)(n-2)}{2}$ arêtes est nécessairement connexe.
```
