def evaluate_loan_application(applicant_data):
    """
    Evaluates a loan application based on simple criteria.

    Args:
        applicant_data: A dictionary containing applicant information 
                        (e.g., 'credit_score', 'income', 'loan_amount').

    Returns:
        A string indicating the loan decision ('Approved', 'Rejected', or 'Review').
    """

    # Define simple approval criteria
    min_credit_score = 600
    min_income_multiplier = 3  # Loan amount should be no more than 3 times income

    # Check if required data is present
    if 'credit_score' not in applicant_data or 'income' not in applicant_data or 'loan_amount' not in applicant_data:
        return 'Review'  # Not enough information to make a decision

    credit_score = applicant_data['credit_score']
    income = applicant_data['income']
    loan_amount = applicant_data['loan_amount']

    # Apply criteria
    if credit_score >= min_credit_score and loan_amount <= (income * min_income_multiplier):
        return 'Approved'
    elif credit_score < min_credit_score:
        return 'Rejected'
    else:
        return 'Review'  # Further review needed for other cases


# ===========================
# Example usage (First set)
# ===========================

applicant1 = {'credit_score': 700, 'income': 50000, 'loan_amount': 100000}
applicant2 = {'credit_score': 550, 'income': 60000, 'loan_amount': 150000}
applicant3 = {'credit_score': 650, 'income': 40000, 'loan_amount': 130000}
applicant4 = {'credit_score': 720, 'income': 70000}  # Missing loan_amount

print(f"Applicant 1 decision: {evaluate_loan_application(applicant1)}")
print(f"Applicant 2 decision: {evaluate_loan_application(applicant2)}")
print(f"Applicant 3 decision: {evaluate_loan_application(applicant3)}")
print(f"Applicant 4 decision: {evaluate_loan_application(applicant4)}")


# =====================================
# More example applicant data (Second set)
# =====================================

applicant5 = {'name': 'Alice Smith',  'gender': 'Female', 'credit_score': 680, 'income': 55000, 'loan_amount': 120000}
applicant6 = {'name': 'Bob Johnson',  'gender': 'Male',   'credit_score': 590, 'income': 75000, 'loan_amount': 200000}
applicant7 = {'name': 'Charlie Brown','gender': 'Male',   'credit_score': 750, 'income': 90000, 'loan_amount': 250000}
applicant8 = {'name': 'Diana Prince', 'gender': 'Female', 'credit_score': 620, 'income': 45000, 'loan_amount': 100000}
applicant9 = {'name': 'Eve Adams',    'credit_score': 700, 'income': 60000}  # Missing loan_amount and gender


# Print decisions for new applicants
print(f"Applicant 5 decision: {evaluate_loan_application(applicant5)}")
print(f"Applicant 6 decision: {evaluate_loan_application(applicant6)}")
print(f"Applicant 7 decision: {evaluate_loan_application(applicant7)}")
print(f"Applicant 8 decision: {evaluate_loan_application(applicant8)}")
print(f"Applicant 9 decision: {evaluate_loan_application(applicant9)}")
