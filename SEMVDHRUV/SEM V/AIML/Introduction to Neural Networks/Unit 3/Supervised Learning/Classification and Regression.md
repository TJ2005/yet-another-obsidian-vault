# Classification
**Goal**: Predicts **discrete outcomes** (categorical labels.
### Two Types
* **Binary Classification**
  * Target has **two possible classes** (e.g., True/False, Yes/No, Default/No Default).
* **Multiclass Classification**
	-  Target has **more than two classes**.
* **Examples / Applications**
	* Email filtering: **spam vs non-spam**.
	* Email security: detect **malware/viruses** without opening messages.
	* **Voice-based security**: distinguish owner’s voice from attacker’s.
	* **Sentiment analysis**: classify customer feedback (positive/negative).
	* **Drug classification** into multiple categories.

### Examples
* **Common Classification Algorithms**
  * Logistic Regression
  * Decision Tree Classifier
  * Support Vector Machines (SVM)
  * Random Forest Classifier
  * Neural Networks
  * K-Nearest Neighbors (KNN)

---
## Regression
* Used to **predict continuous values** (e.g., sales, salary, weight, temperature).
* Models learn the **relation`ship between variables**, where a change in one variable affects another.
* **Examples / Applications**
	* Predicting **real estate prices** using location (e.g., zip code).
	* Estimating **network security outcomes** based on deployed defense tools.
	* Analyzing **correlations** between factors (login attempts, packet patterns) and the likelihood of security breaches or malware infections.
	* Predicting **customer willingness to pay** for a product based on attributes like age.

* **Common Regression Algorithms**
  * [[SEMVDHRUV/SEM V/AIML/Introduction to Neural Networks/Unit 3/Supervised Learning/1. Linear Regression/Linear Regression]]
  * [[SEMVDHRUV/SEM V/AIML/Introduction to Neural Networks/Unit 3/Supervised Learning/1. Linear Regression/Linear Multiple Regression|Multivariate Regression]]
  * [[SEMVDHRUV/SEM V/AIML/Introduction to Neural Networks/Unit 3/Supervised Learning/1. Linear Regression/Linear Regression]]
  * [[SEMVDHRUV/SEM V/AIML/Introduction to Neural Networks/Unit 3/Supervised Learning/1. Linear Regression/Linear Multiple Regression|Multivariate Regression]]
  * Regression Trees
  * Lasso Regression

---

# Classification Vs Regression
For a beginner One can imagine that regression tries to draw a line that fits all the data points under one line. Where as Classification Tries to draw a line that separates the two classes.

| Classification                                                                                                   | Regression                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Classification is a task of predicting values in discrete class labels                                           | Regression is a task of predicting values of a continuous feature                                                     |
| Classification means to group the output in a class                                                              | Regression means to predict output value using training data                                                          |
| Output is typically probability distribution over classes                                                        | Output is a continuous scalar                                                                                         |
| Performance of a Classification task is evaluated based on metrics like f1 score, accuracy, precision and recall | Performance of a Regression task is evaluated based on metrics like Root Mean Squared Error, Mean Squared Error, etc. |
| e.g. Classifying if the input image is a animal or not                                                           | e.g. Predicting the value of a stock price                                                                            |

