import cv2

img = cv2.imread('dog.jpg')
Gray = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow("Dog Image", img)
cv2.imshow("Gray Dog", img)

cv2.waitKey(2500)
cv2.destroyAllWindows()