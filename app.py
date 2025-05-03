import streamlit as st
import joblib
import numpy as np
import time
import pandas as pd

# Load trained model
model = joblib.load('sales_prediction_model.pkl')

# Page Configuration
st.set_page_config(page_title="Sales Prediction App 📈", page_icon="📊", layout="centered")

# Sidebar
st.sidebar.title("📊 About This App")
st.sidebar.info("""
This app predicts **product sales** based on your advertising budget across:
- 📺 TV
- 📻 Radio
- 🗞️ Newspaper  

The prediction model used here is a **Random Forest Regressor**.
""")

# Main Title
st.title("📈 Sales Prediction App")
st.markdown("Predict how much your product will sell based on your advertising budget!")

st.markdown("---")

# Input fields
st.header("📝 Enter your advertising budget:")

col1, col2 = st.columns(2)

with col1:
    tv = st.number_input('📺 TV Advertising Spend ($)', min_value=0.0, value=50.0, step=1.0)

with col2:
    radio = st.number_input('📻 Radio Advertising Spend ($)', min_value=0.0, value=25.0, step=1.0)

newspaper = st.slider('🗞️ Newspaper Advertising Spend ($)', 0.0, 100.0, 10.0, 1.0)

st.markdown("---")

# Prediction button
if st.button('🚀 Predict Sales'):
    with st.spinner('Calculating prediction...'):
        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
            
        input_df = pd.DataFrame({'TV': [tv],'Radio': [radio], 'Newspaper': [newspaper]})
        prediction = model.predict(input_df)
   
    st.success(f'🎯 Predicted Sales: **{prediction[0]:.2f} units**')

# Footer
st.markdown("---")
st.markdown("Made by Arin Talavadekar using Streamlit")

