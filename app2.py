import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np
import speech_recognition as sr

def recognize_speech():
    """Capture audio and recognize speech."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            st.success(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            st.error("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            st.error("Could not request results from Google Speech Recognition service.")
            return None

def parse_voice_command(command):
    """Parse the command into numbers and operation."""
    try:
        if "plus" in command:
            operation = "Add"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        elif "minus" in command:
            operation = "Subtract"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        elif "multiply" in command:
            operation = "Multiply"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        elif "divide" in command:
            operation = "Divide"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        elif "sine" in command:
            operation = "Sine"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        elif "cosine" in command:
            operation = "Cosine"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        elif "tangent" in command:
            operation = "Tangent"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        elif "log" in command:
            operation = "Logarithm (base 10)"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        elif "square root" in command:
            operation = "Square Root"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        elif "power" in command:
            operation = "Power (x^y)"
            numbers = [float(x) for x in command.split() if x.replace('.', '', 1).isdigit()]
        else:
            st.error("Sorry, I did not recognize that operation.")
            return None, None
        
        return operation, numbers
    except Exception as e:
        st.error(f"Error parsing command: {e}")
        return None, None

def scientific_calculator():
    # Green heading for the title
    st.markdown("<h1 style='color: green;'>Scientific Calculator</h1>", unsafe_allow_html=True)
    
    # Displaying an image with specified dimensions (width=300 pixels and height=75 pixels)
    #st.image("https://via.placeholder.com/300x75.png?text=Your+Calculator+Image", width=300, height=75)

    # Displaying your name in blue and italic
    st.markdown("<p style='color: blue; font-style: italic;'>Created by Zulfiqar Ali Mir</p>", unsafe_allow_html=True)

    # Initialize session state for history
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Voice input button
    if st.button("Speak"):
        command = recognize_speech()
        if command:
            operation, numbers = parse_voice_command(command)
            if operation and numbers:
                # Calculate based on parsed input
                perform_calculation(operation, numbers)

    operation = st.selectbox("Select operation", [
        "Add", "Subtract", "Multiply", "Divide", 
        "Sine", "Cosine", "Tangent", "Logarithm (base 10)", 
        "Square Root", "Power (x^y)", "Graph Function"
    ])

    # Handling single-operand operations
    if operation in ["Sine", "Cosine", "Tangent", "Logarithm (base 10)", "Square Root"]:
        num = st.number_input("Enter the number", value=0.0)
        
        if st.button("Calculate"):
            perform_calculation(operation, [num])

    # Handling two-operand operations
    elif operation in ["Add", "Subtract", "Multiply", "Divide", "Power (x^y)"]:
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)
        
        if st.button("Calculate"):
            perform_calculation(operation, [num1, num2])

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

def perform_calculation(operation, numbers):
    """Perform the calculation based on operation and numbers."""
    try:
        if operation == "Sine":
            result = math.sin(math.radians(numbers[0]))
            calculation = f"sin({numbers[0]}) = {result}"
            st.latex(f"\\text{{sin}}({numbers[0]}) = {result}")
        elif operation == "Cosine":
            result = math.cos(math.radians(numbers[0]))
            calculation = f"cos({numbers[0]}) = {result}"
            st.latex(f"\\text{{cos}}({numbers[0]}) = {result}")
        elif operation == "Tangent":
            result = math.tan(math.radians(numbers[0]))
            calculation = f"tan({numbers[0]}) = {result}"
            st.latex(f"\\text{{tan}}({numbers[0]}) = {result}")
        elif operation == "Logarithm (base 10)":
            result = math.log10(numbers[0])
            calculation = f"log({numbers[0]}) = {result}"
            st.latex(f"\\text{{log}}({numbers[0]}) = {result}")
        elif operation == "Square Root":
            result = math.sqrt(numbers[0])
            calculation = f"√{numbers[0]} = {result}"
            st.latex(f"\\sqrt{{{numbers[0]}}} = {result}")
        elif operation == "Add":
            result = numbers[0] + numbers[1]
            calculation = f"{numbers[0]} + {numbers[1]} = {result}"
            st.latex(f"{numbers[0]} + {numbers[1]} = {result}")
        elif operation == "Subtract":
            result = numbers[0] - numbers[1]
            calculation = f"{numbers[0]} - {numbers[1]} = {result}"
            st.latex(f"{numbers[0]} - {numbers[1]} = {result}")
        elif operation == "Multiply":
            result = numbers[0] * numbers[1]
            calculation = f"{numbers[0]} × {numbers[1]} = {result}"
            st.latex(f"{numbers[0]} \\times {numbers[1]} = {result}")
        elif operation == "Divide":
            if numbers[1] != 0:
                result = numbers[0] / numbers[1]
                calculation = f"{numbers[0]} ÷ {numbers[1]} = {result}"
                st.latex(f"{numbers[0]} \\div {numbers[1]} = {result}")
            else:
                st.markdown("<h2 style='color: red; font-weight: bold; font-size: 24px;'>Cannot divide by zero</h2>", unsafe_allow_html=True)
                return
        elif operation == "Power (x^y)":
            result = math.pow(numbers[0], numbers[1])
            calculation = f"{numbers[0]} ^ {numbers[1]} = {result}"
            st.latex(f"{numbers[0]}
