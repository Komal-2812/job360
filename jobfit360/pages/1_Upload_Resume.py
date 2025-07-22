# Upload Resume Page
import streamlit as st
from components.resume_parser import extract_text_from_pdf, extract_text_from_docx, extract_sections

st.set_page_config(page_title="Upload Resume", layout="centered")

st.title('📤 Upload Resume')

st.markdown("""
Welcome to **JobFit360**!  
Upload your resume below in **PDF** or **DOCX** format.  
We’ll extract key info like skills, experience, and contact details ✨
""")

uploaded_file = st.file_uploader("📄 Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")

    with st.spinner("🔍 Extracting resume content..."):
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_docx(uploaded_file)

        parsed_data = extract_sections(text)
        st.session_state['resume_data'] = parsed_data

    st.markdown("---")
    st.subheader("📋 Parsed Resume Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**👤 Name:** {parsed_data.get('name', 'Not Found')}")
        st.markdown(f"**📧 Email:** {parsed_data.get('email', 'Not Found')}")
        st.markdown(f"**📞 Phone:** {parsed_data.get('phone', 'Not Found')}")
        st.markdown(f"**🎯 Role:** {parsed_data.get('role', 'Not Found')}")

    with col2:
        st.markdown(f"**🎓 Education:** {', '.join(parsed_data.get('education', [])) or 'N/A'}")
        st.markdown(f"**💼 Experience:** {', '.join(parsed_data.get('experience', [])) or 'N/A'}")
        st.markdown(f"**🛠 Skills:** {', '.join(parsed_data.get('skills', [])) or 'N/A'}")
        st.markdown(f"**📁 Projects:** {', '.join(parsed_data.get('projects', [])) or 'N/A'}")

    st.success("✅ Resume data stored! Use the left menu to view your ATS Score or Matched Jobs.")
else:
    st.info("👈 Upload your resume above to begin analysis.")
