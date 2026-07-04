import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales = pd.read_excel("Cleaned_Data.xlsx")

print("=" * 30)
print("DATA VISUALIZATION")
print("=" * 30)

# Bar Chart
# Top 10 Products by Revenue

product_sales = sales.groupby("ProductID")["Revenue"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))

plt.bar(product_sales.index, product_sales.values)
plt.title("Top 10 Products by Revenue")
plt.xlabel("Product ID")
plt.ylabel("Revenue")
plt.show()
plt.savefig("barGraph.png")

# Line Chart
# Monthly Revenue

monthly_revenue = sales.groupby("Month")["Revenue"].sum()

plt.figure(figsize=(10,5))

plt.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
plt.savefig("LineChart.png")

# Histogram
# Revenue Distribution

plt.figure(figsize=(8,5))

plt.hist(
    sales["Revenue"],
    bins=20
)

plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()
plt.savefig("histogram.png")

# Scatter Plot
# Quantity vs Revenue

plt.figure(figsize=(8,5))

plt.scatter(
    sales["OrderQty"],
    sales["Revenue"]
)

plt.title("Quantity vs Revenue")
plt.xlabel("Order Quantity")
plt.ylabel("Revenue")
plt.show()
plt.savefig("ScatterPlot.png")
#  Heatmap
# Between Numeric Columns

numeric_data = sales[
    [
        "OrderQty",
        "UnitPrice",
        "UnitPriceDiscount",
        "Revenue"
    ]
]
plt.figure(figsize=(8,5))
sns.heatmap(
    numeric_data.corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()
plt.savefig("heatmap.png")
