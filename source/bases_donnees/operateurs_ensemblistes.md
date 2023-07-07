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

# Opérateurs ensemblistes

```{code-cell}
:tags: ["remove-stdout", "remove-input"]
%load_ext sql
%sql sqlite://
```

```{code-cell}
:tags: ["remove-stdout", "remove-input", "remove-output"]
%%sql
DROP TABLE IF EXISTS t1;
DROP TABLE IF EXISTS t2;
CREATE TABLE t1 (col_a varchar(10), col_b int);
CREATE TABLE t2 (col_c varchar(10), col_d int);
INSERT INTO t1 VALUES
("abc", 1),
("def", 2),
("ghi", 3);
INSERT INTO t2 VALUES
("abc", 3),
("def", 2);
```

Dans cette section, on considère les deux tables `t1` et `t2` suivantes.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM t1
```

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM t2
```

## Union, intersection, différence

Comme son nom l'indique l'opérateur ensembliste `UNION` permet de créer la **réunion** de deux tables. Plus précisément, cet opérateur crée une table dont les lignes figurent dans l'une des deux tables.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM t1
UNION
SELECT * FROM t2
```

___

L'opérateur `INTERSECT` permet de créer l\\'**intersection** de deux tables, c'est-à-dire la table dont les lignes figurent dans les deux tables à la fois.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM t1
INTERSECT
SELECT * FROM t2
```

___

Enfin, l'opérateur `EXCEPT` crée la différence de deux tables, c'est-à-dire la table dont les lignes figurent dans la première table mais pas dans la seconde.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM t1
EXCEPT
SELECT * FROM t2
```

___

```{note}
A chaque fois, les noms des colonnes de la table résultante sont les noms de la **première** table.
```

```{warning}
Le nombre de colonnes des deux tables intervenant dans une union, une intersection ou une différence doit être le même.
```

```{code-cell}
%%sql
SELECT col_a FROM t1
UNION
SELECT col_c, col_d FROM t2
```

## Produit cartésien

On peut effectuer le produit cartésien de deux tables (ou plus) à l'aide de la commande suivante.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM t1, t2
```

Les lignes de la table résultante sont formées des lignes de la première table appariées à chacune des lignes de la seconde table.

On peut sélectionner uniquement certaines colonnes de chacune des deux tables comme le montre l'exemple suivant.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT col_a, col_d FROM t1, t2
```

<!-- TODO Introduire la syntaxe table.nom en cas d'ambiguïté -->
