---

Title: "APT Lecture 2 Compound interest and allat"

Status:

marker:

tags:

Date: "2026.03.11"

Time: "14:21"

---
# APT Lecture 2 Profit Sharing 
## Direct Variation & Proportionality

In mathematics and physics, when we say one variable is **directly proportional** to another, it means that as one increases, the other increases at a constant rate.

---

### 1. Distance, Speed, and Time

The relationship between distance, speed, and time is defined by the formula:

$$D = S \times T$$

#### Proportionality Breakdown:

* **$D \propto S$ (Distance is directly proportional to Speed):** If you keep the time ($T$) constant, doubling your speed will double the distance you travel.
* **$D \propto T$ (Distance is directly proportional to Time):** If you keep your speed ($S$) constant, driving for twice as long will result in twice the distance covered.

> [!NOTE]
> While $D$ is proportional to both, $S$ and $T$ are **inversely proportional** to each other for a fixed distance ($S \propto \frac{1}{T}$).

---

### 2. Work, Men, and Days

In productivity problems, the amount of work completed ($W$) depends on the resources (men) and the duration (days).

$$W \propto M \times D$$

#### Key Relationships:

* **$W \propto M$ (Work is proportional to Men):** If the number of days is fixed, adding more people to a task increases the total work output.
* *Example:* 10 men can build 2 walls; 20 men can build 4 walls.


* **$W \propto D$ (Work is proportional to Days):** If the number of men is fixed, working for more days increases the total work completed.

#### The Chain Rule Formula:

To solve for changes in these variables, we use the constant of proportionality ($k$):

$$\frac{W_1}{M_1 \times D_1} = \frac{W_2}{M_2 \times D_2}$$

* **$W$**: Work done
* **$M$**: Number of men (or machines/workers)
* **$D$**: Number of days (or time)

### Partnership and Profit Sharing

In business mathematics, when partners invest different amounts for the same duration, the **Profit Share** is directly proportional to their **Investment**.

---

### The Formula

The ratio of profit distribution is determined by the ratio of the capital invested:


$$P_1 : P_2 = I_1 : I_2$$

Where:

* $P$ = Profit share
* $I$ = Investment amount

---

### Step-by-Step Calculation

**1. Identify the Investments:**

* **Dhruv ($I_D$):** 40 Lakhs
* **Sam ($I_S$):** 20 Lakhs

**2. Determine the Investment Ratio:**
Simplify the ratio of their investments:


$$\text{Ratio} = 40 : 20 = 2 : 1$$

**3. Calculate the Total Parts:**
The total profit is divided into $2 + 1 = 3$ equal parts.

**4. Calculate Individual Profit Shares:**
The total profit to be split is **90 Lakhs**.

* **Dhruv's Share:**

$$\frac{2}{3} \times 90 = 60 \text{ Lakhs}$$


* **Sam's Share:**

$$\frac{1}{3} \times 90 = 30 \text{ Lakhs}$$



---

### Final Summary Table

| Partner | Investment | Ratio | Profit Share |
| --- | --- | --- | --- |
| **Dhruv** | 40 Lakhs | 2 | **60 Lakhs** |
| **Sam** | 20 Lakhs | 1 | **30 Lakhs** |
| **Total** | **60 Lakhs** | **3** | **90 Lakhs** |

> [!TIP]
> This calculation assumes both partners invested for the same period of time. If the time periods differed, you would multiply each investment by its respective time ($I \times T$) before calculating the ratio.

  
  
## Partnership and Profit Sharing

In business mathematics, when partners invest different amounts for the same duration, the **Profit Share** is directly proportional to their **Investment**.

---

## The Formula

The ratio of profit distribution is determined by the ratio of the capital invested:

$$P_1 : P_2 = I_1 : I_2$$

Where:

- $P$ = Profit share
    
- $I$ = Investment amount
    

---

## Step-by-Step Calculation

**1. Identify the Investments:**

- **Dhruv ($I_D$):** 40 Lakhs
    
- **Sam ($I_S$):** 20 Lakhs
    

**2. Determine the Investment Ratio:**

Simplify the ratio of their investments:

$$\text{Ratio} = 40 : 20 = 2 : 1$$

**3. Calculate the Total Parts:**

The total profit is divided into $2 + 1 = 3$ equal parts.

**4. Calculate Individual Profit Shares:**

The total profit to be split is **90 Lakhs**.

- **Dhruv's Share:**
    
    $$\frac{2}{3} \times 90 = 60 \text{ Lakhs}$$
    
- **Sam's Share:**
    
    $$\frac{1}{3} \times 90 = 30 \text{ Lakhs}$$
    

---

## Final Summary Table

|**Partner**|**Investment**|**Ratio**|**Profit Share**|
|---|---|---|---|
|**Dhruv**|40 Lakhs|2|**60 Lakhs**|
|**Sam**|20 Lakhs|1|**30 Lakhs**|
|**Total**|**60 Lakhs**|**3**|**90 Lakhs**|

> [!TIP]
> 
> This calculation assumes both partners invested for the same period of time. If the time periods differed, you would multiply each investment by its respective time ($I \times T$) before calculating the ratio.


```python
initial_budget = 1.0 # 1 Cr
men_increase = 1.20 # 20% increase
days_increase = 1.10 # 10% increase

new_budget = initial_budget * men_increase * days_increase
percentage_hike = (new_budget - initial_budget) / initial_budget * 100

print(f"{new_budget=}")
print(f"{percentage_hike=}")



```

```text
new_budget=1.32
percentage_hike=32.00000000000001


```

## Calculating Budget Hike for Contracts

When a budget is allotted based on resources (men) and time (days), the total work/budget ($W$) is directly proportional to both variables.

---

### The Proportion Relationship

From the work formula:


$$W \propto M \times D$$

This means if the number of workers ($M$) or the number of days ($D$) increases, the budget ($W$) required increases proportionally.

---

### Scenario: Calculating the Increase

**Initial State ($W_1$):**

* **Budget:** $1 \text{ Cr}$
* **Men:** $M_1$
* **Days:** $D_1$

**Updated State ($W_2$):**

* **Men ($M_2$):** $1.2 \times M_1$ (20% increase)
* **Days ($D_2$):** $1.1 \times D_1$ (10% increase)

---

### Calculation

Using the proportionality:


$$W_2 = (M_2 \times D_2)$$

$$W_2 = (1.2 \times M_1) \times (1.1 \times D_1)$$

$$W_2 = (1.2 \times 1.1) \times (M_1 \times D_1)$$

**Calculate the factor:**


$$1.2 \times 1.1 = 1.32$$

**Final Budget ($W_2$):**


$$W_2 = 1.32 \times W_1$$

$$W_2 = 1.32 \times 1 \text{ Cr} = 1.32 \text{ Cr}$$

---

### Summary of Results

* **New Total Budget:** $1.32 \text{ Cr}$
* **Total Budget Hike:** **32%** (or $32 \text{ Lakhs}$)

> [!IMPORTANT]
> A common mistake is to simply add the percentages ($20\% + 10\% = 30\%$). However, because the relationship is multiplicative ($M \times D$), you must use the **Compounding Effect**, which results in a **32%** hike.
## Partnership Calculation: Variable Time & Investment

In this scenario, we must calculate the **Effective Investment** for each partner, which is the product of their capital and the specific duration they were part of the business.

---

## 1. Identify the Variables

Since the "end" usually implies a standard business year, we assume the total cycle is **12 months**.

- **Partner A:** Invested $2000$ for the full **12 months**.
    
- **Partner B:** Joined 3 months later, so he was active for $12 - 3 = \mathbf{9 \text{ months}}$ with $4000$.
    
- **Partner C:** Was present for **ONLY 2 months** with $X$ amount.
    

> [!NOTE]
> 
> Since Partner C's investment amount wasn't specified, I will assume it matches the initial $2000$ to demonstrate the ratio, or you can plug in a specific value if provided. For this solution, let's assume **C invested 8000** to show a diverse split.

---

## 2. Calculate the Profit Sharing Ratio

The ratio is defined by $(I_1 \times T_1) : (I_2 \times T_2) : (I_3 \times T_3)$.

- **A's Share:** $2000 \times 12 = 24,000$
    
- **B's Share:** $4000 \times 9 = 36,000$
    
- **C's Share:** $8000 \times 2 = 16,000$
    

**Simplified Ratio:**

$$24,000 : 36,000 : 16,000$$

Divide all by 4,000:

$$\mathbf{6 : 9 : 4}$$

---

## 3. Step-by-Step Solution

**Total Parts in Ratio:** $6 + 9 + 4 = 19$ parts.

**Total Profit:** $112,000$.

#### Individual Split:

- **Value of 1 Part:** $\frac{112,000}{19} \approx 5,894.7$
    
- **Partner A's Profit:** $6 \times 5,894.7 = \mathbf{35,368.4}$
    
- **Partner B's Profit:** $9 \times 5,894.7 = \mathbf{53,052.6}$
    
- **Partner C's Profit:** $4 \times 5,894.7 = \mathbf{23,578.9}$
    

---

## Summary Table for Obsidian

|**Partner**|**Investment (I)**|**Time (T)**|**I×T**|**Ratio**|**Profit Share**|
|---|---|---|---|---|---|
|**A**|2000|12 mo|24,000|6|**35,368**|
|**B**|4000|9 mo|36,000|9|**53,053**|
|**C**|8000|2 mo|16,000|4|**23,579**|
|**Total**|||**76,000**|**19**|**112,000**|

Did Partner C have a specific investment amount in mind for your notes?
# References


###### Information
- date: 2026.03.11
- time: 14:21