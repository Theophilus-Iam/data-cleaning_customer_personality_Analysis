''' This Script cleans and prepares a raw dataset(with nulls,duplicates,inconsistent formats)'''

#---------------------------- IMPORT LIBRARIES BELOW ----------------------------------------------
#1. Import modules/libraries

import pandas as pd #This will be used for loading and cleaning our data 

#-----------------------  DEFINE CONSTANTS BELOW (OPTIONAL) --------------------------------------
#2. Here we want to declare any variables that are constants 

f1 = 'marketing_campaign.csv' #(File name can be taken as a constant)

#---------------------------- LOAD DATA BELOW -----------------------------------------------------
#Load datasets here...Making sure to use unique variable names 

#df = pd.read_csv(f1) # 1st read of the raw data

# ------------------ UNDERSTAND THE DATA AND IDENTIFY PROBLEMS -----------------------------------
# Preview the first 5 rows
#print(df.head()) # Everything looks clustered, and hard to read at this point we see a lot of "/t"

# "\t" is a tab character telling us that this is the end of one column,after it,follows another col
df = pd.read_csv(f1,sep = '\t') # Use tab as separator

# Review the first 5 rows (after fixing separator) 
#print(df.head()) # The data looks better now, but we can'nt see all columns

'''
# View all column names (one per line for clarity)
for col in df.columns:
    print(col)

# Total number of columns
print(len(df.columns)) # 29 columns
'''          

# ---------------------------- STRUCTURE CHECK ---------------------------------------------------
'''
# Shape of dataset (rows, columns)
print("Shape:", df.shape) #2240 rows and 29 columns

# Data types and missing values overview
print(df.info()) # "Income" has mising data(2216 non null of 2240)

'''
# --------------------------- DATA QUALITY CHECK --------------------------------------------------
'''
# Check missing values per column
print("\nMissing Values:")
print(df.isnull().sum()) 
#Income has 24 missing values → needs handling to avoid incomplete analysis

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum()) 
#No duplicates, dataset represents unique customers
'''

# --------------------------- CATEGORY INSPECTION --------------------------------------------------
'''
# Check unique values in key categorical columns
print("\nEducation categories:")
print(df['Education'].unique())
# Most categories appear consistent,but '2n Cycle' naming is a invalid Education category


print("\nMarital Status categories:")
print(df['Marital_Status'].unique())

 
print("\nMarital Status categories:")
print(df['Marital_Status'].unique())  
# Most categories valid, but 'Absurd' and 'YOLO' are invalid,need cleaning or removal

'''

# ------------------------------ DATA CLEANING ------------------------------------------------------

# --------------------------- HANDLE MISSING VALUES -------------------------------------------------

# We replace missing values with a representative value
# Median is preferred over mean because income data can have outliers

#df['Income'].fillna(df['Income'].median(), inplace=True) # may cause complications in the future
df['Income'] = df['Income'].fillna(df['Income'].median())

# --------------------------- REMOVE DUPLICATES -----------------------------------------------------

# Even though no duplicates were found, this ensures dataset remains clean and safe
df.drop_duplicates(inplace=True)


# ----------------------------- FIX DATA TYPES ------------------------------------------------------

# Dt_Customer is currently stored as text (object), but should be a datetime format
# This allows for proper date-based analysis later
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y')
#df['Dt_Customer'] = df['Dt_Customer'].dt.strftime('%d-%m-%Y')
#
# -------------------------- STANDARDIZE TEXT VALUES ------------------------------------------------

# Ensure consistency in categorical data (avoid issues like different casing or spaces)
df['Education'] = df['Education'].str.strip()
df['Marital_Status'] = df['Marital_Status'].str.strip()

# Remove or handle invalid categories like 'Absurd' and 'YOLO'
# Here we replace them with 'Other' to keep the data usable
df['Marital_Status'] = df['Marital_Status'].replace(['Absurd', 'YOLO'], 'Other')


# ------------------------------ RENAME COLUMNS -----------------------------------------------------

# Clean column names improve readability and make coding easier (no spaces, consistent format)
df.columns = df.columns.str.lower().str.replace(" ", "_")


# -------------------------------- FINAL CHECK ------------------------------------------------------
'''
# Confirm that cleaning was successful
print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nData Types After Cleaning:")
print(df.info())

'''

# ------------------------------ SAVE CLEANED DATA ---------------------------------------------------

# WHY: Save the cleaned dataset so it can be submitted and used for analysis or modelling
df.to_csv("cleaned_customer_personality.csv", index=False)

print("\nCleaned dataset saved successfully.")


 
