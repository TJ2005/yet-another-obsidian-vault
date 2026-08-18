## Metrics for Cost and Loss Functions ( For Regression )

## Variable Definitions

- $y_i$: Actual (true) value for the $i^{th}$ data point
- $\hat{y}_i$: Predicted value for the $i^{th}$ data point
- $n$: Total number of data points (samples)
- $y_i - \hat{y}_i$: Prediction error (residual) for the $i^{th}$ sample
- $|y_i - \hat{y}_i|$: Absolute error
- $(y_i - \hat{y}_i)^2$: Squared error

---
### Mean Error  
- Average of all error values  
- Can cancel out due to positive and negative errors  
$$
\text{Mean Error} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)
$$

### Mean Squared Error (MSE)  
- Also known as **L2 loss**  
- Squares the error to avoid cancellation  
- Sensitive to outliers  
$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

### Mean Absolute Error (MAE)  
- Also known as **L1 loss**  
- Uses absolute difference  
- Robust to outliers  
$$
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|
$$

### Root Mean Squared Error (RMSE)  
- Square root of MSE  
- Easier to interpret in original units  
$$
\text{RMSE} = \sqrt{ \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 }
$$

---