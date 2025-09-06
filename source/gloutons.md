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

# Algorithmes gloutons

## Rendu de monnaie

Le problème du rendu de monnaie est un exemple classique d'utilisation d'un algorithme glouton. On dispose d'un système de monnaie (pièces ou billets de valeurs déterminées) et on cherche à rendre une somme d'argent à l'aide de cette monnaie.

```{prf:example}
On dipose de pièces de monnaie de 1€, 2€ et 5€ et on souhaite à totaliser la somme de 23€. On peut par exemple donner 4 pièce de 5€, 1 pièce de 2€ et 1 pièce de 1€. Ce n'est pas la seule possibilité : on aurait aussi pu donner 2 pièces de 5€, 4 pièces de 2€ et 5 pièces de 1€.
```

Un algorithme glouton consiste alors à toujours rendre une pièce de valeur maximale et inférieure à la somme restant à rendre.

```{prf:example}
On reprend l'exemple précédent. On dipose de pièces de monnaie de 1€, 2€ et 5€ et on souhaite à totaliser la somme de 23€. On donne alors des pièces de 5€ tant que la somme restant à rendre est inférieure à 5€. On donne donc 4 pièces de 5€. La somme restante est alors de 3€. On donne donc 1 pièce de 2€. La somme restante est de 1€ et on termine donc en donnant 1 pièce de 1€.
```

```{code-cell}
def rendu_monnaie(somme, pieces):
    pieces_triees = sorted(pieces, reverse=True)
    d = {}
    r = somme
    for piece in pieces_triees:
        q, r = divmod(r, piece)
        d[piece] = q
    return d, r
```

```{code-cell}
rendu_monnaie(23, [1, 2, 5])
```

Il n'est pas toujours possible de rendre la somme suivant le système de monnaie employée. Par exemple, avec des pièces de 3€, 9€ et 12€, on ne pourra atteindre que des sommes qui sont des multiples de 3€.

L'algorithme glouton peut également ne pas trouver de solution alors qu'il en existe une.

```{code-cell}
rendu_monnaie(16, [2, 15])
```

On pourrait ici tout simplement rendre 8 pièces de 2€.
