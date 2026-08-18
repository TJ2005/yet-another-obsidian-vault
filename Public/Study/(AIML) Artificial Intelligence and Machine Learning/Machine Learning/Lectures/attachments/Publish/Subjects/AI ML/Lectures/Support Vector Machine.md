---
Title: "Support Vector Machine"
Status: 
marker: 
tags: 
Date: "2025.10.09"
Time: "07:30"
---
# Support Vector Machine
## Support Vector Machine (SVM)

Support Vector Machine (SVM) is a **supervised machine learning algorithm** mainly used for **classification**.
It finds the **best boundary (hyperplane)** that separates data points of different classes with the **maximum margin**.

---

### Core Idea

> SVM tries to find a **hyperplane** that best separates two or more classes, with the **maximum distance** between them.

* Works best on **small datasets**
* Performs well when the dataset has **high dimensions** relative to the number of observations

---

### Types of SVM

#### Linear SVM

* Data is **linearly separable**
* Classification into two classes can be done using a **single line (or plane)**
![[IMG-20260114210326354.png]]
#### Non-Linear SVM

* Used when data **cannot be separated linearly**
* Implemented in practice using a **kernel function**
* The **choice of kernel** determines how data is mapped to a higher-dimensional space where it becomes separable

![[IMG-20260114210326390.png]]
---

### Key Terms

| Term                | Meaning                                                                               |
| ------------------- | ------------------------------------------------------------------------------------- |
| **Hyperplane**      | The decision boundary separating different classes                                    |
| **Support Vectors** | The data points closest to the hyperplane that influence its position and orientation |
| **Margin**          | The distance between the hyperplane and the nearest data points of each class         |

> [!tip] Margin and Error
> A larger **margin** generally means fewer classification errors and better generalization.
> When classes **overlap**, SVM still tries to find the hyperplane with **minimum misclassification**.

---

### Where It Works Well

* Datasets with **many features** but **few samples**
* Examples:

  * DNA records
  * IP address datasets (multiple IPs but limited information)

---

### Pros

* Effective in **high-dimensional spaces**
* **Memory efficient** — only depends on **support vectors**
* Performs well even when **dimensions exceed the number of samples**

---

> [!fact] Fact
> The SVM model is defined entirely by the **support vectors**. Other data points have no effect on the final decision boundary.

---

> [!tip] The Kernel Trick
> Kernels allow SVMs to separate data that is **not linearly separable** by projecting it into a higher-dimensional space where a linear boundary exists.
> Common kernel types include:
>
> * Linear
> * Polynomial
> * Radial Basis Function (RBF)
> * Sigmoid

---

> [!bug] Misconception Alert
> SVMs are **not ideal** for very large or noisy datasets.
>
> * Training can become **computationally expensive**
> * Performance may degrade if data has significant overlap or noise without proper kernel tuning

---

# References


###### Information
- date: 2025.10.09
- time: 07:30