# Job Matches Page
import streamlit as st
import pandas as pd
from components.linkedin_scraper import scrape_jobs
from components.match_score import calculate_match

st.set_page_config(page_title="Job Matches", layout="wide")
st.title("💼 Matched Jobs Based on Your Resume")

# Check if resume is available in session
if "resume_data" not in st.session_state:
    st.warning("⚠️ Please upload your resume first from the 'Upload Resume' page.")
else:
    parsed_data = st.session_state["resume_data"]

    st.info("🔎 Searching for jobs that match your skills...")

    # Get job matches based on parsed resume data
    job_df = scrape_jobs(parsed_data)

    if job_df.empty:
        st.warning("😕 No matching jobs found. Try adding more skills or updating your resume.")
    else:
        st.success(f"🎯 {len(job_df)} jobs found matching your skills!")

        # Calculate match score
        match_scores = calculate_match(parsed_data["skills"], job_df["title"])
        job_df["Match Score (%)"] = [score["match_score"] for score in match_scores]

        # Show job cards
        for _, row in job_df.iterrows():
            st.markdown(f"""
                <div class="job-card">
                    <h4>💼 {row['title']}</h4>
                    <p>
                        <b>🏢 Company:</b> {row['company']}<br>
                        <b>📍 Location:</b> {row['location']}<br>
                        <b>📊 Match Score:</b> {row['Match Score (%)']}%
                    </p>
                    <a href="{row['job_link']}" target="_blank">🔗 Apply Now</a>
                </div>
            """, unsafe_allow_html=True)

        # Download as CSV
        st.download_button(
            label="📥 Download Job Matches as CSV",
            data=job_df.to_csv(index=False),
            file_name="job_matches.csv",
            mime="text/csv"
        )
