### ECG Machine Learning Practice Project
## Project Overview

This project explores the fundamentals of data science, machine learning, and biomedical signals using Python.

The goal is to understand:
- Basic statistics used in data science
- Core Python programming techniques
- Building a baseline machine learning model
- Understanding ECG signals from a biomedical perspective

The machine learning experiment uses the Breast Cancer Wisconsin dataset to build a simple classification model.

## Tools and Libraries
This project uses the following tools:
- Python
- NumPy
- Matplotlib
- scikit-learn

These libraries help with:
- numerical computation
- visualization
- machine learning modeling

## 1. Basic Math Concepts
- Mean
The mean represents the average value of a dataset.

Formula:
Mean = sum(x) / n

Example:
[2, 4, 6, 8]
Mean = 5

- Median
The median is the middle value in a sorted dataset.

Examples:
[1, 3, 5] → median = 3
[1, 3, 5, 7] → median = 4

- Variance
Variance measures how spread out values are from the mean.

Steps:
- Compute mean
- Subtract mean from each value
- Square differences
- Average the squared values

- Standard Deviation
Standard deviation is the square root of variance.
It indicates how far values typically deviate from the mean.

- Normalization
Normalization rescales features so different variables become comparable.

Two common techniques:
- Min-Max Scaling
x' = (x - min) / (max - min)
- Z-score Standardization
z = (x - mean) / std

## 2. Python Concepts Practiced
- List Comprehension
Used for creating lists in a concise way.
squares = [x**2 for x in range(5)]

Output:
[0,1,4,9,16]

- Dictionaries
Dictionaries store key-value pairs.
student = {"name": "Anna", "marks": 92}

- Lambda Functions
Lambda functions are small anonymous functions.
square = lambda x: x**2

- Sorting with Key
Sorting objects using custom rules.
Example: sorting students by marks.
sorted(students, key=lambda s: s["marks"])

## 3. Machine Learning Baseline Model
- Dataset used:
Breast Cancer Wisconsin Dataset

- Goal:
Classify tumors as benign or malignant.

- Workflow
Step 1 — Load Dataset
Step 2 — Train/Test Split
Step 3 — Train Model
Step 4 — Model Evaluation
- Accuracy
Accuracy measures the percentage of correct predictions.
Accuracy = correct predictions / total predictions

- Confusion Matrix

	     Predicted Positive	     Predicted Negative
Actual Positive	True Positive	 False Negative
Actual Negative	False Positive	 True Negative

- Recall
Recall measures how many actual positive cases were correctly detected.
Recall = TP / (TP + FN)
This is important in medical diagnosis because missing a disease case can be dangerous.

## 4. ECG Biomedical Concepts
An ECG (Electrocardiogram) records the electrical activity of the heart.

It is commonly used to detect:
- arrhythmias
- heart attacks
- abnormal heart rhythms

ECG Components
- P Wave
Represents atrial depolarization (atria contract).
- QRS Complex
Represents ventricular depolarization (ventricles contract).
This is the largest spike in an ECG signal.
- T Wave
Represents ventricular repolarization (ventricles relax).

Heartbeat Cycle
P wave → QRS complex → T wave

Typical resting heart rate:
60–100 beats per minute

ECG Signal Visualization
Example of a simple simulated ECG waveform in Python.

## Learning Outcomes
From this project I learned:
- fundamental statistics for data science
- Python programming basics
- building a baseline machine learning model
- evaluating classification models
- understanding ECG biomedical signals
- plotting signals using Python