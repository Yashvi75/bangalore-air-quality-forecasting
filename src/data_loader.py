import pandas as pd

def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        print("✅ Data loaded successfully")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None


if __name__ == "__main__":
    file_path = "/Users/yashvivyas/Documents/bangalore-air-quality-forecasting/data/city_day.csv"
    df = load_data(file_path)

    if df is not None:
        print("\n--- First 5 Rows ---")
        print(df.head())

        print("\n--- Dataset Info ---")
        print(df.info())

        print("\n--- Missing Values ---")
        print(df.isnull().sum())