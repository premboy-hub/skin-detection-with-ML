# 🔬 Skin Disease Detection using Deep Learning

## 🧠 Overview

This project is a **Machine Learning + Deep Learning based web application** that detects different types of skin diseases from images.

Users can upload an image of a skin condition, and the system will:

* Predict the disease type
* Show confidence score
* Provide basic medical advice

---

## 🚀 Features

* 🖼️ Image upload using Streamlit UI
* 🤖 CNN-based deep learning model
* 📊 Multi-class classification (7 diseases)
* 📈 Confidence score display
* 💡 Basic precaution advice
* ⚠️ Medical disclaimer

---

## 🧪 Technologies Used

* Python
* TensorFlow / Keras
* OpenCV
* NumPy, Pandas
* Streamlit

---

## 📊 Dataset

The model is trained on the **HAM10000 dataset**, which contains dermatoscopic images of skin lesions.

### Classes:

* akiec (Actinic keratoses)
* bcc (Basal cell carcinoma)
* bkl (Benign keratosis-like lesions)
* df (Dermatofibroma)
* mel (Melanoma)
* nv (Melanocytic nevi)
* vasc (Vascular lesions)

---

## ⚙️ How It Works

1. User uploads a skin image
2. Image is preprocessed (resize, normalization)
3. CNN model predicts the class
4. Output is displayed:

   * Prediction
   * Confidence score
   * Advice

---

## 📂 Project Structure

```
Skin_detection/
│
├── dataset/              # Organized dataset
├── model/                # Trained model (skin_model.h5)
├── app.py                # Streamlit application
├── train_model.py        # Model training script
├── organize_data.py      # Dataset organizer
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd Skin_detection
```

### 2️⃣ Create virtual environment

```
py -3.11 -m venv venv
```

### 3️⃣ Activate environment

```
.\venv\Scripts\Activate.ps1
```

### 4️⃣ Install dependencies

```
python -m pip install numpy==1.23.5
python -m pip install tensorflow==2.15
python -m pip install pandas==1.5.3
python -m pip install scipy==1.10.1
python -m pip install opencv-python==4.7.0.72 --no-deps
python -m pip install pillow
python -m pip install streamlit
```

### 5️⃣ Run the application

```
python -m streamlit run app.py
```

---

## 🎯 Model Performance

The model is evaluated using validation data and achieves good accuracy depending on dataset size and training.

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.
It is not a substitute for professional medical diagnosis.

---

## 🚀 Future Improvements

* 🔥 Grad-CAM (highlight affected area)
* 📱 Mobile app version
* 📊 Better UI/UX
* 🧠 Higher accuracy models

---

## 🧑‍💻 Author

Developed as a Machine Learning project.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
