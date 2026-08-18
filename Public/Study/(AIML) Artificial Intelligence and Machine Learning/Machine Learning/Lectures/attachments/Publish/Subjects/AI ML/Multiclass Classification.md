---
Title: Multiclass Classification
Status: true
marker:
tags:
Date: 2025.09.23
Time: 14:18
---
# Multiclass Classification
- Data is imbalanced for some reason
	- Oversampling / Up Sample
		- Oversampled using replacements
		- Biasedness
		- Methods of generating data
			- Synthesizing data using certain neighbours that are associated to a tuple. 
			- Based on that characteristic we generate more data
			- **SMOTE**
			- **XGBoost**
			- When there are too many classes to check patterns for we typically merge them into one single column/feature.
	- Undersampling 
		- Randomly delete from majority class
		- Significant loss in data
		- Could become Biased
		- But fewer storage requirement
		- Better run times

# References


###### Information
- date: 2025.09.23
- time: 14:18