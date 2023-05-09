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

# Mutabilité

## Introduction

Il s'agit d'un paragraphe un peu subtil : il s'agit d'expliquer la différence fondamentale qu'il existe en Python entre les objets que l'on peut modifier (listes) ou que l'on ne peut modifier (tuples ou chaînes de caractère).

Considérons ce premier exemple où les variables sont des entiers.

```{code-cell}
a = 1
b = a
a = 2   # on modifie a
a, b    # b n'a pas ete modifiée
```

Considérons maintenant l'exemple suivant où les variables sont des listes.

```{code-cell}
a = [1, 2, 3]
b = a
a[0] = 'foo'    # on modifie la liste a
a, b            # la liste b a aussi ete modifiée !
```

Pour expliquer la différence entre ces deux exemples, il faut comprendre la représentation des objets Python en mémoire. Pour cela, on va utiliser la fonction `id`. Pour schématiser, celle-ci renvoie l'emplacement en mémoire d'un objet.

```{code-cell}
a = 1
b = a
id(a), id(b)    # les variables a et b pointent vers le même emplacement en mémoire
```

```{code-cell}
a = 2
id(a), id(b)    # la variable b pointe toujours vers le même emplacement mais plus la variable a
```

L'instruction `a = 2` a fait pointer la variable `a` vers un autre emplacement en mémoire où est stocké l'entier `2`.

```{mermaid}
flowchart LR
    subgraph before [Avant]
    a_before((a))
    b_before((b))
    1_before(1)
    a_before-->1_before
    b_before-->1_before
    end

    subgraph after [Après]
    a_after((a))
    b_after((b))
    1_after(1)
    2(2)
    a_after-->2
    b_after-->1_after
    end

    before==>after
```

```{code-cell}
a = [1, 2, 3]
b = a
id(a), id(b)    # les variables a et b pointent vers le même emplacement en mémoire
```

```{code-cell}
a[0] = 'foo'
id(a), id(b)    # les variables a et b pointent toujours vers le même emplacement
```

Ici, l'instruction `a[0] = 'foo'` a modifié l'objet stocké à l'emplacement commun vers lequel pointent les variables `a` et `b`. Comme `a` et `b` pointent toujours le même emplacement en mémoire, la variable `b` est maintenant associée à ce nouvel objet.

```{mermaid}
flowchart LR
    subgraph before [Avant]
    a_before((a))
    b_before((b))
    l_before("[1, 2, 3]")
    a_before-->l_before
    b_before-->l_before
    end

    subgraph after [Après]
    a_after((a))
    b_after((b))
    l_after("['foo', 2, 3]")
    a_after-->l_after
    b_after-->l_after
    end

    before==>after
```

## Objets mutables et immutables

Mais pourquoi cette différence de comportement ? Il existe en Python deux types d'objets : les objets **mutables** et les objets **immutables**. On peut donner la définition suivante.

> Un objet est dit **mutable** si on peut changer sa valeur après sa création. Il est dit **immutable** dans le cas contraire.

* Objets immutables : entiers, flottants, complexes, tuples, chaînes de caractères, ...

* Objets mutables : listes, dictionnaires, ...

Voilà la solution du mystère : toutes les variables pointant vers un même objet mutable sont affectées par la modification de cet objet. Ceci ne peut pas se produire lorsque des variables pointent vers un objet immutable puisque celui-ci ne peut-être modifié.

```{note}
Ce n'est pas rigoureusement exact. Un objet immutable tel qu'un tuple peut contenir des objets mutables comme des listes. Néanmoins, chaque objet du tuple conserve le même emplacement en mémoire même s'il a été modifié.
```

```{code-cell}
a = ([1, 2, 3], 'toto', 'tata')
b = a
a[0][1] = 1000
a, b                # b a egalement ete modifié
```

```{code-cell}
id(a[0]), id(b[0])  # le premier élément du tuple est toujours le même
```

## Copie

Bien souvent, on veut copier une liste ou un dictionnaire dans un nouvel objet pour qu'il ne subisse pas les modifications de l'objet initial. Pour cela, il ya plusieurs possibilités :

* le slicing `[:]` pour les listes ;
* l'utilisation de la méthode `copy` ;
* l'utilisation du constructeur `list` pour les listes ou du constructeur `dict` pour les dictionnaires.

```{code-cell}
liste1 = [1, 2, 3]
liste2 = liste1[:]
liste3 = liste1.copy()
liste4 = list(liste1)
id(liste1), id(liste2), id(liste3), id(liste4)  # les objets sont bien distincts
```

```{code-cell}
liste1[0] = 'toto'
liste1, liste2, liste3, liste4                  # liste1 a ete modifiée mais pas les autres listes
```

___

Il faut prendre garde au fait que les copies de listes ou de dictionnaires ne sont que des copies **superficielles**.

Créons un dictionnaire `eleve`. Il est important de remarquer que la valeur associé à la clé `'nom'` est un objet immutable (une chaîne de caractères) tandis que la valeur associé à la clé `'notes'` est un objet mutable (une liste).

```{code-cell}
eleve  = { 'nom': 'Pierrette', 'notes': [14, 8, 15]}
```

On effectue une copie de `eleve` que l'on stocke dans une variable `eleve2`.

```{code-cell}
eleve2 = eleve.copy()
eleve2
```

On modifie le contenu du dictionnaire `eleve` ; on s'attend à ce que le contenu de `eleve2` ne soit pas modifié.

```{code-cell}
eleve['nom'] = 'Alphonse'
eleve['notes'].append(20)
```

On constate que dans le dictionnaire `eleve2`, la valeur associée à la clé `'nom'` est bien restée inchangée tandis que la valeur associée à la clé `'notes'` a subit la même modifiaction que dans `eleve`.

```{code-cell}
eleve, eleve2
```

___

Le lecteur attentif aura remarqué qu'on semblerait pouvoir modifier un objet immutable telle qu'une chaîne de caractères ou un tuple à l'aide des opérateurs `+` ou `+=`. Mais ces opérateurs ne modifient pas l'objet en question ; ils créent en fait un **nouvel** objet. On peut s'en convaincre à l'aide de la fonction `id`.

```{code-cell}
t = (1, 2, 3)
id(t)
```

```{code-cell}
t = t + (4, 5)
id(t)
```

```{code-cell}
t += (6, 7, 8)
id(t)
```

Pour les objets mutables tels que les listes, les opérateurs `+` et `+=` se comportent de manières différentes : l'opérateur `+` crée un nouvel objet tandis que l'opérateur `+=` modifie l'objet initial.

```{code-cell}
liste1 = [1, 2, 3]
liste2 = liste1
liste1 = liste1 + [4, 5]
liste1, liste2          # seule liste1 a ete modifiée
```

```{code-cell}
id(liste1), id(liste2)  # c'est normal : liste1 et liste2 pointent vers des objets distincts
```

```{code-cell}
liste1 = [1, 2, 3]
liste2 = liste1
liste1 += [4, 5]
liste1, liste2          # liste1 et liste2 ont ete modifiées
```

```{code-cell}
id(liste1), id(liste2)  # c'est normal : liste1 et liste2 pointent vers le même objet
```

## Egalité structurelle ou physique

On a vu que l'opérateur `==` permettait de tester si deux objets étaient égaux. Mais de quel type d'égalité parle-t-on alors ? L'opérateur `==` teste si deux objets ont la même **valeur** sans pour autant qu'il partage le même emplacement en mémoire. On parle alors d\\'**égalité structurelle**.

Lorsque "deux" objets sont en fait identiques (c'est-à-dire lorsqu'ils ont le même emplacement en mémoire), on parle d\\'**égalité physique**. Pour tester l'égalité physique, on peut comparer les emplacements en mémoire à l'aide de la fonction `id` ou plus simplement utiliser l'opérateur `is`.

```{code-cell}
dict1 = {'nom': 'toto', 'age': 43}
dict2 = dict1
dict3 = dict1.copy()
dict1, dict2, dict3
```

```{code-cell}
id(dict1), id(dict2), id(dict3)
```

```{code-cell}
dict2 == dict1, dict3 == dict1
```

```{code-cell}
dict2 is dict1, dict3 is dict1
```

Un exemple peut-être un peu plus surprenant.

```{code-cell}
[1, 2, 3] == [1, 2, 3]
```

```{code-cell}
[1, 2, 3] is [1, 2, 3]
```

Python a en fait stocké deux versions de la liste `[1, 2, 3]` dans deux emplacements en mémoire distincts.

___

On termine par un cas plus vicieux que les deux exemples initiaux et qui peut faire passer des nuits blanches au programmeur débutant en Python.

```{code-cell}
a = [[0] * 3] * 4
a
```

```{code-cell}
a[0][0] = 1     # on pense n'avoir modifié qu'un élément de la liste de listes a
a               # en fait non...
```
