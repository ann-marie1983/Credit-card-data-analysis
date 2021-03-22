##Create Data arrays for analysis
import pandas as pd
import numpy as np
# import CSV file credit card cust data
data = pd.read_csv( "BankChurners.csv" )
# How any clients have left, and proportion of clients that have left
Attrition = data["Attrition_Flag"].value_counts()
print( Attrition )
## Proportion of clients that left
Attrition_props = data["Attrition_Flag"].value_counts( normalize=True )
print( Attrition_props )
# I want to check the card and income category to see if there is a trend
list1 = ["Card_Category", "Income_Category"]
print(data[list1].head(50))
# The blue card initially looks very popular, lets see
print(data['Card_Category'].value_counts().head())
# This is an example of how I would extract client volumes per card type and credit card limit data separately the merge for reporting purposes
df1=pd.DataFrame({ "Card_type":["blue","gold","platinum", "silver"],"no_clients": [9436,116,20,555 ]})
print(df1)
df2=pd.DataFrame({ "Card_type":["blue","gold","platinum", "silver"],"credit limit": [25000,30000,35000,20000]})
print(df2)
merge_card_type = pd.merge(df1,df2,on="Card_type")
print(merge_card_type)
# Lets see how any times each income category appears especially 'unknown'
print(data['Income_Category'].value_counts().head())
# Lets check the age profile of a client
print(data["Customer_Age"].mean())
Age = data[data["Customer_Age"]>= 30]
Age1 = data[data["Customer_Age"]>= 46]
Age2 = data[data["Customer_Age"]>= 56]
Age3 = data[data["Customer_Age"]>= 66]
print(Age)
print(Age1)
print(Age2)
print(Age3)
## If we create a feature, dividing the total transactions by the months on the books we can see average usage
data['Avg_trans_per_month'] = data['Total_Trans_Ct'] / data['Months_on_book']
print(data['Avg_trans_per_month'].head(11))
## We know how many clients left, lets see how any months in total they were on the books on average
Attrite_clients_on_books = data[data["Attrition_Flag"] == "Attrited Customer"]["Months_on_book"].sum()
print( Attrite_clients_on_books/1627)
## Lets compare the months on the books of attrite clients to the average existing client
Existing_clients_on_books = data[data["Attrition_Flag"] == "Existing Customer"]["Months_on_book"].sum()
print( Existing_clients_on_books/8500)
# Subset those that have left and compare to those that haven't and client interactions
Total_relationship_A = data[data["Attrition_Flag"] == "Attrited Customer"]["Total_Relationship_Count"].sum()
print( Total_relationship_A )
Total_relationship_B = data[data["Attrition_Flag"] == "Existing Customer"]["Total_Relationship_Count"].sum()
print( Total_relationship_B )
# Average relationship interactions for client attrition versus existing clients
print( Total_relationship_A / 1627 )
print( Total_relationship_B / 8500 )
# Look at numerical data that we can analyse using min, max, mean, and median and see if a pattern emerges
Client_review_inactive = data.groupby("Attrition_Flag")["Months_Inactive_12_mon"].agg([np.min, np.max, np.mean, np.median])
print(Client_review_inactive)
Client_review_Age = data.groupby("Attrition_Flag")["Customer_Age"].agg([np.min, np.max, np.mean, np.median])
print(Client_review_Age)
Client_review_Contacts = data.groupby("Attrition_Flag")["Contacts_Count_12_mon"].agg([np.min, np.max, np.mean, np.median])
print(Client_review_Contacts)
Client_review_Credit_Limit = data.groupby("Attrition_Flag")["Credit_Limit"].agg([np.min, np.max, np.mean, np.median])
print(Client_review_Credit_Limit)
Client_review_Rev_Bal = data.groupby("Attrition_Flag")["Total_Revolving_Bal"].agg([np.min, np.max, np.mean, np.median])
print(Client_review_Rev_Bal)
Client_review_trans_amount = data.groupby("Attrition_Flag")["Total_Trans_Amt"].agg([np.min, np.max, np.mean, np.median])
print(Client_review_trans_amount)
Client_review_Aver_Util_ratio = data.groupby("Attrition_Flag")["Avg_Utilization_Ratio"].agg([np.min, np.max, np.mean, np.median])
print(Client_review_Aver_Util_ratio)
Dep_Relationships= data.groupby("Marital_Status")["Dependent_count"].agg([np.min, np.max, np.mean, np.median])
print(Dep_Relationships)
# Reviewing string data: Martial Status, Education level, card type and attrition
print(data.groupby('Marital_Status')['Attrition_Flag'].value_counts())
print(data.groupby('Education_Level')['Attrition_Flag'].value_counts())
print(data.groupby('Card_Category')['Attrition_Flag'].value_counts())
print(data.groupby('Income_Category')['Attrition_Flag'].value_counts())
Dep_Relationships= data.groupby("Marital_Status")["Dependent_count"].agg([np.min, np.max, np.mean, np.median])
print(Dep_Relationships)