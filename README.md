
# 📌 SkillCraft Technology — Machine Learning Internship  
## **Task 01: House Price Prediction using Linear Regression**

This repository contains the implementation of **Task 01** for my **Machine Learning Internship at SkillCraft Technology**.  
The objective of this task is to **build a Linear Regression model** that predicts house prices based on:

- **Square Footage (GrLivArea)**
- **Number of Bedrooms (BedroomAbvGr)**
- **Number of Bathrooms (FullBath)**

Dataset used:  
📎 *Kaggle — House Prices: Advanced Regression Techniques*  
(Only `train.csv` was used, placed in `data/raw/`)

---

## 🚀 **Project Structure**
```

SCT_ML_1/
│
├── notebooks/
│     └── task01_linear_regression.ipynb        # Jupyter notebook (EDA + Model Training)
│
├── data/
│     ├── raw/                                  # Contains train.csv (not uploaded to GitHub)
│     ├── processed/                             # Cleaned data (optional)
│
├── models/
│     └── linear_regression.pkl                  # Saved trained model
│
├── src/
│     ├── data_prep.py                           # Data loading & cleaning
│     └── train_model.py                         # Model training script
│
├── reports/
│     ├── slides.pptx                            # Presentation (optional)
│     └── final_report.pdf                       # Detailed report
│
└── README.md

````

---

## 🧪 **Model Training Overview**

🎯 **Goal:** Predict house prices using a simple linear regression model.

📌 **Steps Performed:**
1. Loaded raw data  
2. Selected features  
3. Cleaned missing values  
4. Removed outliers (top 1% GrLivArea)  
5. Split into train/test  
6. Trained Linear Regression model  
7. Evaluated model  
8. Saved trained model (`linear_regression.pkl`)

---

## 📊 **Model Performance**
After training the baseline model using 3 features:

| Metric | Score |
|--------|--------|
| **MAE** | ~36,307 |
| **RMSE** | ~52,888 |
| **R² Score** | **0.59** |

✔ This is a reasonable baseline for a simple linear model using only 3 features.  
✔ Performance can be improved by adding more features or using regularized models (Ridge/Lasso).

---

## ▶️ **How to Run the Project**

### **1️⃣ Create Virtual Environment**
```bash
python -m venv .venv
.venv\Scripts\activate
````

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3️⃣ Add Dataset**

Download `train.csv` from Kaggle and place it in:

```
data/raw/train.csv
```

### **4️⃣ Run Training Script**

```bash
python src/train_model.py
```

### **5️⃣ Run Prediction Script**

```bash
python predict.py
```

---

## 📌 **Internship Requirement**

This repository serves as the submission for Task 01 of the **SkillCraft Machine Learning Internship**.
A LinkedIn post explaining the task and results has been published as required.

---

## 📞 **Contact**

For queries or collaboration:

* **GitHub:** [https://github.com/sattvik-shukla](https://github.com/sattvik-shukla)
* **Email:** sattvikshukla@gmail.com

---

## ⭐ **If you like this project, feel free to star the repo!**

or  
**"Give report"**
```
