import cv2
import os

inputImage = cv2.imread("508281f296223ed2_jpg.rf.2cc5c29c2e4dc9d7544e824f673b4c5e.jpg")

cropped_img = cv2.resize(inputImage, (416,416))

return_image_path = 'cropped_image.jpg'
cv2.imwrite(return_image_path, cropped_img)


