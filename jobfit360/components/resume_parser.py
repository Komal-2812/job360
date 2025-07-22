import fitz
import docx
import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_sections(text):
    text = text.lower()
    doc = nlp(text)

    name = re.findall(r"name[:\-]?\s*([a-zA-Z ]+)", text)
    email = re.findall(r"[\w\.-]+@[\w\.-]+", text)
    phone = re.findall(r"(\+91[\s-]?[0-9]{10}|[0-9]{10})", text)
    role = re.findall(r"(data analyst|ml engineer|frontend|developer|intern)", text)

    skills_list = ['python', 'sql', 'excel', 'react', 'ml', 'flask', 'tableau']
    skills = [token.text for token in doc if token.text in skills_list]
    education = re.findall(r'(btech|mtech|bachelor|master|phd)', text)
    projects = re.findall(r'project[:\-\s]+([a-zA-Z0-9 \-]+)', text)
    experience = re.findall(r'(intern(?:ship)? at [\w &]+)', text)

    return {
        'name': name[0] if name else '',
        'email': email[0] if email else '',
        'phone': phone[0] if phone else '',
        'role': role[0] if role else '',
        'skills': list(set(skills)),
        'education': list(set(education)),
        'projects': list(set(projects)),
        'experience': list(set(experience))
    }