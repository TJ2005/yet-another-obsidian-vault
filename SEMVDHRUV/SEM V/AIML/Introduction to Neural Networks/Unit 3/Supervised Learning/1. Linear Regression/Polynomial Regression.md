## Polynomial Regression

### Definition  
A regression equation where the independent variable has a power greater than one is called a polynomial regression equation.

Example:  

$$y = a + b x^2$$

### Characteristics  
- The best fit line is a **curve**, not a straight line  
- Captures **curvilinear relationships** between independent and dependent variables

### Model Behavior  
- **Higher-degree polynomials** may reduce error but risk **overfitting**  
- **Lower-degree polynomials** may lead to **underfitting**  
- It is important to choose an **optimal degree** to balance bias and variance
- Easy to overfit and underfit


---

## Polynomial Regression – Categories and Applications

### Degree-Based Classification  
Polynomial regression models are categorized based on the degree of the independent variable:

- **Linear**: Degree = 1  
  $$
  y = a + b_1 x
 $$
- **Quadratic**: Degree = 2  
  $$
  y = a + b_1 x + b_2 x^2
 $$
- **Cubic**: Degree = 3  
  $$
  y = a + b_1 x + b_2 x^2 + b_3 x^3
 $$
- Higher degrees follow similarly:
  $$
  y = a + b_1 x + b_2 x^2 + \dots + b_n x^n
 $$

### Sensitivity to Outliers  
- Outliers can significantly distort the shape of the fitted curve  
- Nonlinear models are more sensitive to extreme values than linear models

### Applications  
Polynomial regression is useful in domains where relationships between variables are nonlinear, including:

- Finance  
- Physics  
- Engineering  
- Social sciences

---
