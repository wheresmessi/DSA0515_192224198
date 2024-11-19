import pandas as pd

# Create the departments dataframe
departments_data = {
    'DEPARTMENT_ID': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 
                     150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270],
    'DEPARTMENT_NAME': ['Administration', 'Marketing', 'Purchasing', 'Human Resources', 
                       'Shipping', 'IT', 'Public Relations', 'Sales', 'Executive', 
                       'Finance', 'Accounting', 'Treasury', 'Corporate Tax', 
                       'Control And Credit', 'Shareholder Services', 'Benefits', 
                       'Manufacturing', 'Construction', 'Contracting', 'Operations', 
                       'IT Support', 'NOC', 'IT Helpdesk', 'Government Sales', 
                       'Retail Sales', 'Recruiting', 'Payroll']
}

# Create DataFrame
df_departments = pd.DataFrame(departments_data)

# Select distinct department IDs
distinct_dept_ids = df_departments['DEPARTMENT_ID'].unique()

# Display results
print("Distinct Department IDs:")
print(distinct_dept_ids)