import numpy as np
import matplotlib.pyplot as plt
from imageio import imread

name = input("Enter image filename (with .tif): ")

img = imread(name)

rows = img.shape[0]
cols = img.shape[1]

h = rows // 3

B = img[0:h, :]
G = img[h:2*h, :]
R = img[2*h:3*h, :]

color = np.zeros((h, cols, 3), dtype=img.dtype)
color[:, :, 0] = R
color[:, :, 1] = G
color[:, :, 2] = B

base = name.split('.')[0]

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(R, cmap='gray')
plt.title("Red Channel")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(G, cmap='gray')
plt.title("Green Channel")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(B, cmap='gray')
plt.title("Blue Channel")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(color)
plt.title("Final Color Image")
plt.axis("off")

plt.tight_layout()
plt.savefig(base + "_result.png", dpi=300)
plt.show()
