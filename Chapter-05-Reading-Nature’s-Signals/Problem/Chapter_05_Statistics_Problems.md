# Chapter 5: Reading Nature's Signals – Statistics Problems

## Practice Problems for "The Pattern Hunters"
**Chapter 5: Statistics as a Pattern Hunter's Toolkit**

---

## Problem Set Overview

**Total Problems:** 10  
**Difficulty Distribution:**
- ⭐ Easy (3 problems): 5.1, 5.2, 5.3
- ⭐⭐ Moderate (4 problems): 5.4, 5.5, 5.6, 5.7
- ⭐⭐⭐ Hard (3 problems): 5.8, 5.9, 5.10

**Topics Covered:**
1. Hypothesis testing and p-values
2. T-tests (one-sample and independent)
3. ANOVA with post-hoc tests
4. Correlation and causation
5. Linear regression
6. Chi-square tests
7. Multiple testing corrections
8. Effect sizes and confidence intervals
9. Non-parametric tests
10. Comprehensive case study

---

## ⭐ Problem 5.1: Understanding P-values (Easy)

**Learning Objective:** Correctly interpret p-values and avoid common misconceptions

### Problem Statement

Dr. Meera at AIIMS Delhi tests a new blood pressure medication on 50 patients. After treatment, she finds that the average systolic blood pressure decreased from 145 mmHg to 138 mmHg. She performs a statistical test and obtains p = 0.03.

Her colleague Dr. Sharma makes several interpretations. Which statements are **correct** and which are **incorrect**?

**Statement A:** "There is a 3% probability that the medication has no effect."

**Statement B:** "If the medication truly had no effect, we would observe a decrease this large or larger only 3% of the time by chance."

**Statement C:** "There is a 97% probability that the medication works."

**Statement D:** "We have strong evidence against the hypothesis that the medication has no effect."

**Statement E:** "The medication reduces blood pressure by 7 mmHg in all patients."

### Questions

**(a)** For each statement (A-E), indicate whether it is **correct** or **incorrect** and explain why.

**(b)** Write your own correct interpretation of p = 0.03 in plain language.

**(c)** If Dr. Meera had tested 500 patients instead of 50 and found the same 7 mmHg decrease, would the p-value likely be:
   - Smaller (closer to 0)
   - Larger (closer to 1)
   - About the same
   
   Explain your reasoning.

**(d)** What additional information would you need to determine whether this 7 mmHg reduction is **clinically important**?

---

## ⭐ Problem 5.2: Choosing the Right Test (Easy)

**Learning Objective:** Select appropriate statistical tests based on data type and research question

### Problem Statement

You are consulting for various research projects at the Wildlife Institute of India. For each scenario below, recommend the most appropriate statistical test.

**Scenario A:** Comparing tiger weights between Bandhavgarh National Park (n=15 tigers) and Ranthambore National Park (n=12 tigers). Weight data are normally distributed.

**Scenario B:** Testing whether the observed sex ratio of 60 males : 40 females in a deer population differs from the expected 50:50 ratio.

**Scenario C:** Examining the relationship between forest canopy cover (%) and bird species richness (number of species) across 30 forest plots.

**Scenario D:** Comparing stress hormone levels in elephants measured before and after a translocation event (same 20 elephants measured twice).

**Scenario E:** Testing whether four different fertilizer treatments produce different crop yields. You have 25 plots per treatment.

**Scenario F:** Comparing survival times of 8 control mice versus 8 treatment mice, where the data are heavily skewed and contain outliers.

### Questions

For each scenario (A-F):

**(a)** Name the most appropriate statistical test.

**(b)** Briefly explain why this test is appropriate (1-2 sentences).

**(c)** State the null hypothesis (H₀) for each scenario.

---

## ⭐ Problem 5.3: Type I and Type II Errors (Easy)

**Learning Objective:** Understand the consequences of statistical errors in biological contexts

### Problem Statement

The Forest Department is testing whether a new GPS collar affects leopard movement patterns. They track 30 leopards: 15 with the new collar and 15 with the old collar design.

**Possible outcomes:**

**Reality A:** The new collar does NOT affect leopard movement (no real effect)  
**Reality B:** The new collar DOES affect leopard movement (real effect exists)

**Decision 1:** Statistical test concludes "No significant effect" (fail to reject H₀)  
**Decision 2:** Statistical test concludes "Significant effect" (reject H₀)

### Questions

**(a)** Create a 2×2 table showing all four possible combinations of Reality (A or B) and Decision (1 or 2).

**(b)** Label each cell as either:
   - Correct decision
   - Type I error (false positive)
   - Type II error (false negative)

**(c)** For each type of error, describe the **practical consequence** for leopard conservation:
   - What would happen if we make a Type I error?
   - What would happen if we make a Type II error?

**(d)** If you had to choose, which error would be more serious in this context? Explain your reasoning.

**(e)** The researchers set α = 0.05 (5% Type I error rate). They calculate that their study has 70% power (30% Type II error rate). 

If they repeat this study 100 times (hypothetically), and the new collar truly has NO effect, how many times would they expect to:
   - Correctly conclude "no effect"?
   - Incorrectly conclude "significant effect"?

---

## ⭐⭐ Problem 5.4: Independent Samples T-Test (Moderate)

**Learning Objective:** Perform and interpret a t-test with biological data

### Problem Statement

A botanist at the Indian Institute of Science, Bangalore, is studying the effect of elevated CO₂ on plant growth. She grows rice plants in two controlled environments:

**Control (Normal CO₂):** 400 ppm CO₂  
**Treatment (Elevated CO₂):** 550 ppm CO₂

After 60 days, she measures plant height (cm) for 20 plants per group:

**Control Group (n = 20):**
```
Heights: 45, 48, 46, 50, 47, 49, 44, 51, 48, 46, 
         47, 49, 48, 45, 50, 46, 48, 47, 49, 48
```

**Treatment Group (n = 20):**
```
Heights: 52, 54, 53, 56, 51, 55, 50, 57, 54, 52, 
         53, 55, 54, 51, 56, 52, 54, 53, 55, 54
```

### Provided Information

**Control Group Statistics:**
- Mean (x̄₁) = 47.6 cm
- Standard deviation (s₁) = 1.79 cm
- n₁ = 20

**Treatment Group Statistics:**
- Mean (x̄₂) = 53.6 cm
- Standard deviation (s₂) = 1.79 cm
- n₂ = 20

**Critical t-value:** For df = 38, α = 0.05 (two-tailed): t_critical = 2.024

### Questions

**(a)** State the null hypothesis (H₀) and alternative hypothesis (H₁) for this study.

**(b)** Calculate the pooled standard deviation using the formula:
```
Pooled SD = √[((n₁-1)s₁² + (n₂-1)s₂²) / (n₁+n₂-2)]
```

**(c)** Calculate the t-statistic using:
```
t = (x̄₁ - x̄₂) / (pooled SD × √(1/n₁ + 1/n₂))
```

**(d)** Compare your calculated t-statistic to the critical value. What is your decision? (Reject or fail to reject H₀?)

**(e)** Write a conclusion in biological terms. Does elevated CO₂ significantly affect rice plant height?

**(f)** Calculate Cohen's d (effect size):
```
d = (x̄₂ - x̄₁) / pooled SD
```

Is this a small (d ≈ 0.2), medium (d ≈ 0.5), or large (d ≈ 0.8) effect?

**(g)** The researcher wants to estimate the 95% confidence interval for the mean difference. The formula is:
```
(x̄₂ - x̄₁) ± (t_critical × SE)

where SE = pooled SD × √(1/n₁ + 1/n₂)
```

Calculate and interpret the 95% CI.

---

## ⭐⭐ Problem 5.5: ANOVA with Post-Hoc Analysis (Moderate)

**Learning Objective:** Conduct ANOVA and identify which groups differ

### Problem Statement

A wildlife veterinarian is testing four different anesthetic drugs for safe tiger capture. She measures recovery time (minutes until the tiger can walk steadily) for 6 tigers per drug:

**Drug A (Ketamine):** 45, 48, 46, 50, 47, 44  
**Drug B (Medetomidine):** 32, 35, 34, 33, 36, 32  
**Drug C (Tiletamine):** 38, 41, 39, 40, 42, 38  
**Drug D (Combination):** 28, 30, 29, 31, 28, 30  

### Provided Summary Statistics

| Drug | n | Mean | Sum | Sum of Squares |
|------|---|------|-----|----------------|
| A    | 6 | 46.67 | 280 | 13,078 |
| B    | 6 | 33.67 | 202 | 6,810 |
| C    | 6 | 39.67 | 238 | 9,450 |
| D    | 6 | 29.33 | 176 | 5,170 |
| **Total** | **24** | **37.33** | **896** | **34,508** |

**Critical F-value:** For df₁ = 3, df₂ = 20, α = 0.05: F_critical = 3.10

**Tukey HSD critical value:** q₀.₀₅,₄,₂₀ = 3.96

### Questions

**(a)** State the null and alternative hypotheses for this ANOVA.

**(b)** Calculate the Between Groups Sum of Squares (BSS):
```
BSS = Σ[nⱼ(x̄ⱼ - x̄_overall)²]
```

**(c)** Calculate the Total Sum of Squares (TSS):
```
TSS = Σ(all individual observations - overall mean)²
    = (Sum of all x²) - (Grand total)²/N

where Sum of all x² = 34,508
```

**(d)** Calculate the Within Groups Sum of Squares (WSS):
```
WSS = TSS - BSS
```

**(e)** Complete the ANOVA table:

| Source | SS | df | MS | F |
|--------|----|----|----|----|
| Between Groups | ___ | ___ | ___ | ___ |
| Within Groups | ___ | ___ | ___ | |
| Total | ___ | ___ | | |

**(f)** Compare your F-statistic to F_critical. What is your decision?

**(g)** Conduct Tukey HSD post-hoc test. Calculate:
```
HSD = q × √(MSW/n)
```

Then compare all pairwise differences to HSD:
- A vs B: |46.67 - 33.67| = ?
- A vs C: |46.67 - 39.67| = ?
- A vs D: |46.67 - 29.33| = ?
- B vs C: |33.67 - 39.67| = ?
- B vs D: |33.67 - 29.33| = ?
- C vs D: |39.67 - 29.33| = ?

Which pairs are significantly different?

**(h)** Based on the results, which drug would you recommend for tiger capture and why?

---

## ⭐⭐ Problem 5.6: Correlation and Causation (Moderate)

**Learning Objective:** Calculate correlation and critically evaluate causal claims

### Problem Statement

An ecologist studies 12 forest plots in the Western Ghats and records:
- X: Canopy cover (percentage)
- Y: Ground temperature (°C)

### Data

| Plot | Canopy Cover (%) | Ground Temp (°C) |
|------|------------------|------------------|
| 1 | 85 | 22 |
| 2 | 70 | 25 |
| 3 | 90 | 20 |
| 4 | 60 | 28 |
| 5 | 75 | 24 |
| 6 | 80 | 23 |
| 7 | 65 | 27 |
| 8 | 95 | 19 |
| 9 | 55 | 30 |
| 10 | 88 | 21 |
| 11 | 72 | 26 |
| 12 | 78 | 24 |

### Provided Calculations

```
n = 12
Σx = 913
Σy = 289
Σx² = 70,407
Σy² = 7,117
Σxy = 21,628

Mean canopy cover (x̄) = 76.08%
Mean ground temp (ȳ) = 24.08°C
```

### Questions

**(a)** Calculate the Pearson correlation coefficient (r) using:
```
r = [nΣxy - (Σx)(Σy)] / √{[nΣx² - (Σx)²][nΣy² - (Σy)²]}
```

**(b)** Interpret the correlation:
   - What is the direction of the relationship?
   - What is the strength (weak/moderate/strong)?

**(c)** The ecologist concludes: "Canopy cover causes ground temperature to decrease."

List **three alternative explanations** for this correlation that do NOT involve canopy cover directly causing temperature changes.

**(d)** Calculate the regression equation: Temperature = a + b(Canopy)
```
b = [nΣxy - (Σx)(Σy)] / [nΣx² - (Σx)²]
a = ȳ - b(x̄)
```

**(e)** Using your regression equation, predict ground temperature for:
   - A plot with 50% canopy cover
   - A plot with 100% canopy cover

**(f)** Calculate R² and interpret what it means.

**(g)** For which prediction (50% or 100% canopy) are you more confident? Explain why, referring to the concept of interpolation versus extrapolation.

---

## ⭐⭐ Problem 5.7: Chi-Square Test for Mendelian Ratios (Moderate)

**Learning Objective:** Apply chi-square test to genetic data and interpret deviations

### Problem Statement

A geneticist at the National Institute of Plant Genome Research crosses two heterozygous pea plants (Rr × Rr) where R (round seeds) is dominant over r (wrinkled seeds).

**Mendelian prediction:** 3 round : 1 wrinkled (75% : 25%)

**Observed results from 200 seeds:**
- Round seeds: 142
- Wrinkled seeds: 58

A second cross using different parent plants yields:
- Round seeds: 165
- Wrinkled seeds: 35

**Critical value:** For df = 1, α = 0.05: χ²_critical = 3.841

### Questions

**(a)** For the **first cross** (142 round, 58 wrinkled):

Calculate the expected frequencies for 200 seeds following a 3:1 ratio.

**(b)** Calculate the chi-square statistic:
```
χ² = Σ[(Observed - Expected)² / Expected]
```

**(c)** Compare to the critical value. Do you reject or fail to reject H₀? What does this mean biologically?

**(d)** For the **second cross** (165 round, 35 wrinkled):

Calculate the chi-square statistic following the same procedure.

**(e)** Compare to the critical value. What is your decision for this cross?

**(f)** The second cross significantly deviates from the expected 3:1 ratio. Provide **three biological explanations** for why this might occur:
   - Explanation 1: (Hint: Think about gamete viability)
   - Explanation 2: (Hint: Think about seed development)
   - Explanation 3: (Hint: Think about measurement/sampling)

**(g)** If you pooled both crosses together (total of 400 seeds: 307 round, 93 wrinkled), would you expect the combined data to:
   - Better fit the 3:1 ratio
   - Worse fit the 3:1 ratio
   - About the same fit
   
Calculate the chi-square for the pooled data to test your prediction.

---

## ⭐⭐⭐ Problem 5.8: Multiple Testing Correction (Hard)

**Learning Objective:** Apply and compare different multiple testing correction methods

### Problem Statement

A genome-wide association study (GWAS) tests 20 genes for association with diabetes risk in an Indian population. The researchers test each gene separately using α = 0.05.

### Results: P-values for 20 genes

| Gene | P-value | Gene | P-value |
|------|---------|------|---------|
| Gene 1 | 0.001 | Gene 11 | 0.234 |
| Gene 2 | 0.003 | Gene 12 | 0.456 |
| Gene 3 | 0.008 | Gene 13 | 0.567 |
| Gene 4 | 0.012 | Gene 14 | 0.678 |
| Gene 5 | 0.025 | Gene 15 | 0.123 |
| Gene 6 | 0.048 | Gene 16 | 0.345 |
| Gene 7 | 0.052 | Gene 17 | 0.789 |
| Gene 8 | 0.067 | Gene 18 | 0.234 |
| Gene 9 | 0.089 | Gene 19 | 0.456 |
| Gene 10 | 0.123 | Gene 20 | 0.890 |

### Questions

**(a)** **Without any correction** (naive approach), which genes would be declared "significant" at α = 0.05? List them.

**(b)** **Calculate the family-wise error rate** if we use no correction:
```
P(at least one false positive) = 1 - (1 - α)^m
where m = number of tests
```

What is the probability of getting at least one false positive among the 20 genes by chance alone?

**(c)** **Apply Bonferroni correction:**

Calculate the adjusted significance threshold:
```
α_Bonferroni = α / m = 0.05 / 20
```

Which genes are significant after Bonferroni correction?

**(d)** **Apply False Discovery Rate (FDR) using Benjamini-Hochberg procedure:**

Steps:
1. Rank p-values from smallest to largest (already done in table)
2. For each p-value at rank i, calculate: (i/m) × α
3. Find the largest i where p_i ≤ (i/m) × α
4. Declare all genes with p ≤ p_i as significant

Complete this table:

| Rank | Gene | P-value | (i/20) × 0.05 | Significant? |
|------|------|---------|---------------|--------------|
| 1 | Gene 1 | 0.001 | 0.0025 | ? |
| 2 | Gene 2 | 0.003 | 0.0050 | ? |
| 3 | Gene 3 | 0.008 | 0.0075 | ? |
| 4 | Gene 4 | 0.012 | 0.0100 | ? |
| 5 | Gene 5 | 0.025 | 0.0125 | ? |
| 6 | Gene 6 | 0.048 | 0.0150 | ? |

Which genes are significant after FDR correction?

**(e)** **Compare the three approaches:**

Create a summary table:

| Method | # Significant | Gene IDs |
|--------|---------------|----------|
| No correction | ? | ? |
| Bonferroni | ? | ? |
| FDR (B-H) | ? | ? |

**(f)** **Discuss the trade-offs:**
   - Which method is most conservative (fewest false positives)?
   - Which method is most liberal (most discoveries)?
   - Which method would you recommend for this GWAS study and why?

**(g)** **Statistical power consideration:**

If the Bonferroni method fails to detect Gene 5 (p = 0.025) but this gene truly affects diabetes risk, what type of error occurred?

Explain why Bonferroni correction might be problematic for GWAS studies testing thousands of genes.

---

## ⭐⭐⭐ Problem 5.9: Non-Parametric Alternative (Hard)

**Learning Objective:** Recognize when parametric assumptions fail and apply non-parametric tests

### Problem Statement

A conservation biologist measures mercury contamination (ppm) in fish from two rivers in Kerala:

**Periyar River (n=10):**
```
Mercury levels: 0.12, 0.15, 0.18, 0.14, 0.21, 0.16, 0.13, 0.19, 2.34, 0.17
```

**Pamba River (n=10):**
```
Mercury levels: 0.08, 0.10, 0.11, 0.09, 0.13, 0.10, 0.12, 0.11, 0.09, 0.10
```

### Initial Analysis

The biologist calculates:

**Periyar River:**
- Mean = 0.379 ppm
- Median = 0.165 ppm
- SD = 0.660 ppm

**Pamba River:**
- Mean = 0.103 ppm
- Median = 0.105 ppm
- SD = 0.014 ppm

### Questions

**(a)** **Assess normality:**

Looking at the Periyar River data, identify the potential problem. Which value is unusual? Calculate how many standard deviations it is from the mean.

**(b)** **Compare mean vs median** for Periyar River:
   - Why is the mean (0.379) so much higher than the median (0.165)?
   - Which measure (mean or median) better represents the "typical" mercury level in this river?

**(c)** **Evaluate parametric assumptions:**

For an independent samples t-test to be valid, we need:
   - Normal distributions
   - Equal variances
   
Which assumption(s) are violated in this dataset? Provide evidence.

**(d)** **Conduct Mann-Whitney U test** (non-parametric alternative):

**Step 1:** Rank all 20 values from lowest to highest (assign ranks 1-20):

```
Value | 0.08 | 0.09 | 0.09 | 0.10 | 0.10 | 0.10 | 0.11 | 0.11 | 0.12 | 0.12
River | Pam  | Pam  | Pam  | Pam  | Pam  | Pam  | Pam  | Pam  | Pam  | Per
Rank  | 1    | 2.5  | 2.5  | 5    | 5    | 5    | 8    | 8    | 10   | 10

(Continue for remaining values: 0.13, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.21, 2.34)
```

**Step 2:** Sum the ranks for each group:
   - R_Periyar = sum of ranks for Periyar River
   - R_Pamba = sum of ranks for Pamba River

**Step 3:** Calculate U statistics:
```
U₁ = n₁n₂ + n₁(n₁+1)/2 - R_Periyar
U₂ = n₁n₂ + n₂(n₂+1)/2 - R_Pamba
```

Use the smaller U value for the test.

**(e)** **Critical value:** For n₁=10, n₂=10, α=0.05 (two-tailed): U_critical = 23

Compare your U statistic to the critical value. What is your decision?

**(f)** **Compare approaches:**

If you had ignored the outlier and conducted a regular t-test anyway, how might your conclusion differ? Discuss why the non-parametric test is more appropriate here.

**(g)** **Practical implications:**

Based on your analysis, write a recommendation for the Kerala Pollution Control Board about mercury contamination in these two rivers. Should they focus monitoring/cleanup efforts on one river over the other?

---

## ⭐⭐⭐ Problem 5.10: Comprehensive Case Study (Hard)

**Learning Objective:** Integrate multiple statistical concepts to analyze a complex biological dataset

### Problem Statement

The Indian Council of Medical Research (ICMR) investigates whether a traditional Ayurvedic supplement reduces blood glucose in pre-diabetic patients. They design a randomized controlled trial with three groups:

**Group 1 - Placebo** (n=30): Sugar pills  
**Group 2 - Low Dose** (n=30): 500mg supplement daily  
**Group 3 - High Dose** (n=30): 1000mg supplement daily  

**Baseline:** All patients have fasting glucose 100-125 mg/dL (pre-diabetic range)  
**Treatment Duration:** 12 weeks  
**Outcome Measured:** Change in fasting blood glucose (negative = improvement)

### Results After 12 Weeks

**Change in Blood Glucose (mg/dL):**

**Placebo Group:**
```
Mean change = -2.1 mg/dL (slight decrease)
SD = 5.8
Individual changes: -8, -4, -3, -2, -1, 0, 0, 0, +1, +2, +3, +4, -5, -3, -1, 
                     0, +1, +2, -2, -4, +1, +3, -1, 0, +2, -3, +1, 0, -1, +2
```

**Low Dose Group:**
```
Mean change = -8.4 mg/dL
SD = 6.2
Individual changes: -15, -12, -10, -8, -7, -9, -6, -11, -8, -5, -10, -7, -9, 
                     -6, -8, -4, -12, -9, -7, -8, -6, -10, -5, -9, -11, -7, 
                     -8, -6, -9, -10
```

**High Dose Group:**
```
Mean change = -12.6 mg/dL
SD = 7.1
Individual changes: -20, -18, -15, -12, -10, -14, -11, -16, -13, -9, -15, -11, 
                     -13, -8, -12, -10, -17, -14, -11, -13, -9, -15, -7, -12, 
                     -16, -10, -13, -11, -14, -15
```

### Additional Information

**Adverse Events Reported:**
- Placebo: 2 patients (mild stomach upset)
- Low Dose: 3 patients (mild stomach upset)
- High Dose: 8 patients (6 mild upset, 2 moderate nausea)

**Patient Adherence:**
- Placebo: 98% took ≥80% of pills
- Low Dose: 96% took ≥80% of pills
- High Dose: 87% took ≥80% of pills (some stopped due to nausea)

**Cost per Patient (12 weeks):**
- Placebo: ₹200
- Low Dose: ₹1,800
- High Dose: ₹3,600

### Questions

**Part A: Statistical Analysis (ANOVA)**

**(a.1)** State the null and alternative hypotheses.

**(a.2)** Calculate the grand mean (overall average change across all 90 patients).

**(a.3)** Estimate the Between Groups Sum of Squares (BSS) using:
```
BSS = n × [(mean₁ - grand mean)² + (mean₂ - grand mean)² + (mean₃ - grand mean)²]
where n = 30 per group
```

**(a.4)** Estimate the Within Groups Sum of Squares (WSS) using:
```
WSS = (n₁-1)×SD₁² + (n₂-1)×SD₂² + (n₃-1)×SD₃²
```

**(a.5)** Complete the ANOVA and calculate F-statistic.

**(a.6)** Critical F-value for df₁=2, df₂=87, α=0.05 is approximately 3.10. What is your decision?

**Part B: Effect Sizes**

**(b.1)** Calculate Cohen's d for:
   - Low Dose vs Placebo
   - High Dose vs Placebo
   - High Dose vs Low Dose

Use pooled SD for each comparison. Interpret the effect sizes.

**(b.2)** Calculate the 95% confidence interval for the difference between High Dose and Placebo:
```
(Mean_high - Mean_placebo) ± (t_critical × SE)

where t_critical ≈ 2.00 for df ≈ 58
and SE = pooled SD × √(1/30 + 1/30)
```

Interpret this CI.

**Part C: Clinical Significance**

**(c.1)** A reduction of ≥10 mg/dL is considered clinically meaningful for pre-diabetes management. Based on this criterion:
   - Is the Low Dose effect clinically significant?
   - Is the High Dose effect clinically significant?

**(c.2)** Even though High Dose shows the largest statistical effect, identify three concerns about recommending it as standard treatment.

**Part D: Cost-Effectiveness Analysis**

**(d.1)** Calculate "cost per mg/dL reduction" for each treatment:
```
Cost efficiency = Cost / |Mean change|
```

**(d.2)** Which dose offers the best cost-effectiveness?

**Part E: Comprehensive Recommendation**

**(e)** Write a one-paragraph recommendation for ICMR addressing:
   - Which treatment (if any) should be approved for pre-diabetic patients
   - The evidence supporting your recommendation
   - Any limitations or concerns
   - What additional studies might be needed

Consider: statistical significance, clinical significance, safety, adherence, cost-effectiveness, and patient benefit.

---

## Summary of Problems

| Problem | Difficulty | Main Topic | Skills Tested |
|---------|-----------|------------|---------------|
| 5.1 | ⭐ Easy | P-value interpretation | Conceptual understanding |
| 5.2 | ⭐ Easy | Test selection | Decision framework |
| 5.3 | ⭐ Easy | Type I/II errors | Error consequences |
| 5.4 | ⭐⭐ Moderate | Independent t-test | Calculation, interpretation |
| 5.5 | ⭐⭐ Moderate | ANOVA + post-hoc | Multiple comparisons |
| 5.6 | ⭐⭐ Moderate | Correlation/regression | Causation, prediction |
| 5.7 | ⭐⭐ Moderate | Chi-square | Genetic ratios |
| 5.8 | ⭐⭐⭐ Hard | Multiple testing | Bonferroni, FDR |
| 5.9 | ⭐⭐⭐ Hard | Non-parametric | Assumption checking |
| 5.10 | ⭐⭐⭐ Hard | Comprehensive | Integration of concepts |

---

**Total Coverage:**
- ✅ Hypothesis testing and p-values (5.1, 5.3)
- ✅ Test selection (5.2)
- ✅ T-tests (5.4)
- ✅ ANOVA (5.5, 5.10)
- ✅ Correlation and regression (5.6)
- ✅ Chi-square tests (5.7)
- ✅ Multiple testing corrections (5.8)
- ✅ Effect sizes and confidence intervals (5.4, 5.10)
- ✅ Non-parametric tests (5.9)
- ✅ Real-world decision making (5.10)

---

*Problems created for "The Pattern Hunters" by Dr. Alok Patel*  
*Chapter 5: Reading Nature's Signals – Statistics as a Pattern Hunter's Toolkit*
