import pandas as pd

def scrape_jobs(parsed_resume):
    skills = parsed_resume.get('skills', [])
    job_db = [
        {"title": "Data Analyst", "company": "TCS", "location": "Mumbai", "job_link": "https://linkedin.com/job/1"},
        {"title": "Python Developer", "company": "Infosys", "location": "Bangalore", "job_link": "https://linkedin.com/job/2"},
        {"title": "Frontend Intern", "company": "StartupX", "location": "Remote", "job_link": "https://linkedin.com/job/3"},
    ]
    df = pd.DataFrame(job_db)
    return df[df['title'].str.lower().apply(lambda x: any(skill in x for skill in skills))]