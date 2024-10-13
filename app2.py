import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

def apply_theme(dark_mode):
    if dark_mode:
        st.markdown(
            """
            <style>
            body {
                background-color: #121212;
                color: white;
            }
            div.stButton > button {
                background-color: #1e1e1e;
                color: white;
                font-weight: bold;
            }
            h1, h2, h3, p {
                color: white;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <style>
            body {
                background-color: white;
                color: black;
            }
            div.stButton > button {
                background-color: black;
                color: white;
                font-weight: bold;
            }
            h1, h2, h3, p {
                color: black;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

def plot_function(function, x_range):
    x = np.linspace(x_range[0], x_range[1], 100)
    y = eval(function)  # Evaluate the function safely (ensure input is controlled)
    
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, label=f'y = {function}', color='blue')
    plt.title('Graph of the function')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid()
    plt.legend()
    plt.tight_layout()
    
    st.pyplot(plt)

def scientific_calculator():
    # Dark mode toggle
    dark_mode = st.sidebar.checkbox("Enable Dark Mode")
    apply_theme(dark_mode)

    # Green heading for the title
    st.markdown("<h1 style='color: green;'>Scientific Calculator</h1>", unsafe_allow_html=True)
    
    # Displaying an image with specified dimensions (width=300 pixels and height=75 pixels)
    #st.image("https://via.placeholder.com/300x75.png?text=Your+Calculator+Image", width=300, height=75)

    # Displaying your name in blue and italic
    st.markdown("<p style='color: blue; font-style: italic;'>Created by Zulfiqar Ali Mir</p>", unsafe_allow_html=True)

    operation = st.selectbox("Select operation", [
        "Add", "Subtract", "Multiply", "Divide", 
        "Sine", "Cosine", "Tangent", "Logarithm (base 10)", 
        "Square Root", "Power (x^y)", "Plot Function"
    ])

    # Handling single-operand operations
    if operation in ["Sine", "Cosine", "Tangent", "Logarithm (base 10)", "Square Root"]:
        num = st.number_input("Enter the number", value=0.0)
        
        if st.button("Calculate"):
            if operation == "Sine":
                result = math.sin(math.radians(num))
                st.latex(f"\\text{{sin}}({num}) = {result}")
            elif operation == "Cosine":
                result = math.cos(math.radians(num))
                st.latex(f"\\text{{cos}}({num}) = {result}")
            elif operation == "Tangent":
                result = math.tan(math.radians(num))
                st.latex(f"\\text{{tan}}({num}) = {result}")
            elif operation == "Logarithm (base 10)":
                result = math.log10(num)
                st.latex(f"\\text{{log}}({num}) = {result}")
            elif operation == "Square Root":
                result = math.sqrt(num)
                st.latex(f"\\sqrt{{{num}}} = {result}")

    # Handling two-operand operations
    elif operation in ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)"]:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)
        
        if st.button("Calculate"):
            if operation == "Add":
                result = num1 + num2
                st.latex(f"{num1} + {num2} = {result}")
            elif operation == "Subtract":
                result = num1 - num2
                st.latex(f"{num1} - {num2} = {result}")
            elif operation == "Multiply":
                result = num1 * num2
                st.latex(f"{num1} \\times {num2} = {result}")
            elif operation == "Divide":
                if num2 != 0:
                    result = num1 / num2
                    st.latex(f"{num1} \\div {num2} = {result}")
                else:
                    st.markdown("<h2 style='color: red; font-weight: bold; font-size: 24px;'>Cannot divide by zero</h2>", unsafe_allow_html=True)
            elif operation == "Power (x^y)":
                result = math.pow(num1, num2)
                st.latex(f"{num1} ^ {num2} = {result}")

    # Handling plotting of a mathematical function
    elif operation == "Plot Function":
        function = st.text_input("Enter a mathematical function of x (e.g., np.sin(x), x**2, np.log(x))", value="np.sin(x)")
        x_min = st.number_input("Enter minimum x value", value=-10.0)
        x_max = st.number_input("Enter maximum x value", value=10.0)
        
        if st.button("Plot"):
            plot_function(function, (x_min, x_max))

# Running the app
if __name__ == "__main__":
    scientific_calculator()
