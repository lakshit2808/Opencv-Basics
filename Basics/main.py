import cv2

img = cv2.imread("galaxy.jpg" , 0) # this methon give the intensity of the image as here '0' refer to black n white image '1' refer to colour image and '-1' refer to transparent img
#print(img)
#print(img.shape) # shape will give us no of value in horizonal as well as in vertical direction
#print(img.ndim) # this will give dimensions of img

resize_img = cv2.resize(img , (1000,500)) # here this tuple is the new size of the img
cv2.imshow("Galaxy" , resize_img) # Galaxy is the name of the img
cv2.waitKey(0) # 1000 means window will be closed in 1000 miniseconds i.e 1 second and 0 means it will close when ever i press the key
cv2.destroyAllWindows()
cv2.imwrite("Galaxy_resized.jpg" , resize_img) # this methon will create a new img i.e "Galaxy_resized.jpg"
