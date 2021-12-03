import cv2

trained_objects=cv2.CascadeClassifier('car_detector.xml')

img=cv2.imread('car.jpg')
img = cv2.resize(img, (600, 600))

greyscaled_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

car_coordinates= trained_objects.detectMultiScale(greyscaled_img)
#draw rectangles around the face or multiple faces
for (x,y,w,h) in car_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
# print(face_coordinates)

cv2.imshow('face',img)
cv2.waitKey()