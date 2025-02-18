# 🚗 Predicting Average Price of Used Cars

![Python](https://img.shields.io/badge/Python-3.8-blue)
![Machine Learning](https://img.shields.io/badge/ML-Regression-orange)
![Data](https://img.shields.io/badge/Data-Used%20Cars-green)

## 📌 Project Overview
This project aims to predict the average price of used cars using **machine learning models**. By analyzing key features such as mileage, brand, model, fuel type, and repair status, we build regression models to assist buyers in making **data-driven decisions** while purchasing second-hand cars.

## 📂 Dataset
- **Source**: [Used Cars Dataset](https://data.world/data-society/used-cars-data)
- **Size**: 370,000 rows, 20 columns
- **Key Features**:
  - `name`: Car name
  - `seller`: Private or dealer
  - `vehicleType`: Sedan, SUV, Coupe, etc.
  - `yearOfRegistration`: Year the car was registered
  - `gearbox`: Automatic or Manual
  - `kilometer`: Total kilometers driven
  - `fuelType`: Diesel, Petrol, Electric, etc.
  - `notRepairedDamage`: Indicates unrepaired damage
  - `price`: Target variable (used car price)

## 🛠 Tools & Technologies
- **Programming Language**: Python (v3.8)
- **Libraries**: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `xgboost`
- **Machine Learning Models**:
  - Decision Tree Regressor
  - Random Forest Regressor
  - XGBoost Regressor
  - Support Vector Regressor
  - Lasso & Ridge Regression
  - Gradient Boosting Regressor

## 🔍 Data Processing
1. **Data Cleaning**
   - Removed missing & duplicate values
   - Translated German categorical values into English
   - Converted categorical variables using **One-Hot Encoding**
2. **Feature Selection**
   - Removed redundant columns
   - Engineered new features (`age_of_car`, `mileage_per_year`)
3. **Scaling & Normalization**
   - Applied **MinMax Scaling** for numeric features
   - Used **Log Transformation** for skewed distributions

## 📊 Exploratory Data Analysis (EDA)
- **Feature Correlation**: Identified key features affecting price.
- **Distribution Analysis**: Checked price distribution using **histograms & boxplots**.
- **Outlier Detection**: Used **IQR method** to handle extreme values.
- **Trend Analysis**: Observed price variations across car brands, fuel types, and gearbox types.

## 🤖 Model Training & Evaluation
### ✅ Model Performance Metrics
- **R² Score**: Measures model accuracy
- **Mean Absolute Error (MAE)**: Average absolute errors in predictions
- **Mean Squared Error (MSE)**: Penalizes large errors
- **Root Mean Squared Error (RMSE)**: Square root of MSE

| Model                      | R² Score | RMSE |
|----------------------------|---------|------|
| Decision Tree Regressor    | 0.74    | 2223 |
| Random Forest Regressor    | 0.82    | 1805 |
| XGBoost Regressor          | 0.85    | 1720 |
| Support Vector Regressor   | 0.76    | 2105 |
| Lasso Regression           | 0.74    | 2223 |
| Ridge Regression           | 0.75    | 2205 |
| Gradient Boosting Regressor| 0.86    | 1698 |

### 🔥 Best Performing Model: **XGBoost & Gradient Boosting**
- **Feature Importance**: Mileage, car age, brand, fuel type
- **Hyperparameter Tuning**: Used **Grid Search CV** for optimal settings.

## 🚀 Installation & Usage
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/used-car-price-prediction.git
cd used-car-price-prediction
```
### 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/used-car-price-prediction.git
cd used-car-price-prediction
```
### 📦 Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```
### 🚀 Running the Project
```bash
# Start Jupyter notebook
jupyter notebook
