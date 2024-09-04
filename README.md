# Kearney-Technical-Assesment

This Repo contains Data Analytics use case for answering Analytics and Engineering Questions using SQL & Python Code

# SQL Task:
Considering the database schema displayed in the SQL Server - style diagram below, write a SQL query to return a list of all the invoices. For each invoice, show the Invoice ID, the billing date, the customer’s name, and the name of the customer who referred to that customer (if any). The list should be ordered by billing date.

This question simply tests the candidate’s ability take a plain-English requirement and write a corresponding SQL query. There is nothing tricky in this one, it just covers the basics:
Did the candidate remember to use a LEFT JOIN instead of an inner JOIN when joining the customer table for the referring customer name? If not, any invoices by customers not referred by somebody will be left out altogether.
Did the candidate alias the tables in the JOIN? Most experienced T-SQL programmers always do this, because repeating the full table name each time it needs to be referenced gets tedious quickly. In this case, the query would actually break if at least the Customer table wasn’t aliased, because it is referenced twice in different contexts (once as the table which contains the name of the invoiced customer, and once as the table which contains the name of the referring customer).
Did the candidate disambiguate the Id and Name columns in the SELECT? Again, this is something most experienced programmers do automatically, whether or not there would be a conflict. And again, in this case there would be a conflict, so the query would break if the candidate neglected to do so.
Note that this query will not return Invoices that do not have an associated Customer. This may be the correct behavior for most cases (e.g., it is guaranteed that every Invoice is associated with a Customer, or unmatched Invoices are not of interest). However, in order to guarantee that all Invoices are returned no matter what, the Invoices table should be joined with Customers using LEFT JOIN

# Python Task

Python Pandas – I expect to do at least couple of the tasks. 
Run following code:
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


# Tasks:
1. Please calculate the average, median, lower and upper quartiles of an employees' salaries.

2. Please calculate the average salary per department. Please include the department name in the results.

3. Please create a new column named `SALARY_CATEGORY` with value "low" when the salary is lower than average and "high" if is it higher or equal.

4. Please create another column named `SALARY_CATEGORY_AMONG_DEPARTMENT` with value "low" when the employee salary is lower than average in his / her department and "high" in the other case.


5. Please filter the dataframe `employees` to include only the rows where `DEPARTMENT_ID` equals to 20. Assign the result to new variable.

6. Please increase the salary by 10% for all employees working at the department 20.

7. Please check if any of the `PHONE_NUMBER` column values are empty.


# Solutions

 1. Emp_Dept_Analysis.py file : contains python data analytics solution fro employees and departments datasets
 2. Inv_Cust_Query.sql file : conatins sql query solution for invoice and customer query
