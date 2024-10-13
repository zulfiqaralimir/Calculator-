import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np

def scientific_calculator():
    # Green heading for the title
    st.markdown("<h1 style='color: green;'>Scientific Calculator</h1>", unsafe_allow_html=True)
    
    # Displaying an image with specified dimensions (width=300 pixels and height=75 pixels)
    st.image("https://via.placeholder.com/300x75.png?text=Your+Calculator+Image", width=300, height=75)

    # Displaying your name in blue and italic
    st.markdown("<p style='color: blue; font-style: italic;'>Created by Zulfiqar Ali Mir</p>", unsafe_allow_html=True)

    # Initialize session state for history
    if 'history' not in st.session_state:
        st.session_state.history = []

    operation = st.selectbox("Select operation", [
        "Add", "Subtract", "Multiply", "Divide", 
        "Sine", "Cosine", "Tangent", "Logarithm (base 10)", 
        "Square Root", "Power (x^y)", "Graph Function"
    ])

    # Handling single-operand operations
    if operation in ["Sine", "Cosine", "Tangent", "Logarithm (base 10)", "Square Root"]:
        num = st.number_input("Enter the number", value=0.0)
        
        if st.button("Calculate"):
            if operation == "Sine":
                result = math.sin(math.radians(num))
                calculation = f"sin({num}) = {result}"
                st.latex(f"\\text{{sin}}({num}) = {result}")
            elif operation == "Cosine":
                result = math.cos(math.radians(num))
                calculation = f"cos({num}) = {result}"
                st.latex(f"\\text{{cos}}({num}) = {result}")
            elif operation == "Tangent":
                result = math.tan(math.radians(num))
                calculation = f"tan({num}) = {result}"
                st.latex(f"\\text{{tan}}({num}) = {result}")
            elif operation == "Logarithm (base 10)":
                result = math.log10(num)
                calculation = f"log({num}) = {result}"
                st.latex(f"\\text{{log}}({num}) = {result}")
            elif operation == "Square Root":
                result = math.sqrt(num)
                calculation = f"√{num} = {result}"
                st.latex(f"\\sqrt{{{num}}} = {result}")

            # Add calculation to history
            st.session_state.history.append(calculation)

    # Handling two-operand operations
    elif operation in ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)"]:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)
        
        if st.button("Calculate"):
            if operation == "Add":
                result = num1 + num2
                calculation = f"{num1} + {num2} = {result}"
                st.latex(f"{num1} + {num2} = {result}")
            elif operation == "Subtract":
                result = num1 - num2
                calculation = f"{num1} - {num2} = {result}"
                st.latex(f"{num1} - {num2} = {result}")
            elif operation == "Multiply":
                result = num1 * num2
                calculation = f"{num1} × {num2} = {result}"
                st.latex(f"{num1} \\times {num2} = {result}")
            elif operation == "Divide":
                if num2 != 0:
                    result = num1 / num2
                    calculation = f"{num1} ÷ {num2} = {result}"
                    st.latex(f"{num1} \\div {num2} = {result}")
                else:
                    st.markdown("<h2 style='color: red; font-weight: bold; font-size: 24px;'>Cannot divide by zero</h2>", unsafe_allow_html=True)
                    return  # Skip history for this operation
            elif operation == "Power (x^y)":
                result = math.pow(num1, num2)
                calculation = f"{num1} ^ {num2} = {result}"
                st.latex(f"{num1} ^ {num2} = {result}")

            # Add calculation to history
            st.session_state.history.append(calculation)

    # Handling graphing capabilities
    elif operation == "Graph Function":
        function_input = st.text_input("Enter a mathematical function (e.g., sin(x), cos(x), x**2)")
        x_values = np.linspace(-10, 10, 400)
        
        if st.button("Plot"):
            try:
                # Safely evaluate the function
                y_values = eval(function_input)
                plt.plot(x_values, y_values)
                plt.title(f'Graph of {function_input}')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.grid()
                st.pyplot(plt)
            except Exception as e:
                st.error(f"Error in function: {e}")

    # Display calculation history
    if st.session_state.history:
        st.markdown("<h2 style='color: blue;'>Calculation History</h2>", unsafe_allow_html=True)
        for calc in st.session_state.history:
            st.write(calc)

# Running the app
if __name__ == "__main__":
    scientific_calculator()
