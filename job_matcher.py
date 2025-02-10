job_description = "Looking for a Data Scientist with experience in Python, Machine Learning, and NLP."

def match_resume_with_job(parsed_resume):
    job_skills = set(job_description.lower().split())
    resume_skills = set(parsed_resume['skills'])
    
    match_score = (len(resume_skills.intersection(job_skills)) / len(job_skills)) * 100
    return round(match_score, 2)
