# Solution 7.1: Understanding Genetic Drift Variance

## Problem Summary
Three isolated butterfly populations with same initial allele frequencies (p=0.6, q=0.4) but different sizes: N=10, 100, 1000.

---

## Question (a): Calculate Variance

**Formula:**
```
σ² = pq / (2N)
```

**Population 1 (Nilgiri, N=10):**
```
σ² = (0.6)(0.4) / (2×10)
   = 0.24 / 20
   = 0.012
```

**Population 2 (Anamalai, N=100):**
```
σ² = (0.6)(0.4) / (2×100)
   = 0.24 / 200
   = 0.0012
```

**Population 3 (Periyar, N=1000):**
```
σ² = (0.6)(0.4) / (2×1000)
   = 0.24 / 2000
   = 0.00012
```

**Results Summary:**
- Population 1: σ² = 0.012
- Population 2: σ² = 0.0012 (10× smaller)
- Population 3: σ² = 0.00012 (100× smaller than Pop 1)

---

## Question (b): Standard Deviation

**Calculate σ = √σ²**

**Population 1:**
```
σ = √0.012 = 0.110 (11.0%)
```

**Population 2:**
```
σ = √0.0012 = 0.035 (3.5%)
```

**Population 3:**
```
σ = √0.00012 = 0.011 (1.1%)
```

**Interpretation:**

**Population 1 (N=10):** 
- Expected change per generation: ±11% around p=0.6
- Range: 0.49 to 0.71 (very unpredictable!)

**Population 2 (N=100):**
- Expected change: ±3.5% around p=0.6
- Range: 0.565 to 0.635 (moderate variation)

**Population 3 (N=1000):**
- Expected change: ±1.1% around p=0.6
- Range: 0.589 to 0.611 (very stable)

**Key Insight:** Standard deviation is inversely proportional to √N. Smaller populations show much larger random fluctuations.

---

## Question (c): Likelihood of Change to 0.7

**Change needed:** From p=0.6 to p=0.7 (increase of 0.10)

**Express as standard deviations:**
- **Population 1:** 0.10/0.110 = 0.91 SD
- **Population 2:** 0.10/0.035 = 2.86 SD
- **Population 3:** 0.10/0.011 = 9.09 SD

**Statistical interpretation:**
- Within 1 SD: ~68% of outcomes
- Within 2 SD: ~95% of outcomes
- Within 3 SD: ~99.7% of outcomes
- Beyond 3 SD: <0.3% chance

**Answers:**

**MOST likely:** Population 1 (N=10)
- Only 0.91 SD from mean
- Well within normal variation
- Probability: ~20% chance

**LEAST likely:** Population 3 (N=1000)
- 9.09 SD from mean
- Extremely rare event
- Probability: <0.00001% chance

**Population 2 (N=100):** Intermediate
- 2.86 SD from mean
- Rare but possible
- Probability: ~0.2% chance

---

## Question (d): Observed Results Consistent?

**Observations after 5 generations:**
- Population 1: Change = +0.2 (20%)
- Population 2: Change = +0.03 (3%)
- Population 3: Change = +0.01 (1%)

**Expected cumulative change over 5 generations:**
```
Expected cumulative σ = σ_single × √5

Population 1: 0.110 × √5 = 0.246 (24.6%)
Population 2: 0.035 × √5 = 0.078 (7.8%)
Population 3: 0.011 × √5 = 0.025 (2.5%)
```

**Comparison:**

**Population 1:** Observed 20% vs expected ±24.6%
- ✓ Consistent (within 1 SD)
- Large change expected in small population

**Population 2:** Observed 3% vs expected ±7.8%
- ✓ Consistent (within 1 SD)
- Moderate change as predicted

**Population 3:** Observed 1% vs expected ±2.5%
- ✓ Consistent (within 1 SD)
- Minimal change as predicted

**Conclusion:** All observations are consistent with drift predictions. The pattern perfectly matches theory: smallest population shows largest change, largest population shows smallest change.

---

## Question (e): Conservation Priority

**Answer: Population 3 (N=1000) - Periyar Reserve**

**Reasoning:**

### **Genetic Stability:**
- Drift effect minimal (σ = 1.1% per generation)
- Retains diversity over many generations
- Less vulnerable to random allele loss

### **Long-term Viability:**
Calculate heterozygosity loss over 20 generations:
```
Population 1 (N=10): H_20 = H_0 × (1-1/20)^20 = H_0 × 0.358
Loss: 64.2% of diversity

Population 2 (N=100): H_20 = H_0 × (1-1/200)^20 = H_0 × 0.905
Loss: 9.5% of diversity

Population 3 (N=1000): H_20 = H_0 × (1-1/2000)^20 = H_0 × 0.990
Loss: 1.0% of diversity
```

### **Evolutionary Potential:**
- Maintains rare alleles better
- Can respond to environmental changes
- Genetic toolkit preserved

### **Cost-Effectiveness:**
- Already large and stable
- Less intensive management needed
- Natural processes maintain diversity

### **Population 1 & 2 Concerns:**
- Population 1: Likely lose 64% diversity in ~40 years (assuming 2-year generation)
- Population 2: Moderate loss (9.5%) requires intervention
- Both need genetic rescue or population enhancement

**Conservation Strategy:**
1. **Protect Population 3** (core genetic reservoir)
2. **Enhance Populations 1 & 2** (increase N_e)
3. **Establish corridors** (gene flow between populations)

---

## Key Takeaways

### **Drift Variance Principles:**
- σ² inversely proportional to N (σ² ∝ 1/N)
- Standard deviation inversely proportional to √N (σ ∝ 1/√N)
- 10× larger population → 10× smaller variance
- 100× larger population → 100× smaller variance

### **Predictability vs Population Size:**
- **Small populations (N<50):** Highly unpredictable, large random changes
- **Medium populations (N=50-500):** Moderate variation
- **Large populations (N>500):** Relatively predictable, small changes

### **Cumulative Effects:**
Over t generations, cumulative change = σ × √t
- Random walk increases with √t, not linearly
- Long-term effects compound

### **Conservation Implications:**
- **Population counting insufficient** - must track genetic variance
- **Small populations at high risk** - even if no immediate threats
- **Large populations are genetic insurance** - protect as core reserves
- **Gene flow can rescue small populations** - connectivity critical

---

## Common Mistakes

**Mistake 1:** Confusing σ² with σ
- Variance and standard deviation are different
- Must take square root to get standard deviation

**Mistake 2:** Expecting linear relationship with N
- Drift variance ∝ 1/N (inverse)
- Not: larger N = slightly less drift
- Reality: 10× larger N = 10× less drift

**Mistake 3:** Assuming cumulative change = single generation × t
- Wrong: 5 generations ≠ 5× single generation change
- Correct: 5 generations = √5× single generation change
- Random walk (not directional)

**Mistake 4:** Ignoring practical meaning of SD
- 11% SD in Population 1 is HUGE
- Allele can swing from 0.6 to 0.7 easily
- Can fix or lose alleles rapidly

**Mistake 5:** Protecting smallest populations
- Emotional appeal: "save the most vulnerable"
- Genetic reality: smallest may be doomed by drift
- Strategy: Protect large populations, rescue small ones

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.1*
