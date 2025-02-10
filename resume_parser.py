import pdfplumber
import re

def parse_resume(filepath):
    with pdfplumber.open(filepath) as pdf:
        text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    
    name_match = re.search(r'([A-Z][a-z]+\s[A-Z][a-z]+)', text)
    name = name_match.group(0) if name_match else "Unknown"
    
    skills = ["Python", "Machine Learning", "Data Science", "NLP", "Flask"]
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    
    return {"name": name, "skills": found_skills}
