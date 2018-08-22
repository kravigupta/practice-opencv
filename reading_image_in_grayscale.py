# Author: Ravi Kumar Gupta
# Github: https://github.com/kravigupta
# Twitter: https://twitter.com/kravigupta

import cv2

# Image downloaded from https://pixabay.com/en/math-symbols-blackboard-classroom-1500720/

pathToImage = 'images/math-1500720_640.jpg'

# reading an image
img = cv2.imread(pathToImage)

# reading an image with flag gray
gray_image = cv2.imread(pathToImage, cv2.IMREAD_GRAYSCALE)

# showing an image
cv2.imshow('Image - ' + pathToImage, img)

# showing the grayscale image
cv2.imshow('Grey image - '+ pathToImage, gray_image)

cv2.waitKey(0)

cv2.destroyAllWindows()