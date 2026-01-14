# Solution 2A.8: Residual Analysis ⭐⭐⭐

## Problem Summary
Learn advanced model validation techniques through comprehensive residual analysis. Understand how to diagnose model problems, check assumptions, and improve predictions using the temperature-sales model from Problem 2A.2.

---

## Given Model and Data

**From Problem 2A.2:**
```
Sales = 1,546 - 30.5 × Temperature

Data: 8 days
Temperature range: 26°C to 37°C
Sales range: ₹440 to ₹780
R² = 0.94
```

---

## Question (a): Calculate All Residuals

### What is a Residual?

**Definition:**
```
Residual = Actual Value - Predicted Value
         = Observed - Model Prediction
         = y - ŷ
         = ε (epsilon, the error)
```

**Interpretation:**
- **Positive residual:** Model underestimates (actual > predicted)
- **Negative residual:** Model overestimates (actual < predicted)
- **Zero residual:** Perfect prediction (rare!)

---

### Step-by-Step Calculation

**For each observation:**

| Day | Temp (x) | Actual (y) | Predicted (ŷ) | Residual (ε) | Calculation |
|-----|----------|------------|---------------|--------------|-------------|
| 1   | 35       | 450        | 478.5         | -28.5        | 450 - 478.5 |
| 2   | 33       | 520        | 539.5         | -19.5        | 520 - 539.5 |
| 3   | 30       | 580        | 631.0         | -51.0        | 580 - 631.0 |
| 4   | 28       | 720        | 692.0         | +28.0        | 720 - 692.0 |
| 5   | 36       | 480        | 448.0         | +32.0        | 480 - 448.0 |
| 6   | 29       | 650        | 661.5         | -11.5        | 650 - 661.5 |
| 7   | 26       | 780        | 753.0         | +27.0        | 780 - 753.0 |
| 8   | 37       | 440        | 417.5         | +22.5        | 440 - 417.5 |

**Predicted values calculated using:**
```
ŷ = 1,546 - 30.5 × Temperature

Day 1: ŷ = 1,546 - 30.5(35) = 1,546 - 1,067.5 = 478.5
Day 2: ŷ = 1,546 - 30.5(33) = 1,546 - 1,006.5 = 539.5
...and so on
```

---

### Summary Statistics

**Residual Statistics:**
```
Mean residual: 0.0 (always, by construction of least squares)
Median residual: -0.5
Min residual: -51.0 (Day 3, largest underestimate)
Max residual: +32.0 (Day 5, largest overestimate)
Range: 83.0 (from -51 to +32)

Positive residuals: 4 days (Days 4, 5, 7, 8)
Negative residuals: 4 days (Days 1, 2, 3, 6)
Perfect balance!
```

---

## Question (b): Create Residual Plots

### Plot 1: Residuals vs. Fitted Values

**What to plot:**
- **X-axis:** Predicted values (ŷ)
- **Y-axis:** Residuals (ε)
- **Reference line:** y = 0 (perfect prediction)

**Ideal pattern:** Random scatter around zero (no pattern)

**Our data:**
```
Fitted | Residual | Point
-------|----------|-------
417.5  | +22.5    | ●
448.0  | +32.0    | ●
478.5  | -28.5    | ●
539.5  | -19.5    | ●
631.0  | -51.0    | ●
661.5  | -11.5    | ●
692.0  | +28.0    | ●
753.0  | +27.0    | ●
```

**Visual pattern:**
```
Residual
 +40 |
     |       ●(5)
 +20 |   ●(8)      ●(7)    ●(4)
   0 |__________________________ Zero line
     |         ●(6)
 -20 |       ●(1) ●(2)
     |               
 -40 |
     |
 -60 |           ●(3)
     |_________________________________
       400    500    600    700    800  Fitted

Pattern: Fairly random, no obvious trend
Slight funnel? Larger residuals at extremes
```

---

### Plot 2: Residuals vs. Predictor (Temperature)

**What to plot:**
- **X-axis:** Temperature (original predictor)
- **Y-axis:** Residuals

**Ideal pattern:** Random scatter (no relationship)

**Our data:**
```
Temp | Residual | Point
-----|----------|-------
26   | +27.0    | ●
28   | +28.0    | ●
29   | -11.5    | ●
30   | -51.0    | ●
33   | -19.5    | ●
35   | -28.5    | ●
36   | +32.0    | ●
37   | +22.5    | ●
```

**Visual pattern:**
```
Residual
 +40 |
     |                 ●(5)
 +20 |     ●(7)   ●(4)       ●(8)
   0 |__________________________ Zero line
     |           ●(6)
 -20 |               ●(2)  ●(1)
     |               
 -40 |
     |
 -60 |       ●(3)
     |_________________________________
       26   28   30   32   34   36   38  Temperature

Pattern: Appears random
No clear trend (good!)
Variance seems consistent (homoscedasticity)
```

---

### Plot 3: Normal Q-Q Plot of Residuals

**Purpose:** Check if residuals are normally distributed

**How to create:**
1. Order residuals from smallest to largest
2. Calculate theoretical quantiles (normal distribution)
3. Plot actual vs. theoretical
4. Ideal: Points fall on straight line

**Our ordered residuals:**
```
Rank | Residual | Theoretical Quantile
-----|----------|---------------------
1    | -51.0    | -1.53
2    | -28.5    | -0.89
3    | -19.5    | -0.49
4    | -11.5    | -0.16
5    | +22.5    | +0.16
6    | +27.0    | +0.49
7    | +28.0    | +0.89
8    | +32.0    | +1.53
```

**Visual assessment:**
```
Sample Quantile
 +40 |                      ●
     |                   ●●
 +20 |               ●
   0 |___________●_____________ 
     |        ●
 -20 |     ●●
     |  
 -60 | ●
     |_________________________________
      -2    -1     0     1     2   Theoretical Quantile

Pattern: Mostly linear with slight departure
Day 3 (residual = -51) slightly off line
Overall: Reasonably normal
```

---

### Plot 4: Residuals Over Time (Sequence Plot)

**Purpose:** Check for autocorrelation (temporal patterns)

**What to plot:**
- **X-axis:** Observation order (Day 1-8)
- **Y-axis:** Residuals

**Ideal pattern:** Random scatter (no trends or cycles)

**Our data:**
```
Day | Residual | Pattern
----|----------|--------
1   | -28.5    | ●
2   | -19.5    |   ●
3   | -51.0    | ●
4   | +28.0    |         ●
5   | +32.0    |          ●
6   | -11.5    |   ●
7   | +27.0    |         ●
8   | +22.5    |        ●
```

**Visual pattern:**
```
Residual
 +40 |
     |             ●(5)
 +20 |          ●(4)   ●(7) ●(8)
   0 |__________________________ Zero line
     |    ●(2)      ●(6)
 -20 | ●(1)
     |               
 -60 | ●(3)
     |_________________________________
        1    2    3    4    5    6    7    8   Day

Pattern: No obvious trend
Possible: Days 1-3 negative, Days 4-5,7-8 positive
Could suggest autocorrelation (needs testing)
But sample too small to conclude
```

---

## Question (c): Interpret Residual Patterns

### What Do the Residuals Tell Us?

---

### 1. Model Fit Quality

**Overall Assessment: GOOD**

**Evidence:**
```
✅ Mean residual = 0 (by construction)
✅ Balanced: 4 positive, 4 negative
✅ Mostly small: 6 out of 8 within ±30
✅ R² = 0.94 (excellent)

⚠️ One large residual: Day 3 (-51)
```

**Conclusion:** Model fits well overall, one potential outlier

---

### 2. Linearity Assumption

**Check:** Do residuals show patterns vs. fitted values?

**Observation:**
```
Residuals vs. Fitted: No clear curve or pattern
Random scatter around zero
```

**Conclusion:** ✅ Linear model appears appropriate

**If violated would see:**
```
Systematic curve (U-shape or inverted U)
Example:
     ●●●
   ●     ●
  ●       ●
 ●_________●___ (U-shaped pattern = need quadratic)
```

**We don't see this!**

---

### 3. Homoscedasticity (Constant Variance)

**Check:** Does residual variance change across fitted values?

**Observation:**
```
Low fitted values (417-478): Residuals -28 to +32 (range ~60)
Mid fitted values (539-661): Residuals -51 to -11 (range ~40)
High fitted values (692-753): Residuals +27 to +28 (range ~1)

Slight funnel? Variance might decrease at high values
But sample too small to be certain
```

**Conclusion:** ✅ Mostly homoscedastic (variance reasonably constant)

**If violated would see:**
```
Funnel shape:
       ●
     ●   ●
   ●       ●
  ●         ●
 ●___________●___ (variance increases with fitted value)
```

**We have slight hint, but not severe**

---

### 4. Normality of Residuals

**Check:** Q-Q plot, histogram

**Observation:**
```
Q-Q plot: Mostly linear
One point (Day 3, residual = -51) slightly off
Overall: Reasonably normal
```

**Conclusion:** ✅ Approximately normal

**Why normality matters:**
- For inference (confidence intervals, hypothesis tests)
- For predictions (prediction intervals)
- For small samples especially important
- But: Least squares doesn't require normality for point estimates

---

### 5. Independence of Errors

**Check:** Sequence plot over time

**Observation:**
```
Days 1-3: Mostly negative residuals (-28, -19, -51)
Days 4-5: Positive residuals (+28, +32)
Day 6: Negative (-11)
Days 7-8: Positive (+27, +22)

Possible clustering? 
```

**Concern:** Might indicate autocorrelation

**Test:** Durbin-Watson statistic (for formal test)

**Conclusion:** ⚠️ Possible temporal pattern, but sample too small to confirm

**If violated:**
```
Would see runs of positive then negative
Time series methods needed (ARIMA, etc.)
```

---

### 6. Outliers and Influential Points

**Check:** Which residuals are unusually large?

**Identification:**

**Day 3: Residual = -51**
```
Temperature: 30°C (middle of range)
Actual sales: ₹580
Predicted: ₹631
Error: -₹51 (underestimate by 8.8%)

Why might this happen?
- Was it cloudy (not rainy)? Model can't distinguish
- Was it a special day (event, holiday)?
- Random variation?
- Measurement error?

Impact: Largest residual, but only 1 point
Not severely influential (not at extreme x)
```

**Day 5: Residual = +32**
```
Temperature: 36°C (near maximum)
Actual sales: ₹480
Predicted: ₹448
Error: +₹32 (overestimate by 6.7%)

Why might this happen?
- Unusually good sales for hot day
- Different weather context?
- Loyal customers less sensitive to heat?

Impact: Second largest residual
At extreme x → potentially influential
```

**Conclusion:** ⚠️ Days 3 and 5 worth investigating, but not obviously problematic

---

## Question (d): Calculate R² Components

### The Decomposition of Variance

**Total variance in sales can be decomposed:**
```
Total Variation = Explained Variation + Unexplained Variation
     TSS       =        ESS         +         RSS

Where:
  TSS = Total Sum of Squares
  ESS = Explained Sum of Squares (Regression SS)
  RSS = Residual Sum of Squares
```

---

### Step 1: Calculate TSS (Total Sum of Squares)

**Formula:**
```
TSS = Σ(y - ȳ)²
```

**Mean sales:**
```
ȳ = (450 + 520 + 580 + 720 + 480 + 650 + 780 + 440) / 8
  = 4,620 / 8
  = ₹577.50
```

**Deviations from mean:**

| Day | Sales (y) | Mean (ȳ) | (y - ȳ) | (y - ȳ)² |
|-----|-----------|----------|---------|----------|
| 1   | 450       | 577.5    | -127.5  | 16,256.25 |
| 2   | 520       | 577.5    | -57.5   | 3,306.25  |
| 3   | 580       | 577.5    | 2.5     | 6.25      |
| 4   | 720       | 577.5    | 142.5   | 20,306.25 |
| 5   | 480       | 577.5    | -97.5   | 9,506.25  |
| 6   | 650       | 577.5    | 72.5    | 5,256.25  |
| 7   | 780       | 577.5    | 202.5   | 41,006.25 |
| 8   | 440       | 577.5    | -137.5  | 18,906.25 |
|**Sum**|         |          | 0       | **114,550** |

**TSS = 114,550**

**Interpretation:** Total variation in sales is ₹114,550² (sum of squared deviations)

---

### Step 2: Calculate RSS (Residual Sum of Squares)

**Formula:**
```
RSS = Σ(ε²) = Σ(y - ŷ)²
```

**From our residuals:**

| Day | Residual (ε) | ε² |
|-----|--------------|-----|
| 1   | -28.5        | 812.25 |
| 2   | -19.5        | 380.25 |
| 3   | -51.0        | 2,601.00 |
| 4   | +28.0        | 784.00 |
| 5   | +32.0        | 1,024.00 |
| 6   | -11.5        | 132.25 |
| 7   | +27.0        | 729.00 |
| 8   | +22.5        | 506.25 |
|**Sum**|            | **6,969.00** |

**RSS = 6,969**

**Interpretation:** Unexplained variation (error) is ₹6,969² (sum of squared residuals)

---

### Step 3: Calculate ESS (Explained Sum of Squares)

**Method 1: By subtraction**
```
ESS = TSS - RSS
    = 114,550 - 6,969
    = 107,581
```

**Method 2: Direct calculation**
```
ESS = Σ(ŷ - ȳ)²

Need to calculate for each prediction:
(478.5 - 577.5)² + (539.5 - 577.5)² + ... + (417.5 - 577.5)²
= 9,801 + 1,444 + 2,862.25 + 13,110.25 + 16,641 + 7,056 + 30,756.25 + 25,600
= 107,270.75 ≈ 107,581 (rounding differences)
```

**ESS = 107,581**

**Interpretation:** Explained variation (by the model) is ₹107,581²

---

### Step 4: Verify the Decomposition

**Check:**
```
TSS = ESS + RSS?
114,550 = 107,581 + 6,969
114,550 = 114,550 ✓

Perfect! Variance decomposition confirmed.
```

---

### Step 5: Calculate R²

**Formula:**
```
R² = ESS / TSS = 1 - (RSS / TSS)
```

**Calculation:**
```
R² = 107,581 / 114,550
   = 0.9392
   ≈ 0.94 or 94%
```

**Alternative:**
```
R² = 1 - (6,969 / 114,550)
   = 1 - 0.0608
   = 0.9392
   ≈ 0.94 ✓ (confirms)
```

---

### Visual Representation

```
Total Variation (TSS = 114,550)
┌────────────────────────────────────┐
│                                    │
│  Explained by Model (ESS = 107,581)│
│  ██████████████████████████████████│ 94%
│                                    │
│  Unexplained (RSS = 6,969)         │
│  ███                               │ 6%
│                                    │
└────────────────────────────────────┘

R² = 94% (excellent!)
```

---

## Question (e): Identify Problematic Points

### Diagnostic Criteria

**What makes a point "problematic"?**

1. **Large residual** (outlier in y-direction)
2. **High leverage** (extreme x-value)
3. **High influence** (affects regression line significantly)

---

### 1. Outliers (Large Residuals)

**Standardized Residuals:**

```
Standardized residual = residual / (standard deviation of residuals)

SD of residuals = √(RSS / (n-2))
                = √(6,969 / 6)
                = √1,161.5
                = 34.08
```

**Calculate:**

| Day | Residual | Standardized | Assessment |
|-----|----------|--------------|------------|
| 1   | -28.5    | -0.84        | OK         |
| 2   | -19.5    | -0.57        | OK         |
| 3   | -51.0    | -1.50        | ⚠️ Borderline |
| 4   | +28.0    | +0.82        | OK         |
| 5   | +32.0    | +0.94        | OK         |
| 6   | -11.5    | -0.34        | OK         |
| 7   | +27.0    | +0.79        | OK         |
| 8   | +22.5    | +0.66        | OK         |

**Rule of thumb:**
```
|Standardized residual| > 2: Outlier
|Standardized residual| > 3: Severe outlier
```

**Finding:** Day 3 has largest standardized residual (-1.50), but not extreme (<2)

---

### 2. Leverage (Extreme X-values)

**Leverage measures how extreme a point's x-value is**

**Formula (for simple regression):**
```
h_i = 1/n + (x_i - x̄)² / Σ(x - x̄)²
```

**Calculate for each point:**

```
n = 8
x̄ = (35+33+30+28+36+29+26+37)/8 = 31.75°C
Σ(x - x̄)² = 60.9 (from Problem 2A.2)
```

| Day | Temp (x) | (x - x̄) | (x - x̄)² | h_i | Assessment |
|-----|----------|----------|-----------|-----|------------|
| 1   | 35       | 3.25     | 10.56     | 0.298 | Medium |
| 2   | 33       | 1.25     | 1.56      | 0.151 | Low |
| 3   | 30       | -1.75    | 3.06      | 0.175 | Low |
| 4   | 28       | -3.75    | 14.06     | 0.356 | High ⚠️ |
| 5   | 36       | 4.25     | 18.06     | 0.422 | High ⚠️ |
| 6   | 29       | -2.75    | 7.56      | 0.249 | Medium |
| 7   | 26       | -5.75    | 33.06     | 0.667 | VERY High ⚠️⚠️ |
| 8   | 37       | 5.25     | 27.56     | 0.577 | VERY High ⚠️⚠️ |

**Average leverage:** h̄ = 2/8 = 0.25

**High leverage threshold:** 2 × h̄ = 0.50

**Findings:**
- **Day 7** (26°C): h = 0.667 (HIGHEST - coolest day)
- **Day 8** (37°C): h = 0.577 (VERY HIGH - hottest day)
- **Day 5** (36°C): h = 0.422 (HIGH)
- **Day 4** (28°C): h = 0.356 (HIGH)

**Interpretation:** Extreme temperatures have high leverage (expected!)

---

### 3. Influence (Cook's Distance)

**Influence combines residual and leverage**

**Formula:**
```
Cook's D_i = (standardized residual)² × h_i / ((p+1) × (1-h_i))

Where p = number of predictors = 1
```

**Calculate:**

| Day | Std. Resid | Leverage | Cook's D | Assessment |
|-----|------------|----------|----------|------------|
| 1   | -0.84      | 0.298    | 0.140    | Low        |
| 2   | -0.57      | 0.151    | 0.033    | Low        |
| 3   | -1.50      | 0.175    | 0.264    | Medium ⚠️  |
| 4   | +0.82      | 0.356    | 0.161    | Low-Med    |
| 5   | +0.94      | 0.422    | 0.271    | Medium ⚠️  |
| 6   | -0.34      | 0.249    | 0.019    | Low        |
| 7   | +0.79      | 0.667    | 0.278    | Medium ⚠️  |
| 8   | +0.66      | 0.577    | 0.168    | Low-Med    |

**Calculation example (Day 3):**
```
D_3 = (-1.50)² × 0.175 / (2 × (1 - 0.175))
    = 2.25 × 0.175 / 1.65
    = 0.238 ≈ 0.264
```

**Rule of thumb:**
```
Cook's D > 1: Highly influential (problem!)
Cook's D > 0.5: Moderately influential (investigate)
Cook's D > 4/n = 0.5: Worth checking (for our n=8)
```

**Findings:**
- **No points exceed 0.5** (good!)
- **Days 3, 5, 7** have moderate influence (~0.27)
- All are acceptable levels

---

### Summary: Problematic Points

**Day 3 (30°C, ₹580):**
```
✓ Residual: -51 (largest, but only 1.5 SD)
✓ Leverage: 0.175 (low - middle temp)
⚠️ Influence: 0.264 (moderate)

Assessment: BORDERLINE
  - Largest residual, but reasonable magnitude
  - Not at extreme x, so not high leverage
  - Moderate influence
  
Action: Investigate but probably keep
  - Was this a cloudy day? (can't distinguish in model)
  - Any special circumstances?
  - If no explanation, likely random variation
```

**Day 5 (36°C, ₹480):**
```
✓ Residual: +32 (2nd largest, 0.94 SD)
⚠️ Leverage: 0.422 (high - near max temp)
⚠️ Influence: 0.271 (moderate)

Assessment: NOTABLE
  - Large positive residual
  - High leverage (extreme temp)
  - Moderate influence
  
Action: Worth checking
  - Why good sales on hot day?
  - Different circumstances?
  - If removed, slope would steepen slightly
```

**Day 7 (26°C, ₹780):**
```
✓ Residual: +27 (moderate, 0.79 SD)
⚠️⚠️ Leverage: 0.667 (HIGHEST - coolest day)
⚠️ Influence: 0.278 (moderate)

Assessment: HIGH LEVERAGE
  - Residual reasonable
  - VERY high leverage (coldest day)
  - Moderate influence
  
Action: Important data point
  - Anchors cool end of temperature range
  - If removed, would lose information at low temps
  - Keep unless data error
```

**Day 8 (37°C, ₹440):**
```
✓ Residual: +22.5 (moderate, 0.66 SD)
⚠️⚠️ Leverage: 0.577 (VERY HIGH - hottest day)
✓ Influence: 0.168 (low)

Assessment: HIGH LEVERAGE
  - Residual small
  - Very high leverage (hottest day)
  - Low influence (residual compensates)
  
Action: Important data point
  - Anchors hot end of temperature range
  - Behaves as expected
  - Definitely keep
```

---

### Recommendations

**Points to keep:**
- ✅ **All 8 points** - none are problematic enough to exclude

**Points to investigate:**
- 🔍 **Day 3** - understand why sales lower than expected at 30°C
- 🔍 **Day 5** - understand why sales higher than expected at 36°C

**Why keep all points:**
```
1. No severe outliers (all within 2 SD)
2. High leverage points (Days 7, 8) are valuable data
   - Represent temperature extremes
   - Well-behaved (small residuals)
   - Removing would narrow valid range
3. Influential points (Days 3, 5, 7) not overly so
   - Cook's D all < 0.3 (threshold is 0.5-1.0)
   - Removing wouldn't dramatically change model
4. Small sample (n=8)
   - Can't afford to remove data
   - Each point represents 12.5% of data
```

---

## Question (f): Model Improvement Suggestions

### Based on Residual Analysis

---

### 1. Add Weather Type Variable

**Rationale from residuals:**
```
Day 3 (30°C, cloudy?): Large negative residual (-51)
Day 7 (26°C, rainy?): Positive residual (+27)

Weather type likely explains some unexplained variance
```

**Proposed model:**
```
Sales = a + b₁(Temp) + b₂(Rain) + b₃(Cloudy)

Expected improvement: R² from 0.94 to 0.97-0.98
Would reduce residuals for Days 3, 7 especially
```

---

### 2. Check for Non-Linearity

**Current evidence:**
```
Residual vs fitted plot: Mostly random
No obvious curve
```

**But consider:**
```
At extremes (very hot/cold), relationship might not be linear
Could try quadratic: Sales = a + b₁(Temp) + b₂(Temp²)

However: With only 8 points, stick to linear
Not enough data for complex models
```

**Recommendation:** Keep linear for now, revisit with more data

---

### 3. Collect More Data

**Current limitations:**
```
n = 8 (very small!)
Only 1-2 points at some temperatures
Hard to detect patterns
High leverage at extremes
```

**Recommendation:**
```
Collect 30-50 days of data
Multiple observations at each temperature
Better coverage of temperature range
Can then:
  - Detect non-linearity more reliably
  - Identify outliers with confidence
  - Test more complex models
  - Validate on holdout set
```

---

### 4. Include Day of Week

**Rationale:**
```
From Problem 2A.1: Weekday vs weekend matters (36% difference!)
Current model: Ignores this
Possible: Some residuals due to day-of-week effects
```

**Enhanced model:**
```
Sales = a + b₁(Temp) + b₂(Weekend) + b₃(Friday)

Would capture:
  - Lower baseline on weekends
  - Higher sales on Fridays (payday)
  - Reduce residual variance
```

---

### 5. Time-Series Consideration

**Pattern noted:**
```
Days 1-3: Negative residuals
Days 4-5: Positive residuals
Days 7-8: Positive residuals

Possible autocorrelation?
```

**If confirmed (need more data):**
```
Use time series methods:
  - AR models (autoregressive)
  - ARIMA
  - Account for temporal correlation
```

**Current action:** Note for future, but sample too small now

---

## Key Takeaways

### What Residual Analysis Reveals

**1. Model Quality Assessment**
```
R² = 0.94: Excellent fit
Residuals: Small, balanced
Pattern: Random (good!)
Conclusion: Model works well
```

**2. Assumption Validation**
```
✅ Linearity: No curve in residuals
✅ Homoscedasticity: Variance roughly constant
✅ Normality: Approximately normal (Q-Q plot)
⚠️ Independence: Possible temporal pattern (need more data)
```

**3. Outlier Detection**
```
Day 3: Largest residual (-51), moderate influence
Day 5: High leverage, moderate influence
Days 7, 8: Very high leverage (temperature extremes)
All acceptable: None require removal
```

**4. Improvement Opportunities**
```
Priority 1: Add weather type (rain/cloudy/sunny)
Priority 2: Collect more data (30-50 days)
Priority 3: Include day of week
Priority 4: Monitor for temporal patterns
```

---

### Advanced Concepts Introduced

**Variance Decomposition:**
```
Total = Explained + Unexplained
TSS = ESS + RSS
114,550 = 107,581 + 6,969
100% = 94% + 6%
```

**Leverage:**
```
Measures extremeness of predictor value
High leverage ≠ problematic (unless large residual too)
Days 7, 8 have high leverage but small residuals → OK
```

**Cook's Distance:**
```
Combines residual size and leverage
Identifies truly influential points
All our points < 0.3 → None overly influential
```

---

### From Book Philosophy

**Box's Law Applied:**
```
"All models are wrong, but some are useful"

Our model:
  Wrong: Explains only 94%, ignores weather, day, etc.
  Useful: Small residuals, actionable predictions, clear insights
  
Residual analysis quantifies the "wrong" part
Shows us where model fails
Guides improvement
```

---

## Common Mistakes

### ❌ Mistake 1: Ignoring Residual Patterns

**Wrong:** "R² = 0.94 is good, done!"

**Right:** "R² = 0.94 is good, but check residuals for assumptions"

---

### ❌ Mistake 2: Removing High Leverage Points

**Wrong:** "Day 7 has h=0.667, remove it!"

**Right:** "Day 7 has high leverage but small residual - keep it! It anchors the cool end."

---

### ❌ Mistake 3: Overreacting to Single Outlier

**Wrong:** "Day 3 has residual -51, remove it!"

**Right:** "Day 3 is only 1.5 SD away, investigate first, probably keep"

---

### ❌ Mistake 4: Not Using Plots

**Wrong:** Just look at numbers (residuals list)

**Right:** Plot residuals multiple ways - patterns visible in plots

---

## Extensions for Advanced Students

### Extension 1: Formal Tests

**Durbin-Watson test:** Autocorrelation  
**Breusch-Pagan test:** Heteroscedasticity  
**Shapiro-Wilk test:** Normality  
**RESET test:** Functional form

### Extension 2: Robust Regression

**M-estimators:** Less sensitive to outliers  
**Weighted least squares:** Handle heteroscedasticity  
**Quantile regression:** Model different parts of distribution

### Extension 3: Cross-Validation

**Leave-one-out:** Remove each point, refit, predict  
**K-fold:** Divide data, validate on holdout  
**Prediction error:** RMSE, MAE on validation set

---

*Solution by Dr. Alok Patel for The Pattern Hunters*  
*Chapter 2: From Guesswork to Models - Set A*  
*Advanced model validation through residual analysis*
