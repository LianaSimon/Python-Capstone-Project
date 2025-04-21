# EMPLOYEE DATA ANALYSIS OF ABC COMPANY USING PYTHON(PYTHON CAPSTONE PROJECT)


## 📋 PROJECT OVERVIEW

This project involves analyzing employee data from ABC Company to uncover insights related to team distribution, job roles, salary expenditure, and more. The dataset comprises 458 records with 9 columns, and Python was used to preprocess the data, perform analysis, and visualize key trends.


## 🔧A) PREPROCESSING

- Replaced the incorrect `Height` values (originally stored as datetime) with random integers between 150 and 180 cm.
- 
- Filled missing salary values with `0` for analysis purposes.
- 

#### ✅ Preprocessing Step 1: Open Jupyter Notebook

If you're using:

Anaconda: Launch the Anaconda Navigator and click on "Jupyter Notebook"

VS Code: Open a .ipynb file using the Jupyter extension

Online tools: You can use Google Colab or Jupyter Notebook in Kaggle


#### ✅ Preprocessing Step 2: Import Required Libraries

In the first cell of your notebook, run:

![image](https://github.com/user-attachments/assets/3169b6eb-286b-41ea-9092-663e215a689c)


#### ✅ Preprocessing Step 3: Load the Excel File

If the Excel file is on your computer, move it to the same folder as your notebook.

![image](https://github.com/user-attachments/assets/83698a29-1e50-4351-a131-cdf8965f1b75)

##### Output

![image](https://github.com/user-attachments/assets/a3c63f60-6cdf-447b-9bb2-e96253927427)

🔍 Check if the "Height" column looks like a date (e.g., 2023-02-06) — that confirms it needs fixing.


#### ✅ Preprocessing Step 4: Replace the "Height" Column with Random Numbers (150–180 cm)


![image](https://github.com/user-attachments/assets/c9565197-8a0a-4280-aa4f-b7555f7c8bc6)


##### Output

![image](https://github.com/user-attachments/assets/547a7771-5af0-44c1-8ac6-96401d56504a)



#### ✅ Preprocessing Step 5: Save the Cleaned Data (Optional but Useful)

![image](https://github.com/user-attachments/assets/b6ac9642-0de0-4e20-a172-cb4d593e6692)


You can now use this file (cleaned_employee_data.csv) for all further analysis steps.


#### 🧼 Summary of Preprocessing

1. Loaded the Excel file

2. Replaced the "Height" column with valid random values

3. (Optional) Saved the cleaned file for reuse




## 📊 B) Analysis Tasks Step-by-Step in Jupyter Notebook


#### ✅ Analysis Step 6: Import Visualization Libraries

Add this to a new cell:

![image](https://github.com/user-attachments/assets/e2b23b49-f5ae-4ae1-b7d7-7be5d1ce8194)


#### ✅ Analysis Step 7: Task 1 – Distribution of Employees by Team









