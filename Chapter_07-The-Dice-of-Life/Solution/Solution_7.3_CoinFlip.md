# Solution 7.3: The Coin Flip Analogy

## Problem Summary
Classroom simulation of genetic drift using coin flips. Three groups simulate populations of different sizes (10, 50, 500 individuals).

---

## Question (a): Calculate Deviations

**Expected:** 50% A allele (heads)

**Deviations:**
```
Group 1: |70% - 50%| = 20%
Group 2: |54% - 50%| = 4%
Group 3: |49.6% - 50%| = 0.4%
```

**Results:**
- Group 1 (N=10): 20% deviation
- Group 2 (N=50): 4% deviation
- Group 3 (N=500): 0.4% deviation

---

## Question (b): Largest Deviation

**Answer: Group 1 (smallest population)**

**Is this predicted by drift theory?** ✅ YES

**Drift theory predicts:**
```
σ ∝ 1/√N

Group 1: σ ∝ 1/√10 = 0.316
Group 2: σ ∝ 1/√50 = 0.141  (2.2× smaller)
Group 3: σ ∝ 1/√500 = 0.045 (7× smaller than Group 1)
```

**Observed pattern matches perfectly:**
- Smallest population: Largest deviation (20%)
- Medium population: Medium deviation (4%)
- Largest population: Smallest deviation (0.4%)

---

## Question (c): Expected Standard Deviations

**Formula:**
```
σ = √(pq/n)  where p=q=0.5
σ = √(0.25/n) = 0.5/√n
```

**Group 1 (n=10):**
```
σ = 0.5/√10 = 0.5/3.16 = 0.158 (15.8%)
```

**Group 2 (n=50):**
```
σ = 0.5/√50 = 0.5/7.07 = 0.071 (7.1%)
```

**Group 3 (n=500):**
```
σ = 0.5/√500 = 0.5/22.36 = 0.022 (2.2%)
```

**Do observations fall within 1 SD?**

**Group 1:** Observed 20% vs expected ±15.8%
- **Slightly outside** (1.3 SD) but not extreme

**Group 2:** Observed 4% vs expected ±7.1%
- ✓ **Within 1 SD**

**Group 3:** Observed 0.4% vs expected ±2.2%
- ✓ **Well within 1 SD**

**Conclusion:** All reasonable given sampling variation.

---

## Question (d): Pattern in Group 1 Repeated Trials

**Five trials for Group 1 (N=10):**
- Trial 1: 70% A
- Trial 2: 40% A
- Trial 3: 60% A
- Trial 4: 50% A
- Trial 5: 30% A

**Pattern observed:**
1. **High variability:** Range from 30% to 70% (40% spread)
2. **No trend:** Doesn't consistently increase or decrease
3. **Random walk:** Bounces around unpredictably
4. **Clusters near 50%:** Mean ≈ 50% but individual trials vary widely

**What this tells us:**

### **Unpredictability in Small Populations:**
- Cannot predict next generation from current
- Each generation is independent random sample
- Historical trend doesn't predict future

### **Random Walk Behavior:**
- Drift is non-directional
- Sometimes increases, sometimes decreases
- No "memory" of previous values

### **High Variance:**
```
Observed variance across 5 trials:
Mean = 50%
Trials: 70, 40, 60, 50, 30
Variance = [(20)² + (-10)² + (10)² + (0)² + (-20)²] / 5
         = [400 + 100 + 100 + 0 + 400] / 5
         = 200

SD = √200 = 14.1%
```
Matches theoretical prediction of σ = 15.8%!

### **Conservation Implication:**
- Small populations behave unpredictably
- Cannot rely on current allele frequencies staying stable
- Management must account for random swings

---

## Question (e): Will 1000 Flips Give Exactly 50%?

**Answer:** Almost certainly **NO**, but very close.

**Explanation:**

### **Expected Outcome:**
```
Expected heads = 1000 × 0.5 = 500
Standard deviation = √(1000 × 0.5 × 0.5) = √250 = 15.8 heads

As percentage: σ = 15.8/1000 = 0.0158 (1.58%)
```

### **Probability of EXACTLY 50.0%:**
Very low! Probability of exactly 500/1000 ≈ 2.5%

### **Probability of being CLOSE (within 1%):**
Within 1% means 490-510 heads (49%-51%)
Using normal approximation: ~68% probability

### **The Law of Large Numbers:**
- Larger samples → closer to expected value
- But NOT exact, just more precise
- Still subject to random variation

### **Relationship Between Population Size and Predictability:**

| Population Size | Expected σ | Predictability |
|----------------|------------|----------------|
| 10 | ±15.8% | Very unpredictable |
| 50 | ±7.1% | Moderately unpredictable |
| 500 | ±2.2% | Fairly predictable |
| 1000 | ±1.6% | Quite predictable |
| 10,000 | ±0.5% | Very predictable |

**Key Insight:**
- Large populations approach expected values but never exactly
- Precision improves with √N
- 100× larger population → 10× more precise
- But still fundamentally stochastic (random)

---

## Key Takeaways

### **Genetic Drift as Sampling:**
- Like drawing colored balls from a bag
- Each generation = random sample from parent generation
- Smaller samples = more sampling error

### **Population Size Effects:**
- **Small (N<50):** Highly unpredictable, large swings
- **Medium (N=50-500):** Moderate variation
- **Large (N>500):** Relatively predictable, small changes

### **Random Walk Properties:**
1. **Non-directional:** Equal probability up or down
2. **No memory:** Past doesn't predict future
3. **Variance increases with time:** But as √t, not linearly
4. **Eventually reaches boundaries:** Can fix or lose alleles

### **Law of Large Numbers:**
- Averages converge to expectation
- But individual outcomes still variable
- Precision ∝ 1/√N

### **Teaching Value:**
- Coin flips make drift concrete
- Students see randomness directly
- Builds intuition before mathematics
- Shows sampling error visually

---

## Common Mistakes

**Mistake 1:** "Drift is just noise, doesn't matter"
- Wrong: Drift can fix or lose alleles permanently
- In small populations, drift > selection

**Mistake 2:** "Larger samples always give 50% exactly"
- Wrong: Still variation, just smaller
- 1000 flips ≈ 50% ± 1.6%, not exactly 50.0%

**Mistake 3:** "Seeing 70% in Trial 1 means next will be higher"
- Wrong: Each trial independent
- No momentum or trend
- Gambler's fallacy

**Mistake 4:** "If average is 50%, population is stable"
- Wrong: Individual lineages highly variable
- Average across many populations ≠ single population

**Mistake 5:** "Drift only affects neutral alleles"
- Wrong: Drift affects ALL alleles
- Can override weak selection
- In small populations, drift dominates

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.3*
