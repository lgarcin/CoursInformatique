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

# Parcours d'un graphe et applications

```{code-cell}
:tags: ["remove-input"]
import warnings
warnings.filterwarnings("ignore")
import networkx as nx
```

```{code-cell}
:tags: ["remove-input"]
:load: ../../_scripts/graphe.py
```

## Piles et files

On décrit d'abord deux structures de données que sont les **piles** et les **files** dans lesquelles on peut insérer et retirer des éléments un par un.

### Piles

Une pile est une structure de donnée dont les éléments sont insérés et retirés par le même "côté" comme le montre le schéma suivant.

```{tikz}
\usetikzlibrary{matrix,positioning}
\begin{tikzpicture}[draw, minimum width=1cm, minimum height=1cm]
    \matrix (queue)[matrix of nodes, nodes={draw, nodes={draw}}, nodes in empty cells]
    {
       & & & & \\
    };
    \node[draw,above right=0.5cm and 2cm of queue] (in) {};
    \node[draw,below right=0.5cm and 2cm of queue] (out) {};

    \draw[-latex] (in.west) .. controls ++(180:1) and ++(0:1) .. ([yshift=0.25cm]queue.east);
    \draw[-latex] ([yshift=-0.25cm]queue.east) .. controls ++(0:1) and ++(180:1) .. (out.west);
\end{tikzpicture}
```

Autrement dit, le dernier élément inséré sera le premier à être retiré (dernier arrivé, premier sorti).

Quand on insère un élément dans la pile, on dit qu'on **empile** cet élément ; quand on retire un élément, on dit qu'on le **dépile**.

On peut simuler le comportement d'une pile à l'aide de listes Python.

On empile un élément à l'aide de la méthode `append`.

```{code-cell}
L = []
L.append('abc')
L.append(42)
L.append('def')
L
```

On dépile un élément à l'aide de la méthode `pop`.

```{code-cell}
L.pop()
```

```{code-cell}
L
```

### Files

Une file est une structure de donnée dont les éléments sont insérés par un "côté" et retirés par l'autre "côté" comme le montre le schéma suivant.

```{tikz}
\usetikzlibrary{matrix,positioning}
\begin{tikzpicture}[draw, minimum width=1cm, minimum height=1cm]
    \matrix (queue)[matrix of nodes, nodes={draw, nodes={draw}}, nodes in empty cells]
    {
       & & & & \\
    };
    \node[draw,above right=.5cm and 2cm of queue] (in) {};
    \node[draw,below left=.5cm and 2cm of queue] (out) {};

    \draw[-latex] (in.west) .. controls ++(180:1) and ++(0:1) .. ([yshift=0.25cm]queue.east);
    \draw[-latex] ([yshift=-0.25cm]queue.west) .. controls ++(180:1) and ++(0:1) .. (out.east);
\end{tikzpicture}
```

Autrement dit, le premier élément inséré sera le premier à être retiré (premier arrivé, premier sorti).

Quand on insère un élément dans la file, on dit qu'on **enfile** cet élément ; quand on retire un élément, on dit qu'on le **défile**.

On peut à nouveau simuler le comportement d'une file à l'aide de listes Python.

On enfile un élément à l'aide de la méthode `append`.

```{code-cell}
L = []
L.append('abc')
L.append(42)
L.append('def')
L
```

On défile un élément à l'aide de la méthode `pop(0)`.

```{code-cell}
L.pop(0)
```

```{code-cell}
L
```

### Problèmes d'efficacité

L'implémentation des listes Python (nous ne rentrerons pas dans les détails) fait que l'appel à la méthode `pop()` se fait en temps **constant** tandis que l'appel à la méthode `pop(0)` se fait en temps **linéaire**.[^lineaire]

[^lineaire]: De manière schématique, une fois que le premier élément de la liste a été supprimé lors de l'appel de `pop(0)`, tous les autres éléments doivent êtres décalés pour combler l'emplacement laissé libre.

Néanmoins, le module `collections` du langage Python dipose d'une classe `deque` (**D**oubled **E**nded **Que**ue) implémentant de manière efficace les piles et les files à la fois.

Un objet de classe `deque` peut représenter une **pile** à l'aide des méthodes `append` et `pop`.

```{code-cell}
from collections import deque

d = deque()
d.append('abc')
d.append(42)
d.append('def')
d
```

```{code-cell}
d.pop()
```

```{code-cell}
d
```

On peut également représenter une **file** à l'aide des méthodes `append` et `popleft()`.

```{code-cell}
from collections import deque

d = deque()
d.append('abc')
d.append(42)
d.append('def')
d
```

```{code-cell}
d.popleft()
```

```{code-cell}
d
```

## Parcours d'un graphe

On élabore des algorithmes permettant de parcourir un graphe, c'est-à-dire de visiter une et une seule fois chacun de ses sommets. Dans ce qui suit, un graphe sera représenté par un dictionnaire de listes d'adjacence. Ceci permet d'avoir rapidement accès aux **voisins** d'un sommet.

Pour simplifier, on supposera par la suite que les graphes considérés sont **connexes**.

### Parcours en profondeur

```{code-cell}
import collections

def parcours_profondeur(G, sommet_initial):
    visites = {sommet : False for sommet in G.keys()}   # Aucun des sommets n'a été visité
    pile = collections.deque()
    pile.append(sommet_initial)                         # Empiler le sommet initial
    while pile:                                         # Tant que la pile n'est pas vide
        sommet = pile.pop()                             # Dépiler un sommet
        if not visites[sommet]:                         # Si le sommet n'est pas visité
            visites[sommet] = True                      # Marquer le sommet comme visité
            print("Sommet "+str(sommet)+" visité")
        for voisin in G[sommet]:                        # Empiler les voisins du sommet
            if not visites[voisin]:                     # s'ils n'ont pas été visités
                pile.append(voisin)
```

```{code-cell}
G = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 3, 5], 4: [1, 2], 5: [3]}
```

```{code-cell}
:tags: ["remove-input"]
Graphe(G).get_parcours_profondeur_animation(1)
```

```{code-cell}
parcours_profondeur(G, 1)
```

```{code-cell}
G = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [], 5: [], 6: [], 7:[]}
```

```{code-cell}
:tags: ["remove-input"]
Graphe(G).get_parcours_profondeur_animation(1)
```

```{code-cell}
parcours_profondeur(G, 1)
```

### Parcours en largeur

```{code-cell}
import collections

def parcours_largeur(G, sommet_initial):
    visites = {sommet : False for sommet in G.keys()}   # Aucun des sommets n'a été visité
    file = collections.deque()
    file.append(sommet_initial)                         # Enfiler le sommet initial
    while file:                                         # Tant que la file n'est pas vide
        sommet = file.popleft()                         # Défiler un sommet
        if not visites[sommet]:                         # Si le sommet n'est pas visité
            visites[sommet] = True                      # Marquer le sommet comme visité
            print("Sommet "+str(sommet)+" visité")
        for voisin in G[sommet]:                        # Enfiler les voisins du sommet
            if not visites[voisin]:                     # s'ils n'ont pas été visités
                file.append(voisin)
```

```{code-cell}
G = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 3, 5], 4: [1, 2], 5: [3]}
```

```{code-cell}
:tags: ["remove-input"]
Graphe(G).get_parcours_largeur_animation(1)
```

```{code-cell}
parcours_largeur(G, 1)
```

```{code-cell}
G = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [], 5: [], 6: [], 7:[]}
```

```{code-cell}
:tags: ["remove-input"]
Graphe(G).get_parcours_largeur_animation(1)
```

```{code-cell}
parcours_largeur(G, 1)
```

## Applications

### Détection de cycles

```{code-cell}
import collections

def contient_cycle_profondeur(G, sommet_initial):
    visites = {sommet : False for sommet in G.keys()}
    pile = collections.deque()
    pile.append((sommet_initial, None))
    while pile:
        sommet, parent = pile.pop()
        if not visites[sommet]:
            visites[sommet] = True
        for voisin in G[sommet]:
            if not visites[voisin]:
                pile.append((voisin, sommet))
            elif parent != voisin:
                return True
    return False
```

```{code-cell}
import collections

def contient_cycle_largeur(G, sommet_initial):
    visites = {sommet : False for sommet in G.keys()}
    file = collections.deque()
    file.append((sommet_initial, None))
    while file:
        sommet, parent = file.popleft()
        if not visites[sommet]:
            visites[sommet] = True
        for voisin in G[sommet]:
            if not visites[voisin]:
                file.append((voisin, sommet))
            elif parent != voisin:
                return True
    return False
```

```{code-cell}
G = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 3, 5], 4: [1, 2], 5: [3]}
#G = {1: [2], 2: [1]}
```

```{code-cell}
:tags: ["remove-input"]
nx.draw_spring(nx.Graph(G), with_labels=True, font_weight="bold", font_size=20, node_size=600)
```

```{code-cell}
contient_cycle_profondeur(G, 1), contient_cycle_largeur(G, 1)
```

```{code-cell}
G = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [], 5: [], 6: [], 7:[]}
```

```{code-cell}
:tags: ["remove-input"]
nx.draw_spring(nx.Graph(G), with_labels=True, font_weight="bold", font_size=20, node_size=600)
```

```{code-cell}
contient_cycle_profondeur(G, 1), contient_cycle_largeur(G, 1)
```

### Connexité

```{code-cell}
import collections

def connexite_profondeur(G, sommet_initial):
    visites = {sommet : False for sommet in G.keys()}
    pile = collections.deque()
    pile.append(sommet_initial)
    while pile:
        sommet = pile.pop()
        if not visites[sommet]:
            visites[sommet] = True
        for voisin in G[sommet]:
            if not visites[voisin]:
                pile.append(voisin)
    return False not in visites.values()
```

```{code-cell}
import collections

def connexite_largeur(G, sommet_initial):
    visites = {sommet : False for sommet in G.keys()}
    file = collections.deque()
    file.append(sommet_initial)
    while file:
        sommet = file.popleft()
        if not visites[sommet]:
            visites[sommet] = True
        for voisin in G[sommet]:
            if not visites[voisin]:
                file.append(voisin)
    return False not in visites.values()
```

```{code-cell}
G = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 3, 5], 4: [1, 2], 5: [3]}
```

```{code-cell}
:tags: ["remove-input"]
nx.draw_spring(nx.Graph(G), with_labels=True, font_weight="bold", font_size=20, node_size=600)
```

```{code-cell}
connexite_profondeur(G, 1), connexite_largeur(G, 1)
```

```{code-cell}
G = {1: [2, 3, 4], 2: [1, 3, 4], 3: [1, 2, 3], 4: [1, 2], 5: [6, 7], 6 :[5], 7: [5]}
```

```{code-cell}
:tags: ["remove-input"]
nx.draw_spring(nx.Graph(G), with_labels=True, font_weight="bold", font_size=20, node_size=600)
```

```{code-cell}
connexite_profondeur(G, 1), connexite_largeur(G, 1)
```

<!-- Faire la même chose pour les graphes orientés -->

<!-- Peut-être renvoyer la liste des visités pour parcours -->