# 📊 Assignment 5 – Data Cleaning and Data Model Building using Python

---

## 🎯 AIM

To perform different data cleaning and data model building operations using Python on:

- Air Quality Dataset
- Heart Disease Dataset

---

## 🎯 OBJECTIVES

- To learn data processing methods
- To understand preprocessing techniques
- To perform data cleaning and transformation
- To build a predictive model
- To understand the complete data analysis value chain

---

# 📘 THEORY

## 📌 Data Analysis Value Chain

A statistical analysis project follows a structured pipeline:

Raw Data  
↓  
Technically Correct Data  
↓  
Consistent Data  
↓  
Statistical Results  
↓  
Formatted Output  

Each stage increases the value of data.

---

# 📂 DATASETS USED

## 1️⃣ Air Quality Dataset
Contains:
- City
- PM2.5
- NO2
- SO2
- Temperature

Issues present:
- Missing values
- Possible outliers

---

## 2️⃣ Heart Disease Dataset
Contains:
- PatientID
- Age
- Cholesterol
- BloodPressure
- HeartDisease (Target variable)

Issues present:
- Missing values
- Extreme cholesterol value (outlier)
- Need for scaling before model building

---

# 🔹 (a) DATA CLEANING

Data cleaning improves data quality before analysis.

---

## 1️⃣ Missing Value Treatment

Missing values are represented as NaN.

We handled missing values using:

- Mean (for normally distributed data)
- Median (for skewed data or outlier-prone data)

Example:

```python
heart_df['Cholesterol'] = heart_df['Cholesterol'].fillna(
    heart_df['Cholesterol'].median()
)
```

Why median?
Because it is robust to extreme values.

---

## 2️⃣ Outlier Detection and Treatment

Outliers were detected using the IQR (Interquartile Range) method.

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR  
Upper Bound = Q3 + 1.5 × IQR  

Extreme values were capped to upper bound.

Purpose:
- Prevent model bias
- Improve prediction stability

---

# 🔹 (b) DATA INTEGRATION

Data Integration means combining multiple datasets.

Performed using:

```python
pd.concat()
```

Used when:
- Data comes from multiple sources
- Combining different files into one dataset

---

# 🔹 (c) DATA TRANSFORMATION

Data transformation prepares data for modeling.

---

## 1️⃣ Feature Scaling (Standardization)

Performed using StandardScaler.

Formula:

Scaled Value = (x − mean) / standard deviation

Effect:
- Mean becomes 0
- Standard deviation becomes 1

Why needed?
Machine learning models perform better when features are on similar scale.

---

## 2️⃣ Skewness Correction (Log Transformation)

If data is highly right-skewed:

```python
np.log(value + 1)
```

Purpose:
- Normalize distribution
- Reduce impact of extreme values

---

# 🔹 (d) ERROR CORRECTING

Error correction includes:

- Fixing data types
- Removing invalid entries
- Correcting inconsistent values

Example:

```python
heart_df['Age'] = heart_df['Age'].astype(int)
```

---

# 🔹 (e) DATA MODEL BUILDING

We built a Logistic Regression model.

---

## 1️⃣ Why Logistic Regression?

Because:
- Target variable (HeartDisease) is binary (0 or 1)
- Logistic regression is suitable for binary classification

---

## 2️⃣ Steps Performed

1. Selected predictor variables:
   - Age
   - Cholesterol
   - BloodPressure

2. Selected target variable:
   - HeartDisease

3. Split dataset:
   - 70% Training
   - 30% Testing

4. Trained model

5. Evaluated using accuracy score

---

# 📊 MODEL EVALUATION

Accuracy Score measures:

Correct Predictions / Total Predictions

Higher accuracy indicates better model performance.

---

# 🧠 IMPORTANT CONCEPTS LEARNED

✔ Handling Missing Values  
✔ Difference between Mean and Median Imputation  
✔ Outlier Detection using IQR  
✔ Feature Scaling  
✔ Log Transformation  
✔ Data Integration  
✔ Error Correction  
✔ Train-Test Split  
✔ Logistic Regression Model  

---

# 🎓 VIVA QUESTIONS

### Q1: Why is data cleaning necessary?
Because raw data may contain missing values, inconsistencies, and errors that affect analysis.

### Q2: Why use median instead of mean?
Median is less affected by extreme values.

### Q3: Why scaling is important?
Because models like Logistic Regression are sensitive to feature magnitude.

### Q4: What is IQR?
Interquartile Range = Q3 − Q1, used to detect outliers.

### Q5: Why split data into train and test?
To evaluate model performance on unseen data.

### Q6: What happens if we do not treat outliers?
Model may become biased and inaccurate.

---

# ✅ CONCLUSION

In this assignment, we implemented a complete data preprocessing and modeling pipeline.

We started with raw datasets containing:
- Missing values
- Outliers
- Inconsistent data

We applied:
- Cleaning techniques
- Transformation techniques
- Scaling
- Error correction

Finally, we built a Logistic Regression model for heart disease prediction.

This assignment demonstrates the real-world workflow of data science projects, where raw data is transformed into meaningful insights through systematic preprocessing and modeling.

---

This assignment builds a strong foundation in data analytics and machine learning pipelines.