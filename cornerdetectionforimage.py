import cv2
import  numpy as np

def empty(x):
    pass

cv2.namedWindow('images')
#tracebar for variying no of corners and quality
cv2.createTrackbar("quality", "images", 1, 100, empty)
cv2.createTrackbar("num_of_corners", "images", 10, 100, empty)


filepath = "/home/kawaii/opencvminorprojects/squares.jpg"
img = cv2.imread(filepath)
#convert to gray scale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#getting tracebar positions
numofcorner = cv2.getTrackbarPos("num_of_corners", "images")
quality = cv2.getTrackbarPos("quality", "images")
quality = quality/100

#corner detection
corners = cv2.goodFeaturesToTrack(img_gray, numofcorner, quality, 10)


#eliminate . from cordinates
corners = np.int0(corners)
print(corners)



#looping through every corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 4, (0,255, 0), -1)

cv2.imshow("images", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

