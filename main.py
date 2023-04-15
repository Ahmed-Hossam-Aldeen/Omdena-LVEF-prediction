import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO
import cv2

st.markdown("<h1 style='text-align: center; color: white;'>🎆Omdena LVEF prediction 🎆</h1>", unsafe_allow_html=True)

with st.expander("Instructions"):
     st.markdown('Insert how to use this application')
###########################################################################################

option = st.selectbox('Approach',("Upload ES and ED images", "Upload video")) 

# Function to preprocess image for prediction
def preprocess_image(image):
    image = cv2.resize(np.array(image), (224, 224))
    image = image / 255.0
    return image

# Function to preprocess video for prediction
def preprocess_video(video):
    video = cv2.cvtColor(np.array(video), cv2.COLOR_RGB2BGR)
    video = cv2.resize(video, (224, 224))
    video = video / 255.0
    video = np.expand_dims(video, axis=0)
    return video


if option == "Upload ES and ED images":
     # File upload for images
     image_files = st.file_uploader("Upload 2 Images", type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)

     # Image prediction
     if image_files is not None and len(image_files) == 2:
        images = [Image.open(image_file) for image_file in image_files]
        images = [preprocess_image(image) for image in images]

        # Display images
        col1, col2 = st.columns(2)
        col1.header("Image 1")
        col1.image(images[0], use_column_width=True)
        col2.header("Image 2")
        col2.image(images[1], use_column_width=True)

        #### prediction
        dummy_prediction = 56
        st.write("Ejection Fraction (EF) Prediction: {:.2f}%".format(dummy_prediction))


else:
     video_file = st.file_uploader("Upload a Video", type=['mp4', 'avi'])
     print(type(video_file))
     if video_file is not None:
          st.video(video_file, format="video/avi")
          dummy_prediction = 56
          st.write("Ejection Fraction (EF) Prediction: {:.2f}%".format(dummy_prediction))