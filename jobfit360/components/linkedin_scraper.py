import pandas as pd

def scrape_jobs(parsed_resume):
    """Mock job scraper that filters sample jobs based on resume skills."""
    # Sample job database
    job_db = [
        {"title": "Data Analyst", "company": "TCS", "location": "Mumbai", "job_link": "https://linkedin.com/job/1"},
        {"title": "Machine Learning Intern", "company": "Infosys", "location": "Remote", "job_link": "https://linkedin.com/job/2"},
        {"title": "Python Developer", "company": "Wipro", "location": "Bangalore", "job_link": "https://linkedin.com/job/3"},
        {"title": "Frontend Developer", "company": "StartUpX", "location": "Remote", "job_link": "https://linkedin.com/job/4"},
        {"title": "Business Analyst", "company": "Accenture", "location": "Hyderabad", "job_link": "https://linkedin.com/job/5"}
    ]

    df = pd.DataFrame(job_db)

    # Filter using skills
    skills = parsed_resume.get("skills", [])
    if not skills:
        return df

    def skill_match(title):
        return any(skill.lower() in title.lower() for skill in skills)

    filtered_df = df[df["title"].apply(skill_match)].reset_index(drop=True)
    return filtered_df
