#IMG Write and colors 
import cv2
import numpy as np
img=cv2.imread("sea.jpg") #read img
img=cv2.resize(img,(300,300)) #resize img
#RGB , HSV , Gray
"""
cv2.imwrite("river.jpg",img) #group img is called but with friends name new same ing is created
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
HSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

r,b,g=cv2.split(img)
cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)
merge_img=cv2.merge([r,b,g])
cv2.imshow("merge_img",merge_img)
cv2.imshow("original_img",img)

cv2.imshow("gray_img",gray)#show image
cv2.imshow("HSV_img",HSV)#show image
"""
# Gaussian , Median_blur , Bilateral_filter
"""
blur=cv2.blur(img,(5,5))

gaussian_blur=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gaussian",gaussian_blur)

median_blur=cv2.medianBlur(img,9)
cv2.imshow("median",median_blur)

bilateral_filter=cv2.bilateralFilter(img,9,75,75)
cv2.imshow("Bilateral",bilateral_filter)

cv2.imshow("original_img",img)
cv2.imshow("blur",img)
"""

# Kernels ,Erode ,Dilate
"""
cv2.imshow("original_img",img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("original_gray",gray)
kernel=np.ones((5,5),np.uint8)

erode=cv2.erode(gray,kernel)
cv2.imshow("erode_img",erode)

dilate=cv2.dilate(gray,kernel)
cv2.imshow("dilate",dilate)


open_img=cv2.morphologyEx(gray,cv2.MORPH_OPEN,kernel)
cv2.imshow("open_img",open_img)

close_img=cv2.morphologyEx(gray,cv2.MORPH_CLOSE,kernel)
cv2.imshow("close_img",close_img)
"""

# Threshs Segmentation
"""
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.imshow("gray_img",gray)

ret,thresh1=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
cv2.imshow("Thresh binary",thresh1)

ret,thresh2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh binary_inv",thresh2)

ret,thresh3=cv2.threshold(gray,125,255,cv2.THRESH_TOZERO)
cv2.imshow("Thresh to zero",thresh3)

ret,thresh4=cv2.threshold(gray,125,255,cv2.THRESH_TOZERO_INV)
cv2.imshow("Thresh to zero_inv",thresh4)

ret,thresh5=cv2.threshold(gray,125,255,cv2.THRESH_TRUNC)
cv2.imshow("Thresh_trunc",thresh5)
"""

# Brightness and Sharpness

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
brightness=cv2.convertScaleAbs(img,beta=+120)
kernal=np.array([[-1,-1,-1],[-1,-9.5,-1],[-1,-1,-1]])
sharpness=cv2.filter2D(img,-1,kernal)

cv2.imshow("original_img",img)
cv2.imshow("gray_img",gray)
cv2.imshow("bright_img",brightness)
cv2.imshow("sharp_img",sharpness)




