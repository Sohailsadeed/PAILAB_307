import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork # Added import
from pgmpy.inference import VariableElimination
from pgmpy.estimators import MaximumLikelihoodEstimator # Added for clarity

# Step 1: Define Dataset
data = pd.DataFrame(data={
    'Rain':       ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes']
})

# Step 2: Define Bayesian Network Structure
model = DiscreteBayesianNetwork([('Rain', 'TrafficJam'), ('TrafficJam', 'ArriveLate')])

# Step 3 & 4: Parameter Learning (MLE)
# fit() uses MaximumLikelihoodEstimator by default
model.fit(data, estimator=MaximumLikelihoodEstimator)

print("--- Conditional Probability Distributions (CPDs) ---")
for cpd in model.get_cpds():
    print(cpd)

# Step 5 & 6: Initialize Inference and Query
inference = VariableElimination(model)
query_result = inference.query(variables=['ArriveLate'], evidence={'Rain': 'Yes'})

print("\n--- Inference Result: P(ArriveLate | Rain = Yes) ---")
print(query_result)