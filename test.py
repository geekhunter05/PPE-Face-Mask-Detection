from ultralytics import YOLO

model = YOLO(
    r"C:\Users\Lenovo\Downloads\lab.py\runs\detect\runs\train\mask_detection_v2\weights\best.pt"
)

results = model.val(
    data=r"C:\Users\Lenovo\Downloads\lab.py\Corona-2\data.yaml",
    split="test",
    imgsz=640,
    batch=16
)

print("\n===== FINAL TEST RESULTS =====")
print("Precision:", results.box.mp)
print("Recall:", results.box.mr)
print("mAP@50:", results.box.map50)
print("mAP@50-95:", results.box.map)

precision = results.box.mp
recall = results.box.mr

f1 = 2 * precision * recall / (precision + recall)

print("F1 Score:", f1)