import streamlit as st
import speech_recognition as sr
import math

def scientific_calculator():
    # Title and image
    st.markdown("<h1 style='color: green;'>Scientific Calculator</h1>", unsafe_allow_html=True)
    #st.image("https://via.placeholder.com/300x75.png?text=Your+Calculator+Image", width=300, height=75)
    st.markdown("<p style='color: blue; font-style: italic;'>Created by Zulfiqar Ali Mir</p>", unsafe_allow_html=True)

    # Button for voice input
    if st.button("Speak"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.write("Listening...")
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio)
                st.success(f"You said: {command}")
                # Here you can parse the command to perform calculations
            except sr.UnknownValueError:
                st.error("Could not understand audio")
            except sr.RequestError:
                st.error("Could not request results from Google Speech Recognition service")

    # Other calculator functionalities remain the same
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
    else:
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

# Running the app
if __name__ == "__main__":
    scientific_calculator()
