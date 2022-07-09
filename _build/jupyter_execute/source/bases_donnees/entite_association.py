#!/usr/bin/env python
# coding: utf-8

# # Modèle entité-association

# In[1]:


get_ipython().run_line_magic('load_ext', 'sql')
get_ipython().run_line_magic('sql', 'sqlite:///../../_databases/dummy.db')


# ## Entités et associations
# 
# On cherche à modéliser les différents liens qui existent entre les tables d'une base de données. Une **entité** désigne une table de ces bases de données et une **association** désigne un lien entre deux entités. Par exemple, on manipulera une base de données dont les **entités** sont `REALISATEUR`, `FILM`, `SPECTATEUR` et `SPECTATEUR_DETAILS`.
# 
# ```{mermaid}
# erDiagram
#   REALISATEUR ||--|{ FILM : "réalise"
#   SPECTATEUR }o--o{ FILM : "note"
#   SPECTATEUR_RENSEIGNEMENTS ||--|| SPECTATEUR : "renseigne"
# ```
# 
# Les associations entre ces entités sont les suivantes :
# 
# * Les réalisateurs **réalisent** des films.
# * Les spectateurs **notent** des films.
# * Les fiches de renseignements **renseignent** sur les spectateurs.
# 
# ## Clés primaires et étrangères
# 
# Pour réaliser concrètement des associations entre entités d'une base de données, on utilise la notion de **clé**.
# 
# Une **clé primaire** est un attribut ou la combinaison de plusieurs attributs d'une table d'une base de données permettant d'identifier chaque enregistrement de la table de manière unique. Considérons par exemple la table `films` suivante.
# 
# ```{mermaid}
# erDiagram
#   films {
#     string  titre
#     int     annee
#     int     duree
#   }
# ```
# 
# Une clé primaire pourrait être l'attribut `titre` ou encore le couple `(titre, annee)`. Malheureusement, deux films pourraient avoir le même titre ou, encore pire, le même titre et la même année de sortie, ce qui ne permettrait pas d'identifier chaque enregistrement de manière unique. C'est pourquoi l'on rajoute souvent à une table un attribut **identifiant**. Cet identifiant (le plus souvent un entier ou éventuellement une chaîne de caractères) est généré de manière automatique à chaque ajout d'un enregistrement dans la table de telle sorte qu'il soit distinct des identifiants des enregistrements précédents.
# 
# Dans la table suivante, l'attribut `id` désigne un identifiant qui servira de clé primaire (`PK` signifie **P**rimary **K**ey).
# 
# ```{mermaid}
# erDiagram
#   films {
#     int     id    PK
#     string  titre
#     int     annee
#     int     duree
#   }
# ```
# 
# De la même manière, on considère la table `realisateurs` suivante où l'attribut `id` désigne à nouveau un identifiant servant de clé primaire.
# 
# ```{mermaid}
# erDiagram
#   realisateurs {
#     int     id    PK
#     string  nom
#     string  pays
#   }
# ```
# 
# On peut relier ces deux entités `films` et `realisateurs` par une association à l'aide de ces clés. On utilise pour cela une **clé étrangère**, c'est-à-dire un attribut d'une table faisant référence à une clé primaire d'une autre table.
# 
# Par exemple, l'attribut `realisateur_id` de la table `films` suivante est une clé étrangère (`FK` signifie **F**oreign **K**ey) faisant référence à l'attribut `id` de la table `realisateurs`.
# 
# ```{mermaid}
# erDiagram
#   films {
#     int     id              PK
#     string  titre
#     int     annee
#     int     duree
#     int     realisateur_id  FK
#   }
# ```
# 
# ## Cardinalité d'une association
# 
# Dans l'exemple donné initialement, on remarque que les associations sont de plusieurs types :
# 
# * Un réalisateur peut réaliser plusieurs films tandis qu'un film est réalisé par un unique réalisateur : l'association **réalise** `REALISATEUR->FILM` est dite de type `1-*`.
# * Un spectateur peut noter plusieurs films et un film peut être noté par plusieurs spectateurs : l'association **note** `SPECTATEUR->FILM` est dite de type `*-*`.
# * Chaque fiche de renseignement est associé à un unique spectateur et chaque spectateur possède une unique fiche de renseignements : la relation **renseigne** `SPECTATEUR_RENSEIGNEMENTS->SPECTATEUR` est dite de type `1-1`.
# 
# De manière générale :
# 
# * Une association entre une entité `A` et une entité `B` est dite de type `1-*` si tout élément de `A` est en relation avec plusieurs éléments de `B` et que chaque élément de `B` est en relation avec un unique élément de `A`.
# * Une association entre une entité `A` et une entité `B` est dite de type `1-1` si tout élément de `A` est en relation un unique élement de `B` et inversement.
# * Une association entre une entité `A` et une entité `B` est dite de type `*-*` si tout élément de `A` est en relation avec plusieurs éléments de `B` et inversement.
# 
# ### Associations `1-*`
# 
# L'utilistation d'une clé étrangère permet naturellement de réaliser des associations de type `1-*` comme le montre l'exemple suivant.
# 
# ```{mermaid}
# erDiagram
#   realisateurs ||--|{ films : "réalise"
# 
#   films {
#     int     id              PK
#     string  titre
#     int     annee
#     int     duree
#     int     realisateur_id  FK
#   }
# 
#   realisateurs {
#     int     id    PK
#     string  nom
#     string  pays
#   }
# ```

# In[2]:


from myst_nb import glue
id=5
glue("id", id)
result_films = get_ipython().run_line_magic('sql', 'SELECT * FROM films WHERE id = :id')
dicts = next(result_films.dicts())
titre = dicts['titre']
glue("titre", titre)
realisateur_id = dicts['realisateur_id']
glue("realisateur_id", realisateur_id)
result_realisateurs = get_ipython().run_line_magic('sql', 'SELECT * FROM realisateurs WHERE id = :realisateur_id')
dicts = next(result_realisateurs.dicts())
nom = dicts['nom']
glue("nom", nom)


# Examinons par exemple l'enregistrement de la table `films` dont l'identifiant est {glue:}`id`.

# In[3]:


result_films


# Le film {glue:}`titre` a donc été réalisé par le réalisateur dont l'identifiant est {glue:}`realisateur_id`.

# In[4]:


result_realisateurs


# Autrement dit, {glue:}`titre` a été réalisé par {glue:}`nom`.
# 
# ### Associations `1-1`
# 
# Pour réaliser une relation `1-1` entre deux tables, il suffit de définir une clé étrangère sur l'une des tables qui est également une clé primaire.
# 
# Considérons les deux tables suivantes.
# 
# ```{mermaid}
# erDiagram
#   spectateurs_renseignements ||--|| spectateurs : "renseigne"
# 
#   spectateurs {
#     int     id              PK
#     string  nom
#   }
# 
#   spectateurs_renseignements {
#     int     spectateur_id    PK "FK"
#     string  ville
#     int     date_naissance
#   }
# ```
# 
# La clé `spectateur_id` de la table `spectateurs_renseignements` est à la fois une clé étrangère est une clé primaire. De cette façon, chaque enregistrement de la table `spectateurs_renseignements` est associé de manière unique à un enregistrement de la table `spectateurs`.
# 
# ```{note}
# Il ne s'agit pas rigoureusement d'une association `1-1` car un enregistrement de la table `spectateurs` est en fait associé à **au plus un** enregistrement de la table `spectateurs_renseignements`.
# ```
# 
# Observons le contenu de ces deux tables.

# In[5]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM spectateurs\n')


# In[6]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM spectateurs_renseignements\n')


# In[7]:


id=7
result_spectateurs = get_ipython().run_line_magic('sql', 'SELECT * FROM spectateurs WHERE id = :id')
dicts = next(result_spectateurs.dicts())
nom_spectateur = dicts['nom']
glue("nom_spectateur", nom_spectateur)
result_spectateurs_renseignements = get_ipython().run_line_magic('sql', 'SELECT * FROM spectateurs_renseignements WHERE spectateur_id = :id')
dicts = next(result_spectateurs_renseignements.dicts())
ville = dicts['ville']
glue("ville", ville)
date_naissance = dicts['date_naissance']
glue("date_naissance", date_naissance)


# Par exemple, {glue:}`nom_spectateur` habite à {glue:}`ville` et est né en {glue:}`date_naissance`.
# 
# ```{note}
# Deux entités qui sont en relation `1-1` peuvent toujours être fusionnées.
# ```
# 
# Par exemple, les tables `spectateurs` et `spectateurs_renseignements` pourraient être fusionnées en l'unique table `spectateurs` suivante.
# 
# ```{mermaid}
# erDiagram
#   spectateurs {
#     int     id              PK
#     string  nom
#     string  ville
#     int     date_naissance
#   }
# ```
# 
# ### Associations `*-*`
# 
# On ne peut pas réaliser des associations `*-*` comme on l'a fait précédemment pour les associations `1-*` et `1-1` puisqu'une clé étrangère ne peut faire référence qu'à un seul enregistrement d'une table. L'idée est alors de séparer une assosiaton `*-*` en deux assocations `1-*` à l'aide d'une entité intermédiaire.
# 
# Dans notre exemple, on peut modéliser l'association `note` entre les entités `FILM` et `SPECTATEUR` à l'aide d'une entité intermédiaire que l'on appelera encore `NOTE`.
# 
# ```{mermaid}
# erDiagram
#   FILM ||--|{ NOTE : "est noté"
#   SPECTATEUR ||--|{ NOTE : "attribue"
# ```
# 
# Chaque film peut être associé à plusieurs notes de même que chaque spectateur peut être associé à plusieurs notes.
# 
# Plus précisément, voici le schéma relationnel entre les tables `films`, `spectateurs` et `notes`.
# 
# ```{mermaid}
# erDiagram
#   films ||--|{ notes : "est noté"
#   spectateurs ||--|{ notes : "attribue"
# 
#   films {
#     int     id              PK
#     string  titre
#     int     annee
#     int     duree
#     int     realisateur_id  FK
#   }
# 
#   spectateurs {
#     int     id              PK
#     string  nom
#   }
# 
#   notes {
#     int film_id       FK
#     int spectateur_id FK
#     int note
#   }
# ```

# In[8]:


result_notes = get_ipython().run_line_magic('sql', 'SELECT * FROM notes ORDER BY RANDOM() LIMIT 1')
dicts = next(result_notes.dicts())
spectateur_id = dicts['spectateur_id']
glue("spectateur_id", spectateur_id)
film_id = dicts['film_id']
glue("film_id", film_id)
note = dicts['note']
glue("note", note)


# Examinons un enregistrement particulier de la table `notes`.

# In[9]:


result_notes


# Ceci signifie que la note {glue:}`note` a été attribuée au film dont l'identifiant est {glue:}`film_id` par le spectateur dont l'identifiant est {glue:}`spectateur_id`.

# In[10]:


film = get_ipython().run_line_magic('sql', 'SELECT * FROM films WHERE id = :film_id')
spectateur = get_ipython().run_line_magic('sql', 'SELECT * FROM spectateurs WHERE id = :spectateur_id')
titre_notes = next(film.dicts())['titre']
glue("titre_notes", titre_notes)
spectateur_notes = next(spectateur.dicts())['nom']
glue("spectateur_notes", spectateur_notes)


# Regardons les enregistrements correspondants des tables `films` et `spectateurs`.

# In[11]:


film


# In[12]:


spectateur


# Ceci signifie que le spectateur {glue:}`spectateur_notes` a attribué la note {glue:}`note` au film {glue:}`titre_notes`.
# 
# ## Jointures
# 
# Les **jointures** permettent de retrouver de l'information sur deux ou plusieurs tables associées.

# In[13]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM films JOIN realisateurs ON films.realisateur_id = realisateurs.id\n')


# La requête précédente est en fait équivalente à la requête suivante.
# 
# ```sql
# SELECT * FROM films, realisateurs WHERE films.realisateur_id = realisateurs.id
# ```
# 
# Néanmoins la première requête est plus rapide que la seconde.

# In[14]:


get_ipython().run_cell_magic('sql', '', 'SELECT titre, nom, note FROM films JOIN notes JOIN spectateurs\nON films.id = notes.film_id AND spectateurs.id = notes.spectateur_id\n')


# In[15]:


get_ipython().run_cell_magic('sql', '', 'SELECT nom, date_naissance, ville FROM spectateurs JOIN spectateurs_renseignements\nON spectateurs.id = spectateurs_renseignements.spectateur_id\n')

