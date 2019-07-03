import numpy as np
import cv2
import sys
import time

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # if len(sys.argv) > 1:
    #     inputImage = cv2.imread(sys.argv[1])
    # else:
    #     inputImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    inputImage = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # Display barcode and QR code location
    def display(im, bbox):
        n = len(bbox)
        for j in range(n):
            cv2.line(im, tuple(bbox[j][0]), tuple(bbox[(j + 1) % n][0]), (255, 0, 0), 3)
    #
    #     # Display results
    #     cv2.imshow("Results", im)
    #     cv2.waitKey(0)



    qrDecoder = cv2.QRCodeDetector()

    # Detect and decode the qrcode
    data, bbox, rectifiedImage = qrDecoder.detectAndDecode(inputImage)
    if len(data) > 0:
        print("Decoded Data : {}".format(data))
        display(inputImage, bbox)
        rectifiedImage = np.uint8(rectifiedImage);
        cv2.imshow("Rectified QRCode", rectifiedImage);
        break

    # else:
    #     print("QR Code not detected")
        # cv2.imshow("Results", inputImage)



    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()