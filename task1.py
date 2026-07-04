import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

header = pd.read_excel("Sales.SalesOrderHeader.xlsx")
detail = pd.read_excel("Sales.SalesOrderDetail.xlsx")

print("=" * 30)
print("SALES ORDER HEADER DATASET")
print("=" * 30)

#Data Exploration using dataset 1

print("\nFirst 5 Records")
print(header.head())

print("\nLast 5 Records")
print(header.tail())

print("\nShape")
print(header.shape)

print("\nColumn Names")
print(header.columns)

print("\nInformation")
print(header.info())

print("\nStatistical Summary")
print(header.describe())

print("\n")
print("=" * 30)
print("SALES ORDER DETAIL DATASET")
print("=" * 30)

#Data Exploration using dataset 2

print("\nFirst 5 Records")
print(detail.head())

print("\nLast 5 Records")
print(detail.tail())

print("\nShape")
print(detail.shape)

print("\nColumn Names")
print(detail.columns)

print("\nInformation")
print(detail.info())

print("\nStatistical Summary")
print(detail.describe())

#DATA CLEANING

#Missing Values

print("\n")
print("=" * 30)
print("MISSING VALUES")
print("=" * 30)

print("\nHeader Dataset")
print(header.isnull().sum())

print("\nDetail Dataset")
print(detail.isnull().sum())

#Duplicate Records

print("\n")
print("=" * 30)
print("DUPLICATE RECORDS")
print("=" * 30)

print("Header Dataset :", header.duplicated().sum())
print("Detail Dataset :", detail.duplicated().sum())

# Remove duplicates

header = header.drop_duplicates()
detail = detail.drop_duplicates()

#Merging the 2 datasets

sales = pd.merge(
    header,
    detail,
    on="SalesOrderID"
)

print("\n")
print("=" * 30)
print("MERGED DATASET")
print("=" * 30)

print("Shape :", sales.shape)

print("\nFirst 5 Records")
print(sales.head())


#FEATURE ENGINEERING

# Creating Revenue Column
sales["Revenue"] = (
    sales["OrderQty"]
    * sales["UnitPrice"]
    * (1 - sales["UnitPriceDiscount"])
)

# Converting OrderDate into Date Format
sales["OrderDate"] = pd.to_datetime(sales["OrderDate"])

# Creating Month Column
sales["Month"] = sales["OrderDate"].dt.month_name()

# Creating a new Column
sales["Year"] = sales["OrderDate"].dt.year

#Revenue Info

print("=" * 30)
print("REVENUE ANALYSIS")
print("=" * 30)

print("Total Revenue :", sales["Revenue"].sum())

print("Average Revenue :", sales["Revenue"].mean())

print("Maximum Revenue :", sales["Revenue"].max())

print("Minimum Revenue :", sales["Revenue"].min())

#Saving final dataset 

sales.to_excel(
    "cleaned_Data.xlsx",
    index=False
)

print("\n")
print("=" * 30)
print("Cleaned Dataset Saved Successfully!")
print("File - cleaned_Data.xlsx")
print("=" * 30)