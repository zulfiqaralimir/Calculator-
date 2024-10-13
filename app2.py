import streamlit as st
import math

def scientific_calculator():
    # Green heading for the title
    st.markdown("<h1 style='color: green;'>Scientific Calculator</h1>", unsafe_allow_html=True)
    
    # Displaying your name as the creator
    st.write("Created by Zulfiqar Ali Mir")

    operation = st.selectbox("Select operation", [
        "Add", "Subtract", "Multiply", "Divide", 
        "Sine", "Cosine", "Tangent", "Logarithm (base 10)", 
        "Square Root", "Power (x^y)"
    ])

    if op
