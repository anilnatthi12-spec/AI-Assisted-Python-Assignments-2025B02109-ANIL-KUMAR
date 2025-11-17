def applicant_score(education, experience, technical_skills, communication, certifications, interview):
    """
    Calculates a weighted score for an applicant based on different criteria.
    Each criterion is normalized to a scale and multiplied by its weight.
    """

    # Weights for each category
    weights = {
        "education": 0.20,
        "experience": 0.20,
        "technical_skills": 0.30,
        "communication": 0.15,
        "certifications": 0.10,
        "interview": 0.05
    }

    # Normalize values and compute weighted score
    score = (
        (education / 4) * weights["education"] * 100 +
        (min(experience, 10) / 10) * weights["experience"] * 100 +
        (technical_skills / 10) * weights["technical_skills"] * 100 +
        (communication / 10) * weights["communication"] * 100 +
        (min(certifications, 5) / 5) * weights["certifications"] * 100 +
        (interview / 10) * weights["interview"] * 100
    )

    return round(score, 2)


# Example usage
applicant_total = applicant_score(
    education=3,
    experience=7,
    technical_skills=8,
    communication=9,
    certifications=4,
    interview=6
)
print("Applicant Total Score:", applicant_total)
