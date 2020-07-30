# Image Restoration
import cv2
import numpy as np

# Load our damaged photo
image = cv2.imread('abraham.jpg')
cv2.imshow('Original Damaged Photo' , image)
cv2.waitKey(0)

# Load the photo where we have marked the damaged areas
marked_damages = cv2.imread('mask.jpg' , 0)
cv2.imshow('Marked Damages', marked_damages )
cv2.waitKey(0)

# Let's make a mask out of our marked image be changing all colors
# that are not white , to black
ret , thresh1 = cv2.threshold(src=marked_damages, thresh=254, maxval=255, type=cv2.THRESH_BINARY)
cv2.imshow('Threshold Binary', thresh1)
cv2.waitKey(0)
# WE HAVE USED THRESHOLD =254 because we just want detection of our white lines only

# Let's Dilate (make thicker) Since thresholding has narrowed it slightly
kernel = np.ones( (7,7) , np.uint8)
mask = cv2.dilate(src=thresh1, kernel=kernel, iterations=1)
cv2.imshow('Dilate Mask', mask)
cv2.imwrite('abraham_mask.jpg', mask)
cv2.waitKey(0)

restored = cv2.inpaint(src=image , inpaintMask=mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
cv2.imshow('Restored',restored)
cv2.waitKey(0)
cv2.destroyAllWindows()
