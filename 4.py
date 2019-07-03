import cv2,time

video = cv2.VideoCapture(0)

a=1

while True:
    a=a+1
    check,frame = video.read()
    print(frame)
    #print(check)
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #time.sleep(7)

    cv2.imshow('capture',frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a) #This will print the number of frames
video.release()

cv2.destroyAllWindows()