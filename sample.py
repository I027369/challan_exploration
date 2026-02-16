# ==============================
# Indian E-Challan EDA Script
# ==============================

# Core
import numpy as np
import pandas as pd

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Stats / TS
from scipy import stats
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

# Settings
pd.set_option("display.max_columns", None)
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (14, 6)


def main():

    # ==============================
    # Load Data
    # ==============================
    df = pd.read_csv("../data/echallan_daily_data.csv")

    # Convert date safely
    df["date"] = pd.to_datetime(
        df["date"],
        dayfirst=True,
        errors="coerce",
        format="mixed"
    )

    # Drop invalid dates if any
    df = df.dropna(subset=["date"])

    df = df.sort_values("date").reset_index(drop=True)

    print("\nDataset Info:")
    print(df.info())

    # ==============================
    # Integrity Checks
    # ==============================
    df["amount_check"] = df["pendingAmount"] + df["disposedAmount"]
    df["challan_check"] = df["pendingChallan"] + df["disposedChallan"]
    df["court_check"] = df["pendingCourt"] + df["disposedCourt"]

    print("\nIntegrity Checks:")
    print("Amount mismatch rows:",
          (df["amount_check"] != df["totalAmount"]).sum())
    print("Challan mismatch rows:",
          (df["challan_check"] != df["totalChallan"]).sum())
    print("Court mismatch rows:",
          (df["court_check"] != df["totalCourt"]).sum())

    df.drop(columns=["amount_check", "challan_check",
            "court_check"], inplace=True)

    # ==============================
    # Feature Engineering
    # ==============================

    df["disposal_rate"] = df["disposedChallan"] / \
        df["totalChallan"].replace(0, np.nan)

    df["court_rate"] = df["totalCourt"] / \
        df["totalChallan"].replace(0, np.nan)

    df["avg_fine"] = df["totalAmount"] / \
        df["totalChallan"].replace(0, np.nan)

    df["realization_rate"] = df["disposedAmount"] / \
        df["totalAmount"].replace(0, np.nan)

    df["backlog_ratio"] = df["pendingChallan"] / \
        df["disposedChallan"].replace(0, np.nan)

    print("\nSummary Statistics:")
    print(df.describe())

    # ==============================
    # Time Series Setup
    # ==============================
    df.set_index("date", inplace=True)

    # ==============================
    # Daily Trend
    # ==============================
    sns.lineplot(data=df["totalChallan"])
    plt.title("Daily Total Challans Issued")
    plt.show()

    # ==============================
    # Monthly Aggregation (pandas 2.2+)
    # ==============================
    monthly = df.resample("ME").sum(numeric_only=True)

    sns.lineplot(data=monthly["totalChallan"])
    plt.title("Monthly Total Challans Trend")
    plt.show()

    # ==============================
    # Yearly Aggregation
    # ==============================
    yearly = df.resample("YE").sum(numeric_only=True)

    yearly["YoY_growth_%"] = yearly["totalChallan"].pct_change() * 100

    print("\nYearly Growth:")
    print(yearly[["totalChallan", "YoY_growth_%"]])

    # ==============================
    # Weekday Analysis
    # ==============================
    df["weekday"] = df.index.day_name()

    sns.boxplot(data=df, x="weekday", y="totalChallan")
    plt.xticks(rotation=45)
    plt.title("Challans by Weekday")
    plt.show()

    # ==============================
    # Revenue vs Volume
    # ==============================
    sns.scatterplot(
        x=df["totalChallan"],
        y=df["totalAmount"]
    )
    plt.title("Revenue vs Challans Issued")
    plt.show()

    print("\nCorrelation (Revenue vs Volume):")
    print(df[["totalChallan", "totalAmount"]].corr())

    # ==============================
    # Rolling Trend Detection
    # ==============================
    rolling_mean = df["totalChallan"].rolling(180).mean()

    plt.plot(df["totalChallan"], alpha=0.4)
    plt.plot(rolling_mean, color="red")
    plt.title("180-Day Rolling Mean Trend")
    plt.show()

    # ==============================
    # Stationarity Test
    # ==============================
    adf_result = adfuller(df["totalChallan"].dropna())

    print("\nADF Test Results:")
    print("ADF Statistic:", adf_result[0])
    print("p-value:", adf_result[1])


if __name__ == "__main__":
    main()
