import streamlit as st

# Title and styling
st.markdown("<h1 style='text-align: center; color: #ff6f61;'>🏋️‍♂️ BMI Calculator</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📏 Enter Your Details")

# User input fields with custom styling
weight = st.sidebar.number_input("Enter your weight (kg)", min_value=1.0, step=0.1, help="Enter your weight in kilograms (kg)")
height = st.sidebar.number_input("Enter your height (m)", min_value=0.1, step=0.01, help="Enter your height in meters (m)")

# Calculate BMI when the button is pressed
if st.sidebar.button("🔑 Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = weight / (height ** 2)
        st.markdown(f"### Your BMI is: **{bmi:.2f}**", unsafe_allow_html=True)
        
        # Show BMI category with custom text and colors
        if bmi < 18.5:
            st.markdown("<h3 style='color: #ff6347;'>Category: Underweight</h3>", unsafe_allow_html=True)
        elif 18.5 <= bmi < 24.9:
            st.markdown("<h3 style='color: #32cd32;'>Category: Normal weight</h3>", unsafe_allow_html=True)
        elif 25 <= bmi < 29.9:
            st.markdown("<h3 style='color: #ffcc00;'>Category: Overweight</h3>", unsafe_allow_html=True)
        else:
            st.markdown("<h3 style='color: #ff4500;'>Category: Obesity</h3>", unsafe_allow_html=True)
    else:
        st.error("⚠️ Please enter valid weight and height!")
