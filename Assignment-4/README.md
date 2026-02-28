# 📊 Assignment 4 – Data Preprocessing using Python (Pandas)

## 🎯 AIM
Perform different data preprocessing operations using Python on:
- Facebook Metrics Dataset
- Amazon Book Review Dataset

---

## 📌 OBJECTIVES

- Learn Python programming for data analysis
- Understand Pandas DataFrame operations
- Perform data manipulation and preprocessing
- Apply real-world data transformation techniques

---

## 🛠️ Tools & Technologies Used

- Python 3.x
- Pandas
- NumPy
- VS Code (Jupyter Notebook)

---

## 📂 Datasets Used

### 1️⃣ Facebook Metrics Dataset
Contains information about Facebook posts including:
- Page total likes
- Post type (Photo, Video, Status, Link)
- Category
- Post month and hour
- Paid promotion
- Number of likes
- Number of shares
- Number of comments

This dataset is used to perform sorting, filtering, reshaping, and aggregation operations.

---

### 2️⃣ Amazon Book Reviews Dataset
Contains:
- UserID
- BookID
- Rating
- Review Length

This dataset is used to demonstrate merging operations similar to SQL joins.

---

# 📘 THEORY & IMPLEMENTATION

---

# 🔹 (a) Creating Data Subsets

Data subsetting means selecting specific rows and/or columns from a dataset.

There are three main methods:

---

## 1️⃣ Using `loc()` (Label-Based Indexing)

- Works using column names (labels)
- Syntax:
  ```python
  df.loc[row_range, ['column1', 'column2']]
  ```

Example:
```python
facebook_df.loc[0:3, ['like', 'share']]
```

This selects:
- Rows 0 to 3
- Columns: like and share

---

## 2️⃣ Using `iloc()` (Index-Based Indexing)

- Works using numeric index positions
- Syntax:
  ```python
  df.iloc[row_range, column_range]
  ```

Example:
```python
facebook_df.iloc[0:4, 0:3]
```

This selects:
- First 4 rows
- First 3 columns

---

## 3️⃣ Using Conditional Filtering

Used to filter rows based on conditions.

Example:
```python
facebook_df[facebook_df['like'] > 200]
```

This selects posts having more than 200 likes.

---

# 🔹 (b) Merge Data

Merging combines two DataFrames based on a common key.

Equivalent to SQL JOIN operations.

Syntax:
```python
pd.merge(left_df, right_df, on='column_name', how='inner')
```

Parameters:
- `on` → Common column
- `how` → Type of join:
  - inner
  - left
  - right
  - outer

Example:
```python
merged_df = pd.merge(
    facebook_df,
    amazon_df,
    left_on='Category',
    right_on='Rating',
    how='inner'
)
```

### Join Types Explained:

| Join Type | Meaning |
|-----------|---------|
| INNER | Only matching records |
| LEFT | All left records + matching right |
| RIGHT | All right records + matching left |
| OUTER | All records from both tables |

---

# 🔹 (c) Sort Data

Sorting arranges data in ascending or descending order.

Syntax:
```python
df.sort_values(by='column_name', ascending=True)
```

Example:
```python
facebook_df.sort_values(by='like', ascending=False)
```

This sorts posts by number of likes in descending order.

---

# 🔹 (d) Transposing Data

Transpose swaps rows and columns.

Syntax:
```python
df.T
```

OR

```python
df.transpose()
```

Effect:
- Rows become columns
- Columns become rows

Used when reshaping data for analysis or visualization.

---

# 🔹 (e) Melting Data (Wide → Long Format)

Melt converts wide format into long format.

Wide Format Example:

| User | Jan | Feb |
|------|-----|-----|
| A    | 100 | 150 |

After Melt:

| User | Month | Value |
|------|-------|-------|
| A    | Jan   | 100   |
| A    | Feb   | 150   |

Syntax:
```python
pd.melt(
    df,
    id_vars=['column_name'],
    value_vars=['col1', 'col2'],
    var_name='Variable',
    value_name='Value'
)
```

Purpose:
- Required for visualization
- Used for grouping and aggregation

---

# 🔹 Pivot (Long → Wide Format)

Pivot reshapes long format back into wide format.

Syntax:
```python
df.pivot(index='index_column', columns='column_name', values='value_column')
```

⚠ Important:
`pivot()` works only when index-column combinations are unique.

If duplicates exist, use:

```python
df.pivot_table(
    index='index_column',
    columns='column_name',
    values='value_column',
    aggfunc='mean'
)
```

`pivot_table()` allows aggregation:
- mean
- sum
- count
- max
- min

---

# 📊 Key Concepts Learned

- Difference between loc() and iloc()
- SQL-like merge operations in Pandas
- Sorting datasets
- Transposing DataFrames
- Converting wide format to long using melt
- Reshaping data using pivot and pivot_table
- Handling duplicate index issues

---

# 🧠 Viva Questions & Answers

### Q1: Difference between loc() and iloc()?
- loc() → Label-based
- iloc() → Index-based

### Q2: Difference between pivot() and pivot_table()?
- pivot() → No duplicates allowed
- pivot_table() → Allows aggregation

### Q3: Why melt is used?
To convert wide format data into long format for analysis and visualization.

### Q4: What does ascending=False mean?
It sorts data in descending order.

### Q5: What is merge equivalent to?
SQL JOIN operation.

---

# ✅ Conclusion

In this assignment, we successfully performed various data preprocessing operations using Python and Pandas.

We learned how to:
- Create subsets of data
- Merge datasets
- Sort data
- Transpose data
- Reshape data using melt and pivot
- Handle duplicate index issues using pivot_table

These preprocessing techniques are essential in data analytics as they prepare raw data for further analysis, visualization, and machine learning applications.

---

📌 This assignment demonstrates fundamental data manipulation skills required in real-world data science and analytics workflows.