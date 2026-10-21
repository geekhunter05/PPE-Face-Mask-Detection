from roboflow import Roboflow

rf = Roboflow(api_key="DBTVkwuOYHJFr6ggsjT0")

project = rf.workspace("pratyaksh-ycet").project("corona-5vh6d-zbp6j")
version = project.version(2)

dataset = version.download("yolov8")

print("Dataset downloaded successfully!")
print("Location:", dataset.location)