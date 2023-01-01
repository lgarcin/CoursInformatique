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

Une image est représentée par un tableau à deux dimensions. Chaque case de ce tableau est appelée **pixel**.

```{code-cell}
import imageio.v3 as io
import matplotlib.pyplot as plt

img = io.imread('imageio:camera.png')
plt.imshow(img, cmap='gray')
```

```{code-cell}
img[100:200, 50:450] = 0
plt.imshow(img, cmap='gray')
```

<!-- TODO Image couleurs -->