# 📊 Assignment 6 – Data Preprocessing and Model Building

---

## 🎯 AIM

To perform Data Preprocessing and Model Building using Python on:

- Heart Disease Dataset
- Air Quality Dataset

---

## 🎯 OBJECTIVES

- To understand the concept of Data Preprocessing
- To perform Data Cleaning
- To perform Data Integration
- To perform Data Transformation
- To perform Error Correction
- To build a Machine Learning Model

---

# 📘 INTRODUCTION

Data preprocessing is the most important step in Machine Learning.

Raw data cannot be directly used for model building because it may contain:

- Missing values
- Duplicate records
- Incorrect data types
- Outliers
- Categorical variables

Machine learning algorithms require structured and numerical data.

Hence, preprocessing transforms raw data into clean and usable format.

---

# 📂 DATASETS USED

## 1️⃣ Heart Disease Dataset

This dataset contains medical attributes such as:

- age
- sex
- cp (chest pain type)
- trestbps (resting blood pressure)
- chol (cholesterol)
- thalach (maximum heart rate)
- oldpeak
- slope
- ca
- thal
- target (0 = No Disease, 1 = Disease)

The objective is to predict whether a patient has heart disease or not.

---

## 2️⃣ Air Quality Dataset

This dataset contains pollution parameters such as:

- so2
- no2
- rspm
- spm
- pm2_5
- city
- state
- type

Used for data cleaning and transformation practice.

---

# 🔹 STEP 1 – DATA CLEANING

Data cleaning ensures data quality.

### 1. Checking Data Types

Categorical columns were converted to object type for better interpretation.

### 2. Handling Missing Values

Missing values were replaced using:

- Median (for heart dataset)
- Mean (for air quality dataset)

Median is preferred when data contains outliers.

---

### 3. Removing Duplicate Records

Duplicate rows were detected using:

```python
df.duplicated().sum()
```

Duplicates were removed using:

```python
df.drop_duplicates()
```

---

### 4. Detecting and Removing Outliers

Outliers were detected using:

- Boxplot visualization
- IQR (Interquartile Range) method

Formula:

IQR = Q3 - Q1

Lower Bound = Q1 - 1.5 × IQR  
Upper Bound = Q3 + 1.5 × IQR  

Values outside these bounds were removed.

Outlier removal improves model accuracy.

---

# 🔹 STEP 2 – DATA TRANSFORMATION

Machine learning models require numerical data.

### 1. Encoding Categorical Variables

Categorical columns were converted to numerical format using:

- One Hot Encoding

Why?

Because algorithms cannot understand text categories.

---

### 2. Feature Scaling

StandardScaler was used to normalize features.

Formula:

Scaled Value = (x − mean) / standard deviation

Why scaling is important?

- Prevents one feature from dominating others
- Improves convergence speed
- Improves model stability

---

# 🔹 STEP 3 – DATA INTEGRATION

Data Integration means combining data from multiple sources.

In real-world scenarios, datasets are often stored separately and must be merged.

In this assignment, datasets were loaded and processed independently.

---

# 🔹 STEP 4 – ERROR CORRECTION

Error correction includes:

- Fixing incorrect data types
- Handling unexpected values
- Removing inconsistent entries
- Replacing invalid category values

This ensures accuracy and consistency.

---

# 🔹 STEP 5 – FEATURE MATRIX & TARGET VARIABLE

Independent Variables (X):
All columns except target.

Dependent Variable (y):
target column (Heart Disease outcome)

---

# 🔹 STEP 6 – TRAIN-TEST SPLIT

Dataset was split into:

- 80% Training Data
- 20% Testing Data

Why split data?

Because:

- Training data is used to train model
- Testing data evaluates model performance
- Prevents overfitting

---

# 🔹 STEP 7 – MODEL BUILDING

Decision Tree Classifier was used.

Why Decision Tree?

- Works well for classification problems
- Handles numerical and categorical data
- Easy to interpret

Model was trained using:

```python
model.fit(X_train, y_train)
```

Predictions were made using:

```python
model.predict(X_test)
```

---

# 🔹 STEP 8 – MODEL EVALUATION

Model performance was evaluated using:

- Accuracy Score
- Confusion Matrix

Accuracy = Correct Predictions / Total Predictions

Confusion Matrix shows:

- True Positives
- True Negatives
- False Positives
- False Negatives

---

# 🧠 SUPERVISED LEARNING

Supervised Learning uses labeled data.

Types:

1. Classification → Predict category (Heart Disease)
2. Regression → Predict numerical value

This assignment uses Binary Classification.

---

# 🧠 UNSUPERVISED LEARNING

Unsupervised Learning uses unlabeled data.

Types:

- Clustering
- Association

Example: Customer segmentation.

---

# 📊 IMPORTANT CONCEPTS LEARNED

✔ Data Cleaning  
✔ Handling Missing Values  
✔ Removing Duplicates  
✔ Outlier Detection using IQR  
✔ Categorical Encoding  
✔ Feature Scaling  
✔ Train-Test Split  
✔ Decision Tree Classification  
✔ Model Evaluation  

---

# 🎓 VIVA QUESTIONS

1. Why is data preprocessing necessary?
2. Why use median instead of mean?
3. What is IQR?
4. Why is scaling important?
5. Why split dataset into train and test?
6. Difference between classification and regression?
7. What is supervised learning?
8. What happens if outliers are not removed?

---

# ✅ CONCLUSION

This assignment demonstrated the complete Machine Learning workflow:

Raw Data → Clean Data → Transformed Data → Model → Evaluation

Data preprocessing is the most crucial step in Machine Learning because 
model performance heavily depends on data quality.

Proper cleaning, transformation, and validation ensure accurate and reliable predictions.