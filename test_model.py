from detect_law_type import Law
labor_law_sentences = [
    "The employer must provide a safe and healthy working environment for all staff.",
    "Employees are entitled to a minimum of twenty days of paid annual leave per year.",
    "The collective bargaining agreement was signed between the union and the management.",
    "Any termination of employment without just cause is considered a wrongful dismissal.",
    "The standard workweek shall not exceed forty hours without overtime compensation.",
    "Discrimination in the workplace based on gender, race, or religion is strictly prohibited.",
    "Workers have the legal right to organize and form trade unions for mutual protection.",
    "The minimum wage is adjusted annually to reflect the current cost of living index.",
    "Employers are required to contribute to the social security and unemployment funds.",
    "A formal written warning must be issued before an employee can be fired for misconduct.",
    "Maternity leave provisions allow for twelve weeks of protected absence from work.",
    "Occupational hazards must be clearly communicated to all laborers during induction.",
    "The labor tribunal will adjudicate disputes regarding unpaid bonuses and commissions.",
    "Non-compete clauses in an employment contract must be reasonable in scope and duration.",
    "Whistleblowers are protected by law against retaliation from their superiors.",
    "Part-time employees should receive benefits proportional to their hours worked.",
    "The industrial action was suspended pending further negotiations with the mediator.",
    "Severance pay is calculated based on the total number of years of continuous service.",
    "Employers must maintain accurate records of daily clock-in and clock-out times.",
    "Child labor is strictly forbidden under the current national labor statutes."
]


law = Law(labor_law_sentences)
print(law.types_ratio())

