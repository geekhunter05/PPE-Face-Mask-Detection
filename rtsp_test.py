import cv2
from ultralytics import YOLO

# Load trained model
model = YOLO(
    r"C:\Users\Lenovo\Downloads\lab.py\runs\detect\runs\train\mask_detection_v2\weights\best.pt"
)

# RTSP camera
RTSP_URL = "rtsp://192.168.30.23:8554/primary1"

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)

if not cap.isOpened():
    print("ERROR: Could not open RTSP camera")
    exit()

print("RTSP camera connected.")
print("PPE detection started.")
print("Press Q to quit.")

while True:

    ret, frame = cap.read()

    if not ret:
        print("Frame read failed")
        continue

    # YOLO detection
    results = model.predict(
        frame,
        imgsz=640,
        conf=0.40,
        verbose=False
    )

    annotated_frame = results[0].plot()

    # Default status
    status = "NO PERSON DETECTED"

    # Check detected classes
    if results[0].boxes is not None:

        for box in results[0].boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            class_name = model.names[class_id]

            if class_name == "with_mask":
                status = "SAFE - MASK OK"

            elif class_name == "without_mask":
                status = "WARNING - MASK REQUIRED"

            elif class_name == "mask_weared_incorrect":
                status = "WARNING - WEAR MASK CORRECTLY"

    # Put status on screen
    cv2.putText(
        annotated_frame,
        status,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0) if status == "SAFE - MASK OK" else (0, 0, 255),
        2
    )

    cv2.imshow(
        "Smart PPE Detection System",
        annotated_frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()