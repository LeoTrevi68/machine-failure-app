# Machine Failure Risk Prediction & SPC Monitoring

## Overview

This project develops an end-to-end solution to predict machine failure and monitor process stability using real industrial-like data.

It combines machine learning with statistical process control (SPC) concepts to move beyond prediction and enable actionable operational decisions.

An interactive Streamlit application allows real-time evaluation of machine conditions and visualization of control limits.

---

## Problem Statement

In manufacturing environments, machine failures are often driven by a combination of process variables such as temperature, torque, and tool wear.

The objective of this project is to:

- Predict machine failure using process data  
- Identify key drivers of failure  
- Define safe operating conditions  
- Provide a tool for real-time risk evaluation  

---

## Dataset

**AI4I 2020 Predictive Maintenance Dataset (Kaggle)**

The dataset contains simulated industrial data including:

- Air temperature  
- Process temperature  
- Rotational speed  
- Torque  
- Tool wear  
- Machine failure indicators  

---

## Approach

### 1. Data Preparation
- Removed non-informative identifiers  
- Handled class imbalance (~3% failures)  
- Avoided data leakage by excluding failure-type variables  

---

### 2. Exploratory Analysis

Key findings:

- Higher tool wear is strongly associated with failure  
- Increased torque reflects higher mechanical stress  
- Failures are driven by combined conditions, not single thresholds  

---

### 3. Machine Learning Model

- Model: Logistic Regression  
- Class imbalance handled using `class_weight='balanced'`

**Results:**
- Recall (failure): ~82%  
- Precision: ~14%  

---

### 4. Key Insight

Machine failure is a **multivariate phenomenon** driven by:

- Equipment degradation (tool wear)  
- Mechanical load (torque)  
- Environmental conditions (temperature)  

---

### 5. Operating Envelope Definition

Safe operating ranges were defined using non-failure data (5th–95th percentiles):

- Torque: controlled range  
- Tool wear: preventive replacement threshold  
- Temperature: stable operating conditions  

This enables a **practical framework for process control**, not just prediction.

---

### 6. Interactive Application

A Streamlit app was developed to:

- Input real-time operating conditions  
- Predict failure probability  
- Classify risk level (Low / Medium / High)  
- Visualize SPC charts with control limits  
- Evaluate each variable against safe operating ranges  

---

## Example Output

- Failure probability (real-time)  
- Risk classification  
- SPC charts for key variables  
- Identification of out-of-range conditions  

---

## Business Impact

This solution enables:

- Early detection of high-risk operating conditions  
- Support for preventive maintenance strategies  
- Improved process stability and quality control  
- Translation of data analysis into actionable decisions  

---

## Tech Stack

- Python  
- Pandas / NumPy  
- Scikit-learn  
- Plotly  
- Streamlit  

---

## Live Application

[Insert your Streamlit app link here]

---

## Author

José Leopoldo Treviño Martínez  
Data Analysis & Industrial Applications
