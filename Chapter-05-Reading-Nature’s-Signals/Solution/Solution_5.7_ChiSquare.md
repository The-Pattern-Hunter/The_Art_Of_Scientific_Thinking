# Solution 5.7: Chi-Square Test for Mendelian Ratios

## Problem Summary
Testing Mendelian 3:1 ratio in pea plants (Rr × Rr cross). Two separate crosses with 200 seeds each.

---

## Question (a): Expected Frequencies (First Cross)

**Mendelian Prediction:** 3 round : 1 wrinkled (75% : 25%)

**Calculation for 200 seeds:**
```
Expected round = 200 × 0.75 = 150
Expected wrinkled = 200 × 0.25 = 50
```

**Result:**
- Expected round: 150 seeds
- Expected wrinkled: 50 seeds

---

## Question (b): Chi-Square Statistic (First Cross)

**Observed:** 142 round, 58 wrinkled

**Formula:**
```
χ² = Σ[(O - E)² / E]
```

**Calculation:**
```
χ² = [(142-150)²/150] + [(58-50)²/50]
   = [(-8)²/150] + [(8)²/50]
   = [64/150] + [64/50]
   = 0.427 + 1.280
   = 1.707
```

**Result: χ² = 1.707, df = 1**

---

## Question (c): Decision (First Cross)

**Comparison:**
- **Calculated χ² = 1.707**
- **Critical χ²(1, 0.05) = 3.841**

**Decision:** χ² = 1.707 < 3.841

**Fail to reject H₀**

**Biological Conclusion:**
The observed ratio (142:58 = 2.45:1) is not significantly different from the expected 3:1 Mendelian ratio (p > 0.05). The deviation can be explained by random sampling variation. Data are consistent with Mendelian inheritance.

---

## Question (d): Chi-Square (Second Cross)

**Observed:** 165 round, 35 wrinkled  
**Expected:** 150 round, 50 wrinkled

**Calculation:**
```
χ² = [(165-150)²/150] + [(35-50)²/50]
   = [(15)²/150] + [(-15)²/50]
   = [225/150] + [225/50]
   = 1.500 + 4.500
   = 6.000
```

**Result: χ² = 6.000, df = 1**

---

## Question (e): Decision (Second Cross)

**Comparison:**
- **Calculated χ² = 6.000**
- **Critical χ²(1, 0.05) = 3.841**

**Decision:** χ² = 6.000 > 3.841

**Reject H₀** (p < 0.05)

**Biological Conclusion:**
The observed ratio (165:35 = 4.71:1) significantly deviates from the expected 3:1 ratio. Too many round seeds and too few wrinkled seeds. This suggests non-Mendelian factors are operating.

---

## Question (f): Biological Explanations for Deviation

### Explanation 1: Differential Gamete Viability
**Mechanism:**
- Wrinkled allele (r) carried by some pollen grains may have reduced viability
- r pollen less likely to successfully fertilize ovules
- Results in fewer rr offspring than expected
- **Biological basis:** Wrinkled phenotype caused by defective starch synthesis; same defect may affect pollen function

### Explanation 2: Selective Seed Abortion
**Mechanism:**
- rr embryos may develop abnormally in some maternal environments
- Some rr seeds abort during development
- Selective loss of wrinkled seeds post-fertilization
- **Biological basis:** Nutritional stress or suboptimal conditions favor Rr and RR embryos over rr

### Explanation 3: Measurement/Sampling Bias
**Mechanism:**
- Wrinkled seeds may be smaller, less conspicuous
- Researcher may miss some wrinkled seeds during counting
- Slightly wrinkled seeds misclassified as round
- **Biological basis:** Human error, not genetic - wrinkled phenotype variable in expression

### Additional Possibilities:
- **Linkage to lethal:** r linked to embryonic lethal allele
- **Maternal effect:** Maternal genotype affects offspring ratios
- **Meiotic drive:** Preferential transmission of R allele

---

## Question (g): Pooled Data Analysis

**Pooled Totals (400 seeds):**
- Observed round: 142 + 165 = 307
- Observed wrinkled: 58 + 35 = 93
- **Observed ratio:** 307:93 = 3.30:1

**Expected (3:1 ratio):**
- Expected round: 400 × 0.75 = 300
- Expected wrinkled: 400 × 0.25 = 100

**Chi-Square Calculation:**
```
χ² = [(307-300)²/300] + [(93-100)²/100]
   = [(7)²/300] + [(-7)²/100]
   = [49/300] + [49/100]
   = 0.163 + 0.490
   = 0.653
```

**Result: χ² = 0.653, df = 1**

**Comparison:**
- **Calculated χ² = 0.653**
- **Critical χ²(1, 0.05) = 3.841**

**Decision:** χ² = 0.653 < 3.841

**Fail to reject H₀** (p > 0.05)

---

### Prediction vs Reality

**Prediction:** "Would pooled data fit better or worse?"

**Expected:** WORSE fit
- First cross fits well (χ² = 1.707)
- Second cross deviates significantly (χ² = 6.000)
- Pooling combines good and bad data
- Should show intermediate deviation

**Reality:** BETTER fit (χ² = 0.653)!

**Why the surprise?**
The two crosses deviate in **opposite directions:**
- First cross: Too few round (142 vs 150 expected) → deficit of 8
- Second cross: Too many round (165 vs 150 expected) → excess of 15

When pooled:
- Total deficit/excess approximately cancel out
- Combined ratio (3.30:1) very close to expected (3:1)
- Deviations partially compensate

**Lesson:** Pooling can mask underlying heterogeneity. Second cross still has biological issue even though pooled data appear fine.

---

## Summary Table

| Cross | Observed Ratio | χ² | df | Critical | Decision | Fits 3:1? |
|-------|----------------|----|----|----------|----------|-----------|
| First | 2.45:1 | 1.707 | 1 | 3.841 | Fail to reject | ✓ Yes |
| Second | 4.71:1 | 6.000 | 1 | 3.841 | Reject | ✗ No |
| Pooled | 3.30:1 | 0.653 | 1 | 3.841 | Fail to reject | ✓ Yes |

---

## Key Takeaways

### Chi-Square Test:
- Tests whether observed frequencies differ from expected
- Small χ² → good fit (fail to reject H₀)
- Large χ² → poor fit (reject H₀)
- df = (# categories - 1) = 2 - 1 = 1

### Biological Interpretation:
- First cross: Consistent with Mendelian genetics
- Second cross: Something disrupting expected ratios
- Need to investigate biological cause of deviation

### Statistical Caution:
- **Pooling data can hide problems**
- Second cross has real issue masked in pooled analysis
- Always examine individual experiments, not just totals

### Mendelian Genetics:
- 3:1 ratio expected for single gene, dominant/recessive
- Deviations indicate:
  - Differential viability
  - Selective effects
  - Measurement error
  - Or non-Mendelian inheritance

---

## Common Mistakes

**Mistake 1:** Using wrong expected frequencies
- Must use theoretical prediction (3:1), not observed ratios
- Expected = total × proportion, not rearranging observed

**Mistake 2:** Wrong degrees of freedom
- df = categories - 1 = 2 - 1 = 1 (NOT 2, NOT n-1)

**Mistake 3:** Claiming "proves Mendelian inheritance"
- Fail to reject ≠ proof
- Just means data consistent with hypothesis
- Other explanations possible

**Mistake 4:** Ignoring direction of deviation
- Second cross: excess round, deficit wrinkled
- Suggests specific biological mechanisms
- Pattern matters, not just magnitude

**Mistake 5:** Pooling without considering heterogeneity
- Pooled data look fine, but second cross clearly problematic
- Individual experiments tell different story

---

*Solution for The Pattern Hunters - Chapter 5, Problem 5.7*
