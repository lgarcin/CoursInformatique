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

# Récursivité

<!-- TODO Expliquer le principe général -->

<!-- TODO Expliquer le principe de la pile de récursion -->

## Algorithmes dichotomiques

### Recherche dans un tableau trié

```{code-cell}
def recherche_dicho(tab, elt):
    if len(tab) == 0:
        return False
    m = len(tab)//2
    if elt < tab[m]:
        return recherche_dicho(tab[:m], elt)
    elif elt > tab[m]:
        return recherche_dicho(tab[m+1:], elt)
    else:
        return True
```

```{code-cell}
recherche_dicho([2, 3, 5, 9, 10, 11, 13], 11)
```

```{code-cell}
recherche_dicho([2, 3, 5, 9, 10, 11, 13], 4)
```

```{code-cell}
def indice_dicho(tab, elt):
    if len(tab) == 0:
        return None
    m = len(tab)//2
    if elt < tab[m]:
        return indice_dicho(tab[:m], elt)
    elif elt > tab[m]:
        ind = indice_dicho(tab[m+1:], elt)
        return None if ind == None else m+1+ind
    else:
        return m
```

```{code-cell}
indice_dicho([2, 3, 5, 9, 10, 11, 13], 11)
```

```{code-cell}
print(indice_dicho([2, 3, 5, 9, 10, 11, 13], 4))
```

### Exponentiation rapide

<!-- TODO Explication -->

```{code-cell}
def exponentiation_rapide(x, n):
    if n == 0:
        return 1
    elif n % 2 == 1:
        return x * exponentiation_rapide(x**2, n//2)
    else:
        return exponentiation_rapide(x**2, n//2)
```

```{code-cell}
exponentiation_rapide(2, 10)
```

## Permutations et sous-listes d'une liste

### Permutations d'une liste

```{code-cell}
def permutations(liste):
    if len(liste) == 0:
        return [[]]
    perms = []
    for i in range(len(liste)):
        perms.extend([[liste[i]]+p for p in permutations(liste[:i]+liste[i+1:])])
    return perms
```

```{code-cell}
:tags: ["output_scroll"]
permutations(['a', 'b', 'c', 'd'])
```

### Sous-listes d'une liste

<!-- TODO Définir sous-liste -->

```{code-cell}
def souslistes(liste):
    if len(liste) == 0:
        return [[]]
    sl = souslistes(liste[:-1])
    sl.extend([l+[liste[-1]] for l in sl])
    return sl
```

```{code-cell}
souslistes(['a', 'b', 'c', 'd'])
```

## PGCD

<!-- TODO Peut-être dans l'intro pour expliquer le principe général -->

```{code-cell}
def pgcd(a, b):
    if b == 0:
        return a
    return pgcd(b, a%b)
```

```{code-cell}
pgcd(10, 24), pgcd(70, 98)
```

## Fractales

### Arbres fractaux

```{code-cell}
from math import cos, sin, pi
import matplotlib.pyplot as plt

dangle = pi/12
echelle = .8


def get_fin(branche):
    origine, angle, longueur = branche
    return origine[0]+longueur*cos(angle), origine[1]+longueur*sin(angle)


def get_fils(branche):
    origine, angle, longueur = branche
    fin = get_fin(branche)
    return (fin, angle-dangle, longueur*echelle), (fin, angle+dangle, longueur*echelle)


def trace_branche(branche):
    origine, _, _ = branche
    fin = get_fin(branche)
    plt.plot([origine[0], fin[0]], [origine[1], fin[1]], color='g')


def trace_arbre(arbre, level):
    if level == 0:
        return
    trace_branche(arbre)
    arbre1, arbre2 = get_fils(arbre)
    trace_arbre(arbre1, level-1)
    trace_arbre(arbre2, level-1)
```

```{code-cell}
plt.axis('equal')
plt.axis('off')
a = ((0, 0), 0, 1)
trace_arbre(a, 1)
```

```{code-cell}
plt.axis('equal')
plt.axis('off')
a = ((0, 0), 0, 1)
trace_arbre(a, 3)
```

```{code-cell}
plt.axis('equal')
plt.axis('off')
a = ((0, 0), pi/2, 1)
trace_arbre(a, 8)
```

### Flocon de Koch

```{code-cell}
from math import pi
from cmath import exp
import matplotlib.pyplot as plt

def step(p1, p2):
    l = (p2-p1)/3
    pp1 = p1
    pp2 = pp1 + l
    pp3 = pp2 + l * exp(-1j*pi/3)
    pp4 = pp3 + l * exp(1j*pi/3)
    return [pp1, pp2, pp3, pp4]

def recur(pts,level):
    if level == 0:
        return pts
    pts += [pts[0]]
    pairs = zip(pts[:-1], pts[1:])
    return recur([pp for p in pairs for pp in step(p[0], p[1])], level-1)

def trace(pts):
    pp=pts+[pts[0]]
    plt.plot([p.real for p in pp],[p.imag for p in pp])

def koch(level):
    pts = [0, 1, exp(1j*pi/3)]
    pts = recur(pts, level)
    trace(pts)
```

```{code-cell}
plt.axis('equal')
plt.axis('off')
koch(0)
```

```{code-cell}
plt.axis('equal')
plt.axis('off')
koch(1)
```

```{code-cell}
plt.axis('equal')
plt.axis('off')
koch(2)
```

```{code-cell}
plt.axis('equal')
plt.axis('off')
koch(10)
```
