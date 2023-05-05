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

# Jointures

```{code-cell}
:tags: ["remove-stdout", "remove-input"]
%load_ext sql
%sql sqlite:///../../_databases/dummy.db
```

Les **jointures** permettent de retrouver de l'information sur deux ou plusieurs tables associées par des clés primaires/étrangères. On utilise pour cela une clause `JOIN` assortie d'une condition.

```sql
SELECT _colonnes_ FROM _table1_ JOIN _table2_ ON _condition_
```

Une telle requête est en fait équivalente à la requête suivante (sélection sur un produit cartésien) :

```sql
SELECT _colonnes_ FROM _table1_, _table2_ WHERE _condition_
```

Néanmoins, une jointure est plus rapide qu'une sélection sur un produit cartésien.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT * FROM films JOIN realisateurs ON films.realisateur_id = realisateurs.id
```

On vérifie qu'une sélection sur un produit cartésien produit le même résultat.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT * FROM films, realisateurs WHERE films.realisateur_id = realisateurs.id
```

On peut également effectuer la jointure de plus de deux tables.

```{code-cell}
:tags: ["remove-stdout", "output_scroll"]
%%sql
SELECT titre, nom, note FROM films JOIN notes JOIN spectateurs
ON films.id = notes.film_id AND spectateurs.id = notes.spectateur_id
```
