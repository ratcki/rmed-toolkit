import streamlit as st

# Function to calculate target EtCO2
# This function takes EtCO2, PaCO2, pH, target pH, and tidal volume as inputs
# and calculates the target PaCO2, target EtCO2, Vd/Vt, and Vd.
def calculate_target_etco2(paco2, etco2, ph, target_ph, vt):
    """
    Calculate target EtCO2 and other parameters based on input values.
    Parameters:
    - paco2 (float): PaCO2 in mmHg.
    - etco2 (float): EtCO2 in mmHg.
    - ph (float): pH value.
    - target_ph (float): Target pH value.
    - vt (float): Tidal volume in mL.
    Returns:
    - paco2_target (float): Target PaCO2 in mmHg.
    - etco2_target (float): Target EtCO2 in mmHg.
    - vd_vt (float): Vd/Vt ratio.
    - vd (float): Dead space volume in mL.
    """
    delta_pH = target_ph - ph
    paco2_target = paco2 - ((delta_pH * 10) / 0.08)
    vd_vt = (paco2 - etco2) / paco2
    vd = vd_vt * vt
    etco2_target = paco2_target - (vd_vt * paco2_target)
    return paco2_target, etco2_target, vd_vt, vd

st.title("EtCO2 Target Calculator")

# Input fields
col1, col2= st.columns(2)
with col1:
    etco2 = st.number_input("EtCO2 (mmHg)", min_value=0.0, step=1.0, value=35.0, format="%.1f")
    ph = st.number_input("pH", min_value=0.0, step=0.01, value=7.4, format="%.2f")
with col2:
    paco2 = st.number_input("PaCO2 (mmHg)", min_value=0.0, step=1.0, value=40.0, format="%.1f")
    vt = st.number_input("Tidal volume (mL)", min_value=10.0, step=10.0, value=300.0, format="%.1f")

ph_target = st.number_input("Target pH", min_value=0.0, step=0.01, value=7.25, format="%.2f", help="Enter the desired target pH value")

# Display equations
st.subheader("Equations")
st.latex(r"\frac{VD}{VT} = \frac{PaCO_2 - EtCO_2}{PaCO_2}")
st.latex(r"\Delta \text{pH} = 0.08 \times \left( \frac{PaCO_2 - 40}{10} \right) \quad \text{(Acute)}")

# Display results
st.subheader("Results")
try:
    paco2_target, etco2_target, vd_vt, vd = calculate_target_etco2(paco2, etco2, ph, ph_target, vt)
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**Target PaCO2:** `{paco2_target:.2f} mmHg`")
        st.write(f"**Target EtCO2:** `{etco2_target:.2f} mmHg`")

    with col2:
        st.write(f"Vd/Vt: {vd_vt:.2f}")
        st.write(f"Vd: {vd:.2f} mL")
except ZeroDivisionError:
    st.error("Error: Division by zero. Please check your inputs.")

# References
st.caption("Reference: Kallet RH. The Physiologic Basis of Mechanical Ventilation. In: Tobin MJ, editor. Principles and Practice of Mechanical Ventilation. 3rd ed. New York: McGraw-Hill; 2013. p. 1-20.")