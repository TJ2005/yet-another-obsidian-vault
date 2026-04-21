
## Bias and Variance

### Bias  
- Error from simplifying a complex real-world problem  
- Caused by assumptions that make the target function easier to learn  
- **High bias** → model too simple → **underfitting**  
- Example: Voice assistant trained on one region fails in another due to dialect differences

#### Types of Bias  
- **Prejudicial Bias**: Favoring certain groups (e.g., male candidates)  
- **Sampling Bias**: Over/under-representing population groups  
- **Algorithm Bias**: Poor algorithm choice 
- **Confirmation Bias**: Retaining info that supports prior beliefs

---

### Variance  
- Error from model’s sensitivity to training data fluctuations  
- **High variance** → model fits noise → **overfitting**  
- Example: Decision tree changes splits drastically across datasets

---

### Bias–Variance Trade-off  
- Increasing model complexity ↓ bias but ↑ variance  
- High bias → low variance (stable but inaccurate)  
- High variance → low bias (accurate but unstable)  
- Ideal model balances both, but perfect balance is rare  
- Trade-off is essential for generalization to unseen data

---

### Network Classification Example  
**High Variance Model**:  
- Sample 1 → detects port scans, misses SQL injections  
- Sample 2 → detects SQL injections, misses DDoS  
- Sample 3 → detects DDoS, misses port scans  
→ Overfits to sample-specific patterns

**Low Variance Model**:  
- Learns general rules like:  
  - High packet rate → suspicious  
  - Many ports scanned → port scan  
  - Thousands of requests/sec → DDoS  
→ Predictions remain consistent across samples

---
