import streamlit as st
import PyPDF2
from openai import OpenAI

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def analyze_resume(text):
    skills = ["Python", "Java", "C", "Machine Learning", "AI", "SQL", "IoT", "MATLAB"]
    
    found_skills = [skill for skill in skills if skill.lower() in text.lower()]
    
    if len(found_skills) >= 5:
        level = "Strong Profile 💪"
    elif len(found_skills) >= 3:
        level = "Moderate Profile 👍"
    else:
        level = "Needs Improvement ⚠️" 
    result = f"""
    
✅ Skills Found: {', '.join(found_skills) if found_skills else 'None detected'}

📊 Profile Level: {level}

💪 Strengths:
- Technical background detected
- Project experience present

⚠️ Weaknesses:
- Add more software/IT skills
- Improve formatting and clarity

🎯 Suggested Roles:
- Software Engineer
- Data Analyst
- AI/ML Intern
"""
    return result

if uploaded_file:
    resume_text = extract_text(uploaded_file)

    st.subheader("Resume Preview")
    st.write(resume_text[:1000])

    if st.button("Analyze Resume"):
        result = analyze_resume(resume_text)
        st.subheader("Analysis Result")
        st.write(result)

    # Skill score visualization
    score = len([s for s in ["Python","Java","C","ML","AI","SQL","IoT","MATLAB"] if s.lower() in resume_text.lower()])
    st.progress(score * 10)