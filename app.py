import streamlit as st

def calculator():
    st.title("Simple Calculator")
    operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    if st.button("Calculate"):
        if operation == "Add":
            st.write(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            st.write(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            st.write(f"Result: {num1 * num2}")
        elif operation == "Divide":
            if num2 != 0:
                st.write(f"Result: {num1 / num2}")
            else:
                st.write("Cannot divide by zero")

if __name__ == "__main__":
    calculator()
