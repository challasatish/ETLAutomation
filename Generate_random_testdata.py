import pandas as pd
import random

# Generate 1000 rows of test data
data = {
    'eno': range(1, 1001),  # Employee numbers 1-1000
    'ename': [f'Employee_{i}' for i in range(1, 1001)],  # Employee names
    'deptno': [random.choice([10, 20, 30, 40, 50]) for _ in range(1000)],  # Department numbers
    'Salary': [random.randint(1000, 10000) for _ in range(1000)]  # Salaries
}

# Create DataFrame
df = pd.DataFrame(data)

# Add some null values in deptno (like your original data had row 7)
null_indices = random.sample(range(1000), 50)  # 50 rows with null deptno
for idx in null_indices:
    df.loc[idx, 'deptno'] = None

# Save to CSV
df.to_csv('Target_random_data.csv', index=False)
print(f"Generated Target.csv with {len(df)} rows")
print(df.head(10))