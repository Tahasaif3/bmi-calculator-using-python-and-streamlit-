import streamlit as st

#Title of the web app
st.title("BMI Calculator");

#Input Fields for Weight and Height
height = st.number_input("Enter your height in meters (e.g.,1.85):", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight in kilograms (e.g.,80):", min_value=0.0, format="%.2f")

# Calculator BMI
if st.button("Calculate BMI"):
  if height == 0 or weight == 0:
    st.warning("Please enter valid height and weight values.")
  else: bmi = weight / (height ** 2)
  st.write(f"Your BMI is: {bmi:.2f}")

  # BMI Category
  if bmi < 18.5:
    st.write("You are underweight.")
  elif 18.5 <= bmi < 24.9:
    st.write("Your weight is normal.")
  elif 25 <= bmi < 29.9:
    st.write("You are overweight.")
  else:
    st.write("You are obese or severely obese.");
else :
    st.error("Please enter valid height and weight values.")
      
