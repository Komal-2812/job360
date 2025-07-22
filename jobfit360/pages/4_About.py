# About JobFit360
import streamlit as st

st.set_page_config(page_title="About", layout="centered")
st.title("ℹ️ About JobFit360")

st.markdown("""
Welcome to **JobFit360** — your AI-powered **resume analysis and job matching assistant**.  
Whether you're a **student**, a **job seeker**, or a **recruiter**, this platform helps you:

---

### 💡 Key Features:

- 📤 **Upload your resume** (PDF or DOCX)
- 🧠 **Extract** skills, experience, education, and projects
- 📊 **Get an ATS score** out of 100 based on job relevance
- 💼 **Match jobs** from our smart job suggestion engine
- 📥 **Download a CSV report** of your top matches

---

### 👨‍💻 How It Works:

1. Upload your resume on the **Upload Resume** page  
2. Review your extracted resume details  
3. View your **Resume Score** and optimization tips  
4. Check **matching jobs** with match percentage  
5. Export results to share or apply directly

---

### 🛠️ Technologies Used:

- 🐍 Python
- 🎈 Streamlit (Web UI)
- 📄 PyMuPDF & python-docx (Resume parsing)
- 🤖 spaCy (NLP)
- 📊 Pandas (Data handling)

---

### 🤝 Meet the Creators

Built by aspiring data scientists & developers to help Gen-Z get hired faster!  
🔗 Visit [JobFit360.com](https://jobfit360.com) *(demo link)*  
✉️ Email: support@jobfit360.com

---
""")
