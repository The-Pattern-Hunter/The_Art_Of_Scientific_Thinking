# Solution 5.6: Correlation and Causation

## Problem Summary
Ecologist studies 12 forest plots: canopy cover (%) vs ground temperature (°C).

---

## Question (a): Pearson Correlation Coefficient

**Formula:**
```
r = [nΣxy - (Σx)(Σy)] / √{[nΣx² - (Σx)²][nΣy² - (Σy)²]}
```

**Given:**
- n = 12
- Σx = 913, Σy = 289
- Σx² = 70,407, Σy² = 7,117
- Σxy = 21,628

**Calculation:**
```
Numerator = nΣxy - (Σx)(Σy)
          = 12(21,628) - (913)(289)
          = 259,536 - 263,857
          = -4,321

Denominator = √{[nΣx² - (Σx)²][nΣy² - (Σy)²]}
            = √{[12(70,407) - (913)²][12(7,117) - (289)²]}
            = √{[844,884 - 833,569][85,404 - 83,521]}
            = √{[11,315][1,883]}
            = √21,306,145
            = 4,616

r = -4,321 / 4,616 = -0.936
```

**Result: r = -0.936**

---

## Question (b): Interpretation

**Direction:** 
- Negative correlation (r < 0)
- As canopy cover increases, ground temperature decreases

**Strength:**
- |r| = 0.936
- Very strong correlation (|r| > 0.7)
- Close to perfect negative linear relationship

**Meaning:**
Forest plots with higher canopy cover have consistently lower ground temperatures. The relationship is nearly linear and very predictable.

---

## Question (c): Alternative Explanations (Not Direct Causation)

### Explanation 1: Elevation Confounding
**Mechanism:** 
- Higher elevations → cooler temperatures (lapse rate: -6.5°C per 1000m)
- Higher elevations → more moisture → denser tree growth
- **Confounding variable (elevation) drives both canopy and temperature**

Not canopy causing cooling, but elevation causing both.

### Explanation 2: Reverse Causation
**Mechanism:**
- Cooler areas → less evapotranspiration stress
- Better growing conditions → trees grow taller/denser
- **Temperature affects canopy cover, not vice versa**

Cool spots allow better tree growth, creating dense canopy.

### Explanation 3: Soil Moisture as Common Cause
**Mechanism:**
- Moist soils → high canopy cover (better tree growth)
- Moist soils → cooler temperatures (evaporative cooling)
- **Both driven by underlying water availability**

Wet sites are cool and forested; dry sites are hot and sparse.

---

## Question (d): Regression Equation

**Formula for slope:**
```
b = [nΣxy - (Σx)(Σy)] / [nΣx² - (Σx)²]
  = -4,321 / 11,315
  = -0.382
```

**Formula for intercept:**
```
a = ȳ - b(x̄)
  = 24.08 - (-0.382)(76.08)
  = 24.08 + 29.06
  = 53.14
```

**Regression Equation:**
```
Temperature = 53.14 - 0.382 × Canopy
```

**Interpretation:**
- **Intercept (53.14):** Predicted temperature with 0% canopy (open area)
- **Slope (-0.382):** Each 1% increase in canopy → 0.382°C decrease in temperature

---

## Question (e): Predictions

### Prediction at 50% Canopy:
```
Temperature = 53.14 - 0.382(50)
            = 53.14 - 19.10
            = 34.04°C
```

### Prediction at 100% Canopy:
```
Temperature = 53.14 - 0.382(100)
            = 53.14 - 38.20
            = 14.94°C
```

**Results:**
- **50% canopy:** 34.04°C
- **100% canopy:** 14.94°C

---

## Question (f): R² and Interpretation

**Calculation:**
```
R² = r²
   = (-0.936)²
   = 0.876
```

**Result: R² = 0.876 (87.6%)**

**Interpretation:**
"Canopy cover explains 87.6% of the variance in ground temperature across the 12 forest plots. The remaining 12.4% of variance is due to other factors (elevation, soil type, aspect, microclimate, measurement error)."

**Meaning:**
- Very high R² → strong predictive power
- Canopy cover is the dominant factor affecting ground temperature
- Model fits data very well

---

## Question (g): Prediction Confidence

### 50% Canopy Prediction: MORE CONFIDENT ✓
**Reason:** **Interpolation** (within data range)
- Data range: 55% to 95% canopy
- 50% is just outside but close to observed range
- Model well-validated in this region
- Relationship is linear in this range

### 100% Canopy Prediction: LESS CONFIDENT ✗
**Reason:** **Extrapolation** (beyond data range)
- Far beyond maximum observed (95%)
- Assumes linear relationship continues
- May encounter:
  - Floor effect (can't get cooler than certain point)
  - Diminishing returns (100% canopy no cooler than 95%)
  - Other factors become important
  - Model breaks down at extremes

**General Rule:**
**NEVER extrapolate far beyond data range.**
- Within range: Interpolation (reliable)
- Beyond range: Extrapolation (risky)

**Example:** Predicting temperature at 150% canopy is nonsensical (impossible value), illustrating dangers of extrapolation.

---

## Complete Summary

| Statistic | Value | Interpretation |
|-----------|-------|----------------|
| r | -0.936 | Very strong negative correlation |
| R² | 0.876 | 87.6% variance explained |
| Slope | -0.382 | Each 1% canopy → 0.382°C cooler |
| Intercept | 53.14 | Predicted temp with no canopy |

**Key Insight:** Strong association between canopy and temperature, but correlation ≠ causation. Multiple plausible mechanisms and confounders exist.

---

## Key Takeaways

### Statistical:
- r = -0.936 is very strong correlation
- R² = 0.876 is excellent fit
- Linear model appropriate for this range

### Causation Critical Thinking:
1. **Association ≠ Causation:** Strong correlation doesn't prove mechanism
2. **Confounding:** Third variables can drive both
3. **Reverse causation:** Effect might cause "cause"
4. **Multiple mechanisms:** Several paths may operate simultaneously

### Practical:
- **Interpolation safe:** Predictions within data range reliable
- **Extrapolation dangerous:** Predictions beyond range unreliable
- **Experimental design needed:** To establish causation, need manipulation (not just observation)

---

## Common Mistakes

**Mistake 1:** "High correlation proves causation"
- Wrong: Many explanations for association
- Need: Experimental manipulation or causal inference methods

**Mistake 2:** "Canopy blocks sun, so it must cause cooling"
- Hasty: Plausible but not proven by correlation alone
- Reality: Multiple mechanisms operating

**Mistake 3:** Extrapolating beyond data range
- Dangerous: 100% canopy prediction unreliable
- Model only validated in observed range (55-95%)

**Mistake 4:** Ignoring R² when reporting correlation
- Incomplete: r shows strength, R² shows variance explained
- Both needed for full picture

---

*Solution for The Pattern Hunters - Chapter 5, Problem 5.6*
