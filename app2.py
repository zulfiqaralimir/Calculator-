import streamlit as st
import math

def scientific_calculator():
    # Initialize session state variables if they don't exist
    if 'num1' not in st.session_state:
        st.session_state.num1 = 0
    if 'num2' not in st.session_state:
        st.session_state.num2 = 0

    # Green heading for the title
    st.markdown("<h1 style='color: green;'>Scientific Calculator</h1>", unsafe_allow_html=True)
    
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

    # Input area
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input("Num 1", value=st.session_state.num1, step=1.0, key="num1")
    with col2:
        num2 = st.number_input("Num 2", value=st.session_state.num2, step=1.0, key="num2")
    with col3:
        operation = st.selectbox("Operation", [
            "Add", "Subtract", "Multiply", "Divide", 
            "Sine", "Cosine", "Tangent", "Logarithm", 
            "Square Root", "Power"
        ], key="operation")
    
    # Button grid to simulate a calculator
    st.write("### Calculator")
    calc_layout = st.columns([1,1,1,1])
    
    # First row (Numbers 7, 8, 9)
    with calc_layout[0]:
        if st.button("7"):
            st.session_state.num1 = 7
    with calc_layout[1]:
        if st.button("8"):
            st.session_state.num1 = 8
    with calc_layout[2]:
        if st.button("9"):
            st.session_state.num1 = 9
    
    # Second row (Numbers 4, 5, 6)
    with calc_layout[0]:
        if st.button("4"):
            st.session_state.num1 = 4
    with calc_layout[1]:
        if st.button("5"):
            st.session_state.num1 = 5
    with calc_layout[2]:
        if st.button("6"):
            st.session_state.num1 = 6

    # Third row (Numbers 1, 2, 3)
    with calc_layout[0]:
        if st.button("1"):
            st.session_state.num1 = 1
    with calc_layout[1]:
        if st.button("2"):
            st.session_state.num1 = 2
    with calc_layout[2]:
        if st.button("3"):
            st.session_state.num1 = 3

    # Zero and calculate button
    with calc_layout[0]:
        if st.button("0"):
            st.session_state.num1 = 0
    with calc_layout[3]:
        if st.button("Calculate"):
            if operation == "Add":
                result = st.session_state.num1 + st.session_state.num2
            elif operation == "Subtract":
                result = st.session_state.num1 - st.session_state.num2
            elif operation == "Multiply":
                result = st.session_state.num1 * st.session_state.num2
            elif operation == "Divide":
                result = st.session_state.num1 / st.session_state.num2 if st.session_state.num2 != 0 else "Error: Division by zero"
            elif operation == "Sine":
                result = math.sin(math.radians(st.session_state.num1))
            elif operation == "Cosine":
                result = math.cos(math.radians(st.session_state.num1))
            elif operation == "Tangent":
                result = math.tan(math.radians(st.session_state.num1))
            elif operation == "Logarithm":
                result = math.log10(st.session_state.num1)
            elif operation == "Square Root":
                result = math.sqrt(st.session_state.num1)
            elif operation == "Power":
                result = math.pow(st.session_state.num1, st.session_state.num2)

            st.write(f"**Result: {result}**")

if __name__ == "__main__":
    scientific_calculator()
