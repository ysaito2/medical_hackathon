import streamlit as st
import numpy as np
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

image = Image.open('sunrise.jpg')

st.image(image, caption='Sunrise by the mountains')


st.title('メディカルサーチ')
st.subheader("病院診断実績から良い病院を見つける")
image = Image.open('images/front_page.png')
st.image(image)

st.subheader("病院診断実績から良い病院を見つける")
for_medical = st.button("患者様")
for_patients = st.button("医療関係者様")

if for_medical:
    switch_page('患者様')

if for_patients:
    switch_page('医療関係者様')
