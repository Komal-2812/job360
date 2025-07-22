import streamlit as st
from pathlib import Path
import os

# Optional: Load external CSS for styling
def local_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ CSS file not found: {file_name}")

# 🌙 Theme Toggle
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# Set page metadata
st.set_page_config(page_title="JobFit360", layout="wide", page_icon="📄")

# Apply Theme Styles
if st.session_state.dark_mode:
    st.markdown("""
        <style>
        html, body, [class*="css"] {
            background-color: #121212 !important;
            color: #f5f5f5 !important;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
        }
        a { color: #00f2fe !important; }
        .job-card, .info-box {
            background-color: #1e1e1e !important;
            color: #f0f0f0 !important;
            border: 1px solid #333 !important;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        html, body, [class*="css"] {
            background-color: #ffffff !important;
            color: #2c3e50 !important;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #2c3e50;
        }
        a { color: #0073b1 !important; }
        </style>
    """, unsafe_allow_html=True)


# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/6195/6195700.png", width=80)
st.sidebar.title("🔧 Settings")
st.sidebar.button("🌗 Toggle Dark Mode", on_click=toggle_theme)
st.sidebar.markdown("---")
st.sidebar.markdown("**💬 Quick Guide:**")
st.sidebar.info("""
1. Upload your resume  
2. Get parsed skills & experience  
3. View your resume ATS score  
4. Find matched jobs & download
""")

# Main
st.title("📄 JobFit360")
st.markdown("""
Welcome to **JobFit360** — your AI-powered resume matcher and job finder.  
Start by uploading your resume and navigate using the menu on the left.
""")

# Call to Action
st.markdown("👉 Use the **Upload Resume** page to begin analyzing your resume and explore job matches!")

# Optional: Center image or animation
st.image("https://cdn-icons-png.flaticon.com/512/3557/3557740.png", width=200)
