---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Etude des jeux

```{prf:definition} Graphe *biparti*
:label: def_graphe_biparti
Un graphe est dit **biparti** s'il est possible de partitionner ses sommets en deux sous-ensembles disjoints $A$ et $B$ tels que chaque arête du graphe relie un sommet de $A$ à un sommet de $B$.
```

```{mermaid}
graph TD;
    4 -->|Retire 1| 3;
    4 -->|Retire 2| 2;
    3 -->|Retire 1| 2;
    3 -->|Retire 2| 1;
    2 -->|Retire 1| 1;
    2 -->|Retire 2| 0;
    1 -->|Retire 1| 0;
```
