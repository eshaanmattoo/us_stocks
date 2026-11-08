import pandas as pd
from datetime import datetime

def get_filtered_companies(
    csv_path="nasdaq_USA.csv",
    min_market_cap=0,  # $10 Billion (Large-Cap threshold)
    min_years_since_ipo=0,
    current_year=None
):
    if current_year is None:
        current_year = datetime.now().year

    max_ipo_year = current_year - min_years_since_ipo

    # Load dataset
    df = pd.read_csv(csv_path)

    # Clean Symbol and Name strings
    df["Symbol"] = df["Symbol"].astype(str).str.strip()
    df["Name"] = df["Name"].astype(str).str.strip()

    # Ensure numeric types for filtering
    df["Market Cap"] = pd.to_numeric(df["Market Cap"], errors="coerce")
    df["IPO Year"] = pd.to_numeric(df["IPO Year"], errors="coerce")

    # Filter by Market Cap and IPO Year
    filtered_df = df[
        (df["Market Cap"] >= min_market_cap) &
        (df["IPO Year"] <= max_ipo_year)
    ].sort_values(by="Market Cap", ascending=False)

    symbols_list = filtered_df["Symbol"].tolist()
    names_list = filtered_df["Name"].tolist()

    return symbols_list, names_list, filtered_df


if __name__ == "__main__":
    # Adjust min_market_cap as needed (e.g., 2e9 for $2B+, 10e9 for $10B+, 100e9 for $100B+)
    symbols, names, filtered_data = get_filtered_companies(
        csv_path="nasdaq_USA.csv",
        min_market_cap=0,
        min_years_since_ipo=0,
        current_year=2026
    )

    print(f"Total companies matched: {len(symbols)}\n")
    print("Symbols List:")
    print(symbols)