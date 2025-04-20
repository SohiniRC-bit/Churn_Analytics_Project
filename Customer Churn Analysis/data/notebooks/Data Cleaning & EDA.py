#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# Load the dataset
df = pd.read_csv("C:/Users/sohin/Customer Churn Analysis/data/raw/Telco-Customer-Churn.csv", encoding='utf-8-sig')


# In[3]:


df.columns = df.columns.str.strip()  # Clean column names


# In[4]:


# 🧪 Check column name
print("Churn column in columns:", 'Churn' in df.columns)


# In[5]:


# Quick look
print(df.shape)
print(df.dtypes)
df.head()


# In[6]:


# 🛠️ Convert Churn to string first, then map safely
df['Churn'] = df['Churn'].astype(str).str.strip().map({'Yes': 1, 'No': 0})


# In[7]:


# 🧼 Drop rows where mapping failed
df = df[df['Churn'].isin([0, 1])]


# In[8]:


# ✅ Confirm it worked
print(df['Churn'].value_counts(dropna=False))


# In[9]:


# Create RevenueLoss
df['RevenueLoss'] = df['MonthlyCharges'] * df['Churn']


# In[10]:


plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='Churn')
plt.title('Churn Count')
plt.xticks([0, 1], ['No', 'Yes'])
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.show()


# In[11]:


# Churn by Contract Type
plt.figure(figsize=(7, 5))
sns.barplot(data=df, x='Contract', y='Churn')
plt.title('Churn Rate by Contract Type')
plt.show()


# In[12]:


# Monthly Charges vs Churn
plt.figure(figsize=(8, 5))
sns.kdeplot(df[df['Churn'] == 1]['MonthlyCharges'], label='Churned', shade=True)
sns.kdeplot(df[df['Churn'] == 0]['MonthlyCharges'], label='Retained', shade=True)
plt.title('Distribution of Monthly Charges by Churn')
plt.legend()
plt.show()


# In[13]:


# 🔍 Correlation Heatmap
# -------------------------
numerical_features = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']
plt.figure(figsize=(8, 6))
sns.heatmap(df[numerical_features].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()


# In[14]:


# 📦 Save Cleaned Data
# -------------------------
df.to_csv("C:/Users/sohin/Customer Churn Analysis/data/cleaned/Telco_cleaned.csv", index=False)
print("✅ Cleaned data saved!")


# In[ ]:





# In[ ]:





# In[ ]:




