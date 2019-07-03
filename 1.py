import cv2

            #load an image

img=cv2.imread("p1.jpg",1) #black and white
img2=cv2.imread("avatar.png",1) #color

print(img)
print(img2)

print(type(img))

print(img.shape) #black and white
print(img2.shape) #color

            #Display the image

cv2.imshow('p1',img2)

# cv2.waitKey(0)
#cv2.waitKey(2000)
# cv2.destroyAllWindows()

            #Resize image

resized=cv2.resize(img,(600,600))
resized_image = cv2.resize(img,(int(img.shape[1]/8),int(img.shape[0]/8)))

cv2.imshow('resize',resized)
cv2.imshow('resizeim',resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
