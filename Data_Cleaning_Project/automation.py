from cleaning import load_and_clean_data

from analysis import (
    business_kpis,
    region_sales,
    category_sales,
    subcategory_sales,
    monthly_sales
)

from visualization import (
    plot_region_sales,
    plot_category_sales,
    plot_monthly_sales
)

import os


# ===========================
# REPORT GENERATION
# ===========================
def generate_summary_report(df, region, category, subcategory, monthly):
    os.makedirs("reports", exist_ok=True)

    top_region = region.sort_values("sales", ascending=False).head(1)
    top_category = category.sort_values("sales", ascending=False).head(1)
    top_subcategory = subcategory.sort_values("sales", ascending=False).head(1)
    top_month = monthly.sort_values("sales", ascending=False).head(1)

    with open("reports/summary.txt", "w", encoding="utf-8") as f:
        f.write("=====================================\n")
        f.write(" DATA CLEANING & AUTOMATION REPORT\n")
        f.write("=====================================\n\n")

        f.write("📊 KPI METRICS\n")
        f.write(f"Total Sales: {df['sales'].sum():.2f}\n")
        f.write(f"Total Orders: {len(df)}\n")
        f.write(f"Average Sales: {df['sales'].mean():.2f}\n\n")

        f.write("🏆 TOP REGION\n")
        f.write(top_region.to_string(index=False))
        f.write("\n\n")

        f.write("🏆 TOP CATEGORY\n")
        f.write(top_category.to_string(index=False))
        f.write("\n\n")

        f.write("🏆 TOP SUB-CATEGORY\n")
        f.write(top_subcategory.to_string(index=False))
        f.write("\n\n")

        f.write("📅 TOP MONTH (HIGHEST SALES)\n")
        f.write(top_month.to_string(index=False))
        f.write("\n\n")

        f.write("=====================================\n")
        f.write(" END OF REPORT\n")
        f.write("=====================================\n")


# ===========================
# INSIGHTS GENERATION (NEW ⭐)
# ===========================
def print_insights(df, region, category, subcategory, monthly):

    print("\n=====================================")
    print("📌 BUSINESS INSIGHTS")
    print("=====================================\n")

    top_region = region.loc[region["sales"].idxmax()]
    top_category = category.loc[category["sales"].idxmax()]
    top_subcategory = subcategory.loc[subcategory["sales"].idxmax()]
    top_month = monthly.loc[monthly["sales"].idxmax()]

    print(f"🔥 Top Performing Region: {top_region['region']} ({top_region['sales']:.2f})")
    print(f"🔥 Top Category: {top_category['category']} ({top_category['sales']:.2f})")
    print(f"🔥 Top Sub-Category: {top_subcategory['sub-category']} ({top_subcategory['sales']:.2f})")
    print(f"🔥 Highest Sales Month: {top_month['month']} ({top_month['sales']:.2f})")

    print("\n💡 Key Insight:")
    print("Sales performance is driven mainly by top category and region trends.")
    print("Focus marketing efforts on top-performing regions for higher ROI.")


# ===========================
# MAIN PIPELINE
# ===========================
def main():

    # Load dataset
    df = load_and_clean_data()

    # KPI
    business_kpis(df)

    # Analysis
    region = region_sales(df)
    category = category_sales(df)
    subcategory = subcategory_sales(df)
    monthly = monthly_sales(df)

    # Print tables
    print("\nREGION SALES:\n", region)
    print("\nCATEGORY SALES:\n", category)
    print("\nSUBCATEGORY SALES:\n", subcategory)
    print("\nMONTHLY SALES:\n", monthly)

    # Insights (NEW ⭐)
    print_insights(df, region, category, subcategory, monthly)

    # Visualizations
    plot_region_sales(region)
    plot_category_sales(category)
    plot_monthly_sales(monthly)

    # Report generation
    generate_summary_report(df, region, category, subcategory, monthly)

    print("\n✅ Automation Completed Successfully!")
    print("📁 Report saved in: reports/summary.txt")


if __name__ == "__main__":
    main()