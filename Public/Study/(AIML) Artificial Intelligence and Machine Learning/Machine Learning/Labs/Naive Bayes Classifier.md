---
Title: Naive Bayes Classifier
Status:
marker:
  - "[[Supervised Learning]]"
  - "[[Artificial Intelligence Index]]"
tags:
Date: 2025.09.11
Time: 12:23
---
## Naive Bayes Classifier

---

### Why “Naive”?

It is called **naive** because it assumes that the features are **independent** of each other given the class label.

---

### Usefulness

Popular for **real-world Machine Learning (rML)** tasks and text or categorical classification problems.

---

### Conditional Probability

Works on the principle of **Bayes’ Theorem**:

$$
P(C_k \mid X) = \frac{P(X \mid C_k) , P(C_k)}{P(X)}
$$

Where:

* $P(C_k \mid X)$ → Posterior probability of class $C_k$ given features $X$
* $P(X \mid C_k)$ → Likelihood of observing features $X$ given class $C_k$
* $P(C_k)$ → Prior probability of class $C_k$
* $P(X)$ → Probability of observing $X$

---

### Assumption

All attributes are considered **independent and equally important** in their contribution to the final classification.

> [!fact] Independence in Theory
> In practice, features are rarely fully independent — yet the model still performs surprisingly well on many tasks.

---

### Impact

Each attribute makes its **own independent contribution** to the final classification.

---

### In Practice

In [[DWM Naive Bayes]] we worked on **Gaussian Naive Bayes**.

---

## Handling Continuous Data

When the dataset contains continuous values, we can either:

* Use **Gaussian Naive Bayes** (assumes normal distribution), or
* **Discretize** values into groups or categories.

**Example – Salary Binning**

| Salary          | Category |
| --------------- | -------- |
| ≤ 25,000        | Low      |
| 25,001 – 45,000 | Medium   |
| > 45,000        | High     |

---

## Types of Naive Bayes Models

| Type                        | Usage                   | Description                                                   |
| --------------------------- | ----------------------- | ------------------------------------------------------------- |
| **Gaussian Naive Bayes**    | Continuous data         | Assumes normal distribution; uses mean and standard deviation |
| **Multinomial Naive Bayes** | Discrete/frequency data | Common in text classification                                 |
| **Bernoulli Naive Bayes**   | Boolean/binary data     | Features take 0/1 values                                      |

---

## Steps for Naive Bayes (Continuous → Binned Example)

### 1. Dummy Dataset

| Gender | Income | Illness |
| ------ | ------ | ------- |
| Male   | 20 000 | Yes     |
| Male   | 25 000 | Yes     |
| Male   | 50 000 | No      |
| Female | 22 000 | Yes     |
| Female | 45 000 | No      |
| Female | 60 000 | No      |

---

### 2. Binning Continuous Feature

| Gender | Income | Bin    | Illness |
| ------ | ------ | ------ | ------- |
| Male   | 20 000 | Low    | Yes     |
| Male   | 25 000 | Low    | Yes     |
| Male   | 50 000 | High   | No      |
| Female | 22 000 | Low    | Yes     |
| Female | 45 000 | Medium | No      |
| Female | 60 000 | High   | No      |

---

### 3. Frequency / Likelihood Table

**Illness = Yes**

* Gender: Male → 2, Female → 1
* Income Bin: Low → 3, Medium → 0, High → 0

**Illness = No**

* Gender: Male → 1, Female → 2
* Income Bin: Low → 0, Medium → 1, High → 2

---

### 4. Classification Example

Let

$$
X = {\text{Gender = Female, Income = High}}
$$

Compute:

$$
P(\text{Illness = Yes} \mid X) \propto P(\text{Female}\mid Yes),P(\text{High}\mid Yes),P(Yes)
$$

$$
P(\text{Illness = No} \mid X) \propto P(\text{Female}\mid No),P(\text{High}\mid No),P(No)
$$

---

### 5. Compute with Dummy Probabilities

**Priors**

$$
P(Yes) = \tfrac{3}{6}, \qquad P(No) = \tfrac{3}{6}
$$

**Likelihoods**

$$
P(\text{Female}\mid Yes) = \tfrac{1}{3}, \quad P(\text{High}\mid Yes) = 0
$$
$$
P(\text{Female}\mid No) = \tfrac{2}{3}, \quad P(\text{High}\mid No) = \tfrac{2}{3}
$$

**Posteriors**

$$
P(Yes \mid X) \propto \tfrac{1}{3}\times0\times\tfrac{1}{2}=0
$$
$$
P(No \mid X) \propto \tfrac{2}{3}\times\tfrac{2}{3}\times\tfrac{1}{2}=\tfrac{2}{9}
$$

**Prediction:** Illness = No

---

### 6. Role of Likelihood (Gaussian Case)

For continuous features:

$$
P(x \mid C_k)=\frac{1}{\sqrt{2\pi\sigma_k^2}}\exp!\left(-\frac{(x-\mu_k)^2}{2\sigma_k^2}\right)
$$

where

* $\mu_k$ = mean of feature $x$ in class $C_k$
* $\sigma_k$ = standard deviation of $x$ in $C_k$

Then multiply likelihoods across all features with the prior to get the posterior probability.

---

### Summary

* **Likelihood** → measures how well a data point fits within a class
* **Mean & SD** → describe the Gaussian curve for each class
* **Final Classification** → choose class with highest posterior probability

```mermaid
flowchart TD
A["Start: Dataset with Features & Class Label"] --> B["Handle Continuous Features"]
B -->| "Option 1: Discretize" | C["Convert into Bins ('Low'/'Medium'/'High')"]
B -->| "Option 2: Gaussian" | D["Compute Mean μ & Std Dev σ for Each Class"]
C --> E["Build Frequency Table for Each Class"]
D --> E["Build Likelihood Function P(x|C)"]
E --> F["Compute Prior Probability P(C)"]
F --> G["Compute Posterior: P(C|X) ∝ P(C) × ∏ P(xᵢ|C)"]
G --> H{"Compare Posteriors"}
H -->| "Max Posterior" | I["Final Class Prediction"]
```

---

## Naive Bayes – Benefits and Disadvantages

### Benefits

1. **No heavy preprocessing**
   Works directly on raw data.
   Example:
   $P(\text{Male}\mid \text{Illness = Yes}) = \frac{\text{Count(Male and Yes)}}{\text{Count(Yes)}}$

2. **Feature selection not critical**
   Irrelevant features are treated independently and have limited effect.

3. **Single-scan training**
   One pass is enough to compute frequency tables or mean/variance.
   $$\mu = \frac{1}{n}\sum_{i=1}^{n}x_i,\qquad
   \sigma^2 = \frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2$$

---

### Disadvantages

1. **Independence assumption**
   Assumes conditional independence of features, which may be unrealistic.

2. **Continuous data handling**
   Requires assuming a distribution (usually Gaussian).
   $$P(x \mid C)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

3. **Zero-frequency problem**
   If a feature value never appears with a class, its probability becomes zero:
   $P(\text{Income = High}\mid\text{Yes})=0 \Rightarrow P(X\mid C)=0$
   **Solution – Laplace Smoothing:**
   $$P(x_i\mid C)=\frac{\text{count}(x_i,C)+1}{\text{count}(C)+k}$$
   where $k$ = number of possible feature values.

---

### References

**Information**

* Date: 2025-09-11
* Time: 12:23

---
