import cv2
from ultralytics import YOLO

# ==============================
# Load trained YOLO model
# ==============================

model = YOLO(
    r"C:\Users\Lenovo\Downloads\lab.py\runs\detect\runs\train\mask_detection_v2\weights\best.pt"
)

# ==============================
# RTSP CAMERA
# ==============================

RTSP_URL = "rtsp://192.168.30.23:8554/primary1"

cap = cv2.VideoCapture(RTSP_URL)

# ==============================
# Check camera
# ==============================

if not cap.isOpened():
    print("ERROR: Could not open RTSP camera")
    exit()

print("RTSP Camera started.")
print("Press Q to quit.")

# ==============================
# Main loop
# ==============================

while True:

    ret, frame = cap.read()

    if not ret:
        print("ERROR: Could not receive frame")
        break

    # YOLO detection
    results = model(
        frame,
        conf=0.40,
        verbose=False
    )

    # Draw detections
    annotated_frame = results[0].plot()

    # Show result
    cv2.imshow(
        "Mask Detection - RTSP Camera",
        annotated_frame
    )

    # Quit with Q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ==============================
# Cleanup
# ==============================

cap.release()
cv2.destroyAllWindows()