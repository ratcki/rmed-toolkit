import streamlit as st
from multiapp import MultiApp
from pages import etco2_calculator

# Initialize the multi-page app
app = MultiApp()

# Add pages
app.add_app("Home", lambda: st.write("Welcome to R MED toolkits"))
app.add_app("EtCO2 Target Calculator", etco2_calculator.app)
app.run()