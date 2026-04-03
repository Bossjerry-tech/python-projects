import pandas as pd

# Load dataset
df_jobs = pd.read_csv(r"C:\Users\USER\Downloads\jobs.csv")

# Preview first 10 rows
print(df_jobs.head(10))

# Clean column names (remove spaces + lowercase)
df_jobs.columns = df_jobs.columns.str.strip().str.lower()

# Check updated column names
print(df_jobs.columns)

# Filter required columns
df_filtered = df_jobs[['job_title', 'company']]

# Preview filtered data
print(df_filtered.head())

#To convert text to lowercase, use:

df_jobs['job_title'] = df_jobs['job_title'].str.lower()

print(df_jobs.head())

#To remove spaces, use:

df_jobs['company'] = df_jobs['company'].str.strip()

df_jobs.to_csv('cleaned_data.csv', index=False)