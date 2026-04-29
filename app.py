import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

try:
    with open("model/accuracy.txt", "r") as f:
        accuracy = float(f.read())
    st.info(f"Model Accuracy: {accuracy * 100:.2f}%")
except:
    st.warning("Accuracy not available")
    
# Load model
model = tf.keras.models.load_model("model/skin_model.h5")

# Class names
classes = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']

st.title("Skin Disease Detection System")

uploaded_file = st.file_uploader("Upload Skin Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", width=500)

    # Preprocess
    img = np.array(image)
    img = cv2.resize(img, (128, 128))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    # Prediction
    prediction = model.predict(img)
    class_index = np.argmax(prediction)
    confidence = np.max(prediction)

    st.write("### Prediction:", classes[class_index])
    st.write("### Confidence:", float(confidence))

    # Extra feature (for marks 🔥)
    info = {
        "mel": "⚠️ Serious condition. Consult doctor immediately.",
        "nv": "✅ Generally harmless mole.",
        "bcc": "⚠️ Low risk but needs treatment.",
    }

    st.write("### Advice:", info.get(classes[class_index], "Consult doctor"))