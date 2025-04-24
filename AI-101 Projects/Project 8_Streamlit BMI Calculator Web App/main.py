import streamlit as st
import pandas as pd

st.title("BMI Calculator")

# Height and Weight input
height = st.slider("Enter your height in cm:", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

# BMI Calculation
bmi = weight / ((height / 100) ** 2)

# Show result
st.write(f"Your BMI is {bmi:.2f}")
if bmi < 18.5:
    st.warning("You are underweight.")
elif 18.5 <= bmi < 25:
    st.success("You have a normal weight.")
elif 25 <= bmi < 30:
    st.info("You are overweight.")
else:
    st.error("You are in the obesity range.")


# Interpretation
st.write("- Underweight: BMI less than 18.5")
st.write("- Normal weight: BMI between 18.5 and 24.9")
st.write("- Overweight: BMI between 25 and 29.9")
st.write("- Obesity: BMI 30 or greater")
