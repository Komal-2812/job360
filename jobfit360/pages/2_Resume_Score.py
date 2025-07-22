# Resume Score Page
import streamlit as st
import pandas as pd
import sys
from pathlib import Path
from components.match_score import calculate_resume_score

sys.path.append(str(Path(__file__).resolve().parent.parent))

st.set_page_config(page_title="Resume Score", layout="centered")
st.title("📊 Resume Score Analysis")

# Check if resume data is present
if "resume_data" not in st.session_state:
    st.warning("⚠️ Please upload your resume first from the 'Upload Resume' page.")
else:
    st.success("✅ Resume data found. Calculating ATS score...")

    resume_data = st.session_state["resume_data"]

    # Simulated job titles (replace with scraped titles if needed)
    job_titles = pd.Series([
        "Data Analyst",
        "Machine Learning Engineer",
        "Python Developer",
        "Frontend Developer",
        "Software Engineer"
    ])

    score, breakdown = calculate_resume_score(resume_data, job_titles)

    st.metric(label="📈 Overall Resume ATS Score", value=f"{score} / 100")

    with st.expander("🔍 View Detailed Breakdown"):
        st.markdown("""
        The score is calculated based on:
        - **🧠 Skills Match** with job titles
        - **💼 Experience Count**
        - **🎓 Educational Background**
        - **📁 Project Mentions**
        """)
        for category, val in breakdown.items():
            total = 100 if category == "Skills" else 20
            st.progress(int(val), text=f"{category}: {int(val)} / {total}")

    st.info("🎯 Tip: Add more keywords, relevant projects, or real job titles in your resume to improve this score.")
