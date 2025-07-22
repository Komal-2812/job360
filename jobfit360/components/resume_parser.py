import fitz  # PyMuPDF
import docx
import re
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    """Extracts text from uploaded PDF file."""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

def extract_text_from_docx(file):
    """Extracts text from uploaded DOCX file."""
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_sections(text):
    """Extracts structured information from resume text."""
    text = text.lower()
    doc = nlp(text)

    # Basic fields
    name = re.findall(r"name[:\-]?\s*([a-zA-Z ]+)", text)
    email = re.findall(r"[\\w\\.-]+@[\\w\\.-]+", text)
    phone = re.findall(r"(\+91[\s\-]?[0-9]{10}|[0-9]{10})", text)
    role = re.findall(r"(data analyst|ml engineer|frontend|developer|intern|ai engineer)", text)

    # Predefined skills
    skills_list = [
        "python", "java", "c++", "c", "html", "css", "javascript", "react", "node", "express",
        "django", "flask", "mysql", "mongodb", "sqlite", "sql", "excel", "power bi", "tableau",
        "tensorflow", "pytorch", "machine learning", "deep learning", "nlp", "data analysis",
        "data science", "git", "github", "linux", "bash", "cloud", "aws", "azure", "google cloud",
        "rest api", "bootstrap", "kubernetes", "docker"
    ]
    skills = list(set([token.text for token in doc if token.text in skills_list]))

    # Education
    education = re.findall(r"(btech|b\.tech|mtech|m\.tech|bachelor|master|phd)", text)

    # Projects
    projects = re.findall(r"project[:\-\\s]+([a-zA-Z0-9 \-\_]+)", text)

    # Experience
    experience = re.findall(r"(intern(?:ship)? at [\\w &]+|\\d+\\s+years)", text)

    return {
        'name': name[0].strip().title() if name else '',
        'email': email[0] if email else '',
        'phone': phone[0] if phone else '',
        'role': role[0].strip().title() if role else '',
        'skills': skills,
        'education': list(set(education)),
        'projects': list(set(projects)),
        'experience': list(set(experience))
    }
