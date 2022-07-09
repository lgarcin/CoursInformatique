#!/usr/bin/env python
# coding: utf-8

# # Dictionnaires
# 
# ## Création de dictionnaires et opérations de base
# 
# Dans le langage courant, un dictionnaire associe à chaque mot d'une langue une définition. En informatique, un **dictionnaire** est une structure de données associant une **valeur** à chaque élément, appelé **clé**, d'un ensemble donné. Du point de vue des mathématiques, un dictionnaire est tout simplement une **application**.
# 
# En Python, on déclare un dictionnaire à l'aide d'accolades `{...}`. Par exemple, le dictionnaire suivant associe :
# 
# * à la clé `'nom'` la valeur `'Toto'`;
# * à la clé `'age'` la valeur `10`;
# * à la clé `'taille'` la valeur `135`;

# In[1]:


personne = {'nom': 'Toto', 'age': 10, 'taille': 135}
type(personne)


# Chaque clé est unique.

# In[2]:


{'nom': 'Toto', 'age': 10, 'taille': 135, 'taille': 140}


# La fonction `len` renvoie la "taille" du dictionnaire, autrement dit son nombre de clés.

# In[3]:


personne, len(personne)


# ## Accès aux éléments en lecture
# 
# On peut alors accéder à la valeur associée à une clé à l'aide de l'opérateur `[...]` ou de la méthode `get`.

# In[4]:


personne['nom'], personne.get('age')


# ```{note}
# Les clés ne sont pas nécessairement des chaînes de caractères. N'importe quel type immutable fait l'affaire.
# ```

# In[5]:


d = {'a': 123, 456: 'def', (1,2): 'fgh'}


# In[6]:


d['a'], d[(1,2)], d.get(456)


# On peut accéder à la liste des clés et à la liste des valeurs d'un dictionnaire à l'aide des méthodes `keys` et `values` respectivement.

# In[7]:


d.keys(), d.values()


# L'accès à une clé invalide déclenche une erreur.

# In[8]:


d['amstramgram'], d.get(42)


# ## Accès aux éléments en écriture
# 
# L'opérateur `[...]` permet également d'insérer ou de modifier les éléments d'un dictionnaire.

# In[9]:


personne


# In[10]:


personne['poids'] = 40
personne


# In[11]:


personne['nom'] = 'Titi'
personne

