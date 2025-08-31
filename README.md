# 🛡️ Insurance Claim Fraud Prediction  

A complete **end-to-end Data Science project** to predict fraudulent insurance claims.  
This project demonstrates **data engineering, SQL analysis, exploratory data analysis (EDA), machine learning, model optimization, and deployment** using a dataset of 5,000 records.

---
Live Project Link : https://insurance-claim-fraud-prediction.streamlit.app/
---

## 🔹 1. Dataset  
- **Used 5,000 records** with messy real-world challenges:
  - Missing values  
  - Inconsistent categorical formats (e.g., `Male`, `M`, `male`)  
  - Outliers in claim amounts & hospital bills  
  - Noisy policy & hospital names  
- Contains features such as **policy details, vehicle info, customer demographics, claim history, claim amount, incident severity**, and target: **fraud_reported**.  

---

## 🔹 2. Data Cleaning (Pandas)  
✔ Removed duplicates  
✔ Imputed missing values (mode/median)  
✔ Fixed wrong data types  
✔ Standardized categorical values  
✔ Converted dates to proper datetime  
✔ Treated outliers using IQR  
✔ Fixed negative values  

---

## 🔹 3. Database (MySQL + SQL Analysis)  
The cleaned dataset was stored in a **MySQL database**. Example SQL queries performed:  
1. Total claims count  
2. Average claim amount by fraud status  
3. Fraud distribution by policy type  
4. Top hospitals with fraud cases  
5. Incident severity patterns in fraud cases  
6. Policyholder history vs fraud probability  
7. Vehicle age group vs fraud detection  

---

## 🔹 4. Exploratory Data Analysis (EDA)  
Using **Pandas, Matplotlib, Seaborn**:  
- Fraud vs Non-Fraud distribution  
- Claim amount distribution (outliers, skewness)  
- Average claim amount by policy type  
- Incident severity vs fraud detection  
- Gender & vehicle age effect on fraud probability  
- Hospital-specific fraud patterns  
- Doctor fee vs claim amount correlation  

---

## 🔹 5. Machine Learning Models  

### 🟢 Classification (Fraud Detection)  
- Logistic Regression  
- Decision Tree  
- Random Forest  
- XGBoost  
**Metrics:** Accuracy, Precision, Recall, F1, ROC-AUC  

### 🟢 Regression (Claim Amount Prediction)  
- Linear Regression  
- Gradient Boosting Regressor  
**Metrics:** RMSE, MAE, R²  

### 🟢 Clustering (Unsupervised Fraud Insights)  
- KMeans clustering with PCA visualization  

---

## 🔹 6. Hyperparameter Tuning  
- **GridSearchCV** → Random Forest  
- **RandomizedSearchCV** → XGBoost  

---

## 🔹 7. Model Evaluation  
- **Classification:** Accuracy, Precision, Recall, F1, ROC-AUC, Confusion Matrix  
- **Regression:** RMSE, MAE, R², Cross-validation  
- Best model: **Random Forest (Fraud Detection)** with optimized recall  

---

## 🔹 8. Deployment (Streamlit)  
- Best fraud detection model saved with **Joblib**  
- Built a **Streamlit app** for real-time fraud prediction  

## 🚀 9. Tools & Technologies
- Python: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, XGBoost
- Database: MySQL
- Model Deployment: Streamlit, Joblib
- ML Techniques: Classification, Regression, Clustering, Hyperparameter Tuning

## 📊 10. Example Use Case
- A claims officer enters policy details, claim amount, hospital, and customer history → model predicts fraud probability in real-time.


