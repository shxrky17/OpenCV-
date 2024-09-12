import cv2

# Use the full path to your image
image = cv2.imread('c:/Users/chafl/OneDrive/Desktop/yash/ML/lena.jpg',1)
cv2.imshow('Image',image)
k=cv2.waitKey(0)


if k==27:
 cv2.destroyAllWindows()

elif k==ord('s'):
 cv2.imwrite('lena2.png',image)
 cv2.destroyAllWindows()