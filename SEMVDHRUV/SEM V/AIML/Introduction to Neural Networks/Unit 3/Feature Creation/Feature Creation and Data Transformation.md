## Overview
Feature engineering is the process of transforming raw data into meaningful features that improve the performance of machine learning models. It involves creating, modifying, and selecting variables to capture underlying patterns.

---

## Steps in Feature Engineering
1. Feature Creation:
	-  It involves creating new variables which will be most helpful for our model. This can be adding or removing some features.
	- Ex: Extracting the day of the week from a date

2. **Transformations**
   - Is simply a function that transforms features from one representation to another (Ex: Log transformation, Min-Max scaling, Encoding, Standardization etc.).

1. **Feature Extraction**
   - Is about extracting/deriving information from the original features set to create a new features subspace
   - Encode categorical variables.
   - Apply domain knowledge to derive meaningful attributes.

4. **Feature Transformation**
   - Normalize or standardize numerical features.
   - Apply scaling for algorithms sensitive to magnitude.
   - Log, square root, or polynomial transformations for skewed data.

5. **Feature Selection**
   - Remove irrelevant or redundant features.
   - Use statistical tests, correlation analysis, or model-based importance.

6. **Validation**
   - Evaluate impact of engineered features on model performance.
   - Ensure transformations generalize across datasets.

---

## Techniques for Feature Engineering

### 1. Encoding
- **One-Hot Encoding**: Convert categorical values into binary vectors.
- **Label Encoding**: Assign integer values to categories.
- **Target Encoding**: Replace categories with aggregated target statistics.

### 2. Scaling and Normalization
- **Min-Max Scaling**: Scale values to a fixed range (e.g., [0,1]).
- **Standardization (Z-score)**: Center values around mean with unit variance.
- **Robust Scaling**: Use median and IQR to reduce outlier influence.

### 3. Transformation
- **Log Transformation**: Reduce skewness in distributions.
- **Polynomial Features**: Capture non-linear relationships.
- **Binning**: Group continuous values into discrete intervals.

### 4. Aggregation
- **Group-based Features**: Aggregate statistics (mean, sum, count) by category.
- **Rolling/Aggregated Time Features**: Moving averages, lags, and cumulative sums.

### 5. Interaction Features
- **Feature Crosses**: Combine two or more features (e.g., product, ratio).
- **Domain-Specific Combinations**: Derived from expert knowledge.

### 6. Temporal Features
- Extract components like year, month, day, weekday, hour.
- Calculate elapsed times or durations.

### 7. Text Features
- **Bag of Words / TF-IDF**: Represent text as frequency vectors.
- **Embeddings**: Dense vector representations (Word2Vec, BERT).
- **Text Length / Sentiment Scores**.

### 8. Feature Selection Methods
- **Filter Methods**: Correlation, Chi-square, mutual information.
- **Wrapper Methods**: Recursive Feature Elimination (RFE).
- **Embedded Methods**: Lasso, decision tree feature importance.
