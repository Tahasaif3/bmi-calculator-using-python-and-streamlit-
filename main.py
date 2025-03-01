import streamlit as st

st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            font-size: 18px;
            padding: 10px;
            width: 100%;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #ff1e1e;
            transition: 0.3s;
        }
        .bmi-box {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            color: #333;
            padding: 10px;
            border-radius: 10px;
        }
        .underweight { background-color: #FFD700; }
        .normal { background-color: #4CAF50; color: white; }
        .overweight { background-color: #FF9800; }
        .obese { background-color: #FF4B4B; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("✨ BMI Calculator ✨")
st.write("Enter your details below to calculate your Body Mass Index (BMI).")

height = st.number_input("📏 Enter your height in meters (e.g., 1.75):", min_value=0.1, format="%.2f")
weight = st.number_input("⚖️ Enter your weight in kilograms (e.g., 70):", min_value=0.1, format="%.2f")

if st.button("🚀 Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"✅ Your BMI is: {bmi:.2f}")

        st.progress(min(bmi / 40, 1.0))

        if bmi < 18.5:
            category = "Underweight 😟"
            color_class = "underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal Weight 🎉"
            color_class = "normal"
            st.balloons()
        elif 25 <= bmi < 29.9:
            category = "Overweight 🤔"
            color_class = "overweight"
        else:
            category = "Obese ⚠️"
            color_class = "obese"

        st.markdown(f'<div class="bmi-box {color_class}">{category}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter valid values for height and weight.")
