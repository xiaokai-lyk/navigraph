#encoding=gbk
import cv2
import matplotlib.pyplot as plt
#load and show original image
zl = cv2.imread('f5.jpg', cv2.IMREAD_GRAYSCALE)
#cv2.namedWindow('Original Picture', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
#cv2.imshow('Original Picture', zl)
#cv2.waitKey(-1)
 
# Horizontal edge detection using Sobel operator
#change type to float64
edge_x = cv2.Sobel(zl, cv2.CV_64F, dx=1, dy=0)

# Converted to absolute value for the correct preformence
edge_x_abs = cv2.convertScaleAbs(edge_x)
 
# Vertical edge detection using Sobel operator
#change type to float64
edge_y = cv2.Sobel(zl, cv2.CV_64F, dx=0, dy=1)
 
# Converted to absolute value for the correct preformence
edge_y_abs = cv2.convertScaleAbs(edge_y)
 
#Use the addWeighted function to overlay the horizontal and vertical edge detection 
#results to create a combined edge detection image.
compounded = cv2.addWeighted(edge_x_abs, 1, edge_y_abs, 1, 0)

# Show the result image
#cv2.namedWindow('Edge', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
#cv2.imshow('Edge', compounded)
#cv2.waitKey(-1)

#kernel for erosion
kernel_e = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#kernel for dilation
kernel_d = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
#kernel for getting nodes
kernel_r = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
erosion=cv2.erode(compounded,kernel_e)
dilation=cv2.dilate(erosion,kernel_d)

"""

cv2.namedWindow('Erosion', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.imshow('Erosion', erosion)
cv2.waitKey(-1)


cv2.namedWindow('Dilation', cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
cv2.imshow('Dilation', dilation)
cv2.waitKey(-1)
"""

_,binary = cv2.threshold(dilation, 127, 255, cv2.THRESH_BINARY) 

fig,ax=plt.subplots()
ax.imshow(binary,extent=[0,640,0,480])
plt.show()