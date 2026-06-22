import pandas as pd
import matplotlib.pyplot as plt
import os

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Load dataset
df = pd.read_csv("SampleSuperstore.csv", encoding="latin1")

# ============================
# KPI ANALYSIS
# ============================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
average_sales = df["Sales"].mean()
total_orders = len(df)

print("========== SALES ANALYSIS ==========")
print("Total Sales: $", round(total_sales, 2))
print("Total Profit: $", round(total_profit, 2))
print("Average Sales: $", round(average_sales, 2))
print("Total Orders:", total_orders)

# ============================
# CATEGORY ANALYSIS
# ============================

category_sales = df.groupby("Category")["Sales"].sum()

print("\n========== CATEGORY ANALYSIS ==========")
print(category_sales)

# ============================
# REGION ANALYSIS
# ============================

region_sales = df.groupby("Region")["Sales"].sum()

print("\n========== REGION ANALYSIS ==========")
print(region_sales)

# ============================
# PROFIT BY CATEGORY
# ============================

category_profit = df.groupby("Category")["Profit"].sum()

print("\n========== PROFIT BY CATEGORY ==========")
print(category_profit)

# ============================
# TOP 10 STATES
# ============================

top_states = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 STATES ==========")
print(top_states)

# ============================
# SALES BY CATEGORY
# ============================

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("charts/category_sales.png")

# ============================
# SALES BY REGION
# ============================

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("charts/region_sales.png")

# ============================
# PROFIT BY CATEGORY
# ============================

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/profit_category.png")

# ============================
# TOP STATES
# ============================

plt.figure(figsize=(10,5))
top_states.plot(kind="bar")

plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/top_states.png")

# ============================
# SEGMENT ANALYSIS
# ============================

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(7,7))
segment_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sales by Segment")
plt.ylabel("")

plt.savefig("charts/segment_sales.png")

# ============================
# DISCOUNT VS PROFIT
# ============================

plt.figure(figsize=(8,5))

plt.scatter(
    df["Discount"],
    df["Profit"]
)

plt.title("Discount vs Profit")

plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/discount_profit.png")

plt.show()

print("\nCharts saved successfully in charts folder.")

# ============================
# SEGMENT ANALYSIS
# ============================

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(7,7))
segment_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sales by Segment")
plt.ylabel("")

plt.tight_layout()

plt.savefig("segment_sales.png")

# ============================
# DISCOUNT VS PROFIT
# ============================

plt.figure(figsize=(8,5))

plt.scatter(
    df["Discount"],
    df["Profit"]
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("discount_profit.png")

plt.show()
