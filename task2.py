import pandas as pd

sales = pd.read_excel("Cleaned_Data.xlsx")

print("=" * 30)
print("WORKS SALES ANALYSIS")
print("=" * 30)

#Product wise
print("=" * 30)
print("PRODUCT-WISE SALES")
print("=" * 30)

product_sales = sales.groupby("ProductID")["Revenue"].sum().sort_values(ascending=False)

print(product_sales)

print("\nTop 10 Products")
print(product_sales.head(10))

#Customer wise
print("\n")
print("=" * 30)
print("CUSTOMER-WISE REVENUE")
print("=" * 30)

customer_revenue = sales.groupby("CustomerID")["Revenue"].sum().sort_values(ascending=False)

print(customer_revenue)

print("\nTop 10 Customers")
print(customer_revenue.head(10))

#Sales-person wise
print("\n")
print("=" * 30)
print("SALESPERSON-WISE REVENUE")
print("=" * 30)

salesperson_revenue = sales.groupby("SalesPersonID")["Revenue"].sum().sort_values(ascending=False)

print(salesperson_revenue)

#Monthly Revenue
print("\n")
print("=" * 30)
print("MONTHLY REVENUE")
print("=" * 30)

monthly_revenue = sales.groupby("Month")["Revenue"].sum()

print(monthly_revenue)
