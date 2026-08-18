---
Title: "Regression"
Status: 
marker: 
tags: 
Date: "2025.10.08"
Time: "19:27"
---
# Regression
**Goal:** Predict **continuous values** — numerical outcomes that can take any value in a range.

Regression fits a **line or curve** to the dataset so that the **distance between predicted and actual values is minimized**. Before applying regression, check if the dataset shows a roughly **linear relationship**.

* Close to a line → **Linear Regression**
* Far from a line → consider **Multiple Linear Regression** or **non-linear regression**

> [!tip] The term **regression** was coined by Charles Darwin in the context of **height regression toward the mean**.

---

## Linear Regression Equation
$Y = a + bX + e$

Where:

* (a) = intercept
* (b) = slope
* (e) = error term

> [!fact] Example: Phishing Emails
> 
> $$\text{No of compromised accounts} = -1.91 + 0.146 \times \text{X (phishing mails)}$$
> 
>
> * 0 phishing mails → -1.91 attacks (interpreted as 0)
> * Each phishing mail increases compromised accounts by 0.146

---

### Regression vs Classification

| Aspect     | Regression               | Classification        |
| ---------- | ------------------------ | --------------------- |
| Output     | Continuous               | Discrete              |
| Prediction | Quantitative value       | Class label           |
| Example    | House price, temperature | Spam detection, fraud |

---

## Multiple Regression


$$Y = a + b_1X_1 + b_2X_2 + \dots + b_kX_k + e$$


* Works best when independent variables are **not highly correlated**
* Techniques like **PCA** can reduce dimensionality

---

## Cost & Loss Functions

**Cost function:** Measures **average error across all samples**; goal is to **minimize**.
**Loss function:** Measures **error for a single prediction**.

**Common Metrics:**

* Mean Error (ME) — simple average, can cancel positives & negatives
* Mean Squared Error (MSE) — squares errors, sensitive to outliers
* Mean Absolute Error (MAE) — uses absolute values, robust to outliers

---

## Bias & Variance

**Bias:** Error from model assumptions → high bias = underfitting
**Variance:** How predictions vary with different datasets → high variance = overfitting

> [!tip] Increasing model complexity decreases bias but increases variance. Aim for a balance between the two.

> [!fact] Example: Linear model on polynomial data → high bias; high-degree polynomial → low bias, high variance

---

# Logistic Regression

**Goal:** Predict **categorical outcomes** using a regression-style approach.

* Input types: Nominal, Ordinal, Interval
* Uses **sigmoid function** → outputs probability [0,1]
* Apply threshold (default 0.5) to classify into discrete categories

---

### Applications

* Cancer detection (cancerous / non-cancerous)
* Email spam detection
* Cyber attack detection

---

### Key Points

* Dependent variable must be **categorical**
* Only relevant independent variables should be included
* Independent variables should be **unrelated**

> [!tip] Logistic regression predicts **probabilities**, then bins them into classes using a threshold.

### Types

* **Binomial:** Two possible classes
* **Multinomial:** Three or more unordered classes (**Softmax**)
* **Ordinal:** Three or more ordered categories

---

### Pros & Cons

**Pros:**

* Works well with linearly separable data
* Fast training
* Multi-class classification

**Cons:**

* Sensitive to outliers
* Can overfit if features > observations
* Poor for complex non-linear relationships

---

# References

###### Information

* Date: 2025.10.08
* Time: 19:27

---

If you want, I can make a **visual version** for Obsidian showing **linear regression, sigmoid curve, and logistic threshold** — very intuitive for readers.

