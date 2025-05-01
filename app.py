
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SeedTime Capital - ThriveFund", layout="wide")

with open("index.html", "r") as f:
    html_content = f.read()

components.html(html_content, height=2800, scrolling=True)
