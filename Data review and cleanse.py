# import all required libraries
import pandas as pd
import numpy as np
# import CSV file credit card customer data
data = pd.read_csv( "BankChurners.csv" )
## Firstly we check if the client number is the primary key
ID = len(data.CLIENTNUM.unique())
print(ID)
# Review data
print(data.info())
## I would like to check for duplicates
drop_duplicates= data.drop_duplicates()
print(data.shape,drop_duplicates.shape)
## Then I look for missing values
missing_values_count = data.isnull().sum()
print(missing_values_count)
###Lets assume a missing value occurred in column ‘Months_on_book’
print(data["Months_on_book"].mean())
print(data["Months_on_book"].median())
print(data["Months_on_book"].mode())
### fill the missing values with median value 36, this would for our cleaned data, not required
cleaned_data = data.fillna(35.92840920)
cleaned_data.isnull().sum()
## Columns with that contain null values if present are dropped using this code
dropcolumns = data.dropna(axis=1)
print(data.shape, dropcolumns.shape)
print(data.shape)
#Drop columns that will not assist us with our analysis
data = data.drop(data[['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2']], axis=1)
print(data.columns)
print(data.shape)
# Index data based on Attrition clients
data_ind = data.set_index("Attrition_Flag")
print(data_ind)
# Review personal info on clients using indexing and slicing together
print(data_ind.iloc[0:10, 2:7])
print(data_ind.iloc[10116:101126, 2:7])
data_ind.reset_index()
# I want to review how any card types there are
print(data.Card_Category.unique())
