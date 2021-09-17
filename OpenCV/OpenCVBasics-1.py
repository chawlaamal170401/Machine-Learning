import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('dog.jpg')
new_img = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.show()

plt.imshow(new_img)
plt.show()