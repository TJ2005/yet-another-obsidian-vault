# Aptitude: Ratio & Proportion


---

## Key Formulas

> [!INFO] Definitions
> **Mean Proportional** between $a$ and $b$:
> $$\sqrt{ab}$$
>
> **Third Proportional** of $a$ and $b$ (where $a:b :: b:c$):
> $$c = \frac{b^2}{a}$$

---

## Problem 1: Land–Water Distribution on Earth

### Given
* **Global Ratio:** Land : Water = $1:2$
* **Northern Hemisphere Ratio:** Land : Water = $2:3$

### Solution strategy
Assume a total area that is divisible by the sum of the global ratio terms ($1+2=3$) and the hemisphere ratio terms ($2+3=5$), multiplied by 2 (for two hemispheres).
* $LCM(3, 5) = 15$.
* Let **Total Area of Earth = 30 units**.

### Calculation

**1. Global Distribution**
$$\text{Total Area} = 30$$
$$\text{Land} = \frac{1}{3} \times 30 = 10$$
$$\text{Water} = \frac{2}{3} \times 30 = 20$$

**2. Northern Hemisphere (Area = 15)**
Ratio is $2:3$ (Total 5 parts).
$$\text{1 part} = \frac{15}{5} = 3$$
$$\text{Northern Land} = 2 \times 3 = 6$$
$$\text{Northern Water} = 3 \times 3 = 9$$

**3. Southern Hemisphere (Area = 15)**
$$\text{Southern Land} = \text{Total Land} - \text{Northern Land}$$
$$S_L = 10 - 6 = 4$$

$$\text{Southern Water} = \text{Total Water} - \text{Northern Water}$$
$$S_W = 20 - 9 = 11$$

> [!SUCCESS] Answer
> **Southern Hemisphere Land : Water**
> $$4 : 11$$

---

## Proportions

### Problem 2 & 3: Mean Proportional
**Question:** Find the Mean Proportional of 16 and 36.

Let the mean proportional be $x$.
$$16 : x :: x : 36$$
$$x^2 = 16 \times 36$$
$$x = \sqrt{576}$$
$$x = 24$$

### Problem 4: Third Proportional
**Question:** Find the Third Proportional of 16 and 36.

Let the third proportional be $x$.
$$16 : 36 :: 36 : x$$
$$x = \frac{36^2}{16}$$
$$x = \frac{1296}{16}$$
$$x = 81$$

---

## Problem 5: Income & Expenditure

### Given
* **Income Ratio (A:B):** $4:5$
* **Expenditure Ratio (A:B):** $3:2$
* **Savings:** Each saves ₹5000

### Calculation
Let Income of A be $4x$ and Income of B be $5x$.
Using the formula:
$$\text{Expenditure} = \text{Income} - \text{Savings}$$

We set up the ratio of expenditures:
$$\frac{4x - 5000}{5x - 5000} = \frac{3}{2}$$

**Solve for $x$:**
$$2(4x - 5000) = 3(5x - 5000)$$
$$8x - 10000 = 15x - 15000$$
$$15x - 8x = 15000 - 10000$$
$$7x = 5000$$
$$x = \frac{5000}{7}$$

### Final Values

| Person | Income ($4x, 5x$) | Expenditure ($I - S$) |
| :--- | :--- | :--- |
| **A** | $$\frac{20000}{7}$$ | $$\frac{15000}{7}$$ |
| **B** | $$\frac{25000}{7}$$ | $$\frac{20000}{7}$$ |

> [!NOTE] Observation
> The numbers in this specific problem result in fractions. In typical exam questions, variables usually align to produce integer results (e.g., if Savings were ₹1000 or the ratios differed slightly).


## Problem 6: Bag of Coins (Value Breakdown)

### Given
* **Coins:** 1 Rupee, 50 Paise ($0.50$), 25 Paise ($0.25$)
* **Ratio of Quantity:** $5 : 7 : 9$
* **Total Value in Bag:** ₹430

### Solution
Let the number of coins be $5x$, $7x$, and $9x$.

**1. Calculate Total Value Equation**
$$(1 \times 5x) + (0.50 \times 7x) + (0.25 \times 9x) = 430$$
$$5x + 3.5x + 2.25x = 430$$

**2. Solve for $x$**
$$10.75x = 430$$
$$x = \frac{430}{10.75}$$
To simplify, multiply numerator/denominator by 100 or convert $10.75$ to fraction ($\frac{43}{4}$):
$$x = \frac{430}{\frac{43}{4}} = 430 \times \frac{4}{43} = 10 \times 4$$
$$x = 40$$

### Final Answer: Amount of Each Denomination
Substitute $x=40$ back into the value components:
* **1 Rupee Amount:** $5x \rightarrow 5(40) =$ **₹200**
* **50 Paise Amount:** $3.5x \rightarrow 3.5(40) =$ **₹140**
* **25 Paise Amount:** $2.25x \rightarrow 2.25(40) =$ **₹90**

> [!CHECK] Verification
> $$200 + 140 + 90 = 430 \quad \checkmark$$
### Extension: Total Number of Coins (Physical Count)

Now that we know $x = 40$, we calculate the actual **number of coins** using the original quantity ratio ($5:7:9$), *not* the value multipliers.

* **1 Rupee Coins:** $5x = 5(40) =$ **200 coins**
* **50 Paise Coins:** $7x = 7(40) =$ **280 coins**
* **25 Paise Coins:** $9x = 9(40) =$ **360 coins**

**Total Number of Coins in Bag:**
$$200 + 280 + 360 = 840 \text{ coins}$$

> [!WARNING] Important: Physical Count vs. Monetary Value
> The **physical quantity** ($7x, 9x$) must always stay as whole numbers—you cannot have "half" a physical coin.
> 
> The **fractional/decimal** multipliers ($0.5, 0.25$) are *only* used to find the monetary **value**.
> * **Physical:** $7 \times 40 = 280$ (Count)
> * **Value:** $0.5 \times 280 = 140$ (Rupees)
> 
> *The value becomes fractional/decimal, but the physical count stays as it is.*
---

## Problem 7: Sita & Gita (Income Calculation)

### Given
* **Income Ratio:** $5 : 7$
* **Expenditure Ratio:** $2 : 3$
* **Savings:** Each saves ₹3000
* **Goal:** Find Gita's Income.

### Solution (Using $E = I - S$)
Let Incomes be $5x$ and $7x$.
Since $\text{Expenditure} = \text{Income} - \text{Savings}$, the ratio of expenditures is:

$$\frac{5x - 3000}{7x - 3000} = \frac{2}{3}$$

**Cross Multiply:**
$$3(5x - 3000) = 2(7x - 3000)$$
$$15x - 9000 = 14x - 6000$$
$$15x - 14x = 9000 - 6000$$
$$x = 3000$$

**Calculate Gita's Income ($7x$):**
$$7 \times 3000 = 21000$$

> [!SUCCESS] Answer
> **Gita's Income = ₹21,000**

---

## Problem 8: A & B (Income Calculation)

### Given
* **Income Ratio:** $4 : 3$
* **Expenditure Ratio:** $3 : 2$
* **Savings:** Assumed equal savings (based on previous context)

### Solution (Using $E = I - S$)
Let Incomes be $4x$ and $3x$. Let savings be $S$.
The expenditure ratio equation is:

$$\frac{4x - S}{3x - S} = \frac{3}{2}$$

**Cross Multiply:**
$$2(4x - S) = 3(3x - S)$$
$$8x - 2S = 9x - 3S$$
$$3S - 2S = 9x - 8x$$
$$S = x$$

> [!TIP] Short Trick (Uniform Gap)
> Notice the ratio gap is uniform here:
> Income: $4 : 3$
> Expend: $3 : 2$
> Difference: $1 : 1$
>
> Since the difference is equal ($1 \text{ unit}$), **1 unit = Savings**.
> Therefore, **Income of A ($4\text{ units}$) = $4 \times \text{Savings}$**.

## Problem 9: Age Problem (Rahul & Sumit)

### Given
* **Present Age Ratio (Rahul : Sumit):** $11 : 13$
* **Conditional Ratio:** (Rahul's age **9 years ago**) : (Sumit's age **9 years hence**) = $17 : 25$

### Solution
Let the present ages be:
* **Rahul:** $11x$
* **Sumit:** $13x$

**1. Set up the Equation**
Using the conditional ratio:
$$\frac{11x - 9}{13x + 9} = \frac{17}{25}$$

**2. Solve for $x$ (Cross Multiply)**
$$25(11x - 9) = 17(13x + 9)$$
$$275x - 225 = 221x + 153$$

**3. Group Terms**
$$275x - 221x = 153 + 225$$
$$54x = 378$$
$$x = \frac{378}{54}$$
$$x = 7$$

### Final Answer
Calculate Rahul's **Present Age** ($11x$):
$$11 \times 7 = 77 \text{ years}$$

> [!SUCCESS] Answer
> **Rahul's Present Age = 77 years**

