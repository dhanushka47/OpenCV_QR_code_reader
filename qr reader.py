import cv2
import numpy as np
from pyzbar.pyzbar import decode


# decode image
def decoder(image):
    img = cv2.cvtColor(image, 0)  # convert to captured image gray scale
    barcode = decode(img)
    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)
        data = obj.data.decode("utf-8")
        codetype = obj.type
        string = str(codetype) + ": " + str(data)
        cv2.putText(frame, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        if codetype == "QRCODE":
            print("QR Code: " + data + " - Type: " + codetype)
        else:
            print("Barcode: " + data + " - Type: " + codetype)


cap = cv2.VideoCapture(0)  # capture image
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow('Video', frame)
    code = cv2.waitKey(10)
    if code == ord('q'):
        break
