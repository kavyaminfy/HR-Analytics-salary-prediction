# scripts/train.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
from scripts.config import MODEL_PATH, MLFLOW_TRACKING_URI

def run_training():
    mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

    df = pd.read_csv("preprocessed_data.csv")
    y = df['adjusted_total_usd']
    X = df.drop(columns=['adjusted_total_usd'])

    cat_cols = X.select_dtypes(include='object').columns.tolist()
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols)
    ], remainder='passthrough')

    model = Pipeline([
        ('preprocessor', preprocessor),
        ('regressor', RandomForestRegressor(random_state=42))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    rmse = mean_squared_error(y_test, y_pred, squared=False)
    r2 = r2_score(y_test, y_pred)

    with mlflow.start_run(run_name="rf_airflow"):
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.sklearn.log_model(model, artifact_path="model", registered_model_name="SalaryPredictorAirflow")

    joblib.dump(model, MODEL_PATH)

if __name__ == "__main__":
    run_training()
