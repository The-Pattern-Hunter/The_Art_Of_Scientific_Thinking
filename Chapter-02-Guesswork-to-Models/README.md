# Chapter 2 Set A: Datasets Documentation
## From Guesswork to Models - The Art of Scientific Thinking

This document describes all datasets for Chapter 2 Set A problems, aligned with the book's core concepts: simple linear regression, least squares method, and model building from real-world observations.

---

## Overview of Chapter 2 Concepts

**Core Topics:**
- Pattern recognition in everyday life
- Transforming intuition into mathematical models
- Least squares regression method
- Linear relationships and correlation
- Model assumptions and limitations
- "All models are wrong, but some are useful" (Box's Law)

**Mathematical Skills:**
- Calculating means and deviations
- Slope and intercept calculation
- R² (coefficient of determination)
- Residual analysis
- Prediction and validation

---

## Dataset 1: Rajesh's Weekly Sales Pattern
**File:** `chapter_02a_rajesh_weekly.csv`  
**Problem:** 2A.1 (⭐ Easy)  
**Concept:** Pattern recognition, basic averaging, qualitative to quantitative

### Description
Rajesh tracks his tea stall for one complete week to understand customer patterns and revenue fluctuations.

### Variables
| Column | Type | Description | Unit |
|--------|------|-------------|------|
| Day | String | Day of the week | - |
| DayNum | Integer | Day number (1=Mon, 7=Sun) | - |
| Revenue | Integer | Daily sales revenue | ₹ (Rupees) |
| Customers | Integer | Number of customers served | count |

### Data Summary
- **Observations:** 7 (one complete week)
- **Mean Revenue:** ₹467.14
- **Mean Customers:** 46.7
- **Pattern:** Weekdays (Mon-Fri) outperform weekends (Sat-Sun)

### Research Questions
1. What is the weekly revenue pattern?
2. Do weekdays differ significantly from weekends?
3. Can we predict next week's Monday revenue?
4. What factors might cause deviations?

### Biological/Business Context
Small business owners intuitively recognize weekly patterns. This exercise makes that intuition quantitative and testable.

---

## Dataset 2: Temperature and Tea Sales
**File:** `chapter_02a_temperature_sales.csv`  
**Problem:** 2A.2 (⭐⭐ Medium)  
**Concept:** Least squares regression, correlation, model interpretation

### Description
Rajesh suspects temperature affects his tea sales. He collects data over 8 days, recording temperature and daily revenue along with weather conditions.

### Variables
| Column | Type | Description | Unit/Values |
|--------|------|-------------|-------------|
| Day | Integer | Day number | 1-8 |
| Temperature_C | Integer | Daily maximum temperature | °Celsius |
| Sales_Rs | Integer | Daily revenue | ₹ (Rupees) |
| Weather | String | Weather condition | Sunny/Cloudy/Rainy |

### Data Summary
- **Observations:** 8 days
- **Temperature Range:** 26°C to 37°C
- **Sales Range:** ₹440 to ₹780
- **Correlation:** Negative (cooler days = higher sales)
- **Expected Model:** Sales ≈ 1546 - 30.5 × Temperature

### Research Questions
1. What is the relationship between temperature and sales?
2. Calculate the least squares regression line
3. For every 1°C increase, how do sales change?
4. Can we predict sales for a 32°C day?
5. What percentage of variation does temperature explain (R²)?

### Key Insight
This is THE core example from the book (Chapter 2, pages 74-75). Students learn:
- How to calculate slope and intercept manually
- Interpreting negative relationships
- Model validation through residuals
- Real-world limitations (weather type matters too!)

### Expected Results
```
Model: Sales = 1546 - 30.5 × Temperature
R² ≈ 0.70 (70% of variation explained)
Interpretation: Each 1°C warmer → ₹30.50 less revenue
```

---

## Dataset 3: Study Hours and Test Scores
**File:** `chapter_02a_study_hours.csv`  
**Problem:** 2A.3 (⭐⭐ Medium)  
**Concept:** Personal data modeling, linear regression, reality checks

### Description
A student tracks study time and test performance over 8 tests to understand the relationship and optimize study strategy.

### Variables
| Column | Type | Description | Unit |
|--------|------|-------------|------|
| StudyHours | Integer | Hours studied for test | hours |
| TestScore | Integer | Test score achieved | points (0-100) |

### Data Summary
- **Observations:** 8 tests
- **Study Hours Range:** 2-9 hours
- **Score Range:** 65-90 points
- **Expected Model:** Score ≈ 62 + 3.17 × Hours

### Research Questions
1. For each additional hour studied, how many points gained?
2. What does the intercept represent (baseline knowledge)?
3. Is the relationship truly linear? (Diminishing returns?)
4. Predict score for 10 hours of study
5. What factors does this model ignore?

### Key Insight
This is a direct example from the book (Chapter 2, pages 76-77). Perfect for students because:
- Personal relevance (their own study habits!)
- Easy to understand variables
- Raises questions about model assumptions
- Reality check: constant slope assumes no diminishing returns

### Expected Results
```
Model: Score = 62.0 + 3.17 × StudyHours
R² ≈ 0.98 (very high correlation)
Interpretation: Each extra hour → +3.2 points
Reality check: Assumes linear returns (may not hold at extremes)
```

---

## Dataset 4: Kamala's Vegetable Pricing
**File:** `chapter_02a_kamala_pricing.csv`  
**Problem:** 2A.4 (⭐⭐ Medium)  
**Concept:** Dynamic pricing, optimization, demand curves

### Description
Kamala adjusts tomato prices throughout the day. This data reveals her intuitive demand curve and optimization strategy.

### Variables
| Column | Type | Description | Unit |
|--------|------|-------------|------|
| TimeOfDay | String | Time period | Morning/MidMorning/etc. |
| Hour | Integer | Hour of day (24-hr) | 8-18 |
| Price_Rs_per_kg | Integer | Price per kilogram | ₹/kg |
| Kg_Sold | Integer | Quantity sold | kg |
| Revenue_Rs | Integer | Total revenue (Price × Quantity) | ₹ |

### Data Summary
- **Observations:** 6 time points through the day
- **Price Range:** ₹20 to ₹40 per kg
- **Quantity Range:** 25-40 kg sold per period
- **Revenue Range:** ₹600 to ₹1,140

### Research Questions
1. How do price and quantity relate? (Demand curve)
2. What pricing maximizes revenue?
3. Why does Kamala drop prices in the evening?
4. Build model: Quantity = f(Price)
5. What factors does this model ignore? (Quality degradation, competition)

### Key Insight
From Chapter 2 (pages 62-63): Kamala uses "dynamic optimization" intuitively. This data makes her strategy explicit and testable.

### Expected Pattern
- Higher prices → lower quantity (standard demand curve)
- But revenue peaks at mid-range prices
- Evening discounts prevent spoilage (perishable goods)

---

## Dataset 5: Babulal's Monsoon Prediction
**File:** `chapter_02a_monsoon_prediction.csv`  
**Problem:** 2A.5 (⭐⭐⭐ Hard)  
**Concept:** Multi-variable models, traditional knowledge, model comparison

### Description
Babulal tracks environmental indicators to predict monsoon arrival in western Odisha over 10 years (2014-2023).

### Variables
| Column | Type | Description | Unit/Range |
|--------|------|-------------|------------|
| Year | Integer | Year of observation | 2014-2023 |
| AntDepth_cm | Integer | Depth of ant burrows | cm (9-17) |
| MahuaFlowering_Day | Integer | Day of year mahua flowers | Day 126-142 |
| PeacockCalls_PerDay | Integer | Average peacock calls | count (5-15) |
| MonsoonDay_OfYear | Integer | Actual monsoon arrival | Day 158-178 |

### Data Summary
- **Observations:** 10 years
- **Monsoon Range:** Day 158 to 178 (June 7 to June 27)
- **Average Arrival:** Day 167 (mid-June)
- **Traditional Accuracy:** Babulal achieves 80-85% accuracy

### Research Questions
1. Which single variable best predicts monsoon arrival?
2. Build three single-variable models and compare R²
3. Does combining all three improve predictions?
4. Train on 2014-2020, test on 2021-2023
5. How does mathematical model compare to traditional knowledge?

### Biological Context
From Chapter 2 (pages 59-61): Traditional weather prediction based on environmental cues. This data tests whether these folk observations have scientific validity.

### Expected Relationships
- **Ant Depth:** Deeper burrows → earlier monsoon (insects sense atmospheric changes)
- **Mahua Flowering:** Earlier flowering → earlier monsoon (plant phenology responds to climate)
- **Peacock Calls:** More calls → earlier monsoon (bird behavior reflects weather patterns)

### Key Insight
Traditional knowledge encoded as multivariate predictive model. Students see that folk wisdom often has quantitative foundation.

---

## Dataset 6: Commute Time Optimizer
**File:** `chapter_02a_commute_optimizer.csv`  
**Problem:** 2A.6 (⭐ Easy)  
**Concept:** Optimization, decision models, multiple factors

### Description
Daily commute data tracking different routes, traffic conditions, and travel times over 2 weeks.

### Variables
| Column | Type | Description | Unit/Values |
|--------|------|-------------|-------------|
| Day | String | Day of week | Monday-Friday |
| Week | Integer | Week number | 1-2 |
| Route | String | Route taken | NH16/Janpath/Patrapada |
| Distance_km | Integer | Route distance | km |
| TrafficLevel | Integer | Traffic intensity | 1-10 scale |
| Time_min | Integer | Actual commute time | minutes |

### Data Summary
- **Observations:** 10 commutes
- **Routes:** 3 different (NH16=12km, Janpath=10km, Patrapada=11km)
- **Traffic Range:** 5-9 (moderate to heavy)
- **Time Range:** 32-50 minutes

### Research Questions
1. Which route is fastest on average?
2. How much does traffic affect commute time?
3. Build model: Time = f(Distance, Traffic)
4. Create decision rule for route selection
5. What other factors matter? (Weather, time of day, road conditions)

### Biological/Behavioral Context
From Chapter 2 (pages 69-70): Daily route optimization is unconscious "Dijkstra's algorithm" - finding optimal paths through networks.

---

## Using These Datasets

### Learning Progression

**Level 1 (Problems 2A.1, 2A.6):** Basic patterns and averages
- Recognize patterns visually
- Calculate simple statistics
- Make qualitative predictions

**Level 2 (Problems 2A.2, 2A.3, 2A.4):** Linear regression
- Calculate least squares manually
- Interpret slope and intercept
- Make quantitative predictions
- Calculate R²

**Level 3 (Problems 2A.5, 2A.7, 2A.8):** Advanced concepts
- Multi-variable models
- Model assumptions and limitations
- Residual analysis
- Model comparison and validation

### Common Analyses Across All Datasets

1. **Visual Inspection:** Always plot first!
2. **Calculate Means:** Get baseline understanding
3. **Least Squares:** Find best-fit line manually
4. **Interpret Coefficients:** What do slope/intercept mean biologically?
5. **Calculate R²:** How much variation explained?
6. **Residual Analysis:** Where does model fail?
7. **Make Predictions:** Test on new data
8. **Reality Check:** When does model break?

---

## Technical Notes

### Data Format
- All files are CSV (comma-separated values)
- Headers in first row
- No missing values
- Ready for Excel, R, Python, or manual calculation

### Units and Conventions
- **Currency:** Indian Rupees (₹)
- **Temperature:** Celsius (°C)
- **Distance:** Kilometers (km)
- **Time:** Minutes or hours (specified)
- **Day of Year:** 1 = January 1, 365 = December 31

### Recommended Tools
- **Spreadsheet:** Excel, Google Sheets (beginners)
- **Programming:** Python (pandas, numpy, matplotlib)
- **Statistics:** R, SPSS
- **Manual Calculation:** Possible for all datasets!

---

## Pedagogical Notes

### Why These Examples?

**1. Cultural Relevance:**
- Rajesh (tea stall) and Kamala (vegetable vendor) are relatable Indian contexts
- Babulal's traditional knowledge honors indigenous science
- Students see math in their daily lives

**2. Gradual Complexity:**
- Start with simple patterns (weekly sales)
- Build to regression (temperature-sales)
- Advance to multi-variable models (monsoon prediction)

**3. Real-World Messiness:**
- Data includes noise and outliers
- Models never fit perfectly
- Students learn "all models are wrong, but some are useful"

**4. Multiple Perspectives:**
- Business optimization (Rajesh, Kamala)
- Personal improvement (study habits, commute)
- Traditional knowledge (Babulal)
- Each shows modeling applies universally

### Common Student Challenges

**Challenge 1:** "Why doesn't R² = 1.0?"
- **Answer:** Real data has noise. Perfect fit would be overfitting.

**Challenge 2:** "The model predicts negative sales at 50°C!"
- **Answer:** Models have domains. Extrapolation fails. Teach limitations.

**Challenge 3:** "Traditional knowledge seems less precise than the model."
- **Answer:** Traditional knowledge includes qualitative factors models miss. Discuss complementarity.

**Challenge 4:** "I can't do least squares by hand!"
- **Answer:** Break into steps. Provide worked example. Use calculator.

---

## Connection to Book Content

### Direct Book Examples
- **Temperature-Sales:** Pages 74-75 (exact model shown)
- **Study Hours:** Pages 76-77 (exact model shown)
- **Rajesh's Business:** Pages 56-59 (narrative context)
- **Kamala's Pricing:** Pages 62-63 (optimization discussion)
- **Babulal's Prediction:** Pages 59-61 (traditional knowledge)

### Key Quotes to Remember
1. **"Mathematics is organized intuition"** (p. 65)
2. **"All models are wrong, but some are useful"** (p. 80 - Box's Law)
3. **"Making the invisible visible"** (p. 81)

### Learning Objectives Alignment
These datasets directly support Chapter 2's learning objectives:
- ✅ Transform intuitive observations into testable models
- ✅ Build simple mathematical relationships using least squares
- ✅ Distinguish useful simplifications from oversimplifications
- ✅ Apply the scientific pipeline from pattern to model refinement

---

## Dataset Quality and Validation

### Data Generation Method
- Datasets were created to match book examples exactly where applicable
- Other datasets designed to exhibit clear linear relationships
- Realistic noise levels added to avoid "too perfect" fits
- All values checked for biological/practical plausibility

### Expected R² Values
- **Temperature-Sales:** ~0.70 (strong negative correlation)
- **Study Hours:** ~0.98 (very strong positive correlation)
- **Monsoon Prediction (single variable):** ~0.60-0.75
- **Commute Optimizer:** ~0.80 (traffic has strong effect)

### Validation Checks Performed
✅ No impossible values (e.g., negative sales)  
✅ Ranges realistic for context  
✅ Relationships match expected biological/economic principles  
✅ Sufficient variation for interesting analysis  
✅ Not so perfect that students suspect fake data  

---

## Suggested Exercises by Difficulty

### ⭐ Beginner (First exposure to modeling)
- Problem 2A.1: Recognize weekly patterns
- Problem 2A.6: Understand optimization
- Focus on visual patterns and simple averages

### ⭐⭐ Intermediate (Learning regression)
- Problem 2A.2: Temperature-sales (THE core example)
- Problem 2A.3: Study hours (personal relevance)
- Problem 2A.4: Pricing optimization
- Focus on least squares calculation and interpretation

### ⭐⭐⭐ Advanced (Deeper understanding)
- Problem 2A.5: Multi-variable monsoon model
- Problem 2A.7: Model assumptions analysis
- Problem 2A.8: Residual analysis
- Problem 2A.9: Formalization theory
- Problem 2A.10: Student's own data collection
- Focus on limitations, validation, improvement

---

## Additional Resources

### Manual Calculation Guides
See individual problem solutions for step-by-step least squares calculations.

### Code Examples
Companion Python/R code provided separately showing:
- Data loading and visualization
- Least squares implementation from scratch
- Built-in function comparison
- Residual plotting
- R² calculation

### Assessment Rubrics
Solutions include:
- Calculation correctness (40%)
- Interpretation quality (30%)
- Biological reasoning (20%)
- Presentation clarity (10%)

---

## Citation

**Book Reference:**
Patel, A. (2025). *The Pattern Hunters: The Art of Scientific Thinking*. Chapter 2: From Guesswork to Models - The Art of Scientific Thinking, pp. 55-91.

**Dataset Citation:**
If using these datasets for teaching or publication:
> Patel, A. (2025). Chapter 2 Problem Set A Datasets. *The Pattern Hunters: Companion Materials*. Available at: github.com/The-Pattern-Hunter/pattern-hunters-problems

---

*Datasets created by Dr. Alok Patel*  
*For The Pattern Hunters: The Art of Scientific Thinking*  
*Chapter 2: From Guesswork to Models*
