import streamlit as st

def app():
    st.title("EtCO2 Target Calculator")
    
    # Input fields
    col1, col2= st.columns(2)
    with col1:
        etco2 = st.number_input("Current EtCO2 (mmHg)", min_value=0.0, step=1.0, value=35.0, format="%.1f")
    with col2:
        paco2 = st.number_input("Current PaCO2 (mmHg)", min_value=0.0, step=1.0, value=40.0, format="%.1f")
    with col1:
        ph = st.number_input("Current pH", min_value=0.0, step=0.01, value=7.4, format="%.2f")
    with col2:
        vt = st.number_input("Tidal volume (mL)", min_value=10.0, step=10.0, value=300.0, format="%.1f")

    ph_target = st.number_input("Target pH", min_value=0.0, step=0.01, value=7.4, format="%.2f", help="Enter the desired target pH value")

    # Display equations
    st.subheader("Equations")
    st.latex(r"\frac{VD}{VT} = \frac{PaCO_2 - EtCO_2}{PaCO_2}")
    st.latex(r"\Delta \text{pH} = 0.08 \times \left( \frac{PaCO_2 - 40}{10} \right) \quad \text{(Acute)}")

    # Calculate the target EtCO2 by target pH
    # Input: EtCO2, PaCO2, pH, target pH and tidal volume
    # Output: target EtCO2, Vd/Vt, Vd

    delta_pH = ph_target - ph
    paco2_target = paco2 - ((delta_pH * 10) / 0.08)
    vd_vt = (paco2 - etco2) / paco2
    vd = vd_vt * vt
    etco2_target = paco2_target - (vd_vt * paco2_target)

    # Display results
    st.subheader("Results")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"**Target PaCO2:** `{paco2_target:.2f} mmHg`")
    with col2:
        st.write(f"**Target EtCO2:** `{etco2_target:.2f} mmHg`")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.write(f"Delta pH: {delta_pH:.2f}")
    with col2:
        st.write(f"Vd/Vt: {vd_vt:.2f}")
    with col3:
        st.write(f"Vd: {vd:.2f} mL")
    


