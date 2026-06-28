import matplotlib.pyplot as plt
import os


def ensure_folder():
    if not os.path.exists("charts"):
        os.makedirs("charts")


# ---------------- REGION ----------------
def plot_region_sales(df):
    ensure_folder()

    df = df.sort_values("sales", ascending=False)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(df["region"], df["sales"], color="#4C78A8")

    plt.title("Region-wise Sales Performance", fontweight="bold")
    plt.xlabel("Region")
    plt.ylabel("Sales")

    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, h, f"{h:,.0f}",
                 ha="center", va="bottom", fontsize=9)

    plt.grid(axis="y", linestyle="--", alpha=0.3)
    plt.tight_layout()

    plt.savefig("charts/region_sales.png", dpi=300)
    plt.show()


# ---------------- CATEGORY ----------------
def plot_category_sales(df):
    ensure_folder()

    df = df.sort_values("sales", ascending=False)

    plt.figure(figsize=(10, 6))
    bars = plt.bar(df["category"], df["sales"], color="#F58518")

    plt.title("Category-wise Sales Distribution", fontweight="bold")
    plt.xlabel("Category")
    plt.ylabel("Sales")

    for bar in bars:
        h = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, h, f"{h:,.0f}",
                 ha="center", va="bottom", fontsize=9)

    plt.grid(axis="y", linestyle="--", alpha=0.3)
    plt.tight_layout()

    plt.savefig("charts/category_sales.png", dpi=300)
    plt.show()


# ---------------- MONTHLY ----------------
def plot_monthly_sales(df):
    ensure_folder()

    plt.figure(figsize=(10, 6))
    plt.plot(df["month"], df["sales"], marker="o", linewidth=2, color="#54A24B")

    plt.title("Monthly Sales Trend", fontweight="bold")
    plt.xlabel("Month")
    plt.ylabel("Sales")

    plt.xticks(rotation=45)
    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.savefig("charts/monthly_sales.png", dpi=300)
    plt.show()