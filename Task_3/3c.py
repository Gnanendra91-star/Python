
#dataloader.py
import pandas as pd
def load_data():
    df = pd.read_csv("students.csv")
    return df

#statshelper.py
import numpy as np
from scipy import stats
def subject_mean(df, subject):
    return np.mean(df[subject])
def subject_std(df, subject):
    return np.std(df[subject])
def subject_mode(df, subject):
    return stats.mode(df[subject], keepdims=True).mode[0]

#main.py
# Step 1: Imports
from dataloader import load_data
from statshelper import subject_mean, subject_std, subject_mode
import pandas as pd
# Step 2: Load CSV data
df = load_data()
# Step 3: Subjects to analyze
subjects = ["Math", "Science", "English"]
# Step 4: Collect results
results = []
for subj in subjects:
    mean_val = subject_mean(df, subj)
    std_val = subject_std(df, subj)
    mode_val = subject_mode(df, subj)
    results.append([subj, mean_val, std_val, mode_val])
# Step 5: Create results table
results_df = pd.DataFrame(results, columns=["Subject", "Mean", "Standard Deviation", "Mode"])
print(results_df)

output:
Mean Age: 20.4
Median Score: 88.0
Standard Deviation of Score: 5.458937625582473
