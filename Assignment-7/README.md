# 📊 Assignment 7 – Data Visualization using Python

---

## 🎯 AIM

To visualize the data using Python by plotting different types of graphs 
for Assignment 2 and Assignment 3 datasets.

---

## 🎯 OBJECTIVES

1. To understand and apply data visualization techniques.
2. To study detailed visualization concepts in Python.
3. To interpret data patterns using graphical representation.

---

# 📘 INTRODUCTION

Data Visualization is the graphical representation of data.

It helps to:
- Understand patterns
- Detect trends
- Identify outliers
- Compare distributions
- Analyze relationships between variables

In this assignment, we visualize:

- Heart Disease Dataset
- Air Quality Dataset

We use Python libraries:
- Matplotlib
- Seaborn
- Pandas

---

# 🔹 LIBRARIES USED

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

# 📂 DATASETS USED

## 1️⃣ Heart Dataset
Used for:
- Pie chart
- Bar chart
- Boxplot
- Histogram
- Scatter plot
- Scatter matrix

## 2️⃣ Air Quality Dataset
Used for:
- Bar chart
- Line chart
- Histogram

---

# 🔹 1️⃣ PIE CHART

## Definition
A pie chart represents proportional distribution of categories.

Used to show percentage contribution.

## Example:
Distribution of Heart Disease vs No Disease

```python
heart_df['target'].value_counts().plot.pie(
    autopct='%1.1f%%',
    colors=['skyblue','lightcoral']
)
plt.title("Heart Disease Distribution")
plt.ylabel("")
plt.show()
```

### Interpretation:
Shows percentage of patients with and without heart disease.

---

# 🔹 2️⃣ BAR CHART

## Definition
Bar chart compares categorical data using rectangular bars.

## Example:
Count of Chest Pain Types

```python
sns.countplot(x='cp', data=heart_df)
plt.title("Chest Pain Type Distribution")
plt.show()
```

### Interpretation:
Shows frequency of each chest pain category.

---

# 🔹 3️⃣ BOX PLOT

## Definition
Boxplot shows data distribution using:

- Minimum
- Q1 (25%)
- Median
- Q3 (75%)
- Maximum

Used to detect outliers.

## Example:
Cholesterol vs Heart Disease

```python
sns.boxplot(x='target', y='chol', data=heart_df)
plt.title("Cholesterol vs Heart Disease")
plt.show()
```

### Interpretation:
Compares cholesterol levels between diseased and non-diseased patients.

---

# 🔹 4️⃣ HISTOGRAM

## Definition
Histogram shows frequency distribution of continuous data.

## Example:
Distribution of Age

```python
plt.hist(heart_df['age'], bins=5, color='orange', edgecolor='black')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
```

### Interpretation:
Shows age frequency distribution.

---

# 🔹 5️⃣ LINE CHART

## Definition
Line chart shows trend over ordered values.

## Example:
SO2 levels across cities

```python
plt.plot(air_df['so2'], marker='o')
plt.title("SO2 Levels Trend")
plt.xlabel("City Index")
plt.ylabel("SO2 Level")
plt.show()
```

### Interpretation:
Shows variation of SO2 across cities.

---

# 🔹 6️⃣ SCATTER PLOT

## Definition
Scatter plot shows relationship between two continuous variables.

## Example:
Age vs Cholesterol

```python
plt.scatter(heart_df['age'], heart_df['chol'])
plt.title("Age vs Cholesterol")
plt.xlabel("Age")
plt.ylabel("Cholesterol")
plt.show()
```

### Interpretation:
Shows correlation between age and cholesterol.

---

# 🔹 7️⃣ SCATTER PLOT MATRIX

## Definition
Scatter matrix shows pairwise relationship among multiple variables.

## Example:

```python
sns.pairplot(heart_df[['age','chol','thalach','oldpeak']])
plt.show()
```

### Interpretation:
Shows correlation between multiple continuous features.

---

# 📊 IMPORTANT VISUALIZATION CONCEPTS

| Graph Type | Used For |
|------------|----------|
| Pie Chart | Percentage distribution |
| Bar Chart | Categorical comparison |
| Boxplot | Distribution & Outliers |
| Histogram | Frequency distribution |
| Line Chart | Trend analysis |
| Scatter Plot | Relationship between two variables |
| Scatter Matrix | Multi-variable relationship |

---

# 🎓 VIVA QUESTIONS

1. Difference between Bar chart and Histogram?
2. What is IQR in Boxplot?
3. When do we use scatter plot?
4. What is pairplot used for?
5. Why visualization is important in Big Data?

---

# ✅ CONCLUSION

In this assignment, we successfully visualized the datasets using:

- Pie Chart
- Bar Chart
- Boxplot
- Histogram
- Line Chart
- Scatter Plot
- Scatter Plot Matrix

Data visualization helps in better understanding of patterns, 
relationships and trends in data.

Thus, we have learned visualization techniques using Python.