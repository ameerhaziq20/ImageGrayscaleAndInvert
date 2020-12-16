import cv2   #import library

def invert(I, name):   #invert function
    I = (255-I)       #invert formula
    cv2.imwrite(name,I) 

image = cv2.imread('D:\FILES\Data\Development\Python\Assignment\wrc.jpg') #image import
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)     #open image as grayscale
invert(grayscale_image, "inverted.png")       #invert and export image
