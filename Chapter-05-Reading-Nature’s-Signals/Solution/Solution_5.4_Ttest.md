# Solution 5.4: Independent Samples T-Test

## Question (a): Hypotheses

**H₀:** μ_control = μ_treatment (elevated CO₂ has no effect on rice height)

**H₁:** μ_control ≠ μ_treatment (elevated CO₂ affects rice height)

*Two-tailed test: testing for any difference, not predicting direction*

---

## Question (b): Pooled Standard Deviation

**Formula:**
```
Pooled SD = √[((n₁-1)s₁² + (n₂-1)s₂²) / (n₁+n₂-2)]
```

**Calculation:**
```
= √[((20-1)(1.79)² + (20-1)(1.79)²) / (20+20-2)]
= √[(19×3.204 + 19×3.204) / 38]
= √[(60.876 + 60.876) / 38]
= √[121.752 / 38]
= √3.204
= 1.79 cm
```

**Result: Pooled SD = 1.79 cm**

*Note: Same as individual SDs because variances are equal*

---

## Question (c): T-statistic

**Formula:**
```
t = (x̄₁ - x̄₂) / (pooled SD × √(1/n₁ + 1/n₂))
```

**Calculation:**
```
SE = pooled SD × √(1/n₁ + 1/n₂)
   = 1.79 × √(1/20 + 1/20)
   = 1.79 × √0.10
   = 1.79 × 0.316
   = 0.566

t = (47.6 - 53.6) / 0.566
  = -6.0 / 0.566
  = -10.60
```

**Result: t = -10.60**

*(Negative because control mean < treatment mean)*

---

## Question (d): Statistical Decision

**Comparison:**
- **Calculated t = -10.60** (absolute value = 10.60)
- **Critical t = 2.024** (df = 38, α = 0.05, two-tailed)

**Decision:** |t| = 10.60 > 2.024

**Reject H₀** - The difference is statistically significant (p < 0.001)

---

## Question (e): Biological Conclusion

**Conclusion:**

"Elevated CO₂ (550 ppm) significantly increases rice plant height compared to normal CO₂ (400 ppm). Plants grown under elevated CO₂ were on average 6.0 cm taller (mean = 53.6 cm) than control plants (mean = 47.6 cm), representing a 12.6% increase in height (t = -10.60, df = 38, p < 0.001).

This finding supports the CO₂ fertilization effect, where higher atmospheric CO₂ concentrations enhance photosynthesis and plant growth."

---

## Question (f): Effect Size (Cohen's d)

**Formula:**
```
d = (x̄₂ - x̄₁) / pooled SD
```

**Calculation:**
```
d = (53.6 - 47.6) / 1.79
  = 6.0 / 1.79
  = 3.35
```

**Result: d = 3.35**

**Interpretation:** 
- d = 0.2 → Small effect
- d = 0.5 → Medium effect
- d = 0.8 → Large effect
- **d = 3.35 → Very large effect**

**Meaning:** Treatment group average is 3.35 standard deviations above control group. This is an extremely large, practically significant effect. The distributions barely overlap.

---

## Question (g): 95% Confidence Interval

**Formula:**
```
95% CI = (x̄₂ - x̄₁) ± (t_critical × SE)
```

**Calculation:**
```
Point estimate = 53.6 - 47.6 = 6.0 cm
Margin of error = 2.024 × 0.566 = 1.146 cm

95% CI = 6.0 ± 1.146
       = [4.85, 7.15] cm
```

**Result: 95% CI = [4.85, 7.15] cm**

**Interpretation:**

"We are 95% confident that the true mean difference in rice height between elevated CO₂ and normal CO₂ conditions is between 4.85 cm and 7.15 cm.

**Key insights:**
- Interval does NOT include zero → confirms significant difference
- Narrow interval (width = 2.29 cm) → precise estimate
- Lower bound (4.85 cm) still substantial → effect is robust
- All plausible values show elevated CO₂ increases height"

---

## Complete Summary Table

| Statistic | Value | Interpretation |
|-----------|-------|----------------|
| Mean difference | 6.0 cm | Treatment 6 cm taller |
| t-statistic | -10.60 | Far exceeds critical value |
| p-value | < 0.001 | Extremely unlikely if no effect |
| Cohen's d | 3.35 | Very large effect |
| 95% CI | [4.85, 7.15] | Precise, does not include 0 |
| Conclusion | Significant | Strong evidence for CO₂ effect |

---

## Key Takeaways

### Statistical Significance
- **p < 0.001:** Extremely strong evidence against H₀
- Highly unlikely to observe this difference by chance

### Practical Significance  
- **6 cm increase:** 12.6% taller plants
- **d = 3.35:** Huge effect, distributions barely overlap
- **Narrow CI:** Effect is both large and precise

### Biological Meaning
- CO₂ fertilization effect confirmed
- Relevant for climate change predictions
- Potential agricultural application
- Need to test: Does increased height → increased yield?

### Study Quality
- **Good sample size:** n=20 per group (adequate power)
- **Equal variances:** Simplifies analysis
- **Clear difference:** Large effect easy to detect
- **Controlled conditions:** Minimizes confounding

---

## Common Mistakes

**Mistake 1:** Using wrong SE formula
- Must use pooled SD × √(1/n₁ + 1/n₂), not just pooled SD

**Mistake 2:** Interpreting p-value as effect size
- p < 0.001 means unlikely under H₀, not that effect is large
- Always report effect size separately

**Mistake 3:** Ignoring practical significance
- Could have p < 0.001 but d = 0.15 (tiny effect)
- Always check: Is difference biologically meaningful?

**Mistake 4:** One-tailed vs two-tailed confusion
- Two-tailed appropriate when testing "any difference"
- One-tailed only when predicting specific direction a priori

---

*Solution for The Pattern Hunters - Chapter 5, Problem 5.4*
