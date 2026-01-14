# Solution 5.8: Multiple Testing Correction

## Problem Summary
GWAS testing 20 genes for diabetes association. Need to correct for multiple testing to control false positives.

---

## Question (a): Naive Approach (No Correction)

**Threshold:** α = 0.05

**Significant genes (p < 0.05):**
1. Gene 1 (p = 0.001)
2. Gene 2 (p = 0.003)
3. Gene 3 (p = 0.008)
4. Gene 4 (p = 0.012)
5. Gene 5 (p = 0.025)
6. Gene 6 (p = 0.048)

**Total: 6 genes declared significant**

---

## Question (b): Family-Wise Error Rate

**Formula:**
```
P(at least one false positive) = 1 - (1 - α)^m
```

**Calculation:**
```
m = 20 tests
α = 0.05

P(≥1 false positive) = 1 - (1 - 0.05)^20
                      = 1 - (0.95)^20
                      = 1 - 0.358
                      = 0.642
```

**Result: 64.2% probability of at least one false positive**

**Interpretation:**
If NONE of the 20 genes truly associate with diabetes, we still expect to find significant results 64% of the time just by chance! This is unacceptably high.

**Expected false positives:** 20 × 0.05 = 1 gene by chance alone

---

## Question (c): Bonferroni Correction

**Adjusted threshold:**
```
α_Bonferroni = α / m
             = 0.05 / 20
             = 0.0025
```

**Result: New threshold = 0.0025**

**Genes significant after Bonferroni:**
1. Gene 1 (p = 0.001 < 0.0025) ✓
2. Gene 2 (p = 0.003 > 0.0025) ✗

**Total: Only 2 genes significant** (Gene 1 and Gene 2)

Wait - Gene 2 (p = 0.003) is borderline. Let me recalculate:
- Gene 2: p = 0.003 > 0.0025, so **NOT significant**

**Correction: Only Gene 1 is significant after Bonferroni**

---

## Question (d): False Discovery Rate (FDR)

**Benjamini-Hochberg Procedure:**

| Rank (i) | Gene | P-value | (i/20) × 0.05 | Compare | Significant? |
|----------|------|---------|---------------|---------|--------------|
| 1 | Gene 1 | 0.001 | 0.0025 | 0.001 < 0.0025 | ✓ Yes |
| 2 | Gene 2 | 0.003 | 0.0050 | 0.003 < 0.0050 | ✓ Yes |
| 3 | Gene 3 | 0.008 | 0.0075 | 0.008 > 0.0075 | ✗ No |
| 4 | Gene 4 | 0.012 | 0.0100 | 0.012 > 0.0100 | ✗ No |
| 5 | Gene 5 | 0.025 | 0.0125 | 0.025 > 0.0125 | ✗ No |
| 6 | Gene 6 | 0.048 | 0.0150 | 0.048 > 0.0150 | ✗ No |

**Procedure:**
Find largest i where p_i ≤ (i/20) × 0.05

- Rank 1: 0.001 ≤ 0.0025 ✓
- Rank 2: 0.003 ≤ 0.0050 ✓
- Rank 3: 0.008 > 0.0075 ✗ STOP

**Largest i = 2**

**Genes significant after FDR:** Gene 1 and Gene 2

**Total: 2 genes significant**

---

## Question (e): Comparison Table

| Method | # Significant | Gene IDs | Conservative? |
|--------|---------------|----------|---------------|
| No correction | 6 | 1,2,3,4,5,6 | Least (liberal) |
| Bonferroni | 1 | 1 | Most (conservative) |
| FDR (B-H) | 2 | 1,2 | Intermediate |

---

## Question (f): Trade-offs Discussion

### Most Conservative: Bonferroni
**Pros:**
- Controls family-wise error rate at exactly 5%
- Guarantees low false positive rate
- Simple to calculate

**Cons:**
- Very stringent, high false negative rate (Type II errors)
- Loses statistical power dramatically with many tests
- May miss true associations (only Gene 1 detected)

### Most Liberal: No Correction
**Pros:**
- Maximum power to detect true effects
- Finds all 6 potentially interesting genes

**Cons:**
- 64% chance of ≥1 false positive
- Expect ~1 false positive among 6 discoveries
- Not publishable in reputable journals

### Middle Ground: FDR (Recommended)
**Pros:**
- Controls proportion of false discoveries (not probability)
- More powerful than Bonferroni
- Appropriate for exploratory research (GWAS)
- Accepts that some discoveries may be false, but limits proportion

**Cons:**
- Doesn't control family-wise error rate
- May still include false positives
- More complex to explain

### Recommendation for GWAS: **FDR (Benjamini-Hochberg)**

**Rationale:**
1. **Balance:** Finds Gene 2 that Bonferroni misses, controls false discoveries
2. **GWAS context:** Testing thousands of SNPs/genes, need power
3. **Exploratory:** Follow-up studies will validate findings
4. **Standard:** Widely accepted in genomics field
5. **Practical:** Bonferroni too conservative for 20,000+ SNP studies

**Note:** For clinical decisions (not discovery), might prefer Bonferroni's stricter control.

---

## Question (g): Power and Bonferroni

**Gene 5 scenario:**
- p = 0.025
- Bonferroni threshold = 0.0025
- Gene 5 NOT detected
- BUT Gene 5 truly affects diabetes (given in question)

**Error type:** **Type II Error (False Negative)**

**Definition:**
- Failed to reject H₀ when H₁ is true
- Missed a real effect
- Reduced power due to stringent correction

### Why Bonferroni Problematic for GWAS

**Scenario:** Testing 20,000 SNPs (typical GWAS)

**Bonferroni threshold:**
```
α = 0.05 / 20,000 = 0.0000025 (2.5 × 10^-6)
```

**Consequences:**
1. **Extreme threshold:** p-value must be < 0.0000025
2. **Massive sample sizes needed:** Thousands of patients
3. **High Type II error:** Miss many true associations
4. **Impractical:** Real effects go undetected

**Example:**
- True causal SNP with p = 0.00001 (very strong signal!)
- Bonferroni: NOT significant (0.00001 > 0.0000025)
- FDR: WOULD be significant
- **Bonferroni throws out real discoveries**

### Solution for GWAS:
1. **Discovery phase:** Use FDR (exploratory)
2. **Validation phase:** Test top hits in independent cohort
3. **Functional studies:** Biological validation
4. **Replication:** Multiple independent studies

**Two-stage approach prevents both:**
- False positives (require replication)
- Excessive false negatives (use FDR initially)

---

## Summary: When to Use Each Method

### Bonferroni:
- Small number of tests (<20)
- Clinical decisions with high stakes
- Confirmatory testing
- When Type I error is critical

### FDR:
- Many tests (>20)
- Exploratory research (GWAS, proteomics)
- Discovery phase
- When Type II error is concerning

### No Correction:
- Preliminary screening only
- Not for final conclusions
- Hypothesis generation (not testing)

---

## Key Takeaways

### Multiple Testing Problem:
- Testing many hypotheses inflates false positive rate
- Without correction, 64% chance of false positive here
- Problem grows exponentially with more tests

### Correction Methods:
- **Bonferroni:** Controls FWER (family-wise error rate)
- **FDR:** Controls false discovery rate (less stringent)
- Trade-off: False positives vs. false negatives (power)

### GWAS Context:
- Modern GWAS test millions of variants
- Bonferroni too conservative
- FDR standard approach
- Validation in independent samples essential

### General Principle:
**Multiple testing correction is non-negotiable for scientific integrity**
- Prevents chasing false leads
- Increases reproducibility
- Required by journals

---

## Common Mistakes

**Mistake 1:** Not correcting at all
- Unacceptable for published research
- High false positive rate

**Mistake 2:** Over-correcting with Bonferroni for GWAS
- Too conservative, miss real signals
- FDR more appropriate

**Mistake 3:** Applying correction after seeing results
- Must pre-specify correction method
- Post-hoc choices are data dredging

**Mistake 4:** Forgetting to correct in analysis plan
- Build correction into study design
- Calculate required sample size accounting for correction

---

*Solution for The Pattern Hunters - Chapter 5, Problem 5.8*
