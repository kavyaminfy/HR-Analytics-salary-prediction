# scripts/preprocess.py
import pandas as pd
from sqlalchemy import create_engine
from scripts.config import DB_URI, TABLE_NAME

def load_data():
    engine = create_engine(DB_URI)
    return pd.read_sql(f"SELECT * FROM {TABLE_NAME}", engine)

def preprocess_data(df):
    # Drop unnecessary columns
    df.drop(columns=['education', 'skills', 'company_location', 'salary_currency', 'currency',
                     'total_salary', 'salary_in_usd', 'conversion_rate'], errors='ignore', inplace=True)

    # Normalize job titles
    job_title_map = {
        'sofware engneer': 'Software Engineer',
        'software engr': 'Software Engineer',
        'softwre engineer': 'Software Engineer',
        'ml engr': 'ML Engineer',
        'ml enginer': 'ML Engineer',
        'machine learning engr': 'ML Engineer',
        'dt scientist': 'Data Scientist',
        'data scntist': 'Data Scientist',
        'data scienist': 'Data Scientist',
    }

    df['job_title'] = df['job_title'].str.lower().str.strip().replace(job_title_map)
    df['job_title'] = df['job_title'].str.title()

    # Fill missing
    df['experience_level'].fillna(df['experience_level'].mode()[0], inplace=True)
    df['employment_type'].fillna(df['employment_type'].mode()[0], inplace=True)

    # Remove outliers
    for col in ['base_salary', 'bonus', 'stock_options', 'adjusted_total_usd']:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        df = df[(df[col] >= q1 - 1.5 * iqr) & (df[col] <= q3 + 1.5 * iqr)]

    df.drop_duplicates(inplace=True)
    return df

def run_preprocessing():
    df = load_data()
    df = preprocess_data(df)
    df.to_csv("preprocessed_data.csv", index=False)

if __name__ == "__main__":
    run_preprocessing()
