# Solution 5.10: Comprehensive Case Study - Ayurvedic Supplement RCT

## Problem Summary
ICMR clinical trial testing Ayurvedic supplement for pre-diabetes. Three groups (Placebo, Low Dose 500mg, High Dose 1000mg), n=30 each, 12-week treatment, measuring blood glucose change.

---

## Part A: ANOVA Analysis

### Question (a.1): Hypotheses

**H₀:** μ_placebo = μ_low = μ_high (no difference in glucose reduction between groups)

**H₁:** At least one group mean differs (supplement affects glucose levels)

---

### Question (a.2): Grand Mean

**Calculation:**
```
Grand mean = (mean_placebo × n + mean_low × n + mean_high × n) / N
           = (-2.1×30 + -8.4×30 + -12.6×30) / 90
           = (-63 + -252 + -378) / 90
           = -693 / 90
           = -7.7 mg/dL
```

**Result: Grand mean = -7.7 mg/dL**

---

### Question (a.3): Between Groups Sum of Squares (BSS)

**Formula:**
```
BSS = n × Σ[(x̄ⱼ - x̄_grand)²]
```

**Calculation:**
```
BSS = 30 × [(-2.1 - (-7.7))² + (-8.4 - (-7.7))² + (-12.6 - (-7.7))²]
    = 30 × [(5.6)² + (-0.7)² + (-4.9)²]
    = 30 × [31.36 + 0.49 + 24.01]
    = 30 × 55.86
    = 1,675.8
```

**Result: BSS = 1,675.8**

---

### Question (a.4): Within Groups Sum of Squares (WSS)

**Formula:**
```
WSS = Σ[(nⱼ-1) × SDⱼ²]
```

**Calculation:**
```
WSS = (30-1)×5.8² + (30-1)×6.2² + (30-1)×7.1²
    = 29×33.64 + 29×38.44 + 29×50.41
    = 975.56 + 1,114.76 + 1,461.89
    = 3,552.21
```

**Result: WSS = 3,552.21**

---

### Question (a.5): Complete ANOVA and F-statistic

**ANOVA Table:**

| Source | SS | df | MS | F |
|--------|----|----|----|----|
| Between Groups | 1,675.8 | 2 | 837.9 | 20.52 |
| Within Groups | 3,552.2 | 87 | 40.8 | |
| Total | 5,228.0 | 89 | | |

**Calculations:**
```
df_between = k - 1 = 3 - 1 = 2
df_within = N - k = 90 - 3 = 87
df_total = N - 1 = 89

MSB = BSS/df_between = 1,675.8/2 = 837.9
MSW = WSS/df_within = 3,552.2/87 = 40.8

F = MSB/MSW = 837.9/40.8 = 20.52
```

---

### Question (a.6): Statistical Decision

**Comparison:**
- **Calculated F = 20.52**
- **Critical F(2,87,0.05) ≈ 3.10**

**Decision:** F = 20.52 >> 3.10

**Reject H₀** (p < 0.001)

**Conclusion:** At least one supplement dose produces significantly different glucose reduction compared to others.

---

## Part B: Effect Sizes

### Question (b.1): Cohen's d for All Comparisons

**Pooled SD calculation needed for each pair:**

**Low Dose vs Placebo:**
```
Pooled SD = √[((29×6.2²) + (29×5.8²))/58]
          = √[(1,114.76 + 975.56)/58]
          = √[2,090.32/58]
          = √36.04 = 6.00

d = (-8.4 - (-2.1)) / 6.00
  = -6.3 / 6.00
  = -1.05
```
**Cohen's d = 1.05 (LARGE effect)**

**High Dose vs Placebo:**
```
Pooled SD = √[((29×7.1²) + (29×5.8²))/58]
          = √[(1,461.89 + 975.56)/58]
          = √[2,437.45/58]
          = √42.02 = 6.48

d = (-12.6 - (-2.1)) / 6.48
  = -10.5 / 6.48
  = -1.62
```
**Cohen's d = 1.62 (VERY LARGE effect)**

**High Dose vs Low Dose:**
```
Pooled SD = √[((29×7.1²) + (29×6.2²))/58]
          = √[(1,461.89 + 1,114.76)/58]
          = √[2,576.65/58]
          = √44.42 = 6.66

d = (-12.6 - (-8.4)) / 6.66
  = -4.2 / 6.66
  = -0.63
```
**Cohen's d = 0.63 (MEDIUM effect)**

**Summary:**

| Comparison | Mean Diff | Cohen's d | Effect Size |
|------------|-----------|-----------|-------------|
| Low vs Placebo | -6.3 mg/dL | 1.05 | Large |
| High vs Placebo | -10.5 mg/dL | 1.62 | Very Large |
| High vs Low | -4.2 mg/dL | 0.63 | Medium |

---

### Question (b.2): 95% Confidence Interval (High vs Placebo)

**Formula:**
```
95% CI = (Mean_high - Mean_placebo) ± (t_critical × SE)

SE = Pooled SD × √(1/n₁ + 1/n₂)
```

**Calculation:**
```
Pooled SD = 6.48 (from b.1)
SE = 6.48 × √(1/30 + 1/30)
   = 6.48 × √0.0667
   = 6.48 × 0.258
   = 1.67

Mean difference = -12.6 - (-2.1) = -10.5 mg/dL
t_critical (df≈58, α=0.05) ≈ 2.00

Margin of error = 2.00 × 1.67 = 3.34

95% CI = -10.5 ± 3.34
       = [-13.84, -7.16] mg/dL
```

**Result: 95% CI = [-13.84, -7.16] mg/dL**

**Interpretation:**
We are 95% confident the true mean difference between High Dose and Placebo is between 7.16 and 13.84 mg/dL reduction. The interval does NOT include zero, confirming significant effect. Even the lower bound (7.16 mg/dL) is clinically meaningful.

---

## Part C: Clinical Significance

### Question (c.1): Clinical Meaningfulness

**Threshold:** ≥10 mg/dL reduction is clinically meaningful

**Low Dose (500mg):**
- Mean reduction: 8.4 mg/dL
- **Below 10 mg/dL threshold**
- **NOT clinically significant** (but close - 84% of threshold)

**High Dose (1000mg):**
- Mean reduction: 12.6 mg/dL
- **Above 10 mg/dL threshold**
- **IS clinically significant** ✓

---

### Question (c.2): Concerns About High Dose

**Concern 1: Adverse Events**
- High Dose: 8/30 patients (27%) had side effects
  - 6 mild stomach upset (20%)
  - 2 moderate nausea (7%)
- Low Dose: Only 3/30 (10%) had mild side effects
- **2.7× higher adverse event rate with High Dose**

**Concern 2: Patient Adherence**
- High Dose: Only 87% took ≥80% of pills
- Low Dose: 96% took ≥80% of pills
- **Real-world effectiveness compromised if patients don't take it**
- Some patients stopped due to nausea → lose benefit

**Concern 3: Cost-Effectiveness**
- High Dose: ₹3,600 per 12 weeks (2× cost of Low Dose)
- Benefit: Only 4.2 mg/dL better than Low Dose (50% more reduction)
- **Diminishing returns:** 2× cost for 1.5× benefit

---

## Part D: Cost-Effectiveness Analysis

### Question (d.1): Cost Per mg/dL Reduction

**Formula:**
```
Cost efficiency = Cost / |Mean change|
```

**Calculations:**

**Placebo:**
```
₹200 / 2.1 mg/dL = ₹95.24 per mg/dL reduced
(Not really a treatment, just comparison)
```

**Low Dose:**
```
₹1,800 / 8.4 mg/dL = ₹214.29 per mg/dL reduced
```

**High Dose:**
```
₹3,600 / 12.6 mg/dL = ₹285.71 per mg/dL reduced
```

---

### Question (d.2): Best Cost-Effectiveness

**Winner: Low Dose (500mg)**

**Cost efficiency: ₹214 per mg/dL** (vs ₹286 for High Dose)

**Analysis:**
- Low Dose is 25% more cost-effective than High Dose
- Provides 8.4 mg/dL reduction at half the cost
- High Dose provides only 50% more benefit for 100% more cost
- **Law of diminishing returns in action**

---

## Part E: Comprehensive Recommendation

### Recommendation for ICMR

**Approve LOW DOSE (500mg) for pre-diabetic patients**

**Evidence Supporting This Decision:**

**1. Statistical Significance** (✓)
- F = 20.52, p < 0.001: Clear group differences
- Cohen's d = 1.05: Large effect size vs placebo
- 95% CI: Effect is robust and reliable

**2. Clinical Significance** (Borderline ✓)
- 8.4 mg/dL reduction (84% of clinical threshold)
- Falls just short of 10 mg/dL criterion
- But: Paired with lifestyle changes, could push into normal range
- Pre-diabetes range: 100-125 mg/dL → 8.4 reduction meaningful

**3. Safety Profile** (✓✓)
- Only 10% adverse events (all mild)
- Comparable to placebo (7% adverse events)
- No serious side effects reported
- Well-tolerated by 90% of patients

**4. Patient Adherence** (✓✓)
- 96% adherence rate (excellent)
- Indicates real-world viability
- Patients willing to continue treatment

**5. Cost-Effectiveness** (✓✓)
- ₹1,800 per 12 weeks (₹150/month)
- Best cost-per-benefit ratio
- Affordable for middle-income patients
- Government healthcare programs could subsidize

**Why NOT High Dose:**

**1. Marginal Additional Benefit**
- Only 4.2 mg/dL better than Low Dose
- 50% more reduction, 100% more cost
- Not justified by cost-benefit analysis

**2. Safety Concerns**
- 27% adverse event rate (unacceptable)
- 7% moderate nausea (limits use)
- 2.7× higher side effects than Low Dose

**3. Adherence Issues**
- Only 87% adherence
- Real-world effectiveness reduced
- Patients stopping due to side effects

**4. Poor Cost-Effectiveness**
- ₹3,600 per 12 weeks (₹300/month)
- Less efficient per mg/dL reduced
- May not be covered by insurance

**Limitations Acknowledged:**

1. **12-week study:** Need long-term safety/efficacy data (6-12 months)
2. **Pre-diabetes only:** Not tested in diagnosed diabetes
3. **Supplement quality:** Manufacturing standards must be ensured
4. **Lifestyle factors:** Should be combined with diet/exercise
5. **Individual variation:** Some patients may need High Dose

**Additional Studies Needed:**

1. **Long-term RCT:** 6-12 month follow-up
   - Sustained glucose reduction?
   - Prevents progression to diabetes?
   - Long-term safety?

2. **Dose-response:** Test intermediate doses (750mg)
   - Optimize benefit-risk ratio
   - Find minimum effective dose

3. **Combination therapy:** Supplement + metformin
   - Synergistic effects?
   - Can reduce pharmaceutical dose?

4. **Mechanistic studies:** How does it work?
   - Active compounds identified
   - Mechanism of action
   - Drug interactions

5. **Population studies:** Real-world effectiveness
   - Adherence in practice
   - Cost-effectiveness in health system
   - Equity of access

**Final Verdict:**

**Approve Low Dose (500mg) with conditional monitoring**
- Require post-market surveillance
- Manufacturers must report adverse events
- Recommend combination with lifestyle modification
- Reserve High Dose for non-responders only

---

## Complete Summary Table

| Criterion | Placebo | Low Dose | High Dose |
|-----------|---------|----------|-----------|
| **Glucose reduction** | -2.1 mg/dL | -8.4 mg/dL ✓ | -12.6 mg/dL ✓✓ |
| **Clinical threshold** | No | Close (84%) | Yes (126%) ✓ |
| **Effect size vs placebo** | - | d=1.05 (Large) | d=1.62 (Very Large) |
| **Adverse events** | 7% | 10% ✓✓ | 27% ✗ |
| **Adherence** | 98% | 96% ✓✓ | 87% ✗ |
| **Cost (12 weeks)** | ₹200 | ₹1,800 ✓ | ₹3,600 ✗ |
| **Cost efficiency** | - | ₹214/mg/dL ✓✓ | ₹286/mg/dL ✗ |
| **Recommendation** | Control | **APPROVE** ⭐ | Conditional |

---

## Key Takeaways

### Statistical Significance ≠ Clinical Decision
- High Dose statistically best
- But Low Dose better overall choice
- Must consider: safety, adherence, cost

### Evidence-Based Medicine Requires Integration
- Statistical evidence (ANOVA, effect sizes)
- Clinical significance (threshold)
- Safety profile
- Cost-effectiveness
- Real-world applicability

### Multiple Testing Contexts
- ANOVA for overall difference
- Post-hoc for pairwise comparisons
- Effect sizes for magnitude
- Confidence intervals for precision
- All contribute to final decision

---

## Common Mistakes

**Mistake 1:** Recommending based solely on efficacy
- High Dose most effective but not best choice overall
- Must balance efficacy with safety, cost, adherence

**Mistake 2:** Ignoring clinical vs statistical significance
- Low Dose significant but just below clinical threshold
- Context matters: pre-diabetes vs diabetes treatment

**Mistake 3:** Not considering real-world factors
- High Dose fails on adherence and cost
- Laboratory efficacy ≠ real-world effectiveness

**Mistake 4:** Missing adverse event patterns
- 27% side effects unacceptable for preventive treatment
- Higher bar for safety in asymptomatic patients

---

*Solution for The Pattern Hunters - Chapter 5, Problem 5.10*
