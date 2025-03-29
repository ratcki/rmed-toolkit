import streamlit as st 

def calculate_creatinine_clearance(weight_kg, age_years, serum_creatinine_mg_dl, gender):
    """
    Calculate creatinine clearance using the Cockcroft-Gault equation.

    Parameters:
    - weight_kg (float): Patient's weight in kilograms.
    - age_years (int): Patient's age in years.
    - serum_creatinine_mg_dl (float): Serum creatinine level in mg/dL.
    - gender (str): Patient's gender, either 'male' or 'female'.

    Returns:
    - float: Estimated creatinine clearance in mL/min.
    """
    if gender.lower() == 'male':
        factor = 1.0
    elif gender.lower() == 'female':
        factor = 0.85
    else:
        raise ValueError("Gender must be 'male' or 'female'.")

    crcl = ((140 - age_years) * weight_kg * factor) / (72 * serum_creatinine_mg_dl)
    return crcl

st.title("Creatinine Clearance Calculator")

# Input fields
col1, col2 = st.columns(2)

with col1:
    weight_kg = st.number_input("Enter weight (kg):", min_value=0.1, step=0.1, value=72.0)
    age_years = st.number_input("Enter age (years):", min_value=1, step=1, value=60)

with col2:
    serum_creatinine_mg_dl = st.number_input("Enter serum creatinine (mg/dL):", min_value=0.1, step=0.01, value=0.8)
    gender = st.selectbox("Select gender:", options=["Male", "Female"])


# Display results
st.subheader("Results")
try:
    crcl = calculate_creatinine_clearance(weight_kg, age_years, serum_creatinine_mg_dl, gender)
    st.write(f"**Estimated Creatinine Clearance:** `{crcl:.2f}` mL/min")
except ValueError as e:
    st.error(str(e))

# Display the Cockcroft-Gault equation using LaTeX
st.subheader("Equations")
st.latex(r"""
\text{Creatinine Clearance (CrCl)} = 
\frac{(140 - \text{Age}) \times \text{Weight (kg)} \times \text{Factor}}
{72 \times \text{Serum Creatinine (mg/dL)}}
""")
st.caption("Where Factor is 1.0 for males and 0.85 for females.")

# References
st.caption("Reference: Cockcroft DW, Gault MH. Prediction of creatinine clearance from serum creatinine. Nephron. 1976;16(1):31-41.")
