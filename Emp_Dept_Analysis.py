import pandas as pd
def get_employees_df():

 return pd.read_csv(
   "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82"
    "ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
 )
def get_departments_df():
 dep_df = pd.read_csv(
   "https://gist.githubusercontent.com/kevin336/5ea0e96813aa88871c20d315b5"
    "bf445c/raw/d8fcf5c2630ba12dd8802a2cdd5480621b6a0ea6/departments.csv"
 )
 dep_df = dep_df.rename(columns={"DEPARTMENT_ID": "DEPARTMENT_IDENTIFIER"})

 return dep_df

employees = get_employees_df()
departments = get_departments_df()

#  1. Please calculate the average, median, lower and upper quartiles of an employees' salaries.
def calculate_salary_statistics(employees):
  """
  Calculates average, median, lower, and upper quartiles of salaries.
  """

  average_salary = employees['SALARY'].mean()
  median_salary = employees['SALARY'].median()
  lower_quartile = employees['SALARY'].quantile(0.25)
  upper_quartile = employees['SALARY'].quantile(0.75)

  return {
      "Average Salary": average_salary,
      "Median Salary": median_salary,
      "Lower Quartile": lower_quartile,
      "Upper Quartile": upper_quartile
  }

# Calculate salary statistics
statistics = calculate_salary_statistics(employees)

# Print the results
#print(statistics)


# 2. Please calculate the average salary per department. Please include the department name in the results.
def calculate_average_salary_per_department(employees, departments):
  """
  Calculates the average salary for each department.
  """

  # Merge the employee and department dataframes based on department identifier
  merged_data = employees.merge(departments, left_on='DEPARTMENT_ID', right_on='DEPARTMENT_IDENTIFIER')

  # Group by department name and calculate average salary
  average_salaries = merged_data.groupby('DEPARTMENT_NAME')['SALARY'].mean().reset_index()
  average_salaries.columns = ['DEPARTMENT_NAME', 'AVERAGE_SALARY']

  return average_salaries

# Calculate average salary per department
average_salaries = calculate_average_salary_per_department(employees, departments)

# Print the results
#print(average_salaries)

# 3. Please create a new column named `SALARY_CATEGORY` with value "low" when the salary is lower than average and "high" if is it higher or equal.
def add_salary_category(employees):
  """
  Adds a new column 'SALARY_CATEGORY' to the employees DataFrame,
  categorizing salaries as 'low' or 'high' based on the average salary.
  """

  # Calculate the average salary
  average_salary = employees['SALARY'].mean()

  # Create a lambda function to categorize salaries
  categorize_salary = lambda salary: "low" if salary < average_salary else "high"

  # Apply the function to create the new column
  employees['SALARY_CATEGORY'] = employees['SALARY'].apply(categorize_salary)

  return employees

# Add the salary category column
employees = add_salary_category(employees)

# Print the modified DataFrame
#print(employees)


# 4. Please create another column named `SALARY_CATEGORY_AMONG_DEPARTMENT` with value "low" when the employee salary is lower than average in his / her department and "high" in the other case.
def add_salary_category_among_department(employees):
  """
  Adds a new column 'SALARY_CATEGORY_AMONG_DEPARTMENT' to the employees DataFrame,
  categorizing salaries as 'low' or 'high' based on the average salary within their department.
  """

  # Group by department and calculate average salary
  department_averages = employees.groupby('DEPARTMENT_ID')['SALARY'].mean()

  # Merge department averages back into the original DataFrame
  employees = employees.merge(department_averages.reset_index(name='DEPARTMENT_AVERAGE'), on='DEPARTMENT_ID')

  # Create a lambda function to categorize salaries
  categorize_salary = lambda row: "low" if row['SALARY'] < row['DEPARTMENT_AVERAGE'] else "high"

  # Apply the function to create the new column
  employees['SALARY_CATEGORY_AMONG_DEPARTMENT'] = employees.apply(categorize_salary, axis=1)

  return employees

# Add the salary category among department column
employees = add_salary_category_among_department(employees)

# Print the modified DataFrame
#print(employees)


# 5. Please filter the dataframe `employees` to include only the rows where `DEPARTMENT_ID` equals to 20. Assign the result to new variable.
def filter_employees_by_department(employees, department_id):
  """
  Filters the employees DataFrame based on a specified department ID.
  """

  filtered_employees = employees[employees['DEPARTMENT_ID'] == department_id]
  return filtered_employees

# Filter employees by department ID 20
filtered_employees = filter_employees_by_department(employees, 20)

# Print the filtered DataFrame
#print(filtered_employees)


# 6. Please increase the salary by 10% for all employees working at the department 20.
def increase_salaries_for_department(employees, department_id, percentage):
  """
  Increases the salaries of employees in a specified department by a given percentage.
  """

  # Filter employees in the specified department
  department_employees = employees[employees['DEPARTMENT_ID'] == department_id]

  # Calculate the increased salary
  department_employees['SALARY'] *= (1 + percentage / 100)

  # Update the original DataFrame with the modified salaries
  employees.update(department_employees)

  return employees

# Increase salaries for department 20 by 10%
employees = increase_salaries_for_department(employees, 20, 10)

# Print the modified DataFrame
#print(employees)


# 7. Please check if any of the `PHONE_NUMBER` column values are empty.
def check_empty_phone_numbers(employees):
  """
  Checks if any values in the 'PHONE_NUMBER' column are empty or missing.
  """

  has_empty_numbers = employees['PHONE_NUMBER'].isnull().any()
  return has_empty_numbers

# Get the employee data
employees = get_employees_df()

# Check for empty phone numbers
has_empty_numbers = check_empty_phone_numbers(employees)

# Print the result
if has_empty_numbers:
  print("There are empty or missing phone numbers.")
else:
  print("All phone numbers are filled.")