from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained pipeline (RandomForest, XGBoost, etc.)
model = joblib.load('model/model.pkl')

@app.route('/', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        try:
            # Get form data
            job_title = request.form['job_title']
            experience_level = request.form['experience_level']
            employment_type = request.form['employment_type']
            company_size = request.form['company_size']
            remote_ratio = float(request.form['remote_ratio'])
            years_experience = float(request.form['years_experience'])
            base_salary = float(request.form['base_salary'])
            bonus = float(request.form['bonus'])
            stock_options = float(request.form['stock_options'])

            # Create input DataFrame
            input_df = pd.DataFrame([{
                'job_title': job_title,
                'experience_level': experience_level,
                'employment_type': employment_type,
                'company_size': company_size,
                'remote_ratio': remote_ratio,
                'years_experience': years_experience,
                'base_salary': base_salary,
                'bonus': bonus,
                'stock_options': stock_options,

                # Include these if they were in training
                'company_location': 'United States',
                'salary_currency': 'USD',
                'currency': 'USD'
            }])

            # Make prediction
            predicted_salary = model.predict(input_df)[0]
            prediction = f"${predicted_salary:,.2f}"

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("form.html", prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True,port=8000)
