# ----------------------------
# AI-Based Online Exam Proctor Assignment using CSP
# ----------------------------

# Exams and required skills
exams = {
    'Exam1': 'Math',
    'Exam2': 'Physics',
    'Exam3': 'Chemistry',
    'Exam4': 'Math',
    'Exam5': 'Physics'
}

# Proctors: skills and availability
proctors = {
    'P1': {'skills': ['Math', 'Physics'], 'available': ['9-10','10-11']},
    'P2': {'skills': ['Physics','Chemistry'], 'available': ['9-10','10-11']},
    'P3': {'skills': ['Math','Chemistry'], 'available': ['9-10']},
    'P4': {'skills': ['Math','Physics','Chemistry'], 'available': ['10-11']},
}

# Exam time slots
exam_time = {
    'Exam1': '9-10',
    'Exam2': '9-10',
    'Exam3': '10-11',
    'Exam4': '10-11',
    'Exam5': '10-11'
}

# ----------------------------
# CSP Class
# ----------------------------
class CSP:
    def __init__(self, variables, domains):
        self.variables = variables  # Exams
        self.domains = domains      # Available proctors per exam

    def is_consistent(self, exam, proctor, assignment):
        # Check skill match
        if exams[exam] not in proctors[proctor]['skills']:
            return False

        # Check time availability: proctor cannot have 2 exams at same time
        for assigned_exam, assigned_proctor in assignment.items():
            if assigned_proctor == proctor:
                if exam_time[exam] == exam_time[assigned_exam]:
                    return False
        return True

    def backtrack(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        # Select unassigned exam
        for exam in self.variables:
            if exam not in assignment:
                break

        # Try all proctors
        for proctor in self.domains[exam]:
            if self.is_consistent(exam, proctor, assignment):
                assignment[exam] = proctor
                result = self.backtrack(assignment)
                if result:
                    return result
                assignment.pop(exam)  # Backtrack

        return None

# ----------------------------
# Prepare Domains for Each Exam
# ----------------------------
domains = {}
for exam in exams:
    domains[exam] = []
    for p in proctors:
        if exam_time[exam] in proctors[p]['available'] and exams[exam] in proctors[p]['skills']:
            domains[exam].append(p)

# ----------------------------
# Solve CSP
# ----------------------------
csp = CSP(list(exams.keys()), domains)
solution = csp.backtrack({})

# ----------------------------
# Output Result
# ----------------------------
if solution:
    print("AI-Based Exam Proctor Assignment:")
    for exam, proctor in solution.items():
        print(f"{exam} ({exam_time[exam]}) -> {proctor}")
else:
    print("No valid assignment found.")