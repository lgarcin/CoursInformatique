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

# Algorithme des k-voisins

## Description de l'algorithme

On dispose d'un jeu d'apprentissage consistant en un certain nombre de couples entrée/sortie.

```{prf:example}
Un jeu d'apprentissage pourrait être une série d'images (entrée) auxquelles on associe ce qu'elles représentent (sortie).
```

Etant donnée une entrée arbitraire $x$, on souhaite déterminer la sortie qui correspond. Pour cela, on choisit dans le jeu d'apprentissage les $k$ entrées "les plus proches" de $x$, disons $x_1,\dots,x_k$. Ces entrées sont associées à des sorties $v_1,\dots,v_k$. On choisit ensuite comme sortie associée à $x$ la sortie la plus représentée parmi $v_1,\dots,v_k$.

```{admonition} Apprentissage supervisé
L'algorithme des $k$-voisins est un algorithme d'apprentissage **supervisé**. En effet, un opérateur a dû au préalable affecté "manuellement" une sortie à chaque entrée du jeu d'apprentissage.
```

## Modélisation du problème

On représentera chaque entrée du jeu d'apprentissage par un vecteur de $\mathbb R^p$ et la distance utilisée pour déterminer les plus proches voisins sera la distance euclidienne.[^distance]

[^distance]: On peut tout à fait décider de représenter les entrées d'une autre manière et utiliser une distance autre que la distance euclidienne.

## Implémentation en Python

```{code-cell}
:tags: ["remove-output", "remove-input"]
import numpy.random as rd
import numpy.linalg as alg

s1 = [(x, 1) for x in rd.normal([1., 4.], 1., (50, 2))]
s2 = [(x, 2) for x in rd.normal([4., 3.], 1., (50, 2))]
s3 = [(x, 3) for x in rd.normal([1., 0.], 1., (50, 2))]
input = [2, 2]
k = 10
n = sorted(s1+s2+s3, key=lambda sample: alg.norm(sample[0]-input))[:k]
```

```{code-cell}
:tags: ["remove-input"]
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.scatter([x[0][0] for x in n], [x[0][1]
            for x in n], label='Voisins', alpha=.3, s=150.)
plt.scatter([x[0][0] for x in s1], [x[0][1]
            for x in s1], label='Classe '+str(s1[0][1]), alpha=.7)
plt.scatter([x[0][0] for x in s2], [x[0][1]
            for x in s2], label='Classe '+str(s2[0][1]), alpha=.7)
plt.scatter([x[0][0] for x in s3], [x[0][1]
            for x in s3], label='Classe '+str(s3[0][1]), alpha=.7)
plt.scatter(input[0], input[1], label='Entrée', s=100.)
plt.legend()
plt.show()
```

```{code-cell}
:tags: ["remove-input"]
c = [x[1] for x in n]
for k in 1, 2, 3:
    print("Nombre de voisins de classe "+str(k)+" : "+str(c.count(k)))
```

```{code-cell}
:tags: ["remove-input"]
d = {k: c.count(k) for k in (1, 2, 3)}
[k for k in d if d[k] == max(d.values())]
```
