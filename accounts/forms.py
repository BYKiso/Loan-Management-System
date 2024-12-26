from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

SECURITY_QUESTIONS = [
    ('pet', 'What was the name of your first pet?'),
    ('school', 'What was the name of your primary school?'),
    ('city', 'In which city were you born?'),
]

LOAN_PURPOSES = [
    ('home', 'Home Improvement'),
    ('auto', 'Auto Loan'),
    ('education', 'Education'),
    ('debt', 'Debt Consolidation'),
]

EMPLOYMENT_OPTIONS = [
    ('full_time', 'Full-Time'),
    ('part_time', 'Part-Time'),
    ('self_employed', 'Self-Employed'),
    ('unemployed', 'Unemployed'),
]

LOAN_TERMS = [
    (12, '12 Months'),
    (24, '24 Months'),
    (36, '36 Months'),
    (48, '48 Months'),
    (60, '60 Months'),
]

class LoanApplicationForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    credit_score = forms.IntegerField(validators=[MinValueValidator(300), MaxValueValidator(999)])
    annual_income = forms.IntegerField()
    security_question = forms.ChoiceField(choices=SECURITY_QUESTIONS)
    security_answer = forms.CharField(max_length=50)
    employment = forms.MultipleChoiceField(choices=EMPLOYMENT_OPTIONS, widget=forms.CheckboxSelectMultiple)
    loan_purpose = forms.ChoiceField(choices=LOAN_PURPOSES)
    loan_term = forms.ChoiceField(choices=LOAN_TERMS)
