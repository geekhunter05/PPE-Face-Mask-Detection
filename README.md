# \# Real-Time PPE and Face Mask Detection Using YOLOv8

# 

# A computer vision project that detects correctly worn masks, incorrectly worn masks, and people without masks using a custom-trained YOLOv8 model. The system supports real-time video analysis through webcam and RTSP camera streams using OpenCV.

# 

# \## Features

# 

# \- Real-time object detection using YOLOv8

# \- Three detection classes: `with\_mask`, `without\_mask`, and `mask\_weared\_incorrect`

# \- Webcam and RTSP video stream support

# \- Custom dataset training and model evaluation

# \- Performance evaluation using Precision, Recall, F1-score, mAP@50, and mAP@50–95

# 

# \## Technologies Used

# 

# \- Python

# \- Ultralytics YOLOv8

# \- OpenCV

# \- Roboflow

# \- PyTorch

# 

# \## Project Structure

# 

# ```text

# PPE-Face-Mask-Detection/

# ├── app.py

# ├── train.py

# ├── camera\_test.py

# ├── camera\_check.py

# ├── rtsp\_test.py

# ├── rtsp\_raw.py

# ├── gui\_test.py

# ├── download\_dataset.py

# ├── smart.py

# ├── test.py

# ├── requirements.txt

# ├── README.md

# └── .gitignore

# ```

# 

# \## Installation

# 

# 1\. Clone the repository:

# 

# &#x20;  ```bash

# &#x20;  git clone https://github.com/geekhunter05/PPE-Face-Mask-Detection.git

# &#x20;  cd PPE-Face-Mask-Detection

# &#x20;  ```

# 

# 2\. Install the dependencies:

# 

# &#x20;  ```bash

# &#x20;  pip install -r requirements.txt

# &#x20;  ```

# 

# 3\. Ensure the dataset configuration and trained model paths are set correctly before running the scripts.

# 

# \## Model Training

# 

# The model was fine-tuned from the pretrained YOLOv8 Nano model using a custom Roboflow dataset.

# 

# Training configuration:

# \- Model: YOLOv8n

# \- Epochs: 50

# \- Image size: 640 × 640

# \- Batch size: 16

# \- Number of classes: 3

# 

# Run training with:

# 

# ```bash

# python train.py

# ```

# 

# Update the dataset path in `train.py` to match your local environment.

# 

# \## Running Detection

# 

# For webcam detection:

# 

# ```bash

# python camera\_test.py

# ```

# 

# For RTSP camera detection:

# 

# ```bash

# python rtsp\_test.py

# ```

# 

# Configure your camera stream URL locally before running RTSP detection. Do not publish private camera credentials or API keys.

# 

# \## Evaluation

# 

# The model was evaluated on a held-out test dataset using standard object-detection metrics:

# 

# | Metric | Test Result |

# |---|---:|

# | Precision | 69.56% |

# | Recall | 71.97% |

# | F1-score | 70.74% |

# | mAP@50 | 72.32% |

# | mAP@50–95 | 46.40% |

# 

# Performance varies by class. Detection of incorrectly worn masks requires further improvement.

# 

# \## Dataset

# 

# The model was trained using a Roboflow Universe face-mask dataset. Refer to the dataset's original page for its details and licensing conditions before redistributing any images or labels.

# 

# \## Future Improvements

# 

# \- Improve detection of incorrectly worn masks

# \- Evaluate performance in different lighting and camera conditions

# \- Measure real-time inference speed and end-to-end latency

# \- Expand testing with additional real-world data

# 

# \## Security

# 

# Never commit API keys, private RTSP URLs, passwords, or other secrets. Keep credentials in environment variables and rotate any key that has been exposed.

# 

# \## Author

# 

# Developed as a computer vision and deep learning project using YOLOv8 and OpenCV.

