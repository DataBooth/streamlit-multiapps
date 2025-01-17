import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, report_coaches # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Report: Coaches", report_coaches.app)
app.add_app("Data Stats", data_stats.app)

# The main app
app.run()