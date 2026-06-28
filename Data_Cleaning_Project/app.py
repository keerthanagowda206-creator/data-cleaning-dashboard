import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from cleaning import load_and_clean_data
from analysis import region_sales, category_sales, monthly_sales


# ===========================
# PAGE CONFIG
# ===========================
st.set_page_config(page_title="Industry Sales Dashboard", layout="wide")

st.title("📊 Industry-Level Sales Intelligence Dashboard")
st.markdown("---")

# ===========================
# LOAD DATA
# ===========================
df = load_and_clean_data()

# ===========================
# SIDEBAR FILTERS
# ===========================
st.sidebar.header("🔎 Business Filters")

region_filter = st.sidebar.multiselect(
    "Region",
    df["region"].unique(),
    default=df["region"].unique()
)

category_filter = st.sidebar.multiselect(
    "Category",
    df["category"].unique(),
    default=df["category"].unique()
)

filtered_df = df[
    (df["region"].isin(region_filter)) &
    (df["category"].isin(category_filter))
]

# ===========================
# KPI SECTION (INDUSTRY STYLE)
# ===========================
st.subheader("📊 Executive KPIs")

col1, col2, col3, col4 = st.columns(4)

total_sales = filtered_df["sales"].sum()
total_orders = filtered_df.shape[0]
avg_sales = filtered_df["sales"].mean()
profit_est = total_sales * 0.25

col1.metric("Total Sales", f"{total_sales:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Average Sales", f"{avg_sales:,.2f}")
col4.metric("Estimated Profit", f"{profit_est:,.0f}")

st.markdown("---")

# ===========================
# ANALYSIS
# ===========================
region = region_sales(filtered_df)
category = category_sales(filtered_df)
monthly = monthly_sales(filtered_df)

# ===========================
# REAL CHARTS (MATPLOTLIB CLEAN VERSION)
# ===========================

# REGION
st.subheader("🌍 Region Performance")
fig, ax = plt.subplots()
ax.bar(region["region"], region["sales"])
ax.set_title("Region-wise Sales")
st.pyplot(fig)

st.markdown("---")

# CATEGORY
st.subheader("📦 Category Performance")
fig, ax = plt.subplots()
ax.bar(category["category"], category["sales"])
ax.set_title("Category-wise Sales")
plt.xticks(rotation=20)
st.pyplot(fig)

st.markdown("---")

# MONTHLY TREND
st.subheader("📈 Monthly Sales Trend")
fig, ax = plt.subplots()
ax.plot(monthly["month"], monthly["sales"], marker="o")
ax.set_title("Monthly Sales Trend")
plt.xticks(rotation=45)
st.pyplot(fig)

st.markdown("---")

# ===========================
# INSIGHTS ENGINE (INDUSTRY LEVEL)
# ===========================
st.subheader("💡 Business Intelligence Insights")

top_region = region.sort_values("sales", ascending=False).iloc[0]
top_category = category.sort_values("sales", ascending=False).iloc[0]
top_month = monthly.sort_values("sales", ascending=False).iloc[0]

st.success(f"""
🔥 Top Region: {top_region['region']} ({top_region['sales']:,.0f})  
🔥 Top Category: {top_category['category']} ({top_category['sales']:,.0f})  
🔥 Peak Month: {top_month['month']} ({top_month['sales']:,.0f})
""")

st.info("""
📌 Key Business Insights:
- Revenue is highly concentrated in top-performing regions.
- Category distribution shows clear demand segmentation.
- Monthly trend indicates seasonal variation in sales.
- Business should focus on top regions for expansion strategy.
""")

st.markdown("---")

st.caption("🚀 Industry-Level Data Analytics Project | Python + Streamlit + Pandas")