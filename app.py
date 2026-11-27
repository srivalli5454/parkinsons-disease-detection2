
import streamlit as st
import numpy as np
from PIL import Image
from ultralytics import YOLO
from pathlib import Path

st.set_page_config(
    page_title="Parkinson's Disease Detection",
    page_icon="",
    layout="centered"
)

st.title("Parkinson's Disease Image Classification")

st.write(
    "Upload a brain image to classify it as Healthy or Parkinson."
)

st.warning(
    "Educational research project only. "
    "This application is not a medical diagnostic tool."
)

MODEL_PATH = Path(__file__).parent / "best.pt"

@st.cache_resource
def load_model():
    return YOLO(str(MODEL_PATH))

if not MODEL_PATH.exists():
    st.error("Trained model best.pt is missing.")
    st.stop()

model = load_model()

uploaded_file = st.file_uploader(
    "Upload a brain image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Predict"):
        with st.spinner("Analyzing image..."):
            results = model.predict(
                image,
                imgsz=224,
                verbose=False
            )

            scores = results[0].probs.data.cpu().numpy()
            names = results[0].names

            healthy_idx = next(
                i for i, name in names.items()
                if name.lower() == "healthy"
            )

            parkinson_idx = next(
                i for i, name in names.items()
                if name.lower() == "parkinson"
            )

            healthy_conf = float(scores[healthy_idx]) * 100
            parkinson_conf = float(scores[parkinson_idx]) * 100

            predicted_idx = int(np.argmax(scores))
            predicted_class = names[predicted_idx]
            predicted_conf = float(scores[predicted_idx]) * 100

        st.subheader("Prediction Results")

        st.success(
            f"Predicted Class: {predicted_class.title()}"
        )

        st.metric(
            "Prediction Confidence",
            f"{predicted_conf:.2f}%"
        )

        st.write(f"Healthy Confidence: {healthy_conf:.2f}%")
        st.progress(healthy_conf / 100)

        st.write(f"Parkinson Confidence: {parkinson_conf:.2f}%")
        st.progress(parkinson_conf / 100)

        st.caption(
            "Confidence scores are model outputs, "
            "not clinically validated probabilities."
        )
