import streamlit as st
import requests
from streamlit_ace import st_ace

# Configure Streamlit page
st.set_page_config(
    page_title="Online Python Compiler",
    page_icon="🐍",
    layout="wide"
)

st.title("🐍 Online Python Compiler")

# Custom CSS for better design
st.markdown(
    """
    <style>
    body { background-color: #E3F2FD; }
    .stTextArea textarea { font-size: 16px; font-family: monospace; }
    .stButton button { background-color: #1E90FF; color: white; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Default Python code template
default_code = '''# Write your Python code here
print("Hello, World!")
'''

# Code editor (using Ace Editor)
code = st_ace(
    value=default_code,
    language="python",
    theme="monokai",
    key="python_editor",
    font_size=16,
    height=300,
    auto_update=True,
)

# Run button
if st.button("▶ Run Code"):
    if code.strip():
        with st.spinner("Running your code..."):
            try:
                # Send code to backend
                response = requests.post("http://127.0.0.1:5000/run", json={"code": code})
                output = response.json().get("output", "Error in execution.")

                # Display output
                st.subheader("📌 Output:")
                st.code(output, language="text")

            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Error connecting to the backend: {e}")
    else:
        st.warning("⚠️ Please write some Python code before running.")

