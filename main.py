import streamlit as st
import tensorflow as tf
import numpy as np

def modelPredict(uploaded_file):
    model = tf.keras.models.load_model("trained_model.h5")
    image = tf.keras.preprocessing.image.load_img(uploaded_file, target_size=(64,64))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    prediction = model.predict(input_arr)
    return np.argmax(prediction)

st.header("Mango Species Predict")

#upload image file
uploaded_file = st.file_uploader("Upload Image")
if uploaded_file is not None:
    st.image(uploaded_file)
else:
    st.write("Please upload an image.")

if(st.button("Predict")):
    # st.write("Prediction is")
    result_index = modelPredict(uploaded_file)
    #reading labels
    with open("labels.txt") as f:
        content = f.readlines()
    label = []
    for i in content:
        label.append(i[:-1])
    st.success('This is {}'.format(label[result_index]))