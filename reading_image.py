# Author: Ravi Kumar Gupta
# Github: https://github.com/kravigupta
# Twitter: https://twitter.com/kravigupta


import cv2

# Image downloaded from https://pixabay.com/en/math-symbols-blackboard-classroom-1500720/

pathToImage = 'images/math-1500720_640.jpg'

# reading an image
img = cv2.imread(pathToImage)

# showing an image
cv2.imshow('Image - ' + pathToImage, img)

# we want to keep the window open. hence setting 0 in waitKey(). If a value xx is set, the image window will be closed after xx milliseconds
cv2.waitKey(0)

cv2.destroyAllWindows()