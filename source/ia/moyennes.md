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

# Algorithme des k-moyennes

## Description du problème

On dispose de $n$ points $x_1,\dots,x_n$ d'un espace euclidien (dont la norme euclidienne est notée $\|\cdot\|$) et on cherche à répartir ces $n$ points en $k$ classes de manière à minimiser les distances entre points à l'intérieur de chaque classe.

De manière plus formelle, notons $\mathfrak{P}$ l'ensemble des partitions de $\{1,\dots,n\}$ en $k$ parties.

```{prf:example}
Par exemple, $\{\{1,3\},\{2,5,7\},\{4,6\}\}$ est une partition de $\{1,2,3,4,5,6,7\}$ en $3$ parties.
```

De manière générale, si $\mathcal{P}\in\mathfrak{P}$, alors $|\mathcal{P}|=k$ et $\bigsqcup_{P\in\mathcal{P}}P=\{1,\dots,n\}$.

On cherche alors la partition $\mathcal{P}\in\mathfrak{P}$ minimisant la fonction

$$
\Phi\colon\mathcal{P}\in\mathfrak{P}\mapsto\sum_{P\in\mathcal{P}}\sum_{j\in P}\|x_j-\mu_P\|^2
$$

où $\mu_P=\frac{1}{|P|}\sum_{i\in P}x_i$ représente le barycentre des points appartenant à la classe $P$ (d'où le nom de $k$-moyennes).

## Algorithme

On dispose de $n$ points à répartir en $k$ classes. Ces classes seront numérotées de $1$ à $k$. L'ensemble des points appartenant à une même classe est appelé **cluster**.

```{prf:algorithm} K-moyennes
- Initialisation : affecter à chaque point une classe (choisie aléatoirement par exemple).
- Répéter les étapes suivantes jusqu'à ce que la répartion des points dans les classes n'évolue plus :

  - Calculer le barycentre $m_i$ de chaque cluster $i\in\{1,\dots,k\}$.
  - Affecter à chaque point $x$ la classe $i$ du barycentre $m_i$ qui lui est le plus proche.
```

On peut montrer que la fonction $\Phi$ décroît strictement à chaque itération. Comme le nombre de partitions est fini, on peut alors garantir que l'algorithme s'arrête. Malheureusment, rien ne garantit que la partition finale obtenue corresponde à un minimum global de $\Phi$.

## Implémentation

La fonction suivante permet de mettre à jour la répartition des données dans chaque classe.

```{code-cell}
def update_classes(data, classes, nb_classes):
    barycentres = [
        np.mean(data[classes == id_classe], axis=0) for id_classe in range(nb_classes)
    ]
    distances = [alg.norm(data - b, axis=1) for b in barycentres]
    return np.argmin(distances, axis=0)
```

On initialise les classes de manière aléatoire et on répète la mise à jour de la répartition jusqu'à ce qu'elle n'évolue plus.

```{code-cell}
def k_moyennes(data, nb_classes):
    N = data.shape[0]
    classes = rd.randint(nb_classes, size=N)
    while True:
        c = update_classes(data, classes, nb_classes)
        if np.unique(c).shape[0] != nb_classes:
            print("Cluster vide, passage à " + str(nb_classes - 1) + " classes")
            return k_moyennes(data, nb_classes - 1)
        if np.all(c == classes):
            classes = c
            break
        classes = c
    return classes
```

```{warning}
La fonction `update_classes` peut éventuellement générer des clusters vides. Le calcul du barycentre d'une telle classe déclencherait alors une erreur. On choisit dans ce cas de redémarrer l'algorithme avec une classe de moins.
```

On teste l'algorithme sur le jeu de données suivantes. Il s'agit de points de $\dR^2$.

```{code-cell}
:tags: ["remove-input"]
import numpy as np
import numpy.random as rd
import numpy.linalg as alg
```

```{code-cell}
:tags: ["remove-input"]
import matplotlib.pyplot as plt

data1 = rd.normal([-4.0, 4.0], 1.0, (20, 2))
data2 = rd.normal([4.0, -4.0], 1.0, (30, 2))
data3 = rd.normal([-4.0, -4.0], 1.0, (40, 2))
data4 = rd.normal([4.0, 4.0], 1.0, (10, 2))

data = np.concatenate((data1, data2, data3, data4))

plt.scatter(data[:, 0], data[:, 1], alpha=0.7)
plt.show()
```

```{code-cell}
nb_classes = 4
classes = k_moyennes(data, nb_classes)
```

```{code-cell}
:tags: ["remove-input"]

for id_classe in range(nb_classes):
    cluster = data[classes == id_classe]
    plt.scatter(cluster[:, 0], cluster[:, 1], alpha=0.7)
plt.show()
```

```{code-cell}
nb_classes = 8
classes = k_moyennes(data, nb_classes)
```

```{code-cell}
:tags: ["remove-input"]

for id_classe in range(nb_classes):
    cluster = data[classes == id_classe]
    plt.scatter(cluster[:, 0], cluster[:, 1], alpha=0.7)
plt.show()
```
