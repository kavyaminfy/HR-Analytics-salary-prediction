# 💼 Salary Prediction Machine Learning Project

A **machine learning-powered salary prediction system** that accurately forecasts total compensation based on job characteristics, experience, and company details. The project integrates **advanced ML models** with a **user-friendly Flask web interface** to deliver **real-time salary predictions globally**.

---

## 🚀 Key Features

- **🔍 High-Accuracy Predictions**  
  Random Forest model achieving **99.98% R² score** and **761.82 RMSE**

- **📊 Multi-Factor Analysis**  
  Considers job title, experience level, company size, location, remote work ratio, and compensation components

- **🌐 Global Coverage**  
  Supports multiple currencies (**USD, EUR, GBP, INR**) and locations

- **🖥 Web Interface**  
  Flask-based web application for intuitive user interaction

- **⚡ Real-Time Processing**  
  Instant salary predictions through interactive form input

---

## 🛠️ Tech Stack

| **Category**         | **Tools/Frameworks**                                                   |
|----------------------|------------------------------------------------------------------------|
| Machine Learning     | Random Forest, XGBoost, Gradient Boosting, Ridge, Linear Regression (scikit-learn) |
| Web Framework        | Flask                                                                  |
| Data Processing      | pandas, NumPy                                                          |
| Model Persistence    | joblib                                                                 |
| Development          | Jupyter Notebook                                                       |

---

## 📈 Model Performance

| **Model**             | **RMSE**   | **R² Score** |
|------------------------|------------|--------------|
| ⭐ Random Forest        | 761.82     | 0.9998       |
| XGBoost                | 911.65     | 0.9998       |
| Gradient Boosting      | 2721.26    | 0.9978       |
| Ridge Regression       | 16433.69   | 0.9204       |
| Linear Regression      | 16433.71   | 0.9204       |

✅ **Random Forest** selected for deployment due to best overall performance.

---

## 🎯 Input Features

### 🧾 Job Details:
- Job Title  
- Experience Level  
- Employment Type  

### 🏢 Company Information:
- Company Size  
- Location  

### 🏠 Work Arrangement:
- Remote Work Percentage  

### 👩‍💻 Professional Experience:
- Years of Experience  

### 💰 Compensation Details:
- Base Salary  
- Bonus  
- Stock Options  

---

## 🔄 Model Pipeline

1. **Data Preprocessing**  
   - OneHotEncoder for categorical features  
   - Numerical features passed through as-is  

2. **Feature Engineering**  
   - 7 categorical + 5 numerical features selected  

3. **Model Training**  
   - Compared five different algorithms  

4. **Model Selection**  
   - Chose Random Forest based on performance metrics  

5. **Deployment**  
   - Saved model using `joblib`  
   - Integrated into Flask app for real-time predictions  

---

## 📊 Key Achievements

✅ Achieved **99.98% prediction accuracy** using Random Forest  
✅ Supported **multi-currency prediction** for global applicability  
✅ Developed a **robust preprocessing pipeline** with error handling  
✅ Built a **production-ready Flask web app**  
✅ Ensured **scalability and extensibility** for future improvements  


# Ml flow

![image](https://github.com/user-attachments/assets/9ab7db0c-b8e9-4ae5-8dc8-f2895ca65a0a)

## RandomForestRegressor
![image](https://github.com/user-attachments/assets/5c772335-3d63-4d4a-97e7-8782d648ba71)

## LinearRegression
![image](https://github.com/user-attachments/assets/49b021c5-d747-4f1e-9118-226e2d96fa65)

## XGBoostRegressor
![image](https://github.com/user-attachments/assets/db58344c-b28a-4933-82df-79e387a3e9cd)

## GradientBoostingRegressor
![image](https://github.com/user-attachments/assets/63aa45c8-1af6-4b33-8edb-81e13d743be0)

## RidgeRegression
![image](https://github.com/user-attachments/assets/4df488d5-a860-4d8c-bfec-f8b34c7187bf)

## Best Model Register
![image](https://github.com/user-attachments/assets/28068631-4bc3-419a-894b-6b58a833275c)
![image](https://github.com/user-attachments/assets/ac532321-3db6-4a32-8f1a-bc4cda53dcbf)

## Data drift
![image](https://github.com/user-attachments/assets/e40ae2e0-2296-4785-a399-14ffc1b7bd51)

# Flask
![Screenshot 2025-07-07 114304](https://github.com/user-attachments/assets/6bcda5c4-af9c-440c-ad28-5661b93f4b23)
![Screenshot 2025-07-07 114428](https://github.com/user-attachments/assets/cc5b1c70-8a78-489c-8585-5489f299dd8d)

# Airflow

![image](https://github.com/user-attachments/assets/ff7e328f-381e-4696-ba33-a3a0883ca1ed)
![image](https://github.com/user-attachments/assets/112ab824-90bc-4fde-9486-8ea7b8f9978f)

