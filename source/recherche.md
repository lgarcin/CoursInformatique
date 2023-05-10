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

# Algorithmes de recherche

En informatique, un tableau est une structure de données représentant une séquence finie d'éléments auxquels on peut accéder par leur position dans la séquence. On utilisera des listes Python pour représenter ces tableaux. On peut également remarquer qu'une chaîne de caractères est un tableau de caractères.

On s'intéresse dans ce paragraphe à divers algorithmes permettant de traiter des tableaux ou de retrouver de l'information dans ceux-ci.

## Recherche d'un élément

On cherche à savoir si une valeur donnée fait bien partie des éléments d'un tableau. On parcourt tout simplement ce tableau et on renvoie `True` dès qu'on trouve cette valeur dans le tableau. Si la valeur n'a pas été trouvée à la fin du parcours, on renvoie `False`.

```{code-cell}
def appartient(valeur, tableau):
    for element in tableau:
        if element == valeur:
            return True
    return False
```

```{code-cell}
appartient('Alice', ['Alice', 'Bob', 'Charles-Antoine'])
```

```{code-cell}
appartient('Dédé', ['Alice', 'Bob', 'Charles-Antoine'])
```

```{note}
Le langage Python dispose de l'opérateur `in` pour déterminer si une valeur appartient à une liste.
```

```{code-cell}
'Alice' in ['Alice', 'Bob', 'Charles-Antoine']
```

```{code-cell}
'Dédé' in ['Alice', 'Bob', 'Charles-Antoine']
```

On peut modifier l'algorithme precédent afin qu'il renvoie l'indice du tableau où on a trouvé la valeur recherché et `None` si la valeur n'a pas été trouvée.

```{code-cell}
def indice(valeur, tableau):
    for i in range(len(tableau)):
        if tableau[i] == valeur:
            return i
    return None
```

```{code-cell}
indice(2, [5, 4, 1, 2, 3])
```

```{code-cell}
print(indice(6, [5, 4, 1, 2, 3]))
```

```{note}
La méthode `index` de la classe `list` permet de déterminer l'indice d'une valeur dans une liste.
```

```{code-cell}
[5, 4, 1, 2, 3].index(2)
```

```{code-cell}
:tags: ["raises-exception"]
[5, 4, 1, 2, 3].index(6)
```

## Recherche du maximum

```{code-cell}
def maximum(tableau):
    m = None
    for element in tableau:
        if m == None or m < element:
            m = element
    return m
```

```{code-cell}
maximum([4, 5, 8, 1, 3])
```

```{code-cell}
print(maximum([]))
```

```{code-cell}
def argmax(tableau):
    index = None
    for i in range(len(tableau)):
        if index == None or tableau[index] < tableau[i]:
            index = i
    return index
```

```{code-cell}
argmax([4, 5, 8, 1, 3])
```

```{code-cell}
print(argmax([]))
```

```{code-cell}
def second_maximum(tableau):
    m1 = None
    m2 = None
    for element in tableau:
        if m1 == None or m1 < element:
            m2 = m1
            m1 = element
        elif m2 == None or m2 < element:
            m2 = element
    return m2
```

```{code-cell}
second_maximum([4, 5, 8, 1, 3])
```

```{code-cell}
print(second_maximum([]))
```

```{code-cell}
print(second_maximum([2]))
```

## Comptage des éléments d'un tableau

```{code-cell}
def comptage(tableau):
    d = {}
    for element in tableau:
        if element in d:
            d[element] += 1
        else:
            d[element] = 1
    return d
```

```{code-cell}
comptage(['Alice', 'Bob', 'Alice', 'Charles', 'Charles', 'Alice'])
```

## Recherche d'un motif dans une chaîne

```{code-cell}
def recherche_motif(motif, chaine):
    n = len(chaine)
    m = len(motif)
    for ind in range(n-m+1):
        nb = 0
        while nb < m and chaine[ind+nb] == motif[nb]:
            nb +=1
        if nb == m:
            return True
    return False
```

```{code-cell}
:tags: ["remove-input"]
:load: ../_scripts/recherche_motif.py
```

```{code-cell}
recherche_motif("pipa", "pitapipapa")
```

```{code-cell}
:tags: ["remove-input"]
RechercheMotif("pipa", "patapipapa").get_animation()
```

```{code-cell}
recherche_motif("tapa", "patapipapa")
```

```{code-cell}
:tags: ["remove-input"]
RechercheMotif("tapa", "patapipapa").get_animation()
```

## Recherche des deux valeurs les plus proches d'un tableau

```{code-cell}
def plus_proches_valeurs(tableau):
    valeurs = None
    for i in range(len(tableau)):
        for j in range(i+1, len(tableau)):
            if valeurs == None or abs(tableau[i] - tableau[j]) < abs(valeurs[0] - valeurs[1]):
                valeurs = tableau[i], tableau[j]
    return valeurs
```

```{code-cell}
plus_proches_valeurs([7, 4, 9, 13])
```

```{code-cell}
print(plus_proches_valeurs([]))
```

```{code-cell}
print(plus_proches_valeurs([7]))
```

## Tri à bulles

Le **tri à bulles** fait partie des algorithmes de tri classiques. Trier un tableau consiste à ordonner ses éléments du plus petit au plus grand. On suppose donc que les éléments du tableau sont à valeurs dans un ensemble muni d'une relation d'ordre total.

Le tri à bulles consiste à déplacer les éléments du plus grand au plus petit vers la fin du tableau comme des bulles d'air dans un liquide. Plus précisément :

* on parcourt le tableau en comparant les couples d'éléments consécutifs ;
* si deux éléments consécutifs ne sont pas dans le bon ordre, on les échange ;
* à la fin de ce premiers parcours du tableau, on peut garantir que le plus grand élément du tableau est en dernière position ;
* on répète alors ce qui précède sur le tableau privé de son dernier élément et ainsi de suite jusqu'à tri complet du tableau.

```{code-cell}
:tags: ["remove-input"]
:load: ../_scripts/tri_bulles.py
```

```{code-cell}
:tags: ["remove-input"]
from numpy.random import permutation
TriBulles(permutation(10)).get_animation()
```

```{code-cell}
def tri_bulles(tableau):
    for i in reversed(range(len(tableau))):
        for j in range(i):
            if tableau[j+1] < tableau[j]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
```

```{code-cell}
t = [4, 2, 5, 3, 8, 7, 6, 1]
tri_bulles(t)
t
```

```{code-cell}
t = []
tri_bulles(t)
t
```

```{code-cell}
t = [4]
tri_bulles(t)
t
```
