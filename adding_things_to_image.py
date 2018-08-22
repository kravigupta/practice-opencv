# Author: Ravi Kumar Gupta
# Github: https://github.com/kravigupta
# Twitter: https://twitter.com/kravigupta

import cv2

# Image downloaded from https://pixabay.com/en/math-symbols-blackboard-classroom-1500720/

pathToImage = 'images/math-1500720_640.jpg'

# reading an image
img = cv2.imread(pathToImage)

# Adding a line to the image
# 0,0 is the top left corner of the image ;)
# Method signature
# cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
# @param img Image.
# @param pt1 First point of the line segment.
# @param pt2 Second point of the line segment.
# @param color Line color.
# @param thickness Line thickness.
# @param lineType Type of the line. See #LineTypes.
# @param shift Number of fractional bits in the point coordinates.

cv2.line(img, (30, 30), (200, 300), (250, 0, 0), 10)

# Adding rectangle
# cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
cv2.rectangle(img, (100, 100), (300, 300), (100, 200, 250), 10)

# Adding a circle
# cv2.circle(img, center, radius, color, thickness=None, lineType=None, shift=None):
cv2.circle(img, (500, 200), 100, (20, 30, 100), 4)

# Adding a text to the image
# font = cv2.FONT_HERSHEY_COMPLEX # choosing a font
# Putting the font on the image
# cv2.putText(img, text, org, fontFace, fontScale, color, thickness=None, lineType=None, bottomLeftOrigin=None)
cv2.putText(img, 'Ravi Kumar Gupta', (100, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (200, 0, 200), 3, cv2.LINE_AA)

# showing an image
cv2.imshow('Image - ' + pathToImage, img)

cv2.waitKey(0)

cv2.destroyAllWindows()
