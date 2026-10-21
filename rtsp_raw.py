import cv2

RTSP_URL = "rtsp://192.168.30.23:8554/primary1"

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print("ERROR: Camera not opened")
    exit()

print("Camera connected")
print("Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Frame read failed")
        continue

    cv2.imshow("RTSP Raw Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()