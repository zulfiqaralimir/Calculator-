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

    # Handling single-operand operations
    if operation in ["Sine", "Cosine", "Tangent", "Logarithm (base 10)", "Square Root"]:
        num = st.number_input("Enter the number", value=0.0)
        
        if st.button("Calculate"):
            if operation == "Sine":
                st.write(f"sin({num}) = {math.sin(math.radians(num))}")
            elif operation == "Cosine":
                st.write(f"cos({num}) = {math.cos(math.radians(num))}")
            elif operation == "Tangent":
                st.write(f"tan({num}) = {math.tan(math.radians(num))}")
            elif operation == "Logarithm (base 10)":
                st.write(f"log({num}) = {math.log10(num)}")
            elif operation == "Square Root":
                st.write(f"√{num} = {math.sqrt(num)}")
    
    # Handling two-operand operations
    else:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)
        
        if st.button("Calculate"):
            if operation == "Add":
                st.write(f"{num1} + {num2} = {num1 + num2}")
            elif operation == "Subtract":
                st.write(f"{num1} - {num2} = {num1 - num2}")
            elif operation == "Multiply":
                st.write(f"{num1} * {num2} = {num1 * num2}")
            elif operation == "Divide":
                if num2 != 0:
                    st.write(f"{num1} / {num2} = {num1 / num2}")
                else:
                    st.write("Cannot divide by zero")
            elif operation == "Power (x^y)":
                st.write(f"{num1}^{num2} = {math.pow(num1, num2)}")

# Running the app
if __name__ == "__main__":
    scientific_calculator()
