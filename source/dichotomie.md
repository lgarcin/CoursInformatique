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

# Dichotomie

<!-- TODO Expliquer le proncipe général de la dichotomie -->

<!-- TODO Remarques sur la complexité -->

## Recherche par dichotomie dans un tableau triée

Lorsque l'on dispose d'une tableau trié, on peut proposer un algorithme de recherche dans un tableau efficace en utilisant le principe de **dichotomie**.

- On recherche tout d'abord l'élément "central" de ce tableau.
- Si c'est l'élément recherché, on s'arrête. Sinon, on le compare à l'élément recherché.
- Si l'élément recherché est inférieur à l'élément central, on le recherche dans la première partie du tableau. Sinon, on le recherche dans la deuxième partie du tableau.
- On retourne donc à la première étape de notre algorithme appliqué à l'un des deux "demi-tableaux".

```{code-cell}
def appartient_dicho(elt, tab):
    g = 0
    d = len(tab) - 1
    while g <= d:
        m = (g + d) // 2
        if tab[m] == elt:
            return True
        if elt < tab[m]:
            d = m - 1
        else:
            g = m + 1
    return False
```

```{code-cell}
appartient_dicho(13, [1, 3, 5, 7, 8, 10, 13, 14, 17, 19])
```

```{code-cell}
appartient_dicho(18, [1, 3, 5, 7, 8, 10, 13, 14, 17, 19])
```

Comme souvent, un dessin vaut mieux qu'un long discours. On donne deux exemples d'application de cet algorithme.

```{code-cell}
:tags: ["remove-input"]
:load: ../_scripts/recherche_dicho.py
```

```{code-cell}
:tags: ["remove-input"]
from random import randint
tab = sorted([randint(1,100) for _ in range(20)])
elt = 0
while elt not in tab:
    elt = randint(1,100)
RechercheDicho(elt, tab).get_animation()
```

```{code-cell}
:tags: ["remove-input"]
from random import randint
tab = sorted([randint(1,100) for _ in range(20)])
elt = tab[0]
while elt in tab:
    elt = randint(1,100)
RechercheDicho(elt, tab).get_animation()
```

On peut proposer une version qui renvoie l'indice de la première occurence de l'élément recherché plutôt qu'un booléen.

```{code-cell}
def indice_dicho(elt, tab):
    g = 0
    d = len(tab) - 1
    while g <= d:
        m = (g + d) // 2
        if tab[m] == elt:
            return m
        if elt < tab[m]:
            d = m - 1
        else:
            g = m + 1
    return None
```

```{code-cell}
indice_dicho(13, [1, 3, 7, 8, 10, 13, 14, 17, 19])
```

```{code-cell}
print(indice_dicho(18, [1, 3, 7, 8, 10, 13, 14, 17, 19]))
```

## Exponentiation rapide

<!-- TODO Expliquer le principe -->

```{code-cell}
def exponentiation_rapide(x, n):
    a = 1
    while n > 0:
        if n % 2 == 1:
            a *= x
        x = x*x
        n //= 2
    return a
```

```{code-cell}
exponentiation_rapide(3, 4)
```
