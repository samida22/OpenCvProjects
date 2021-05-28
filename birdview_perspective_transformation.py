import cv2
import numpy as np
img = cv2.imread("cards.jpg")

width, height = 250, 350
pnts1 = np.float32([[111,219],[287,188], [154,482], [352, 440]])
print(pnts1)
#circel at one corner
cv2.circle(img, (pnts1[0][0], pnts1[0][1]), 3, (0, 0, 255), -1)

#we need for four corner
for i in range(0, 4):
    cv2.circle(img, (pnts1[i][0], pnts1[i][1]), 6, (0, 0, 255), -1)

#let's define 4 perspective points to transform this image 

pnts2 = np.float32([[0,0], [width,0], [0,height], [width, height]])
print(pnts2)


#draw these points into matrix
matrix_pnts = cv2.getPerspectiveTransform(pnts1, pnts2)

#output image 
output_image= cv2.warpPerspective(img, matrix_pnts, (width, height))

cv2.imshow("originalimage", img)
cv2.imshow("transformimage", output_image)

cv2.waitKey(0)