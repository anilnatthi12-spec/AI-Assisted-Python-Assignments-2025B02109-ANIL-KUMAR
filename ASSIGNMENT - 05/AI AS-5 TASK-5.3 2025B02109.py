"""
File: job_scorer.py
Description: A simple scoring function for job applicants based on objective criteria.
It is intentionally designed to avoid using protected attributes like gender, age, 
or name to mitigate algorithmic bias.
"""

def score_applicant(applicant_data: dict) -> float:
    """
    Calculates a composite score for a job applicant based on experience, 
    education, and skill set match.

    Args:
        applicant_data (dict): A dictionary containing applicant details:
            - 'years_of_experience' (int)
            - 'education_level' (str: 'High School', 'Associate', 'Bachelor', 'Master', 'PhD')
            - 'project_portfolio_score' (int: 0-10, based on portfolio review)

    Returns:
        float: The final weighted score for the applicant.
    """
    
    # -----------------------------------------------------------
    # 1. Define Weighting Constants (Transparency)
    # -----------------------------------------------------------
    # These weights dictate the importance of each feature in the final score.
    WEIGHT_EXPERIENCE = 0.40
    WEIGHT_EDUCATION = 0.35
    WEIGHT_PORTFOLIO = 0.25
    
    TOTAL_WEIGHT = WEIGHT_EXPERIENCE + WEIGHT_EDUCATION + WEIGHT_PORTFOLIO 
    # Must sum to 1.0 (100%) for normalized scoring.

    # -----------------------------------------------------------
    # 2. Score Calculation Components
    # -----------------------------------------------------------

    # Component A: Experience Score (Max 10 points)
    # Assumes max weight is given for 10 or more years of experience.
    years = applicant_data.get('years_of_experience', 0)
    experience_score = min(years, 10) 
    
    # Component B: Education Score (Max 10 points)
    education = applicant_data.get('education_level', 'High School')
    education_map = {
        'High School': 4.0,
        'Associate': 6.0,
        'Bachelor': 8.0,
        'Master': 9.5,
        'PhD': 10.0
    }
    education_score = education_map.get(education, 4.0)

    # Component C: Portfolio Score (Max 10 points)
    # This represents a subjective but skill-based review score (e.g., coding test, design review).
    portfolio_score = applicant_data.get('project_portfolio_score', 0)
    portfolio_score = max(0, min(10, portfolio_score)) # Clamp between 0 and 10

    # -----------------------------------------------------------
    # 3. Final Weighted Score Calculation
    # -----------------------------------------------------------
    
    final_score = (
        (experience_score * WEIGHT_EXPERIENCE) +
        (education_score * WEIGHT_EDUCATION) +
        (portfolio_score * WEIGHT_PORTFOLIO)
    )
    
    # Ensure the score is normalized correctly (max possible score is 10)
    if TOTAL_WEIGHT != 1.0:
        # Safety check for weighting error
        print("Warning: Weights do not sum to 1.0. Score may be non-normalized.")
        
    return round(final_score, 2)


# --- Example Usage ---
applicant_A = {
    "name": "Jane Doe",
    "years_of_experience": 7,
    "education_level": "Master",
    "project_portfolio_score": 9
}

applicant_B = {
    "name": "John Smith",
    "years_of_experience": 4,
    "education_level": "Bachelor",
    "project_portfolio_score": 7
}

print(f"Scoring Applicant {applicant_A['name']}: {score_applicant(applicant_A)}")
print(f"Scoring Applicant {applicant_B['name']}: {score_applicant(applicant_B)}")