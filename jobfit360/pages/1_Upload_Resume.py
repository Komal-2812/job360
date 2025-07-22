# Upload Resume Page
import streamlit as st
from components.resume_parser import extract_text_from_pdf, extract_text_from_docx, extract_sections

st.set_page_config(page_title="Upload Resume", layout="wide")
st.title("📤 Upload Your Resume")

st.markdown("""
Welcome to **JobFit360**.  
Upload your resume in **PDF** or **DOCX** format and we’ll extract your:
- 📛 Name, 📧 Email, 📞 Phone  
- 🎓 Education, 🧠 Skills, 💼 Experience  
- 📁 Projects and 🎯 Preferred Role  
""")

uploaded_file = st.file_uploader("📄 Upload your resume", type=["pdf", "docx"])

if uploaded_file:
    st.success("✅ File uploaded successfully.")

    with st.spinner("🔍 Extracting details..."):
        if uploaded_file.type == "application/pdf":
            text = extract_text_from_pdf(uploaded_file)
        else:
            text = extract_text_from_docx(uploaded_file)

        parsed_data = extract_sections(text)
        st.session_state['resume_data'] = parsed_data

    st.markdown("---")
    st.subheader("📋 Resume Summary")

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

    st.success("📌 Resume details saved. Go to the left sidebar ➡ to score or find matching jobs.")

else:
    st.info("👈 Upload your resume to begin. Supported formats: PDF or DOCX")
