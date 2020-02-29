import cv2
from matplotlib import pyplot as plt
img = cv2.imread('../img/yol.jpg', 0)

edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')

plt.title('Orjinal Resim'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(edges, cmap='gray')

plt.title('Koseli Resim'), plt.xticks([]), plt.yticks([])

plt.show()