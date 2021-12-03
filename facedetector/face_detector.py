import cv2
import random

#load some pre trained data on face frontals from opencv 
trained_face_data =cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#to capture video from webcam
webcam = cv2.VideoCapture(0) #0 is default webcam

while True:
    ##read current frames
    successful_frame_red, frame= webcam.read()

    #convert t greyscale
    grayscaled_frames= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates= trained_face_data.detectMultiScale(grayscaled_frames)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(random.randrange(255),random.randrange(255),random.randrange(255)),2)
       
    cv2.imshow('face',frame)
    key=cv2.waitKey(1)
    # if pressed f exit
    if key==70 or key==102:
        break

#relese videocopture object
webcam.release()
#choose an image to detect faces in
# img=cv2.imread('faces.jpg')
# img = cv2.resize(img, (600, 600))

#must convert to grayscale
# grayscaled_img= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #detectface
# face_coordinates= trained_face_data.detectMultiScale(grayscaled_img)

# #draw rectangles around the face or multiple faces
# for (x,y,w,h) in face_coordinates:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(random.randrange(255),random.randrange(255),random.randrange(255)),2)
# # print(face_coordinates)

# cv2.imshow('face',img)
# cv2.waitKey()



