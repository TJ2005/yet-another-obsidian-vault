---
Title: "classification"
Status: 
marker: 
tags: 
Date: "2025.10.08"
Time: "19:17"
---
## Classification
**Goal:** To predict **discrete outcomes** — that is, outcomes that belong to distinct, separate categories rather than continuous ranges.
Classification models learn from labeled data to identify which category a new observation belongs to.

---
### Types of Classification

#### Binary Classification
Used when there are **two possible outcomes**.
Examples:
* True or False
* Spam or Not Spam
* Malicious or Benign

Common algorithms:
* Logistic Regression
	* I know regression is not classification By creating a bins u could transform Logistic Regression into Classification
	* Netflix wants to predict whether a subscriber is likely to **cancel their subscription** based on their usage patterns.
* Decision Tree
* Support Vector Machine (SVM)

---

#### Multi-Class Classification
Used when there are **more than two possible outcomes**.
Examples:

* Sentiment analysis: Positive / Neutral / Negative
* Handwritten digit recognition: Digits $0–9$
* Disease diagnosis: Multiple disease types

Common algorithms:
* Decision Tree
* Random Forest
* K-Nearest Neighbors (KNN)
* Neural Networks

---

> [!note] **Key Point**
> In classification, the **output variable is categorical**.
> Each prediction assigns an input to a specific class label, not a continuous value.

---

> [!example] **Real-World Examples**
>
> * Classifying emails as spam or not spam
> * Predicting the species of a flower based on its measurements
> * Detecting whether network traffic is normal or malicious

---

In essence, **classification** helps machines make decisions in categorical terms  identifying which predefined class a new piece of data belongs to.


# References


###### Information
- date: 2025.10.08
- time: 19:17