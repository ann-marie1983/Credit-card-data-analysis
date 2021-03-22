import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# command to know your working directory
os.getcwd()
# setting your working directory
os.chdir(r"C:\Users\UCD\OneDrive - University College Dublin\Desktop\Online Data analytics course\Credit card customers")
df = pd.read_csv( "BankChurners.csv" )
## Overview of Attrition
sns.countplot(x="Attrition_Flag", data=df)
plt.show()
# Firstly I reviewed the data based on client attributes such as Gender, age, income and education
##Attrition based on gender
sns.countplot(x="Gender", data=df, hue="Attrition_Flag")
plt.show()
## Attrition based on Age
sns.distplot(df['Customer_Age']).set_title('Customer_Age')
plt.show()
## Attrition based on Income
sns.countplot(x="Income_Category", data=df, hue="Attrition_Flag")
plt.show()
## Attrition based on Education
sns.countplot(x="Education_Level", data=df, hue="Attrition_Flag")
plt.show()
#Then I reviewed the product attributes which are the card type and credit limit
##w Attrition based on card type
sns.countplot(x="Card_Category", data=df, hue="Attrition_Flag")
plt.show()
##Credit Limit
fig, ax = plt.subplots()
ax.hist(df["Credit_Limit"], histtype='step', label="clients", bins=5)
ax.set_xlabel("Credit_Limit ($)")
ax.set_ylabel("# of Clients")
plt.show()
## I looked at Client usage of card and attrition
sns.scatterplot(x="Total_Trans_Amt", y ="Total_Revolving_Bal", data=df, hue="Attrition_Flag")
plt.show()
sns.relplot(x="Total_Amt_Chng_Q4_Q1", y="Total_Ct_Chng_Q4_Q1", data=df, kind="scatter", col="Attrition_Flag", hue="Attrition_Flag")
plt.show()
sns.relplot(x="Total_Trans_Ct", y="Avg_Open_To_Buy", data=df, kind="line", hue="Attrition_Flag")
plt.show()
## Review of client relationship and contacts
sns.boxplot(x = 'Attrition_Flag', y = 'Months_on_book', data = df, hue='Contacts_Count_12_mon', sym="")
plt.show()
