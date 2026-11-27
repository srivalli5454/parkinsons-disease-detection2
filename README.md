# Parkinson's Disease Image Classification Using YOLO11

An AI-powered image classification web application built using **YOLO11 and Streamlit** to classify uploaded brain images into two categories: **Healthy** and **Parkinson**.

The application displays the predicted class along with confidence scores for both categories.

## Live Demo

**[Launch the Parkinson's Disease Detection App](https://parkinsons-disease-detection2-f2qrsmeya5okyeuo8jehp3.streamlit.app/)**

## GitHub Repository

**[View Source Code](https://github.com/srivalli5454/parkinsons-disease-detection2)**

## Project Overview

This project explores deep learning-based image classification for Parkinson's disease research.

A YOLO11 classification model was trained on a brain image dataset to distinguish between healthy and Parkinson's classes. The trained model was integrated into a Streamlit web application, allowing users to upload images and receive predictions with confidence scores.

## Features

- Upload images in JPG, JPEG, and PNG formats.
- YOLO11-based image classification.
- Binary classification: Healthy and Parkinson.
- Prediction confidence percentage.
- Separate confidence scores for Healthy and Parkinson.
- Interactive Streamlit web interface.
- Real-time image prediction.

## Technologies Used

- Python
- YOLO11 Classification
- Ultralytics
- Streamlit
- NumPy
- Pillow
- OpenCV

## Model Details

| Parameter | Details |
|---|---|
| Model Architecture | YOLO11n-cls |
| Model Task | Image Classification |
| Number of Classes | 2 |
| Classes | Healthy, Parkinson |
| Input Image Size | 224 × 224 |
| Training Epochs | 25 |

## Dataset Information

The dataset contains two categories:

- Healthy
- Parkinson

A participant-based group split was used to reduce data leakage between training and testing datasets.

| Dataset | Healthy | Parkinson | Total |
|---|---:|---:|---:|
| Training | 78 | 78 | 156 |
| Testing | 24 | 24 | 48 |
| **Total** | **102** | **102** | **204** |

## Model Performance

The YOLO11 classification model achieved the following results on the test dataset:

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 81.25% |
| Precision | 75.86% |
| Recall | 91.67% |
| F1 Score | 83.02% |
| Specificity | 70.83% |
| AUC | 87.33% |

## Application Workflow

1. Open the Streamlit application.
2. Upload a brain image.
3. Click the Predict button.
4. The trained YOLO11 model processes the image.
5. View the predicted class.
6. View the confidence percentages for both Healthy and Parkinson categories.

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/srivalli5454/parkinsons-disease-detection2.git
cd parkinsons-disease-detection2
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Application

```bash
streamlit run app.py
```

**Note:** Ensure that the trained `best.pt` model file is present in the project directory.

## Project Structure

```text
parkinsons-disease-detection2/
│
├── app.py
├── best.pt
├── requirements.txt
├── packages.txt
└── README.md
```

## Future Improvements

- Evaluate the model on larger and more diverse datasets.
- Improve model generalization and reliability.
- Integrate explainable AI techniques such as Grad-CAM.
- Explore additional deep learning architectures.

## Disclaimer

This project is developed strictly for educational and research purposes. It is not a clinically validated medical diagnostic system and must not be used to diagnose Parkinson's disease or make medical decisions.

## Author

**Srivalli Korada**

- **GitHub Profile:** [github.com/srivalli5454](https://github.com/srivalli5454)
- **Project Repository:** [parkinsons-disease-detection2](https://github.com/srivalli5454/parkinsons-disease-detection2)
- **Live Application:** [Streamlit Demo](https://parkinsons-disease-detection2-f2qrsmeya5okyeuo8jehp3.streamlit.app/)

