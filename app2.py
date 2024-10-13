import streamlit as st
import math

def scientific_calculator():
    # Green heading for the title
    st.markdown("<h1 style='color: green;'>Scientific Calculator</h1>", unsafe_allow_html=True)
    
    # Displaying an image (replace with your image URL or path)
    st.image("https://png.pngtree.com/png-vector/20221019/ourmid/pngtree-image-calculator-png-image_6352778.png", use_column_width=True)

    # Displaying your name in blue and italic
    st.markdown("<p style='color: blue; font-style: italic;'>Created by Zulfiqar Ali Mir</p>", unsafe_allow_html=True)
    
    # Style the button with black background and white bold text
    st.markdown(
        """
        <style>
        div.stButton > button {
            background-color: black;
            color: white;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True
    )

    operation = st.selectbox("Select operation", [
        "Add", "Subtract", "Multiply", "Divide", 
        "Sine", "Cosine", "Tangent", "Logarithm (base 10)", 
        "Square Root", "Power (x^y)"
    ])

    # Handling single-operand operations
    if operation in ["Sine", "Cosine", "Tangent", "Logarithm (base 10)", "Square Root"]:
        num = st.number_input("Enter the number", value=0.0)
        
        if st.button("Calculate"):
            if operation == "Sine":
                result = math.sin(math.radians(num))
                st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>sin({num}) = {result}</h2>", unsafe_allow_html=True)
            elif operation == "Cosine":
                result = math.cos(math.radians(num))
                st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>cos({num}) = {result}</h2>", unsafe_allow_html=True)
            elif operation == "Tangent":
                result = math.tan(math.radians(num))
                st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>tan({num}) = {result}</h2>", unsafe_allow_html=True)
            elif operation == "Logarithm (base 10)":
                result = math.log10(num)
                st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>log({num}) = {result}</h2>", unsafe_allow_html=True)
            elif operation == "Square Root":
                result = math.sqrt(num)
                st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>√{num} = {result}</h2>", unsafe_allow_html=True)
    
    # Handling two-operand operations
    else:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)
        
        if st.button("Calculate"):
            if operation == "Add":
                result = num1 + num2
                st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>{num1} + {num2} = {result}</h2>", unsafe_allow_html=True)
            elif operation == "Subtract":
                result = num1 - num2
                st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>{num1} - {num2} = {result}</h2>", unsafe_allow_html=True)
            elif operation == "Multiply":
                result = num1 * num2
                st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>{num1} * {num2} = {result}</h2>", unsafe_allow_html=True)
            elif operation == "Divide":
                if num2 != 0:
                    result = num1 / num2
                    st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>{num1} / {num2} = {result}</h2>", unsafe_allow_html=True)
                else:
                    st.markdown("<h2 style='color: red; font-weight: bold; font-size: 24px;'>Cannot divide by zero</h2>", unsafe_allow_html=True)
            elif operation == "Power (x^y)":
                result = math.pow(num1, num2)
                st.markdown(f"<h2 style='color: blue; font-weight: bold; font-size: 24px;'>{num1}^{num2} = {result}</h2>", unsafe_allow_html=True)

# Running the app
if __name__ == "__main__":
    scientific_calculator()
