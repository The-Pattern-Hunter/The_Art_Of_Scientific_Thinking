# Solution 5.5: ANOVA with Post-Hoc Analysis

## Problem Summary
Testing 4 anesthetic drugs on tigers (n=6 per drug). Measuring recovery time in minutes.

**Data:** Drug A (46.67), Drug B (33.67), Drug C (39.67), Drug D (29.33)

---

## Question (a): Hypotheses

**H₀:** μ_A = μ_B = μ_C = μ_D (all drug means equal - no difference in recovery time)

**H₁:** At least one drug mean differs from the others

---

## Question (b): Between Groups Sum of Squares (BSS)

**Formula:**
```
BSS = Σ[nⱼ(x̄ⱼ - x̄_overall)²]
```

**Calculation:**
```
Grand mean = 37.33 minutes
n = 6 per group

BSS = 6[(46.67-37.33)² + (33.67-37.33)² + (39.67-37.33)² + (29.33-37.33)²]
    = 6[(9.34)² + (-3.66)² + (2.34)² + (-8.00)²]
    = 6[87.24 + 13.40 + 5.48 + 64.00]
    = 6 × 170.12
    = 1,020.72
```

**Result: BSS = 1,020.72**

---

## Question (c): Total Sum of Squares (TSS)

**Formula:**
```
TSS = Σ(all observations - grand mean)² = (Sum of x²) - (Grand total)²/N
```

**Given:**
- Sum of all x² = 34,508
- Grand total = 896
- N = 24

**Calculation:**
```
TSS = 34,508 - (896)²/24
    = 34,508 - 802,816/24
    = 34,508 - 33,450.67
    = 1,057.33
```

**Result: TSS = 1,057.33**

---

## Question (d): Within Groups Sum of Squares (WSS)

**Formula:**
```
WSS = TSS - BSS
```

**Calculation:**
```
WSS = 1,057.33 - 1,020.72
    = 36.61
```

**Result: WSS = 36.61**

---

## Question (e): ANOVA Table

| Source | SS | df | MS | F |
|--------|----|----|----|----|
| Between Groups | 1,020.72 | 3 | 340.24 | 186.19 |
| Within Groups | 36.61 | 20 | 1.83 | |
| Total | 1,057.33 | 23 | | |

**Calculations:**
```
df_between = k - 1 = 4 - 1 = 3
df_within = N - k = 24 - 4 = 20
df_total = N - 1 = 24 - 1 = 23

MSB = BSS/df_between = 1,020.72/3 = 340.24
MSW = WSS/df_within = 36.61/20 = 1.83

F = MSB/MSW = 340.24/1.83 = 186.19
```

---

## Question (f): Statistical Decision

**Comparison:**
- **Calculated F = 186.19**
- **Critical F(3,20,0.05) = 3.10**

**Decision:** F = 186.19 >> 3.10

**Reject H₀** - At least one drug produces significantly different recovery time (p < 0.001)

---

## Question (g): Tukey HSD Post-Hoc Test

**Calculate HSD:**
```
HSD = q × √(MSW/n)
    = 3.96 × √(1.83/6)
    = 3.96 × √0.305
    = 3.96 × 0.552
    = 2.19 minutes
```

**Pairwise Comparisons:**

| Comparison | Difference | > HSD (2.19)? | Significant? |
|------------|------------|---------------|--------------|
| A vs B | \|46.67 - 33.67\| = 13.00 | ✓ | **Yes** |
| A vs C | \|46.67 - 39.67\| = 7.00 | ✓ | **Yes** |
| A vs D | \|46.67 - 29.33\| = 17.34 | ✓ | **Yes** |
| B vs C | \|33.67 - 39.67\| = 6.00 | ✓ | **Yes** |
| B vs D | \|33.67 - 29.33\| = 4.34 | ✓ | **Yes** |
| C vs D | \|39.67 - 29.33\| = 10.34 | ✓ | **Yes** |

**All pairwise differences exceed HSD = 2.19**

**Result:** All 6 comparisons are statistically significant - every drug differs from every other drug.

---

## Question (h): Recommendation

**Ranking by Recovery Time (fastest to slowest):**
1. **Drug D:** 29.33 min (fastest recovery) ⭐
2. **Drug B:** 33.67 min
3. **Drug C:** 39.67 min
4. **Drug A:** 46.67 min (slowest recovery)

**Recommendation: Drug D (Combination)**

**Rationale:**
1. **Fastest recovery:** 29.33 min average (37% faster than Drug A)
2. **Statistically superior:** Significantly better than all other drugs
3. **Animal welfare:** Minimizes time in compromised state
4. **Safety margin:** 17-min faster than slowest drug
5. **Veterinary efficiency:** Can process more captures per day

**Considerations:**
- Verify no adverse side effects with Drug D
- Cost-benefit analysis (if Drug D more expensive)
- Confirm ease of administration
- Check availability/storage requirements

**Clinical significance:** 17-minute difference (Drug D vs A) is highly meaningful for field operations and animal welfare.

---

## Key Results Summary

### Statistical Findings:
- **F = 186.19, p < 0.001:** Extremely strong evidence of differences
- **All pairwise comparisons significant:** Each drug is distinct
- **Large effect:** Drugs explain 96.5% of variance (η² = BSS/TSS = 0.965)

### Practical Implications:
- **Clear winner:** Drug D significantly best
- **Avoid Drug A:** Longest recovery, no advantages
- **Intermediate options:** Drugs B and C if D unavailable

### Biological Meaning:
Drug choice has major impact on tiger recovery. Using optimal drug (D) reduces recovery time by 40% compared to worst drug (A), improving both animal welfare and capture efficiency.

---

## Common Mistakes

**Mistake 1:** Multiple t-tests instead of ANOVA
- Would require 6 comparisons, inflate error rate to 26%
- ANOVA controls family-wise error at 5%

**Mistake 2:** Stopping at ANOVA without post-hoc
- ANOVA says "at least one differs" but not which ones
- Need Tukey HSD to identify specific differences

**Mistake 3:** Using wrong error term
- Must use MSW (within-groups variance), not individual SDs
- MSW pools variance across all groups

**Mistake 4:** Ignoring effect size
- F-statistic alone doesn't show magnitude
- η² = 0.965 shows drugs explain almost all variance (huge effect)

**Mistake 5:** Recommending based solely on fastest mean
- Must confirm difference is statistically significant
- Could be noise if not tested properly

---

*Solution for The Pattern Hunters - Chapter 5, Problem 5.5*
