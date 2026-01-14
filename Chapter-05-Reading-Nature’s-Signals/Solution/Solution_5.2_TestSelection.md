# Solution 5.2: Choosing the Right Test

## Scenario A: Tiger Weights - Two Independent Groups

**Test:** Independent samples t-test

**Why:** 
- Comparing means of two separate groups (Bandhavgarh vs Ranthambore)
- Continuous data (weight in kg)
- Data normally distributed ✓
- Independent samples (different tigers)

**H₀:** μ_Bandhavgarh = μ_Ranthambore (mean weights are equal)

---

## Scenario B: Deer Sex Ratio - One Categorical Variable

**Test:** Chi-square goodness of fit test

**Why:**
- Categorical data (male vs female)
- Comparing observed frequencies to expected ratio
- Single variable (sex)
- Testing against theoretical expectation (50:50)

**H₀:** Population sex ratio = 50:50 (observed 60:40 is due to sampling variation)

---

## Scenario C: Canopy Cover vs Bird Richness - Two Continuous Variables

**Test:** Pearson correlation (or linear regression if predicting)

**Why:**
- Two continuous variables (% canopy cover, # species)
- Examining strength and direction of relationship
- Not comparing groups, finding association
- If goal is prediction: use regression instead

**H₀:** ρ = 0 (no linear correlation between canopy cover and species richness)

---

## Scenario D: Elephant Stress - Paired Measurements

**Test:** Paired samples t-test

**Why:**
- Same subjects measured twice (before and after translocation)
- Continuous data (hormone levels)
- Interest is in within-subject change
- Paired design reduces variability from individual differences

**H₀:** μ_difference = 0 (no change in stress hormones after translocation)

**Note:** Could also use one-sample t-test on the differences.

---

## Scenario E: Four Fertilizer Treatments - Multiple Groups

**Test:** One-way ANOVA (Analysis of Variance)

**Why:**
- Comparing means of >2 groups (4 treatments)
- Continuous outcome (crop yield in kg)
- Independent groups (different plots)
- ANOVA controls family-wise error rate

**H₀:** μ₁ = μ₂ = μ₃ = μ₄ (all treatment means equal)

**Follow-up:** If significant, use post-hoc test (Tukey HSD) to identify which pairs differ.

---

## Scenario F: Survival Times with Outliers - Two Groups, Non-Normal

**Test:** Mann-Whitney U test (non-parametric)

**Why:**
- Two independent groups (control vs treatment)
- Continuous data BUT heavily skewed with outliers
- Parametric assumptions violated (non-normal distribution)
- Mann-Whitney U is robust to outliers and non-normality
- Tests whether distributions differ (not just means)

**H₀:** Distributions of survival times are the same in both groups

**Alternative if normal:** Independent samples t-test  
**Why not used:** Data skewed and outliers present

---

## Test Selection Summary Table

| Scenario | Data Type | # Groups | Relationship | Test | Key Reason |
|----------|-----------|----------|--------------|------|------------|
| A | Continuous | 2 independent | Compare means | Independent t-test | Normal data, 2 groups |
| B | Categorical | 1 variable | Fit to ratio | Chi-square GOF | Testing expected frequency |
| C | Continuous | N/A | Association | Pearson correlation | Two continuous variables |
| D | Continuous | 2 paired | Compare means | Paired t-test | Same subjects, repeated |
| E | Continuous | 4 independent | Compare means | One-way ANOVA | >2 groups, normal data |
| F | Continuous | 2 independent | Compare distributions | Mann-Whitney U | Non-normal, outliers |

---

## Decision Framework Applied

### Step 1: What type of data?
- **Continuous:** A, C, D, E, F → t-tests, ANOVA, correlation
- **Categorical:** B → Chi-square

### Step 2: How many groups/variables?
- **1 variable, expected ratio:** B → Chi-square GOF
- **2 variables, association:** C → Correlation
- **2 groups:** A, D, F → t-tests (or Mann-Whitney)
- **>2 groups:** E → ANOVA

### Step 3: Are observations independent?
- **Independent:** A, B, C, E, F → Between-subjects tests
- **Paired/repeated:** D → Within-subjects test

### Step 4: Are parametric assumptions met?
- **Normal data:** A, C, D, E → Parametric tests
- **Non-normal/outliers:** F → Non-parametric test

---

## Common Mistakes

**Mistake 1:** Using multiple t-tests instead of ANOVA for Scenario E
- **Problem:** 6 pairwise tests inflate Type I error to 26%
- **Solution:** ANOVA maintains α = 0.05 overall

**Mistake 2:** Using independent t-test for Scenario D
- **Problem:** Ignores pairing, loses statistical power
- **Solution:** Paired t-test accounts for individual differences

**Mistake 3:** Using parametric test for Scenario F
- **Problem:** Outliers heavily influence mean, violate assumptions
- **Solution:** Mann-Whitney U robust to outliers

**Mistake 4:** Using chi-square for Scenario A
- **Problem:** Throws away continuous information by categorizing
- **Solution:** Keep continuous data, use t-test

**Mistake 5:** Claiming causation from Scenario C correlation
- **Problem:** Correlation doesn't prove canopy causes species richness
- **Solution:** Recognize correlation shows association only

---

## Key Principles

### Match Test to Question
- **Compare groups:** t-test or ANOVA
- **Find relationships:** Correlation or regression
- **Test frequencies:** Chi-square

### Check Assumptions
- **Normal data:** Parametric tests
- **Non-normal data:** Non-parametric alternatives
- **Small samples (<30):** Be extra cautious with normality

### Consider Study Design
- **Independent observations:** Between-subjects tests
- **Paired/repeated measures:** Within-subjects tests
- **Multiple comparisons:** Use corrections (ANOVA, Bonferroni)

### Balance Power and Robustness
- **Parametric tests:** More powerful IF assumptions met
- **Non-parametric tests:** More robust to violations
- **Choose based on data characteristics, not preference**

---

*Solution for The Pattern Hunters - Chapter 5, Problem 5.2*
