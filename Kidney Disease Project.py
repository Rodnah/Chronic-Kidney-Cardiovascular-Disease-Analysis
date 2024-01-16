#!/usr/bin/env python
# coding: utf-8

# # Correlation Analysis for Kidney Disease

# In[1]:


#import libraries

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# Read the exported CSV file into a pandas DataFrame


data = pd.read_csv('C:/Users/MY LAPTOP/Documents/SQL STUFF/Corr Analysis for Kidney Disease.csv')


# In[3]:


# Calculate correlation matrix
correlation_matrix = data.corr()


# In[4]:


# View the correlation matrix
print(correlation_matrix)


# In[5]:


# Set up the matplotlib figure
plt.figure(figsize=(12, 10))


# In[6]:


# Create a heatmap using seaborn
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# Show the plot
plt.title('Correlation Matrix')
plt.show()


# # Distribution of blood pressure and blood glucose values among patients with kidney disease

# In[9]:


# Read the exported CSV file into a pandas DataFrame
data = pd.read_csv('C:/Users/MY LAPTOP/Downloads/BP BGR.csv')


# In[11]:


import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.lines import Line2D

# Set up a single plot
plt.figure(figsize=(12, 6))

# Superimpose boxplots for Blood Glucose and Blood Pressure
sns.boxplot(x='classification', y='bgr', data=data, color='skyblue')
sns.boxplot(x='classification', y='bp', data=data, color='lightcoral')

# Create custom legend entries
legend_elements = [Line2D([0], [0], marker='s', color='w', markerfacecolor='skyblue', markersize=10, label='Blood Glucose'),
                   Line2D([0], [0], marker='s', color='w', markerfacecolor='lightcoral', markersize=10, label='Blood Pressure')]

# Add labels and title
plt.xlabel('Kidney Disease Classification')
plt.ylabel('Values')
plt.title('Distribution of Blood Glucose and Blood Pressure Values among Patients with Kidney Disease')

# Add legend
plt.legend(handles=legend_elements)

# Show the plot
plt.show()


# # Prevalence of Symptoms in Patients with Kidney Disease

# In[12]:


data = pd.read_csv ('C:/Users/MY LAPTOP/Documents/SQL STUFF/Symptoms and Kidney Disease.csv')


# In[13]:


# Print the column names to verify the presence of 'appet', 'pe', 'ane'
print(data.columns)


# In[14]:


# Reshape the data using the melt function
melted_data = pd.melt(data, id_vars='classification', value_vars=['appe', 'pe', 'ane'], var_name='symptom', value_name='presence')


# In[15]:


# Create a bar plot to visualize the prevalence of symptoms in patients with kidney disease
plt.figure(figsize=(10, 6))
sns.countplot(x='classification', hue='symptom', data=melted_data)

# Add labels and title
plt.xlabel('Kidney Disease Classification')
plt.ylabel('Count')
plt.title('Prevalence of Symptoms in Patients with Kidney Disease')

# Show the plot with a legend
plt.legend(title='Symptom', loc='upper right')
plt.show()

