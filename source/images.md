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

# Images

Une image _en niveaux de gris_ est représentée par un tableau à deux dimensions. Chaque case de ce tableau est appelée **pixel**.

```{code-cell}
import imageio.v3 as io
import matplotlib.pyplot as plt
import numpy as np

img = np.array(io.imread('imageio:camera.png'))
plt.imshow(img, cmap='gray')
```

```{code-cell}
img.shape
```

```{code-cell}
img[100:200, 50:100] = 0
img[250:350, 300:400] = 255
plt.imshow(img, cmap='gray')
```

Une image _en couleurs_ est représentée par trois tableaux à deux dimensions de même taille : un pour le canal rouge, un pour le canal vert et un pour le canal bleu.

```{code-cell}
img = np.array(io.imread('imageio:coffee.png'))
plt.imshow(img)
```

```{code-cell}
img.shape
```

```{code-cell}
rouge = img.copy()
rouge[:,:,1] = rouge[:,:,2] = 0
plt.imshow(rouge)
```

```{code-cell}
vert = img.copy()
vert[:,:,0] = vert[:,:,2] = 0
plt.imshow(vert)
```

```{code-cell}
bleu = img.copy()
bleu[:,:,0] = bleu[:,:,1] = 0
plt.imshow(bleu)
```

```{code-cell}
plt.imshow(rouge+vert+bleu)
```

## Redimensionnement d'une image

```{code-cell}
:tags: ["remove-stdout", "remove-input"]
from bokeh.plotting import output_notebook
output_notebook()
```

```{code-cell}
:tags: ["remove-input"]
:load: ../_scripts/interpolation_bilineaire.py
```
