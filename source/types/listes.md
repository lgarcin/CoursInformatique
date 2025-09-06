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

# Listes

## Création de listes et opérations de base

Une **liste** est tout simplement une collection ordonnée d'objets. En Python, on la déclare en séparant ses éléments par des virgules `,` et en les encadrant par des crochets `[...]`.

```{code-cell}
type([1,2,3])
```

Les objets contenus dans une même liste peuvent être de types différents.

```{code-cell}
[1.23, 'abc', 45]
```

On peut même imbriquer des listes.

```{code-cell}
[1.23, ['abc', 'def', 'ghi'], [45, 67]]
```

L'opérateur `+` permet de _concaténer_ des listes.

```{code-cell}
[1.23, 'abc', 45] + [6, 'def', 'ghi', 7.89]
```

On devine alors l'action de l'opérateur `*` [^monoide].

[^monoide]: En termes savants, l'ensemble des listes munis de la loi `+` est un _monoïde_. La loi `+` est en effet une loi interne associative et la liste vide `[]` est neutre pour cette loi. Le "produit" d'une liste par un entier (positif) n'est autre qu'un _multiple_ de cette liste.

```{code-cell}
[1.23, 'abc', 45] * 3
```

```{note}
On ne peut évidemment multiplier une liste que par un **entier**.
```

La fonction `len` permet de récupérer la longueur d'une liste.

```{code-cell}
len([1.23, 'abc', 45])
```

## Accès aux éléments en lecture

On peut accéder aux éléments d'une liste via leurs indices et l'opérateur `[...]`.

```{code-cell}
ma_liste = [25, 34, 48, 67]
ma_liste[2]
```

```{warning}
Il est à noter que les indices des listes commencent à 0 et non 1. Le dernier indice d'une liste de $n$ éléments est donc $n-1$ et non $n$.
```

On peut bien sûr accéder à des éléments de listes imbriquées.

```{code-cell}
ma_liste = [1.23, ["abc", "def", "ghi"], [45, 67]]
ma_liste[1][2]
```

On peut également accéder à des éléments d'une liste "par la fin".

```{code-cell}
ma_liste = ['a', 'b', 'c', 'd', 'e']
ma_liste[-1], ma_liste[-3]
```

L'accès à une position non valide déclenche une erreur.

```{code-cell}
:tags: ["raises-exception"]
ma_liste[10]
```

## Accès aux éléments en écriture

L'opérateur `[...]` permet également de modifier les éléments d'une liste.

```{code-cell}
ma_liste = [25, 34, 48, 67]
ma_liste[2] = 666
ma_liste
```

Bien évidemment, cela fonctionne aussi pour les listes imbriquées.

```{code-cell}
ma_liste = [1.23, ["abc", "def", "ghi"], [45, 67]]
ma_liste[1][2] = "toto"
ma_liste
```

## Insertion et suppression d'éléments

Il existe plusieurs moyens d'ajouter des éléments à une liste.

La première méthode est de les ajouter un par un grâce aux méthodes `append` (insertion en fin de liste) ou `insert` (insertion à un endroit donné).

```{code-cell}
ma_liste = ['a', 1, 'b']
ma_liste.append(2)
ma_liste
```

```{code-cell}
ma_liste.insert(2, 'toto')
ma_liste
```

Pour ajouter plusieurs éléments d'affilée, on peut utiliser l'opérateur de concaténation `+` ou de concaténation/affectation `+=` ou encore la méthode `append`.

```{code-cell}
ma_liste = ['a', 1, 'b', 2]
ma_liste = ma_liste + ['c', 3, 'd']
ma_liste
```

```{code-cell}
ma_liste += [4, 5]
ma_liste
```

```{code-cell}
ma_liste.extend(['e', 6, 'f'])
ma_liste
```

De même, il existe plusieurs façons de supprimer des éléments d'une liste.

Pour supprimer des éléments, on peut utiliser les méthodes `pop` (renvoie le dernier élément et le supprime de la liste) ou `remove` (supprime un élément de valeur donnée).

```{code-cell}
ma_liste = ['a', 1, 'b', 2, 'c', 3]
ma_liste.pop()
ma_liste
```

```{code-cell}
ma_liste.remove('b')
ma_liste
```

```{note}
La méthode `remove` ne supprime que la *première* occurence d'une valeur donnée.
```

```{code-cell}
ma_liste = [1, 2, 3, 2, 4, 2]
ma_liste.remove(2)
ma_liste
```

La suppression d'éléments peut également se faire au moyen du mot-clé `del` [^del].

[^del]: De manière générale, le mot-clé `del` "supprime" une variable (sans rentrer dans les détails).

```{code-cell}
ma_liste = ['a', 1, 'b', 2, 'c', 3]
del ma_liste[2]
ma_liste
```

## Tranches (slicing)

Il existe une syntaxe permettant de créer une sous-liste (tranche) d'une liste.

```{code-cell}
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f']
ma_liste[2:5]
```

De manière générale, si `li` est une liste, alors `li[a:b]` renvoie la liste formée des éléments de la liste `li` dont les indices sont compris entre `a` (**inclus**) et `b` (**non inclus**).

Si `a` ou `b` sont omis, la sélection s'opére à partir du début ou jusqu'à la fin de la liste.

```{code-cell}
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f']
ma_liste[2:], ma_liste[:4]
```

On peut encore sélectionner des éléments à intervalles réguliers.

```{code-cell}
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
ma_liste[2:9:3], ma_liste[7:2:-2]
```

Le slicing permet aussi de modifier les éléments d'une liste.

```{code-cell}
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
ma_liste[2:9:3]
```

```{code-cell}
ma_liste[2:9:3] = 'toto', 'tata', 'titi'
ma_liste
```

On peut combiner le slicing et le mot-clé `del` pour supprimer plusieurs éléments à la fois.

```{code-cell}
ma_liste = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
ma_liste[5:10:2]
```

```{code-cell}
del ma_liste[5:10:2]
ma_liste
```

## Listes en compréhension

En mathématiques, il existe plusieurs manières de décrire un même ensemble. L'ensemble $\mathcal{A}$ des entiers pairs compris entre 0 et 19 peut être défini en _extension_ :

$$
\mathcal{A}=\{0,2,4,6,8,10,12,14,16,18\}
$$

Il peut également être décrit en _compréhension_ :

$$
\mathcal{A}=\left\{2n,\;n\in\lb0,9\rb\right\}
$$

De la même manière, la liste de ces entiers peut être défini en Python en extension :

```{code-cell}
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

et en compréhension :

```{code-cell}
[2*n for n in range(10)]
```

On parle alors de _liste en compréhension_.

Une autre manière de définir $\mathcal{A}$ en compréhension est la suivante :

$$
\mathcal{A} = \left\{x\in\lb0,19\rb,\;x\equiv0[2]\right\}
$$

La version correspondante en Python est :

```{code-cell}
[n for n in range(20) if n%2==0]
```

Bien entendu, on peut utiliser ce type de liste pour d'autres objets que des entiers.

```{code-cell}
[s.upper() for s in ('toto', 'tata', 'titi', 'zozo', 'zaza', 'zizi') if s[0]=='t']
```
