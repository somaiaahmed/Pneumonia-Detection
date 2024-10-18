

# Pneumonia Detection and GAN Image Generation Project

## Project Overview

This project is focused on the early detection of pneumonia from chest X-ray images and uses a Generative Adversarial Network (GAN) model for the generation of realistic synthetic pneumonia images to augment training data. Early detection of pneumonia can help healthcare providers offer timely treatments, improving patient outcomes and potentially saving lives. The detection system is deployed as a web application using **Flask**.

### Key Features
1. **Pneumonia Detection Model**: A deep learning model that classifies chest X-ray images as either "Pneumonia" or "Normal."
2. **GAN Image Generation**: A GAN model trained to generate realistic pneumonia images, helping to augment training data and improve model performance.
3. **Web Application**: The model is deployed using Flask, providing an interactive web interface for uploading images and receiving real-time predictions.

---

## Table of Contents
- [Business Value](#business-value)
- [Model Overview](#model-overview)
  - [Pneumonia Detection Model](#pneumonia-detection-model)
  - [GAN Model for Image Generation](#gan-model-for-image-generation)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Model Performance](#model-performance)
- [Web Application](#web-application)
  - [Screenshots](#screenshots)
- [Setup Instructions](#setup-instructions)
- [Future Enhancements](#future-enhancements)

---

## Business Value

Pneumonia is a life-threatening illness that affects over **450 million people globally** each year. The **early detection** of pneumonia is critical for administering timely medical interventions, especially in children under five and the elderly. Implementing a **GAN-based pneumonia image generation system** helps in:

1. **Improving Data Quality**: GAN-generated images can enhance training datasets, addressing data imbalance between pneumonia and normal cases.
2. **Enhancing Model Performance**: By augmenting the dataset with synthetic pneumonia images, the model can better generalize, leading to more accurate predictions in real-world scenarios.
3. **Supporting Healthcare Systems**: Such a system reduces diagnostic errors and assists healthcare providers in making more accurate, data-driven decisions.

---

## Model Overview

### Pneumonia Detection Model

The detection model is a convolutional neural network (CNN) trained to classify chest X-ray images into two categories: **Pneumonia** and **Normal**. It takes a chest X-ray image as input and outputs the probability of the image belonging to either class.

- **Input**: X-ray images resized to (224x224).
- **Output**: Prediction of "Pneumonia" or "Normal."
- **Libraries**: TensorFlow, Keras.

![Predict&Actual Images](<assets/Predict&Actual Images.png>)
---

### GAN Model for Image Generation

The **Generative Adversarial Network (GAN)** is used to generate synthetic pneumonia images. This is particularly useful for improving the detection model’s performance by augmenting the dataset with more pneumonia images.

- **Generator**: Creates realistic pneumonia images from noise.
- **Discriminator**: Evaluates whether the generated images are real or synthetic.
- **Purpose**: To alleviate class imbalance in the dataset and improve model generalization.

---

## Exploratory Data Analysis (EDA)

Exploratory Data Analysis was conducted to understand the dataset better. Visualizations such as class distributions, image quality, and correlation analyses were performed to ensure balanced and clean data for model training.

![Edge Contour](<assets/Edge Contour.png>)
---

## Model Performance

### Pneumonia Detection Model
The performance of the pneumonia detection model is evaluated using the following metrics:

![Classification Report](<assets/Classification Report.png>)
### GAN Model
The GAN model is evaluated based on its ability to generate realistic and diverse pneumonia images that can fool the discriminator while improving classification model performance.

![GANS Output](<assets/GANS Output.png>)
---

## Web Application

The project includes a **Flask-based web application** that allows users to upload chest X-ray images and receive predictions on whether the patient has pneumonia or not.

![website screenshot](<assets/Website Screenshot.png>)
---

## Setup Instructions

### Prerequisites
- Python 3.x
- TensorFlow and Keras
- Flask
- OpenCV
- Numpy
- Pickle

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/pneumonia-gan-detection.git
   cd pneumonia-gan-detection
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download or place the trained models (`detection_model.h5` and `gan_model.h5`) in the `model/` directory.

4. Run the Flask web application:
   ```bash
   python app.py
   ```

5. Access the web application by opening a browser and navigating to `http://127.0.0.1:5000/`.

---

## Future Enhancements

- **GAN Image Integration**: Automatically enhance uploaded X-ray images using the GAN model.
- **Deployment on Cloud**: Deploy the app on a cloud platform such as AWS or Google Cloud for real-time access.
- **Model Optimization**: Experiment with more advanced architectures to further improve detection accuracy.
- **Multi-class Classification**: Expand the model to detect other lung diseases like tuberculosis or COVID-19.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

