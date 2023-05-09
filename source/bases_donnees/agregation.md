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

# Agrégation

```{code-cell}
:tags: ["remove-stdout", "remove-input"]
%load_ext sql
%sql sqlite:///../../_databases/dummy.db
```

Les fonctions d'agrégation permettent d'effectuer des opérations sur un ensemble de lignes d'une même table :

* déterminer la somme des éléments d'une colonne ;
* déterminer le minimum d'une colonne ;
* etc...

## Fonctions d'agrégation

### Minimum, maximum

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT MIN(annee) FROM films
```

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT MAX(duree) FROM films
```

### Somme, moyenne

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT SUM(duree) FROM films
```

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT AVG(duree) FROM films
```

### Comptage

La fonction `COUNT` compte le nombre de lignes d'une table dans une ou plusieurs colonnes données.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT COUNT(*) FROM realisateurs
```

Les colonnes spécifiées dans la commande `COUNT` peuvent avoir une importance s'il manque des données dans certaines colonnes (valeur `None` dans les enregistrements).

```{code-cell}
:tags: ["remove-stdout", "remove-input", "remove-output"]
%%sql
DROP TABLE IF EXISTS t;
CREATE TABLE t (col_a varchar(10), col_b int);
INSERT INTO t VALUES
("a", NULL),
("b", 2),
("c", 3),
(NULL, 3),
(NULL, 3),
(NULL, NULL);
```

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT * FROM t
```

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT COUNT(*) FROM t
```

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT COUNT(col_a) FROM t
```

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT COUNT(col_b) FROM t
```

On peut également utiliser le mot-clé `DISTINCT` pour déterminer le nombre de lignes distinctes d'une ou plusieurs colonnes.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT pays FROM realisateurs
```

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT COUNT(DISTINCT pays) FROM realisateurs
```

## Agrégation sur des regroupements

On peut effectuer des agrégations par groupement d'attributs à l'aide d'une clause `GROUP BY`.

La requête suivante permet par exemple de compter le nombre de réalisateurs pour chaque pays d'origine.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT pays, COUNT(id) AS nb_realisateurs FROM realisateurs GROUP BY pays
```

On peut aussi effectuer des groupements sur plusieurs attributs. La requête suivante permet de déterminer la note moyenne donné pour chaque couple `(spectateur, pays)`. Autrement dit, on peut obtenir la note moyenne de chaque spectateur pour tous les films d'un pays donné.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT spectateurs.nom AS nom_spectateur, pays AS pays_film, AVG(note) AS note_moyenne
FROM spectateurs JOIN notes JOIN films JOIN realisateurs
ON notes.spectateur_id=spectateurs.id AND notes.film_id=films.id AND films.realisateur_id=realisateurs.id
GROUP BY spectateurs.nom, pays
```

## Filtrage des agrégats

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT nom, AVG(duree) AS duree_moyenne
FROM realisateurs JOIN films ON films.realisateur_id=realisateurs.id
GROUP BY nom
HAVING duree_moyenne>120
```

<!-- TODO Expliquer la différence entre HAVING et WHERE -->