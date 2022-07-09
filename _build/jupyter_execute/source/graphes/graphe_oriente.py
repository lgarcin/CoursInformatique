#!/usr/bin/env python
# coding: utf-8

# # Graphe orienté

# In[1]:


import networkx as nx
from IPython.display import Latex
edges=[(1,2), (3,1), (2,3), (1,4), (2,4), (3,3), (5,3)]


# ```{prf:definition} Graphe *orienté*
# Un graphe **orienté** est un graphe dont les arêtes sont orientées. On parle alors d\\'**arc** plutôt que d'arête. Chaque arc possède donc un sommet initial (ou origine) et un sommet terminal (ou extrémité).
# ```

# In[2]:


G = nx.DiGraph()
G.add_edges_from(edges)
nx.draw_circular(G, with_labels=True, font_weight="bold", font_size=20, node_size=600)


# La liste des sommets de ce graphe est :

# In[3]:


Latex(",\;".join([str(n) for n in G.nodes]))


# et la liste des arcs est :

# In[4]:


Latex(",\;".join([str(e[0])+r"\to "+str(e[1]) for e in G.edges]))


# ```{prf:definition} Définition formelle d'un graphe orienté
# On appelle graphe orienté tout couple $G=(S,A)$ où $S$ est un ensemble et
# 
# $$
# A\subset\left\{(x,y),\;(x,y)\in S^2\right\}
# $$
# 
# $S$ désigne l'ensemble des sommets tandis que $A$ désigne l'ensemble des arcs.
# ```
# 
# ```{note}
# Les couples de la forme $(x,x)$ désignent des boucles.
# ```

# In[5]:


Latex("S=\left\{"+",\;".join([str(n) for n in G.nodes])+r"\right\}")


# In[6]:


Latex("A=\left\{"+",\;".join(["("+str(e[0])+","+str(e[1])+")" for e in G.edges])+r"\right\}")


# ```{prf:definition} Degré entrant d'un sommet
# Le **degré entrant** d'un sommet $s$ est le nombre $d_-(s)$ d'arcs dont le sommet terminal est $s$.
# ```
# 
# ```{prf:definition} Degré sortant d'un sommet
# Le **degré sortant** d'un sommet $s$  le nombre $d_+(s)$ d'arcs dont le sommet initial est $s$.
# ```
# 
# Dans l'exemple précédent, les degrés entrants et sortants des différents sommets sont les suivants :

# In[7]:


Latex(",\;".join(["d_-("+str(s)+")="+str(d) for (s,d) in G.in_degree()]))


# In[8]:


Latex(",\;".join(["d_+("+str(s)+")="+str(d) for (s,d) in G.out_degree()]))


# ```{prf:definition} Chemin
# On appelle **chemin** d'un sommet $s_1$ à un sommet $s_2$ une suite finie d'arcs consécutifs reliant les sommets $s_1$ et $s_2$.
# ```
# 
# ```{warning}
# L'orientation des arcs compte.
# ```
# 
# Dans l'exemple précédent, $1\to2\to4$ et $5\to3\to1$ sont des chemins.
# 
# ```{prf:definition} Cycle
# Un **cycle** est un chemin dont le sommet initial et le sommet terminal sont identiques.
# ```
# 
# Dans l'exemple précédent, $3\to1\to2\to3$ est un cycle.
