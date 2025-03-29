def convert_drug_dose(drug_mg, volume_ml, body_weight_kg, infusion_rate_ml_per_hr):
    """
    Convert drug dose from mg and volume to mcg/kg/min.

    Parameters:
        drug_mg (float): Drug amount in mg.
        volume_ml (float): Volume in ml.
        body_weight_kg (float): Patient body weight in kg.
        infusion_rate_ml_per_hr (float): Infusion rate in ml/hr.

    Returns:
        float: Dose in mcg/kg/min.
    """
    # Calculate concentration in mg/ml
    concentration_mg_per_ml = drug_mg / volume_ml

    # Convert concentration from mg/ml to mcg/ml
    concentration_mcg_per_ml = concentration_mg_per_ml * 1000

    # Calculate dose in mcg/kg/min
    dose_mcg_per_kg_per_min = (infusion_rate_ml_per_hr * concentration_mcg_per_ml) / (body_weight_kg * 60)

    return dose_mcg_per_kg_per_min

def calculate_infusion_rate(dose_mcg_per_kg_per_min, drug_mg, volume_ml, body_weight_kg):
    """
    calculate infusion rate in ml/hr from dose in mcg/kg/min.

    Parameters:
        dose_mcg_per_kg_per_min (float): Dose in mcg/kg/min.
        drug_mg (float): Drug amount in mg.
        volume_ml (float): Volume in ml.
        body_weight_kg (float): Patient body weight in kg.

    Returns:
        float: Infusion rate in ml/hr.
    """
    # Calculate concentration in mg/ml
    concentration_mg_per_ml = drug_mg / volume_ml

    # Convert concentration from mg/ml to mcg/ml
    concentration_mcg_per_ml = concentration_mg_per_ml * 1000

    # Reverse calculate infusion rate in ml/hr
    infusion_rate_ml_per_hr = (dose_mcg_per_kg_per_min * body_weight_kg * 60) / concentration_mcg_per_ml

    return infusion_rate_ml_per_hr

import streamlit as st
st.title("Drug Dose Converter")

# Input fields
col1, col2 = st.columns(2)

with col1:
    drug_mg = st.number_input("Drug Amount (mg)", min_value=1, step=1, value=8)
    volume_ml = st.number_input("Volume (ml)", min_value=0, step=1, value=125)

with col2:
    body_weight_kg = st.number_input("Body Weight (kg)", min_value=1.0, step=1.0, value=60.0)
    infusion_rate_ml_per_hr = st.number_input("Infusion Rate (ml/hr)", min_value=0, step=1, value=20)


# Display results
st.subheader("Results")
try:
    col1, col2 = st.columns(2)
    with col1:
        current_dose = convert_drug_dose(drug_mg, volume_ml, body_weight_kg, infusion_rate_ml_per_hr)
        st.write(f"**Current Dose:** `{current_dose:.2f} mcg/kg/min`")

    with col2:
        # Calculate infusion rate for a dose of 0.1 mcg/kg/min
        infusion_rate = calculate_infusion_rate(0.1, drug_mg, volume_ml, body_weight_kg)
        st.write(f"**Dose 0.1 mcg/kg/min:** `{infusion_rate:.2f} ml/hr`")
        # Calculate infusion rate for a dose of 0.25 mcg/kg/min
        infusion_rate = calculate_infusion_rate(0.25, drug_mg, volume_ml, body_weight_kg)
        st.write(f"**Dose 0.25 mcg/kg/min:** `{infusion_rate:.2f} ml/hr`")
        # Calculate infusion rate for a dose of 2 mcg/kg/min
        infusion_rate = calculate_infusion_rate(2, drug_mg, volume_ml, body_weight_kg)
        st.write(f"**Dose 2 mcg/kg/min:** `{infusion_rate:.2f} ml/hr`")
except ZeroDivisionError:
    st.error("Error: Division by zero. Please check your inputs.")

# Display the formula for dose calculation
st.subheader("Equations")
st.latex(r"Concentration \, (mcg/ml) = \frac{Drug \, Amount \, (mg)}{Volume \, (ml)} \times 1000")
st.latex(r"Dose \, (mcg/kg/min) = \frac{Infusion \, Rate \, (ml/hr) \times Concentration \, (mcg/ml)}{Body \, Weight \, (kg) \times 60}")
