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

# Requêtes

Pour retrouver des informations dans une base de données, on effectue ce qu'on appelle des **requêtes** décrites dans un langage approprié. Le langage que nous utiliserons est le langage **SQL** (Structured Query Language). Une requête permet de renvoyer une nouvelle table à partir de tables stockées dans la base de données.

```{code-cell}
:tags: ["remove-stdout", "remove-input"]
%load_ext sql
%sql sqlite:///../../_databases/dummy.db
```

## Projection

Pour sélectionner les colonnes d'une table, on utilise la requête `SELECT`. La syntaxe générale est la suivante :

```sql
SELECT _colonnes_ FROM _table_
```

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT titre FROM films
```

On peut sélectionner plusieurs colonnes d'une table.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT titre, duree FROM films
```

```{note}
L'astérique `*` que l'on a utilisé jusqu'à maintenant permet de sélectionner toutes les colonnes d'une table.
```

## Sélection

Pour sélectionner les enregistrements d'une table dont les attributs vérifient une certaine condition on utilise la requête `SELECT` assortie d'une clause `WHERE`.

La syntaxe générale est la suivante :

```sql
SELECT _colonnes_ FROM _table_ WHERE _condition_
```

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM films WHERE annee < 1980
```

On dispose d'opérateurs logiques pour construire des conditions plus complexes.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM films WHERE annee >= 1975 AND annee < 1990
```

La condition peut porter sur plusieurs colonnes.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT * FROM films WHERE annee > 1980 OR duree <= 120
```

On peut également combiner les requêtes de sélection et de projection (sélection de lignes **et** de colonnes).

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT titre, annee FROM films WHERE annee >= 1990
```

## Renommage

On peut renommer les colonnes et les tables à l'aide du mot-clé `AS`.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT nom AS name, pays AS country FROM realisateurs
```

## Mots-clés divers

Le mot clé `LIMIT` que nous avons utilisé depuis le début de ce chapitre pour des raisons cosmétiques permet de limiter le nombre d'enregistrements renvoyés par une requête. La requête suivante renvoie les 10 premiers enregistrements de la table `films`.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM films LIMIT 10
```

___

Dans le même ordre d'idée, le mot-clé `OFFSET` permet de retourner les enregistrements d'une requête à partir d'un certain rang. La requête suivante permet d'ignorer les 3 premiers enregistrements de la table `films` et de renvoyer les 5 suivants.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT * FROM films LIMIT 5 OFFSET 3
```

___

Une clause `ORDER BY` permet d'ordonner les résultats d'une requête. Si le type utilisé dans cette clause est textuel, les enregistrements sont ordonnées par l'ordre lexicographique.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT * FROM films ORDER BY titre
```

Par défaut les enregistrements sont renvoyés par ordre croissant. On peut utiliser les mots clés `ASC` (ascendant) et `DESC` (descendant) si on veut spécifier l'ordre.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT * FROM films ORDER BY titre ASC
```

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT * FROM films ORDER BY titre DESC
```

On peut utiliser plusieurs critères de tris successifs. Dans la requête suivante, les résultats sont triés par année croissante puis par titre décroissant.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT * FROM films ORDER BY annee, titre DESC
```

___

Le mot clé `DISTINCT` permet de supprimer les doublons dans le résultat d'une requête.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT nom, pays FROM realisateurs
```

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT DISTINCT pays FROM realisateurs
```

___

On peut combiner tous les mots clés précédents pour effectuer des requêtes complexes.

```{code-cell}
:tags: ["remove-stdout"]
%%sql
SELECT titre, annee FROM films
WHERE annee > 1980 OR duree > 150
ORDER BY duree DESC
LIMIT 10
```
