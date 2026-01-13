# Solution 2A.2: Temperature and Tea Sales ⭐⭐

## Problem Summary
Build a linear regression model relating temperature to tea sales using least squares method. This is THE core example from the book (Chapter 2, pages 74-75).

---

## Given Data

```
Day | Temperature (°C) | Sales (₹) | Weather
----|------------------|-----------|----------
1   | 35              | 450       | Sunny
2   | 33              | 520       | Sunny
3   | 30              | 580       | Cloudy
4   | 28              | 720       | Rainy
5   | 36              | 480       | Sunny
6   | 29              | 650       | Cloudy
7   | 26              | 780       | Rainy
8   | 37              | 440       | Sunny
```

---

## Question (a): Visual Assessment

### Plot the Relationship

**Scatter Plot Description:**

```
Sales (₹)
800 |                    ●(7)
    |
700 |                ●(4)
    |
600 |            ●(6)    ●(3)
    |
500 |        ●(2)
    |    ●(5)  ●(1)
400 |                        ●(8)
    |________________________
      26  28  30  32  34  36  38  Temperature (°C)
```

### Visual Observations

**1. General Trend:**
- Clear **downward** (negative) relationship
- As temperature increases (left to right), sales decrease
- Points show approximate linear pattern

**2. Relationship Characteristics:**
- **Direction:** Negative (inverse relationship)
- **Strength:** Moderately strong (points cluster around line)
- **Form:** Linear (not curved)
- **Outliers:** None obvious, but some scatter

**3. Biological Reasoning:**

**Why Negative Relationship?**

**Cooler days → Higher sales:**
- People want hot beverages when it's cooler
- Comfort behavior (warm tea on cool day)
- Office workers seek warmth

**Hotter days → Lower sales:**
- People avoid hot drinks in heat
- Prefer cold beverages instead
- Less need for warming up

**4. Weather Type Pattern:**
```
Rainy days (26°C, 28°C): ₹780, ₹720 (HIGHEST sales)
Cloudy days (29°C, 30°C): ₹650, ₹580 (MEDIUM sales)
Sunny days (33-37°C): ₹440-520 (LOWER sales, except ₹520)
```

**Insight:** Both temperature AND weather type matter!

---

## Question (b): Least Squares Regression

### Step-by-Step Calculation

**Goal:** Find the best-fit line: **Sales = a + b × Temperature**

Where:
- **b** = slope (rate of change)
- **a** = intercept (theoretical sales at 0°C)

---

### Step 1: Calculate Means

**Mean Temperature (x̄):**
```
x̄ = (35 + 33 + 30 + 28 + 36 + 29 + 26 + 37) / 8
  = 254 / 8
  = 31.75°C
```

**Mean Sales (ȳ):**
```
ȳ = (450 + 520 + 580 + 720 + 480 + 650 + 780 + 440) / 8
  = 4,620 / 8
  = ₹577.50
```

---

### Step 2: Calculate Deviations

| Day | Temp (x) | Sales (y) | (x - x̄) | (y - ȳ) | (x - x̄)² | (x - x̄)(y - ȳ) |
|-----|----------|-----------|----------|----------|-----------|------------------|
| 1   | 35       | 450       | 3.25     | -127.5   | 10.56     | -414.38          |
| 2   | 33       | 520       | 1.25     | -57.5    | 1.56      | -71.88           |
| 3   | 30       | 580       | -1.75    | 2.5      | 3.06      | -4.38            |
| 4   | 28       | 720       | -3.75    | 142.5    | 14.06     | -534.38          |
| 5   | 36       | 480       | 4.25     | -97.5    | 18.06     | -414.38          |
| 6   | 29       | 650       | -2.75    | 72.5     | 7.56      | -199.38          |
| 7   | 26       | 780       | -5.75    | 202.5    | 33.06     | -1,164.38        |
| 8   | 37       | 440       | 5.25     | -137.5   | 27.56     | -721.88          |
|**Sum**| 254    | 4,620     | 0        | 0        | **115.50**| **-3,525.00**    |

---

### Step 3: Calculate Slope (b)

**Formula:**
```
b = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)²]
```

**Calculation:**
```
b = -3,525.00 / 115.50
  = -30.52 ₹ per °C
  ≈ -30.5 ₹ per °C (rounded)
```

**Interpretation:** For every 1°C increase in temperature, sales **decrease** by ₹30.50

---

### Step 4: Calculate Intercept (a)

**Formula:**
```
a = ȳ - b × x̄
```

**Calculation:**
```
a = 577.50 - (-30.52) × 31.75
  = 577.50 - (-969.02)
  = 577.50 + 969.02
  = 1,546.52
  ≈ ₹1,546 (rounded)
```

**Interpretation:** Theoretical sales at 0°C (extrapolation - not realistic!)

---

### Final Model Equation

```
Sales = 1,546 - 30.5 × Temperature

Or more precisely:
Sales = 1,546.52 - 30.52 × Temperature
```

**This matches the book example exactly! (Pages 74-75)**

---

## Question (c): Interpret the Model

### What Does the Slope Tell Rajesh?

**Slope = -30.5 ₹ per °C**

**Practical Meaning:**

**1. Rate of Change:**
```
For every 1°C warmer → Sales drop by ₹30.50
For every 1°C cooler → Sales increase by ₹30.50
```

**2. Business Examples:**

**Temperature Effect:**
```
If tomorrow is 32°C:
  Sales ≈ 1,546 - 30.5 × 32 = ₹570

If next day is 27°C (5°C cooler):
  Sales ≈ 1,546 - 30.5 × 27 = ₹723
  Difference: ₹723 - ₹570 = ₹153 more!
  (5°C × ₹30.50/°C = ₹152.50)
```

**3. Planning Implications:**

**For Rajesh:**
- **Cool weather forecast?** Buy more milk, expect higher sales
- **Hot weather forecast?** Buy less milk, expect lower sales
- **Seasonal planning:** Winter (cooler) = busier; Summer (hotter) = slower

**4. Magnitude Assessment:**

**Is -30.5 a "large" effect?**
```
Temperature range in data: 26°C to 37°C (11°C span)
Sales range: 11°C × ₹30.5/°C = ₹335.50

Actual sales range: ₹780 - ₹440 = ₹340
Temperature explains: ₹335.50 / ₹340 = 98.7% of range!
```

**Very strong effect!**

---

### What Does the Intercept Mean?

**Intercept = ₹1,546**

**Mathematical Meaning:**
```
When Temperature = 0°C:
Sales = 1,546 - 30.5 × 0 = ₹1,546
```

**Is This Meaningful? NO!**

**Why Not Realistic:**

**1. Extrapolation Problem:**
- Data range: 26°C to 37°C
- 0°C is FAR outside this range
- Extrapolation is dangerous!

**2. Biological Impossibility:**
- 0°C in Bhubaneswar? Never happens!
- Tea stall wouldn't operate at 0°C
- Model breaks down at extremes

**3. What It Actually Represents:**

The intercept is a **mathematical necessity** for the line equation, but has no real-world interpretation in this context.

**Better Interpretation:**
"The intercept anchors the line mathematically. It ensures the line passes through (x̄, ȳ) = (31.75, 577.50)"

**Verification:**
```
At mean temperature (31.75°C):
Sales = 1,546 - 30.5 × 31.75
      = 1,546 - 968.38
      = 577.62
      ≈ ȳ = 577.50 ✓
```

---

## Question (d): Make Predictions

### Predict Sales at 32°C

**Using the Model:**
```
Sales = 1,546 - 30.5 × Temperature
      = 1,546 - 30.5 × 32
      = 1,546 - 976
      = ₹570
```

**Prediction: ₹570**

**Confidence Assessment:**

**High Confidence** because:
- 32°C is **within** the data range (26-37°C)
- This is **interpolation** (between observed points)
- Close to mean temperature (31.75°C)
- Model fits data well in this region

**Expected Range:** ±₹50 (roughly ₹520-₹620)

---

### Predict Sales at 40°C

**Using the Model:**
```
Sales = 1,546 - 30.5 × Temperature
      = 1,546 - 30.5 × 40
      = 1,546 - 1,220
      = ₹326
```

**Prediction: ₹326**

**Confidence Assessment:**

**LOW Confidence** because:
- 40°C is **outside** the data range (26-37°C)
- This is **extrapolation** (beyond observed data)
- Model may not hold at extremes
- Biological factors change at extremes

**Reasons for Low Confidence:**

**1. No Data at 40°C:**
- We've never observed sales at this temperature
- Don't know if linear relationship continues

**2. Extreme Weather Effects:**
- At 40°C, people might avoid going out entirely
- Office workers might work from home
- Different behavior patterns emerge

**3. Physical Constraints:**
```
Model predicts ₹326
But could sales drop even more?
Or might there be a floor (minimum demand)?
```

**4. Comparison to Data:**
```
Observed minimum: ₹440 (at 37°C)
Predicted at 40°C: ₹326
That's 26% lower than observed minimum!
```

**Realistic Estimate:** ₹300-₹400 (with very high uncertainty)

---

### Which Prediction is More Reliable?

**Answer: The 32°C prediction**

**Comparison:**

| Feature | 32°C Prediction | 40°C Prediction |
|---------|----------------|----------------|
| **Position** | Within data range | Outside data range |
| **Type** | Interpolation | Extrapolation |
| **Confidence** | High | Low |
| **Uncertainty** | ±₹50 (~9%) | ±₹100 (~30%) |
| **Biological validity** | Well-supported | Questionable |

**General Rule:**

> **Interpolation (within data range) >> Extrapolation (outside data range)**

**Visual Representation:**
```
         Known          Unknown
    ←  Reliable  →  ←  Uncertain  →
    __________________|___________
    26°  31.75° 37°   40°
         ↑      ↑
      Our data  Extrapolation
```

---

## Question (e): Model Validation

### Calculate Predicted Sales for Each Day

**For Each Observation:**
```
Predicted = 1,546 - 30.5 × Temperature
```

| Day | Temp | Actual | Predicted | Residual | % Error |
|-----|------|--------|-----------|----------|---------|
| 1   | 35   | 450    | 478.5     | -28.5    | -6.3%   |
| 2   | 33   | 520    | 539.5     | -19.5    | -3.8%   |
| 3   | 30   | 580    | 631.0     | -51.0    | -8.8%   |
| 4   | 28   | 720    | 692.0     | +28.0    | +3.9%   |
| 5   | 36   | 480    | 448.0     | +32.0    | +6.7%   |
| 6   | 29   | 650    | 661.5     | -11.5    | -1.8%   |
| 7   | 26   | 780    | 753.0     | +27.0    | +3.5%   |
| 8   | 37   | 440    | 417.5     | +22.5    | +5.1%   |

---

### Residual Analysis

**Residual = Actual - Predicted**

**Positive residual:** Model underestimates (actual > predicted)  
**Negative residual:** Model overestimates (actual < predicted)

**Residuals:**
```
Day 1: -28.5  (Model predicted too high)
Day 2: -19.5  (Model predicted too high)
Day 3: -51.0  (Model predicted too high) ← Largest negative
Day 4: +28.0  (Model predicted too low)
Day 5: +32.0  (Model predicted too low)  ← Largest positive
Day 6: -11.5  (Model predicted too high)
Day 7: +27.0  (Model predicted too low)
Day 8: +22.5  (Model predicted too low)
```

---

### Average Error (Mean Absolute Error)

**Calculate MAE:**
```
MAE = (|−28.5| + |−19.5| + |−51.0| + |+28.0| + |+32.0| + |−11.5| + |+27.0| + |+22.5|) / 8
    = (28.5 + 19.5 + 51.0 + 28.0 + 32.0 + 11.5 + 27.0 + 22.5) / 8
    = 220.0 / 8
    = ₹27.50 average error
```

**Interpretation:** On average, predictions are off by about ₹27.50 (roughly 5% of mean sales)

---

### Root Mean Square Error (RMSE)

**Calculate RMSE:**
```
RMSE = √[Σ(residual²) / n]
     = √[(28.5² + 19.5² + 51.0² + 28.0² + 32.0² + 11.5² + 27.0² + 22.5²) / 8]
     = √[(812.25 + 380.25 + 2,601 + 784 + 1,024 + 132.25 + 729 + 506.25) / 8]
     = √[6,969 / 8]
     = √871.13
     = ₹29.52
```

**Interpretation:** Typical prediction error is about ₹30

---

### Does the Model Work Well?

**YES - The model works reasonably well**

**Evidence Supporting "Good Fit":**

**1. Small Errors:**
- Average error: ₹27.50 (4.8% of mean sales)
- RMSE: ₹29.52 (5.1% of mean sales)
- Most predictions within ₹30 of actual

**2. No Systematic Bias:**
- Positive residuals: 4 days (sum = +109.5)
- Negative residuals: 4 days (sum = -110.5)
- Nearly balanced (sum ≈ 0)

**3. Residuals Appear Random:**
- No obvious pattern by temperature
- No obvious pattern by day
- Suggests linear model is appropriate

**4. Predictions Match Reality:**
```
Best prediction: Day 6 (only ₹11.5 off)
Worst prediction: Day 3 (₹51 off, but still only 8.8% error)
```

**However, Model is Not Perfect:**

**Largest Errors:**
- **Day 3 (30°C):** Predicted ₹631, Actual ₹580 (-₹51)
  - **Why?** Cloudy but not rainy, model doesn't capture this
  
- **Day 5 (36°C):** Predicted ₹448, Actual ₹480 (+₹32)
  - **Why?** Hot sunny day, but still decent sales

**What's Missing:**
```
Temperature explains ~70% of variation
Remaining 30% due to:
  - Weather type (rain vs cloudy vs sunny)
  - Day of week effects
  - Random customer variation
  - Unmeasured factors
```

---

### Calculate R² (Coefficient of Determination)

**Formula:**
```
R² = 1 - (RSS / TSS)

Where:
  RSS = Residual Sum of Squares = Σ(residual²)
  TSS = Total Sum of Squares = Σ(y - ȳ)²
```

**Calculate TSS:**
```
TSS = (450-577.5)² + (520-577.5)² + (580-577.5)² + (720-577.5)² + 
      (480-577.5)² + (650-577.5)² + (780-577.5)² + (440-577.5)²
    = 16,256.25 + 3,306.25 + 6.25 + 20,306.25 + 9,506.25 + 
      5,256.25 + 41,006.25 + 18,906.25
    = 114,550
```

**Calculate RSS:**
```
RSS = 28.5² + 19.5² + 51.0² + 28.0² + 32.0² + 11.5² + 27.0² + 22.5²
    = 812.25 + 380.25 + 2,601 + 784 + 1,024 + 132.25 + 729 + 506.25
    = 6,969
```

**Calculate R²:**
```
R² = 1 - (6,969 / 114,550)
   = 1 - 0.0608
   = 0.939
   ≈ 0.94 or 94%
```

**Wait, that's different from the book!**

**Book says ~70% (0.70), but calculation gives 94%!**

**Resolution:** The book's 70% likely refers to a different interpretation or includes weather effects. Our pure temperature model actually explains 94% of variance, which is excellent!

**Interpretation:**
- **94% of variation in sales is explained by temperature**
- **Only 6% remains unexplained**
- This is a VERY strong relationship!

---

## Real-World Model Insights

### From the Book (Page 75)

> **"Model Insight:** The temperature relationship explains about 70% of sales variation, but weather conditions beyond temperature (rain, clouds) add another layer of complexity."

### Our Enhanced Understanding

**Temperature Model Performance:**

**Strengths:**
- ✅ Explains 94% of variance (R² = 0.94)
- ✅ Clear negative relationship (slope = -30.5)
- ✅ Small prediction errors (RMSE = ₹30)
- ✅ Simple to use (one variable)
- ✅ Intuitive (cooler = more tea)

**Weaknesses:**
- ❌ Doesn't capture weather type (rain/cloudy/sunny)
- ❌ Ignores day of week effects
- ❌ Extrapolation unreliable
- ❌ Assumes linear relationship throughout range

---

## Question Recap: Does the Model Work Well?

### Final Answer: **YES, but with caveats**

**The model works well because:**

1. **High R²:** Explains 94% of variance
2. **Small errors:** Average ±₹27.50 (5% of sales)
3. **No bias:** Errors balance out (positive = negative)
4. **Interpretable:** Clear business meaning (₹30.50 per °C)
5. **Useful:** Better than guessing or using average

**The model has limitations:**

1. **Weather type:** Rainy vs sunny matters beyond temperature
2. **Day effects:** Weekday vs weekend not captured
3. **Extrapolation:** Unreliable beyond 26-37°C range
4. **Causation:** Correlation doesn't prove temperature causes sales changes
5. **Other factors:** Customer mood, competition, holidays ignored

**Box's Law:**

> **"All models are wrong, but some are useful"**

**Our model is:**
- ✅ Definitely "wrong" (oversimplified)
- ✅ Definitely "useful" (predicts well within range)
- ✅ A good starting point for business planning
- ✅ Can be improved by adding more variables

---

## Practical Recommendations for Rajesh

### Daily Decision-Making

**Morning (5 AM) - Check Temperature Forecast:**

```
If forecast = 27°C:
  Expected sales = 1,546 - 30.5 × 27 = ₹722
  Buy milk accordingly
  
If forecast = 35°C:
  Expected sales = 1,546 - 30.5 × 35 = ₹478
  Buy less milk

Adjustment factors:
  - If rainy forecast: Add ₹100-150 (from weather pattern)
  - If weekend: Subtract based on day of week pattern
  - If holiday: Major adjustment needed
```

---

### Strategic Planning

**Seasonal Preparation:**

```
Summer months (Apr-Jun):
  Average temp: 36-38°C
  Expected daily: ₹440-510
  Strategy: Reduce inventory, consider cold beverages

Monsoon (Jul-Sep):
  Average temp: 28-30°C  
  Expected daily: ₹580-690
  Strategy: Stock up, hire part-time help

Winter (Dec-Jan):
  Average temp: 24-27°C
  Expected daily: ₹690-780
  Strategy: Peak season, maximize capacity
```

---

### Model Improvement Path

**Phase 1 (Immediate):**
```
Continue current model
Track actual vs predicted daily
Note major errors and causes
```

**Phase 2 (1-2 months):**
```
Add weather type variable:
  Sales = Base + Temp_Effect + Weather_Effect
  
  Rain_Bonus = +₹150
  Cloudy_Adjustment = +₹50
  Sunny_Baseline = 0
```

**Phase 3 (3-6 months):**
```
Multi-variable model:
  Sales = f(Temperature, Weather, Day, Season, Holiday)
  
Use historical data to fit complex model
Potentially use machine learning
```

---

## Key Takeaways

### Mathematical Concepts Learned

**1. Least Squares Method:**
- Calculate slope: b = Σ[(x-x̄)(y-ȳ)] / Σ[(x-x̄)²]
- Calculate intercept: a = ȳ - b×x̄
- Creates "best fit" line minimizing squared errors

**2. Linear Regression:**
- Form: y = a + bx
- Captures linear relationships
- Simple but powerful

**3. Model Evaluation:**
- Residuals show errors
- R² shows percentage explained
- RMSE shows typical error magnitude

**4. Interpolation vs Extrapolation:**
- Inside data range: reliable
- Outside data range: risky

---

### Biological/Business Insights

**1. Temperature-Behavior Relationship:**
- Humans seek comfort (hot drinks when cool)
- Predictable physiological response
- Universal pattern (applies globally)

**2. Environmental Influence:**
- Weather affects consumer behavior
- Quantifiable through data
- Can be modeled mathematically

**3. Practical Application:**
- Data-driven decisions beat guessing
- Models guide but don't dictate
- Continuous refinement necessary

---

### From Intuition to Science

**Before Analysis:**
"Rajesh knows rainy days are good for business"
(Qualitative intuition)

**After Analysis:**
"For every 1°C cooler, sales increase by ₹30.50, explaining 94% of variation"
(Quantitative precision)

**The Power of Mathematics:**
Mathematics didn't replace Rajesh's intuition - it **organized** and **sharpened** it!

---

## Common Mistakes

### ❌ Mistake 1: Arithmetic Errors

**Wrong:**
```
Slope = -3,525 / 115.5 = -35.0  ❌
```

**Right:**
```
Slope = -3,525 / 115.5 = -30.52 ✓
```

**Lesson:** Double-check calculator entries

---

### ❌ Mistake 2: Sign Confusion

**Wrong:** "Temperature increases sales" (positive relationship)

**Right:** "Temperature *decreases* sales" (negative relationship)

**Lesson:** Negative slope means inverse relationship

---

### ❌ Mistake 3: Intercept Over-Interpretation

**Wrong:** "Sales at 0°C would be ₹1,546"

**Right:** "Intercept is mathematical anchor; 0°C outside valid range"

**Lesson:** Don't interpret intercept if x=0 is unrealistic

---

### ❌ Mistake 4: Extrapolation Confidence

**Wrong:** "At 50°C, sales = 1,546 - 30.5×50 = ₹21" (stated with confidence)

**Right:** "Model breaks down at 50°C; prediction unreliable"

**Lesson:** Stay within data range for reliable predictions

---

### ❌ Mistake 5: Causation Assumption

**Wrong:** "Temperature *causes* sales to change"

**Right:** "Temperature and sales are *correlated*; likely causal but could have confounders"

**Lesson:** Correlation ≠ Causation (though often related)

---

## Extensions for Advanced Students

### Extension 1: Weather Type as Categorical Variable

**Hypothesis:** Weather type adds predictive power beyond temperature

**Approach:**
```
Model: Sales = a + b₁(Temp) + b₂(Rain) + b₃(Cloudy)

Where:
  Rain = 1 if rainy, 0 otherwise
  Cloudy = 1 if cloudy, 0 otherwise
  Sunny = baseline (both = 0)
```

**Expected:** R² improves from 0.94 to 0.98+

---

### Extension 2: Interaction Effect

**Hypothesis:** Temperature effect differs by weather type

**Approach:**
```
Model: Sales = a + b₁(Temp) + b₂(Rain) + b₃(Temp×Rain)

Interaction term b₃ captures:
  Does temperature matter differently when raining?
```

---

### Extension 3: Polynomial Regression

**Hypothesis:** Relationship might be curved (not purely linear)

**Approach:**
```
Model: Sales = a + b₁(Temp) + b₂(Temp²)

Quadratic term allows for curvature:
  - Optimal temperature for sales?
  - Diminishing effects at extremes?
```

---

### Extension 4: Prediction Intervals

**Hypothesis:** Quantify prediction uncertainty

**Approach:**
```
Calculate 95% prediction interval:
  Predicted ± 2 × RMSE
  
For 32°C:
  Point: ₹570
  Interval: ₹570 ± 2(₹29.52) = [₹511, ₹629]
```

---

## Connection to Book Themes

### From Chapter 2 (Pages 74-75)

**Book's Example:**
```
Sales = ₹1,546 - 30.5 × Temperature
```

**Our Calculated Model:**
```
Sales = ₹1,546.52 - 30.52 × Temperature
```

**Perfect match!** ✓

**Book's Key Insights:**

1. **"For every degree the temperature drops, Rajesh can expect ₹30.50 more in sales"**
   - ✓ Confirmed by our slope calculation

2. **"On a scorching 40°C day, he should expect: ₹1546 - 30.5 × 40 = ₹326"**
   - ✓ Confirmed, with caveat about extrapolation

3. **"On a cool 25°C rainy day, he should expect: ₹1546 - 30.5 × 25 = ₹784"**
   - ✓ Confirmed, matches data well

**Core Message:**

> "Even simple mathematical models provide actionable insights, while revealing what factors remain unexplained—the foundation of scientific progress."

---

*Solution by Dr. Alok Patel for The Pattern Hunters*  
*Chapter 2: From Guesswork to Models - Set A*  
*Based on book example (pages 74-75)*
