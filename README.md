# 🚢 Task 1: Data Cleaning & Preprocessing – Titanic Dataset

## 🔍 Objective
To learn and apply essential data preprocessing techniques such as handling nulls, encoding, scaling, and outlier detection, using the Titanic dataset.

---

## 🧰 Tools Used
- Python
- Pandas
- NumPy
- Seaborn & Matplotlib
- Scikit-learn

---

## 📁 Dataset
- Source: [Kaggle – Titanic Dataset](https://www.kaggle.com/datasets/yasserh/titanic-dataset)
- File used: `titanic.csv`

---

## 🧪 Steps Performed

### 1. **Data Loading & Exploration**
- Loaded the dataset using `pandas`
- Explored shape, datatypes, statistical summary
- Verified **no missing values** in the dataset

### 2. **Data Cleaning**
- Dropped the `Name` column (non-informative for modeling)
- Checked and confirmed **no null values** present

### 3. **Feature Encoding**
- `Sex`: Converted to numerical using **Label Encoding** (male = 0, female = 1)

### 4. **Feature Scaling**
- Standardized `Age` and `Fare` using **StandardScaler** from `sklearn`

### 5. **Outlier Detection**
- Used **boxplots** to detect outliers in `Age` and `Fare`
- Chose **not to remove outliers in Age**
- Optionally applied **IQR method** to remove high-value outliers in `Fare`

---

## 📊 Cleaned Data Preview

| Survived | Pclass | Sex | Age | Siblings/Spouses Aboard | Parents/Children Aboard | Fare |
|----------|--------|-----|-----|--------------------------|--------------------------|------|
| 0        | 3      | 0   | -0.55| 1                        | 0                        | -0.5 |
| 1        | 1      | 1   | 0.63 | 1                        | 0                        |  2.1 |

*Values above are representative, not actual*

---

## 💾 Output Files
- `titanic_cleaned.csv` – Cleaned and preprocessed dataset

---

## 🧠 What I Learned
- Practical steps of data preprocessing
- Handling categorical & numerical variables
- Scaling, encoding, and visualizing data
- Importance of detecting and optionally handling outliers

---

## 📂 Folder Structure
Task1_Data_Preprocessing/
├── data/
│   ├── titanic.csv
    └── titanic_cleaned.csv  (if outside data/)
├── notebooks/
    ├── task1_titanic.ipynb
│   └── task1_titanic.py  (or .py file)
├── images/
│   ├── BoxPlot of Age.png
│   └── BoxPlot of Fare.png
└── README.md


---

## ✅ Submission

- Repository: [https://github.com/AiricStorm/AI-ML-Internship-Task1]
- Submitted via: [Google Form Link](https://forms.gle/QBau7ixUUYCxnBA56)

---

## 💡 Learning Outcomes

- Cleaned real-world messy data
- Practiced essential preprocessing steps
- Learned data visualization for outlier detection
- Understood encoding and scaling techniques

---



