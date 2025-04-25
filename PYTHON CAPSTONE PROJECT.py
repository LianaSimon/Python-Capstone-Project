#!/usr/bin/env python
# coding: utf-8

# # EMPLOYEE DATA ANALYSIS OF ABC COMPANY

# ### PREPROCESSING

# In[5]:


import pandas as pd
import numpy as np


# In[14]:


#Load the excel file
df=pd.read_excel("pythoncapstoneexcel.xlsx",sheet_name="myexcel.csv")


# In[16]:


#Preview the data
df.head()


# In[18]:


#Replace the 'Height' column with random values between 150 and 180

np.random.seed(42) #Ensures the same random values every time.

df['Height']=np.random.randint(150,180,size=len(df))

#Preview to confirm changes
df[['Name' ,'Height']].head()


# In[20]:


#Save the modified Dataframe to a new CSV file
df.to_csv("cleaned_emplyee_data.csv",index=False)


# ### DATA ANALYSIS

# ##### Import Visualization Libraries

# In[22]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[24]:


# Optional: To make the plots prettier

sns.set(style="whitegrid")
get_ipython().run_line_magic('matplotlib', 'inline')


# ##### Distribution of Employees by Team

# In[26]:


#Count how many employees are there in each team
team_distribution=df['Team'].value_counts()
team_percentage=df['Team'].value_counts(normalize=True)*100


# In[28]:


#Create a summary table
team_summary=pd.DataFrame({
    'Count':team_distribution,
    'Percentage':team_percentage.round(2)
})

print(team_summary)


# In[37]:


# Plot the distribution

plt.figure(figsize=(10,6))
sns.countplot(data=df,y='Team',order=team_distribution.index,palette='viridis')
plt.title("Employee distribution by team")
plt.xlabel('Number of Employees')
plt.ylabel('Team')
plt.show()


# ##### Segregate Employees by Position

# In[30]:


position_counts=df['Position'].value_counts()
print(position_counts)


# In[32]:


#Plot
plt.figure(figsize=(8,6))
sns.countplot(data=df,x='Position',order=position_counts.index,palette='Set2')
plt.title("Employees by position")
plt.xlabel("Position")
plt.ylabel("Count")
plt.show()


# ##### Identify Predominant Age Group

# In[40]:


bins=[20,25,30,35,40]
labels=['21-25','26-30','31-35','36-40']
df['Age Group']=pd.cut(df['Age'],bins=bins,labels=labels,right=False)


# In[42]:


#count age groups
age_group_counts=df['Age Group'].value_counts().sort_index()
print(age_group_counts)


# In[44]:


#Plot
plt.figure(figsize=(8,6))
age_group_counts.plot(kind='bar',color='skyblue')
plt.title("Age Group Distribution")
plt.xlabel("Age Group")
plt.ylabel("Number of Employees")
plt.show()


# #### Highest Salary Expenditure (Team and Position)

# In[46]:


# Fill Missing Salaries with 0

df['Salary'].fillna(0,inplace=True)

# Total Salary by team

team_salary=df.groupby('Team')['Salary'].sum().sort_values(ascending=False)
print("Top team by salary:",team_salary.idxmax())



#Total Salary by Position

position_salary=df.groupby('Position')['Salary'].sum().sort_values(ascending=False)
print("Top position by salary",position_salary.idxmax())


# In[48]:


#Plot Salary By Team

plt.figure(figsize=(8,5))
team_salary.plot(kind='bar',color='coral')
plt.title("Total salary by team")
plt.ylabel("Total Salary")
plt.show()


# In[50]:


#Plot Salary by position

plt.figure(figsize=(8,5))
position_salary.plot(kind='bar', color='teal')
plt.title("Total Salary by position")
plt.ylabel("Total Salary")
plt.show()


# #### Correlation Between Age and Salary

# In[58]:


#scatter plot to see corelation
plt.figure(figsize=(8,6))
sns.scatterplot(data=df,x='Age',y='Salary',hue='Position',palette='deep')
plt.title("Age vs Salary")
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend(bbox_to_anchor=(1.05,1),loc='upper left')
plt.tight_layout()

plt.show()


# In[62]:


# Calculate correlation

correlation=df[['Age','Salary']].corr()
print("Correlation between Age and Salary :")
print(correlation)


# In[ ]:




