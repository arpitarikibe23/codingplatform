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

# Backend URL (update with deployed backend)
BACKEND_URL = "https://your-backend-service.onrender.com/run"

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
                # Send code to backend (Ensure the backend URL is correct)
                response = requests.post(BACKEND_URL, json={"code": code}, timeout=10)

                if response.status_code == 200:
                    output = response.json().get("output", "No output received.")
                else:
                    output = f"Error: {response.status_code} - {response.text}"

                # Display output
                st.subheader("📌 Output:")
                st.code(output, language="text")

            except requests.exceptions.RequestException as e:
                st.error(f"⚠️ Could not connect to the backend: {e}")

    else:
        st.warning("⚠️ Please write some Python code before running.")


