def calculate_match(resume_skills, job_titles):
    """
    Compare resume skills with job titles and return match % per job.
    """
    match_scores = []
    for title in job_titles:
        matched = sum(1 for skill in resume_skills if skill.lower() in title.lower())
        score = int((matched / len(resume_skills)) * 100) if resume_skills else 0
        match_scores.append({"match_score": score})
    return match_scores


def calculate_resume_score(parsed_data, job_titles):
    """
    Evaluate resume ATS score based on skills, experience, education, projects.
    Returns total score and category-wise breakdown.
    """

    # 1. Skill Match Score (based on overlap with job titles)
    skills = parsed_data.get("skills", [])
    matched_keywords = sum(
        1 for skill in skills for title in job_titles if skill.lower() in title.lower()
    )
    skill_score = min((matched_keywords / len(job_titles)) * 40, 40) if len(job_titles) > 0 else 0

    # 2. Experience Score
    experience_count = len(parsed_data.get("experience", []))
    experience_score = min(experience_count * 10, 20)

    # 3. Education Score
    education_count = len(parsed_data.get("education", []))
    education_score = min(education_count * 10, 20)

    # 4. Projects Score
    projects_count = len(parsed_data.get("projects", []))
    project_score = min(projects_count * 10, 20)

    total_score = skill_score + experience_score + education_score + project_score

    return round(total_score), {
        "Skills": round(skill_score),
        "Experience": round(experience_score),
        "Education": round(education_score),
        "Projects": round(project_score)
    }
