import streamlit as st
import requests
import numpy as np
import pandas as pd



st.markdown("""# MindSee
## Recreating images from MRI scans""")



# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slihe displayed lines

uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])

uploaded_file_name = 'uploaded_file'
