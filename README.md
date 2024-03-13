# Chronic (Kidney & Cardiovascular) Disease Analysis

## Table of Contents
- [Project Overview](#project-overview)
- [Data Sources](#data-sources)
- [Tools](#tools)
- [Data Cleaning](#data-cleaning)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Data Analysis](#data-analysis)
- [Results](#results)
- [Recommendations](#recommendations)
- [References](#references)
 

### Project Overview
The project investigates correlations within kidney disease, analyzing factors such as blood pressure and blood glucose distribution among affected patients. Additionally, it seeks to understand the prevalence of symptoms experienced by individuals with kidney disease, offering insights vital for improved diagnosis and management strategies.

![Untitled](https://github.com/Rodnah/Test/assets/147203468/c7bc876e-e439-4166-b39c-ba26b8a98077)


### Data Sources
The primary dataset was downloaded from Kaggle as a CSV file named "kidney_disease.csv," containing detailed information about various parameters within the dataset.

### Tools
1. Excel - Data Cleaning
2. SQL Server - Data Preprocessing
3. Python- Data Analysis 
4. Matplotlib and Seaborn - Data Visualization

### Data Cleaning
In the initial data preparation phase, I performed the following tasks:
1. Data loading and inspection.
2. Handling missing values.
3. Data cleaning and formatting.

### Exploratory Data Analysis
EDA involved exploring the data to answer critical questions, such as:
1. What does the correlation analysis reveal about kidney disease?
2. How are blood pressure and blood glucose values distributed among patients with kidney disease?
3. What is the prevalence of symptoms among patients with kidney disease?

### Data Analysis
Excerpt of some code worked with:
```sql
--  Symptom Analysis:
-- Investigate the prevalence of symptoms like appetite loss (appet), pedal edema (pe),
	-- and anemia (ane) in patients with kidney disease.

SELECT s.*, classification
FROM kidney_disease.symptoms s
JOIN kidney_disease.disease_classification dc 
ON s.id = dc.id;
```



### Results
The analysis results are summarized as follows:

1. There are strong associations among parameters, such as Serum Creatinine (sc) with Blood Urea (bu) and Hemoglobin (hemo) with Packed Cell Volume (PCV), alongside a notable negative correlation between Serum Sodium (sod) and Serum Creatinine (sc).

2. In kidney disease patients, blood glucose concentrations range between 100mg/dl and 220mg/dl, with blood pressure below 100mmHg. Individuals without kidney disease typically display blood glucose levels at 120mg/dl and blood pressure below 90mmHg. 

3. There is a higher occurrence of appetite issues (appe), pedal oedema (pe), and anaemia (ane) in individuals with kidney disease, with approximately 250 cases observed. In contrast, individuals without kidney disease exhibit a lower prevalence of these symptoms, with around 150 cases recorded.

### Recommendations
Based on the analysis, I recommend the following actions:
1. To accurately assess kidney function, biomarkers with solid correlations, such as Serum Creatinine and Blood Urea, must be monitored regularly.
2. Implementing personalized management plans to maintain optimal blood glucose levels and blood pressure, such as emphasizing lifestyle modifications for sustained control.
3. Comprehensive symptom management plans targeting appetite issues, pedal oedema, and anaemia should be prioritized to enhance overall well-being in kidney disease patients.

### References
1. Kaggle
2. Seaborn
3. Matplotlib
