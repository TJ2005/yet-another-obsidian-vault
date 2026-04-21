Assumes a linear relationship between the input data and the output data.

Problem can be thought as of finding an equation to a straight line.

Where 
$$y = c_0 +c_1x_1 + \dots +c_nx_n$$
- With $n$ independent variables, $x_n$ 
	- Inputs
- One response variable, $y$ 
	- Output
- $n+1$ constants


### Slope
Indicates the steepness of a line change in the dependent variable for each unit change in the independent variable

Slope can be given as , $$C_1 = \frac{\sum_{i=1}^{n}(x_i-\overline{x})}{\sum{i=1}{n}(x_i-\overline{x}}$$

### Intercept
Indicates the location where it intersects an axis and represents the predicted value of the
dependent variable when the independent variable is zero.
$$C_0=\overline{Y}-C_1\overline{X}$$

### Example
**Model**: Predicting test score (`y`) based on hours studied (`x`)

$$\mathrm{Score}=\mathrm{Intercept}+\mathrm{Slope}\cdot \mathrm{Hours}$$

- **Intercept**: 40  
    → A student who studies **0 hours** is expected to score **40** (maybe from class participation or prior knowledge).
- **Slope**: 5  
    → **Each hour of study adds 5 points** to the score.

**Inference**:

- Intercept = **baseline ability**.
- Slope = **effectiveness of studying**

### **Dataset Overview**

- Variables: ( X ) and ( Y )
- Mean values:  
     $$\bar{X} = 135.7,\quad \bar{Y} = 18.0$$ 

### **Regression Formula**

$$ Y = C_0 + C_1 X $$

Where:

- ( $C_1$ ) is the **slope**
- ( $C_0$ ) is the **intercept**

### **Calculations**

- Slope:  $$C_1 = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2} = 0.146 $$
- Intercept:  $$C_0 = \bar{Y} - C_1$$$$ \bar{X} = -1.91$$ 

### **Final Regression Equation**

$$ Y = -1.91 + 0.146X $$

### **Interpretation**
- **Slope ( $C_1 = 0.146$ )**:  
    For every unit increase in ( $X$ ), ( $Y$ ) increases by approximately 0.146 units.
- **Intercept ( $C_0 = -1.91$ )**:  
    When ( $X = 0$ ), the predicted value of ( $Y$ ) is $-1.91$ (may not be meaningful depending on context).

---
