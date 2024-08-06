import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Simple Streamlit App")

# Add a slider to the app
slider_value = st.slider("Select a value", 0, 100, 50)

# Generate random data
data = pd.DataFrame(
    np.random.randn(50, 3),
    columns=['a', 'b', 'c']
)

# Multiply data by slider value
data *= slider_value / 50

# Display the dataframe
st.write("Dataframe:")
st.write(data)

# Display a line chart
st.line_chart(data)
