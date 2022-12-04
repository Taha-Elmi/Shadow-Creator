import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys

filename = "part2.jpg"
coefficient = 1

if len(sys.argv) > 1:
    coefficient = int(sys.argv[1])
if len(sys.argv) > 2:
    filename = sys.argv[2]

transform_matrix = np.matrix([[1, 0],
                              [coefficient, 1]])

img = Image.open(filename)
pixels = np.array(img)
shadow = np.full((pixels.shape[0], (coefficient * pixels.shape[0]) + pixels.shape[1], 3), 255, dtype=int)

for i in range(pixels.shape[0]):
    for j in range(pixels.shape[1]):
        new_coordinate = np.array(transform_matrix * [[i], [j]])
        if new_coordinate[0, 0] < shadow.shape[0] and new_coordinate[1, 0] < shadow.shape[1] and (pixels[i, j] < 240).all():
            shadow[new_coordinate[0, 0], new_coordinate[1, 0]] = (100, 100, 100)

for i in range(pixels.shape[0]):
    for j in range(pixels.shape[1]):
        if (pixels[i, j] < 240).all():
            shadow[i, j + (coefficient * pixels.shape[0])] = pixels[i, j]

new_filename = f'{filename.split(".")[0]}_edited.jpg'
plt.imsave(new_filename, shadow.astype(np.uint8))

plt.imshow(shadow)
plt.show()
