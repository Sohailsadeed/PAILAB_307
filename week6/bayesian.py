import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import BayesianEstimator
from pgmpy.inference import VariableElimination

# 1. Create Synthetic Financial Dataset 
# In a real scenario, you would use: data = pd.read_csv('loan_data.csv')
data = pd.DataFrame({
    'Employment': ['Salaried', 'Freelance', 'Salaried', 'Unemployed', 'Freelance', 'Salaried', 'Unemployed', 'Salaried'],
    'IncomeStability': ['High', 'Low', 'High', 'Low', 'Medium', 'High', 'Low', 'Medium'],
    'CreditHistory': ['Good', 'Bad', 'Average', 'Bad', 'Average', 'Good', 'Bad', 'Good'],
    'DefaultRisk': ['No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No']
})

# 2. Define the Bayesian Network Structure
# Arrows represent causal influence:
# Employment -> IncomeStability
# IncomeStability & CreditHistory -> DefaultRisk
model = DiscreteBayesianNetwork([
    ('Employment', 'IncomeStability'),
    ('IncomeStability', 'DefaultRisk'),
    ('CreditHistory', 'DefaultRisk')
])

# 3. Parameter Learning (using Bayesian Estimator for better handling of incomplete data)
# 'pseudo_counts' acts as Laplace smoothing to prevent 0 probabilities
model.fit(
    data, 
    estimator=BayesianEstimator, 
    prior_type="BDeu", 
    equivalent_sample_size=10
)

# 4. Initialize the Inference Engine
loan_inference = VariableElimination(model)

print("--- AI Financial Risk Predictor Initialized ---\n")

# 5. Query Scenario 1: Predicting with INCOMPLETE data
# We know they are Salaried, but we don't know their Credit History yet.
print("Scenario 1: Applicant is 'Salaried', Credit History is unknown.")
prob_incomplete = loan_inference.query(
    variables=['DefaultRisk'], 
    evidence={'Employment': 'Salaried'}
)
print(prob_incomplete)

# 6. Query Scenario 2: High Risk Profile
# Freelance worker with a Bad credit history.
print("\nScenario 2: Applicant is 'Freelance' with 'Bad' Credit History.")
prob_high_risk = loan_inference.query(
    variables=['DefaultRisk'], 
    evidence={'Employment': 'Freelance', 'CreditHistory': 'Bad'}
)
print(prob_high_risk)

# 7. Inspecting the Causal Logic (CPDs)
# This shows how the AI weights 'Employment' against 'IncomeStability'
print("\n--- Learned Causal Logic (Employment -> Income Stability) ---")
print(model.get_cpds('IncomeStability'))