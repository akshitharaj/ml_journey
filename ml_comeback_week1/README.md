# Project Overview
On Day 1 of my ML comeback journey, I built a complete baseline classification pipeline using the Breast Cancer dataset from scikit-learn.

### The goal was to:
- Load and explore the dataset
- Build a baseline Logistic Regression model
- Apply feature scaling
- Compare multiple models
- Evaluate performance using proper classification metrics

## Dataset
- Dataset: Breast Cancer Wisconsin (Diagnostic)
- Samples: 569
- Features: 30 numerical features
- Target:
  0 → Malignant
  1 → Benign
This is a binary classification problem in a medical domain, where recall for malignant cases is critical.

## Workflow
1. Loaded dataset using sklearn.datasets
2. Performed basic exploratory data analysis
3. Split data into train/test (80/20, stratified)
4. Built baseline models:
   - Logistic Regression
   - Logistic Regression (with StandardScaler)
   - Decision Tree
   - Random Forest
5. Evaluated using:
   - Accuracy
   - Confusion Matrix
   - Precision / Recall / F1-score

## Key observations
- Scaling significantly improved Logistic Regression performance.
- Tree-based models did not require scaling.
- Scaled Logistic Regression achieved the highest accuracy.
- In medical classification problems, recall for malignant cases is more important than overall accuracy.
- Proper preprocessing plays a critical role in model performance.

## Tools Used
- Python
- Pandas
- Scikit-learn
- Matplotlib / Seaborn

## Learning Outcome
- Understood baseline model building
- Practiced train-test split with stratification
- Learned importance of scaling
- Compared linear vs tree-based models
- Evaluated classification metrics properly

# Day 2 Logistic Regression Optimization & Advanced Evaluation

Logistic Regression Optimization & Advanced Evaluation

### Preprocessing
- Applied StandardScaler to normalize feature magnitudes.

- Improved convergence and stability of Logistic Regression.

### Hyperparameter Tuning
- Used GridSearchCV with 5-fold cross-validation.
- Tuned regularization parameter C.
- Optimized for recall, prioritizing detection of malignant cases.

### Advanced Evaluation
- Plotted ROC Curve.
- Computed AUC score on test data.
- Achieved: AUC=0.99

### Interpretation
- The dataset shows strong class separability.
- Logistic Regression generalized better than Random Forest.
- High AUC indicates excellent ranking capability across thresholds.
- Emphasized recall due to medical risk considerations.

### Learning Outcome
- Understood impact of regularization.
- Learned threshold-independent evaluation using AUC.
- Practiced structured model comparison and selection.