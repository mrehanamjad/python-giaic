import streamlit as st

def st_bmi(bmi):
    if bmi is None:
        return "Invalid Input", "gray"
    elif bmi < 18.5:
        return "Underweight", "orange"
    elif 18.5 <= bmi < 25:
        return "Normal weight", "green"
    elif 25 <= bmi < 30:
        return "Overweight", "orange"
    else:
        return "Obesity", "red"

def main():
    st.title("⛨ BMI Calculator")
    st.markdown("Calculate your Body Mass Index to assess your weight status.")

    height = st.slider("Enter your height (in cm)", 100, 250, 175)
    weight = st.slider("Enter your weight (in kg)", 40, 200, 70)

    if st.button("Calculate BMI"):
        bmi = weight / ((height/100) ** 2)
        category, color = st_bmi(bmi)

        st.subheader("Results:")
        if bmi is not None:
            st.markdown(f"<p style='font-size: 24px;'>Your BMI is: <span style='color:{color}; font-weight: bold;'>{bmi:.2f}</span></p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 20px;'>Category: <span style='color:{color}; font-weight: bold;'>{category}</span></p>", unsafe_allow_html=True)

            st.info("### BMI Categories ###\n"
                    "- Underweight: BMI less than 18.5\n"
                    "- Normal weight: BMI between 18.5 and 24.9\n"
                    "- Overweight: BMI between 25 and 29.9\n"
                    "- Obesity: BMI 30 or greater")
        else:
            st.warning("Please enter valid height and weight values.")

if __name__ == "__main__":
    main()