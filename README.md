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


2. **Position-wise Segregation**  
   - Analyzed the count of employees in each job position.
   - Represented through a bar chart.

3. **Age Group Distribution**  
   - Categorized employees into age groups.
   - Visualized using a bar chart.

4. **Salary Expenditure**  
   - Identified the team and position with the highest total salary.
   - Visualized with bar charts for both teams and positions.

5. **Correlation Analysis**  
   - Checked for correlation between age and salary.
   - Represented using a scatter plot and correlation matrix.


#### ✅ Analysis Step 6: Import Visualization Libraries

Add this to a new cell:

![image](https://github.com/user-attachments/assets/e2b23b49-f5ae-4ae1-b7d7-7be5d1ce8194)


#### ✅ Analysis Step 7: Task 1 – Distribution of Employees by Team

1. **Team Distribution**  
   - Counted employees per team and calculated the percentage share.
   - Visualized using a horizontal bar chart.
     

![image](https://github.com/user-attachments/assets/7894a484-a549-4a5d-9a63-c1b85d300a7a)


##### Output

![image](https://github.com/user-attachments/assets/b3da3946-3cee-4f6d-ac80-8a7a2de49726)


##### Plot the distribution

![image](https://github.com/user-attachments/assets/92404005-cb0c-4182-91cd-9a43eb821d3d)


##### Output

![image](https://github.com/user-attachments/assets/368638a7-898a-49c4-9468-8ae0ccafc9fc)




#### ✅ Analysis Step 8: Task 2 – Segregate Employees by Position

![image](https://github.com/user-attachments/assets/edcdba82-c5ba-4763-8f8c-ab62e45134c8)

##### Output

![image](https://github.com/user-attachments/assets/01437941-9c73-49c2-ac54-2268ce0100f0)

##### Plot

![image](https://github.com/user-attachments/assets/aa58eb19-4ee1-4e20-a409-75c6dc7faf25)


##### Output


![image](https://github.com/user-attachments/assets/385eb965-5d60-4eca-8513-d9e97d40fe5d)



#### ✅ Analysis Step 9: Task 3 – Identify Predominant Age Group

![image](https://github.com/user-attachments/assets/34105644-a351-4761-9d9d-e9a5058ec583)

##### Output

![image](https://github.com/user-attachments/assets/d1fc8701-7677-4a6d-88f4-fece1ccecb28)


##### Plot

![image](https://github.com/user-attachments/assets/dbb3c60e-7d4a-4a03-85b5-6bc2b7f7570a)


##### Output

![image](https://github.com/user-attachments/assets/ab177660-c7c8-4aff-921a-2b08d9b4849f)



#### ✅ Analysis Step 10: Task 4 – Highest Salary Expenditure (Team and Position)

![image](https://github.com/user-attachments/assets/53e817d7-6958-4c7b-89ee-2419af56755f)


##### Output

![image](https://github.com/user-attachments/assets/cd0a0c71-03f4-439a-879e-07a17398108f)


##### Plot

![image](https://github.com/user-attachments/assets/1187be76-045d-435c-8e00-5ba266ddff74)


##### Output

![image](https://github.com/user-attachments/assets/5a1e7879-5133-4888-8ea6-b32a77e45baf)


##### Plot

![image](https://github.com/user-attachments/assets/59f14818-026f-423a-a3af-a77221b8e128)

##### Output

![image](https://github.com/user-attachments/assets/17f5ca26-289a-480f-8570-1602553157f0)














