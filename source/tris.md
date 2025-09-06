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

# Tris

On décrit les algorithmes au programmme permettant de trier un tableau de valeurs numériques.

## Tri par insertion

Le principe est très simple : c'est l'algorithme qu'utilise naturellement l'être humain pour trier des objets comme par exemple des cartes à jouer.

On procède en plusieurs étapes. On suppose qu'à l'étape $i$, les éléments d'indice $0$ à $i-1$ du tableau sont déjà triés et on insère alors l'élément d'indice $i$ à sa place parmi les éléments précédents.

Un dessin vaut probablement mieux qu'un long discours.

```{code-cell}
:tags: ["remove-input"]
:load: ../_scripts/tri_insertion.py
```

```{code-cell}
:tags: ["remove-input"]
N = 10
tab = permutation(N)
TriInsertion(tab).get_animation()
```

On peut alors proposer la fonction Python suivante.

```{code-cell}
def tri_insertion(tab):
    for i in range(1,len(tab)):
        val = tab[i]
        pos = i
        while pos > 0 and tab[pos - 1] > val:
            tab[pos] = tab[pos-1]
            pos -= 1
        tab[pos] = val
```

On vérifie qu'elle fonctionne bien sur quelques tableaux choisis aléatoirement.

```{code-cell}
from numpy.random import randint
tab = randint(100, size=20)
tab
tri_insertion(tab)
tab
```

<!-- TODO preuve de l'algorithme + complexité -->

## Tri rapide

Le **tri rapide** est une application du principe _diviser pour régner_. Il consiste

- à choisir un élément du tableau à trier comme _pivot_ ;
- à séparer le tableau à trier en deux sous-tableaux contenant respectivement les éléments inférieurs et supérieurs au pivot ;
- et à répéter le processus sur les deux sous-tableaux.

```{code-cell}
:tags: ["remove-input"]
:load: ../_scripts/tri_rapide.py
```

```{code-cell}
:tags: ["remove-input"]
N = 20
tab = permutation(N)
TriRapide(tab).get_animation()
```

Comme tout algorithme du type _diviser pour régner_, le tri rapide se prête bien à une implémentation récursive.

```{code-cell}
from numpy.random import choice

def tri_rapide(tab):
    if len(tab) == 0:
        return []
    pivot = choice(tab)     # Choix aléatoire d'un élément comme pivot
    t1, t2, t3 = [], [], []
    for x in tab:
        if x < pivot:
            t1.append(x)
        elif x > pivot:
            t2.append(x)
        else:
            t3.append(x)
    return tri_rapide(t1) + t3 + tri_rapide(t2)
```

```{code-cell}
from numpy.random import randint

tab = randint(100, size=10)
tab
tri_rapide(tab)
```

On peut également proposer une implémentation tirant partie des spécificités de Python (listes en compréhension).

```{code-cell}
from numpy.random import choice

def tri_rapide(tab):
    if len(tab) == 0:
        return []
    pivot = choice(tab)
    return tri_rapide([x for x in tab if x < pivot]) +\
        [x for x in tab if x == pivot] +\
        tri_rapide([x for x in tab if x > pivot])
```

```{code-cell}
from numpy.random import randint
tab = randint(100, size=10)
tab
tri_rapide(tab)
```

L'algorithme précédent crée une nouvelle liste à chaque appel de la fonction `tri_rapide`. D'un point de vue de l'utilisation de la mémoire, on peut préférer effectuer un tri _en place_ : on modifie le tableau au cours de l'algorithme de tri.

```{code-cell}
def partition(tab, g, d, p):
    j = g
    tab[p], tab[d] = tab[d], tab[p]
    for i in range(g, d):
        if tab[i] <= tab[d]:
            tab[i], tab[j] = tab[j], tab[i]
            j += 1
    tab[d], tab[j] = tab[j], tab[d]
    return j


def tri_rapide(tab, g=0, d=None):
    if d == None:
        d = len(tab) - 1
    if g < d:
        p = randint(g, d + 1)
        pp = partition(tab, g, d, p)
        tri_rapide(tab, g, pp - 1)
        tri_rapide(tab, pp + 1, d)
```

```{code-cell}
tab = randint(100, size=10)
tab
tri_rapide(tab)
tab
```

## Tri par fusion

Le **tri par fusion** est également une application du principe _diviser pour régner_. Il consiste

- à séparer la liste à trier en deux-sous listes si elle contient plus d'un élément ;
- appliquer l'algorithme de tri aux deux sous-listes ;
- fusionner les deux sous-listes triées en une liste triée.

L'algorithme de tri par fusion est de nature récursive par définition.

```{code-cell}
def tri_fusion(tab):
    if len(tab) < 2:
        return tab
    else:
        m = len(tab)//2
        return fusion(tri_fusion(tab[:m]), tri_fusion(tab[m:]))
```

Le principe de fusion de deux listes triées en une liste triée est très simple :

- on compare les deux premiers éléments de chacune des listes ;
- on déplace le plus petit d'entre eux de la liste auquel il appartient vers la fin de la liste à renvoyer ;
- on répète le processus jusqu'à ce qu'une des deux listes soient vides ;
- on ajoute l'intégralité de l'autre liste à la fin de la liste à renvoyer.

```{code-cell}
:tags: ["remove-input"]
:load: ../_scripts/tri_fusion.py
```

```{code-cell}
:tags: ["remove-input"]
N = 16
tab = permutation(N)
TriFusion(tab).get_animation()
```

```{code-cell}
def fusion(t1, t2):
    t = []
    while t1 and t2:
        if t1[0] < t2[0]:
            t.append(t1.pop(0))
        else:
            t.append(t2.pop(0))
    if t1:
        t.extend(t1)
    else:
        t.extend(t2)
    return t
```

```{code-cell}
from numpy.random import randint
tab = list(randint(100, size=20))
tab
tri_fusion(tab)
```

On peut également donner une implémentation récursive de l'algorithme de fusion.

```{code-cell}
def fusion(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    if t1[0] < t2[0]:
        return [t1[0]] + fusion(t1[1:], t2)
    else:
        return [t2[0]] + fusion(t1, t2[1:])
```

```{code-cell}
from numpy.random import randint
tab = list(randint(100, size=10))
tab
tri_fusion(tab)
```
