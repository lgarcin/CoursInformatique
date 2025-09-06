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

# Algorithme des k-voisins

## Description de l'algorithme

On dispose d'un jeu d'apprentissage consistant en un certain nombre de données réparties dans différentes classes. On peut représenter ce jeu d'apprentissage par une série de couples $(x_i,c_i)$ où $x_i$ représente une donnée et $c_i$ la classe à laquelle elle appartient.

On se donne maintenant une donnée arbitraire $x$ et on souhaite déterminer à quelle classe elle appartient de manière le plus probable. Pour cela, on choisit dans le jeu d'apprentissage les $k$ données "les plus proches" de $x$, disons $x_{i_1},\dots,x_{i_k}$. Ces entrées sont associées à des sorties $c_{i_1},\dots,c_{i_k}$. On choisit ensuite comme classe associée à $x$ la classe la plus représentée parmi $c_{i_1},\dots,c_{i_k}$.

```{admonition} Apprentissage supervisé
L'algorithme des $k$-voisins est un algorithme d'apprentissage **supervisé**. En effet, un opérateur a dû au préalable affecté "manuellement" une sortie à chaque entrée du jeu d'apprentissage.
```

## Modélisation du problème

On représentera chaque entrée du jeu d'apprentissage par un vecteur de $\dR^p$ et la distance utilisée pour déterminer les plus proches voisins sera la distance euclidienne.[^distance]

[^distance]: On peut tout à fait décider de représenter les entrées d'une autre manière et utiliser une distance autre que la distance euclidienne.

## Exemple

```{code-cell}
:tags: ["remove-output", "remove-input"]
import numpy.random as rd
import numpy.linalg as alg
from myst_nb import glue

s1 = [(x, 'A') for x in rd.normal([1., 4.], 1., (50, 2))]
s2 = [(x, 'B') for x in rd.normal([4., 3.], 1., (50, 2))]
s3 = [(x, 'C') for x in rd.normal([1., 0.], 1., (50, 2))]
input = [2, 2]
k = 10
glue("k", k)
n = sorted(s1+s2+s3, key=lambda sample: alg.norm(sample[0]-input))[:k]
```

Donnons-nous par exemple des données représentées par des éléments de $\dR^2$. Ces données sont réparties en trois classes comme le montre le graphique suivant.

```{code-cell}
:tags: ["remove-input"]
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.scatter([x[0][0] for x in s1], [x[0][1]
            for x in s1], label='Classe '+s1[0][1], alpha=.7, color='red')
plt.scatter([x[0][0] for x in s2], [x[0][1]
            for x in s2], label='Classe '+s2[0][1], alpha=.7, color='green')
plt.scatter([x[0][0] for x in s3], [x[0][1]
            for x in s3], label='Classe '+s3[0][1], alpha=.7, color='blue')
plt.legend()
plt.show()
```

On se donne maintenant une entrée et on recherche les $k$ voisins les plus proches de cette entrée. On a choisi arbitrairement $k$ égal à {glue:}`k`.

```{code-cell}
:tags: ["remove-input"]
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.scatter([x[0][0] for x in n], [x[0][1]
            for x in n], label='Voisins', alpha=.3, s=150.)
plt.scatter([x[0][0] for x in s1], [x[0][1]
            for x in s1], label='Classe '+s1[0][1], alpha=.7, color='red')
plt.scatter([x[0][0] for x in s2], [x[0][1]
            for x in s2], label='Classe '+s2[0][1], alpha=.7, color='green')
plt.scatter([x[0][0] for x in s3], [x[0][1]
            for x in s3], label='Classe '+s3[0][1], alpha=.7, color='blue')
plt.scatter(input[0], input[1], label='Entrée', s=100.)
plt.legend()
plt.show()
```

Voici la liste des nombres de voisins dans chaque classe.

```{code-cell}
:tags: ["remove-input"]
c = [x[1] for x in n]
for k in 'A', 'B', 'C':
    print("Nombre de voisins de classe "+k+" : "+str(c.count(k)))
```

On détermine alors la ou les classes les plus représentées.

```{code-cell}
:tags: ["remove-input"]
d = {k: c.count(k) for k in ('A', 'B', 'C')}
[k for k in d if d[k] == max(d.values())]
```

Si deux classes sont représentées le même nombre de fois, on peut éventuellement tenter de changer la valeur de $k$ pour obtenir une unique classe.

## Implémentation en Python

```{code-cell}
import numpy.linalg as alg

def voisins(entree, donnees, k):
    """
    Renvoie les k plus proches voisins de entree dans donnees

    entree : tuple de float
    donnees : liste de couples formés d'un tuple de float et d'une classe
    """
    return sorted(donnees, key=lambda d: alg.norm(d[0]-entree))[:k]
```

```{code-cell}
def vote(classes):
    # Renvoie la liste des éléments les plus représentés dans la liste classes

    d = {c: classes.count(c) for c in classes}
    return [c for c in d if d[c] == max(d.values())]
```

```{code-cell}
vote(["Alphonse", "Bob", "Charlotte", "Bob", "Charlotte", "Charlotte"])
```

```{code-cell}
vote(["Alphonse", "Bob", "Charlotte", "Bob", "Charlotte", "Alphonse"])
```

```{code-cell}
def classification(entree, donnees, k):
    v = voisins(entree, donnees, k)
    return vote([x[1] for x in v])
```

```{code-cell}
import numpy.random as rd

d1 = [(x, 'A') for x in rd.normal([1., 4.], 1., (50, 2))]
d2 = [(x, 'B') for x in rd.normal([4., 3.], 1., (50, 2))]
d3 = [(x, 'C') for x in rd.normal([1., 0.], 1., (50, 2))]
entree = [2, 2]
classification(entree, d1+d2+d3, 10)
```

## Matrice de confusion

Pour mesurer la performance d'un algorithme de **classification** comme l'est l'algorithme des $k$-voisins, on peut utiliser une **matrice de confusion**. On suppose disposer de données dont on sait à quelles classes elles appartiennent. Chaque ligne de la matrice correspond à une classe effective et chaque colonne à une classe prédite par l'algorithme.

Dans l'exemple suivant, les données sont réparties entre 3 classes $A$, $B$ et $C$. On voit par exemple que :

* 83% des éléments de la classe $A$ ont été correctement prédits comme faisant partie de la classe $A$ ;
* 25% des éléments de la classe $B$ ont été incorrectement prédits comme faisant partie de la classe $C$ ;
* 5% des éléments de la classe $C$ ont été incorrectement prédits comme faisant partie de la classe $A$.

```{tikz}
\usetikzlibrary{matrix,fit,positioning}
\tikzset{ 
    table/.style={
        matrix of nodes,
        row sep=\pgflinewidth,
        column sep=\pgflinewidth,
        nodes={
            rectangle,
            draw=black,
            align=center
        },
        minimum height=1.5em,
        text depth=0.5ex,
        text height=2ex,
        column 1/.style={
            nodes={
                fill=black,
                text=white,
                font=\bfseries
            }
        },
        row 1/.style={
            nodes={
                fill=black,
                text=white,
                font=\bfseries
            }
        },
        row 1 column 1/.style={
            nodes={fill=none}
        }
    }
}
\matrix (confusion) [table,text width=6em]
{
            & Classe A  & Classe B  & Classe C  \\
Classe A    & 0.83      & 0.13      & 0.04      \\
Classe B    & 0.10      & 0.65      & 0.25       \\
Classe C    & 0.05      & 0.22      & 0.73      \\
};
\node[fit=(confusion-1-2)(confusion-1-4)](column-header){};
\node[fit=(confusion-2-1)(confusion-4-1)](row-header){};
\node[scale=1.2,above of=column-header]{Prédiction};
\node[scale=1.2,left=of row-header,rotate=90,anchor=north]{Réalité};
```
