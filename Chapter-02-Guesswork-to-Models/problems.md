# Chapter 2: From Guesswork to Models
## Set A: Core Problems

**Based on:** Rajesh's tea stall, least squares method, simple linear regression

**Learning Objectives:**
- Transform qualitative observations into quantitative models
- Apply least squares method to real-world data
- Build and interpret simple linear regression models
- Understand model assumptions and limitations
- Distinguish between useful simplifications and oversimplifications

---

## Problem 2A.1: Rajesh's Weekly Sales Pattern ⭐

**Context:** Rajesh tracks his tea stall sales for one complete week to understand customer patterns.

**Data (Daily Revenue in ₹):**
```
Day       | Mon | Tue | Wed | Thu | Fri | Sat | Sun
Revenue   | 420 | 480 | 510 | 490 | 550 | 380 | 340
Customers | 42  | 48  | 51  | 49  | 55  | 38  | 34
```

**Questions:**

a) **Pattern Recognition:** Describe the weekly pattern you observe. When are sales highest? Lowest? Why might this be?

b) **Calculate Averages:** 
   - What is the average daily revenue?
   - What is the average weekend (Sat-Sun) revenue?
   - What is the average weekday (Mon-Fri) revenue?
   - By what percentage do weekdays outperform weekends?

c) **Simple Prediction:** Based on this pattern, predict:
   - Next Monday's revenue
   - Next Saturday's revenue
   - Explain your reasoning

d) **Model Limitations:** What factors might make your predictions inaccurate?

---

## Problem 2A.2: Temperature and Tea Sales ⭐⭐

**Context:** Rajesh suspects temperature affects his sales. He collects data for 8 days.

**Data:**
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

**Questions:**

a) **Visual Assessment:** 
   - Plot Sales vs. Temperature (sketch by hand or describe the relationship)
   - Does there appear to be a relationship? Positive or negative?

b) **Least Squares Regression:** Calculate the best-fit line: Sales = a + b × Temperature
   - Calculate the mean temperature and mean sales
   - Calculate the slope (b)
   - Calculate the intercept (a)
   - Write the complete equation

c) **Interpret the Model:**
   - What does the slope tell Rajesh about his business?
   - For every 1°C increase in temperature, how do sales change?
   - What does the intercept represent? Is it meaningful?

d) **Make Predictions:**
   - If tomorrow's forecast is 32°C, predict the sales
   - If temperature is 40°C, predict the sales
   - Which prediction is more reliable? Why?

e) **Model Validation:**
   - Calculate predicted sales for each of the 8 days
   - Compare to actual sales
   - Calculate the average error (residuals)
   - Does the model work well?

---

## Problem 2A.3: Your Study Success Model ⭐⭐

**Context:** You want to understand how study time affects your test performance.

**Your Data (8 recent tests):**
```
Study Hours | Test Score
------------|------------
2           | 65
3           | 70
4           | 75
5           | 80
6           | 82
7           | 85
8           | 88
9           | 90
```

**Questions:**

a) **Calculate the Linear Model:** Score = a × Hours + b
   - Show all steps of the least squares calculation
   - Average hours = ?
   - Average score = ?
   - Slope = ?
   - Intercept = ?

b) **Biological/Practical Interpretation:**
   - For each additional hour studied, how many points do you gain?
   - What does the intercept represent? (Your baseline knowledge?)
   - Is this realistic?

c) **Test Your Model:**
   - You plan to study 10 hours for the next test. Predict your score.
   - Calculate predicted scores for all 8 tests
   - How well does the model fit? (Calculate R²)

d) **Reality Check:**
   - Does this model assume diminishing returns? Why or why not?
   - What factors does this model ignore?
   - When might this model fail?

e) **Design an Experiment:**
   - How would you test whether this model works for you?
   - What additional data should you collect?
   - What variables should you control?

---

## Problem 2A.4: Kamala's Vegetable Pricing ⭐⭐

**Context:** Kamala tracks tomato prices and sales throughout one market day.

**Data (Price changes during the day):**
```
Time of Day | Hour | Price (₹/kg) | Kg Sold | Revenue (₹)
------------|------|--------------|---------|-------------
Morning     | 8    | 40           | 25      | 1000
Mid-Morning | 10   | 38           | 30      | 1140
Noon        | 12   | 35           | 28      | 980
Afternoon   | 14   | 32           | 35      | 1120
Evening     | 16   | 28           | 40      | 1120
Late        | 18   | 20           | 30      | 600
```

**Questions:**

a) **Pattern Analysis:**
   - Describe how price and quantity sold change throughout the day
   - Calculate total revenue at each time point
   - When is revenue highest? When is it lowest?

b) **Build a Model:** Revenue = Price × Quantity
   - But quantity depends on price: Quantity = a + b × Price
   - Use least squares to find the relationship between Price and Quantity Sold
   - What does a negative slope mean here?

c) **Optimization Question:**
   - If Kamala starts with 100 kg of tomatoes, what pricing strategy maximizes revenue?
   - Should she keep high prices all day or drop them gradually?
   - What factors does this simple model ignore?

d) **Real-World Complications:**
   - What other factors affect Kamala's pricing decisions?
   - How does competition from nearby vendors matter?
   - How does tomato quality (freshness) change her strategy?

---

## Problem 2A.5: Babulal's Monsoon Prediction ⭐⭐⭐

**Context:** Babulal tracks environmental indicators to predict monsoon arrival.

**Data (10 years of observations):**
```
Year | Ant Depth (cm) | Mahua Flowering (Day) | Peacock Calls/Day | Monsoon Day of Year
-----|----------------|----------------------|-------------------|--------------------
2014 | 12             | 135                  | 8                 | 168
2015 | 15             | 130                  | 12                | 162
2016 | 10             | 140                  | 6                 | 175
2017 | 14             | 132                  | 11                | 164
2018 | 16             | 128                  | 14                | 160
2019 | 11             | 138                  | 7                 | 172
2020 | 13             | 134                  | 9                 | 166
2021 | 17             | 126                  | 15                | 158
2022 | 9              | 142                  | 5                 | 178
2023 | 14             | 133                  | 10                | 165
```

**Questions:**

a) **Single Variable Models:**
   - Build three separate models:
     * Monsoon Day = f(Ant Depth)
     * Monsoon Day = f(Mahua Flowering)
     * Monsoon Day = f(Peacock Calls)
   - Which single variable is the best predictor? (Calculate R² for each)

b) **Interpret Relationships:**
   - For each model, explain the biological reasoning
   - Why would deeper ant burrows predict earlier monsoons?
   - Why would earlier mahua flowering predict earlier monsoons?
   - What is the mechanism?

c) **Multi-Variable Model (Advanced):**
   - Propose: Monsoon Day = a + b₁(Ant Depth) + b₂(Mahua Day) + b₃(Peacock Calls)
   - What assumptions does this make?
   - Would combining all three improve predictions?

d) **Model Validation:**
   - Use data from 2014-2020 to build your best model
   - Test it on 2021-2023 data
   - How accurate were the predictions?
   - Calculate prediction error (actual - predicted)

e) **Traditional Knowledge vs. Scientific Models:**
   - Babulal achieves 80-85% accuracy. How does your model compare?
   - What does this tell you about traditional knowledge systems?
   - What advantages does a mathematical model provide?
   - What advantages does traditional knowledge provide?

---

## Problem 2A.6: The Commute Optimizer ⭐

**Context:** You track your daily commute time via different routes.

**Data (2 weeks of commuting):**
```
Day | Route         | Distance (km) | Traffic Level (1-10) | Time (min)
----|---------------|---------------|----------------------|-----------
Mon | NH16          | 12            | 8                    | 45
Tue | Janpath       | 10            | 6                    | 38
Wed | NH16          | 12            | 9                    | 50
Thu | Janpath       | 10            | 5                    | 32
Fri | Patrapada     | 11            | 7                    | 42
Mon | NH16          | 12            | 8                    | 46
Tue | Janpath       | 10            | 7                    | 40
Wed | Patrapada     | 11            | 6                    | 38
Thu | NH16          | 12            | 7                    | 43
Fri | Janpath       | 10            | 8                    | 44
```

**Questions:**

a) **Simple Model:** Time = Base_Time + Traffic_Effect
   - For each route, calculate average time at low traffic (1-5) vs high traffic (6-10)
   - How much does traffic add to commute time?

b) **Build Regression Model:**
   - Model: Time = a + b × Distance + c × Traffic
   - Should you include both variables? Why?

c) **Optimization:**
   - If traffic is heavy (level 8), which route is fastest?
   - If traffic is light (level 4), which route is fastest?
   - Create a decision rule for choosing routes

d) **Real-World Factors:**
   - What other factors affect commute time?
   - Road conditions? Weather? Time of day?
   - How would you improve this model?

---

## Problem 2A.7: Model Assumptions ⭐⭐

**Context:** Understanding when models work and when they fail.

Given the model from Problem 2A.2: **Sales = 1546 - 30.5 × Temperature**

**Questions:**

a) **Identify Assumptions:**
   - List 5 assumptions this model makes
   - Which assumptions are reasonable?
   - Which are problematic?

b) **When Will the Model Fail:**
   - Predict sales at 0°C using the model
   - Predict sales at 50°C using the model
   - Are these predictions realistic? Why not?

c) **Missing Variables:**
   - What important factors does the model not include?
   - Rain? Holidays? Day of week? Competition?
   - How would including these improve predictions?

d) **Model Improvement:**
   - Design a better model that includes weather type
   - Write the equation: Sales = f(Temperature, Rain, Cloudy)
   - What additional data would you need?

e) **Box's Law:**
   - "All models are wrong, but some are useful"
   - Explain this statement in the context of Rajesh's model
   - In what ways is the model "wrong"?
   - In what ways is it "useful"?

---

## Problem 2A.8: Residual Analysis ⭐⭐⭐

**Context:** Checking how well your model fits the data.

Use data from Problem 2A.2 (Temperature and Sales).

**Questions:**

a) **Calculate Residuals:**
   - For each of the 8 days, calculate: Residual = Actual - Predicted
   - Which days have largest positive residuals? (Model underestimates)
   - Which days have largest negative residuals? (Model overestimates)

b) **Pattern in Residuals:**
   - Plot residuals vs. temperature (or list them)
   - Is there a pattern? Or random scatter?
   - What does a pattern suggest?

c) **R² Calculation:**
   - Total variation: TSS = Σ(Actual - Mean)²
   - Explained variation: ESS = Σ(Predicted - Mean)²
   - Unexplained variation: RSS = Σ(Actual - Predicted)²
   - R² = ESS/TSS = 1 - RSS/TSS
   - What percentage of variation does temperature explain?

d) **Interpret R²:**
   - If R² = 0.70, what does this mean?
   - What causes the remaining 30% variation?
   - Is this a "good" model? How good is "good enough"?

e) **Improving the Model:**
   - Based on residual patterns, suggest improvements
   - What additional variables might help?
   - How would you test these improvements?

---

## Problem 2A.9: From Intuition to Mathematics ⭐

**Context:** Making implicit knowledge explicit.

**Scenario:** An experienced street food vendor can instantly estimate daily sales based on:
- Weather
- Day of week  
- Nearby events
- Time of year

**Questions:**

a) **Explicit Model:**
   - Write a mathematical equation that captures this vendor's intuition
   - Sales = f(Weather, Day, Events, Season)
   - Define each term explicitly

b) **Parameter Estimation:**
   - If you collected data, how would you estimate coefficients?
   - What data would you need?
   - How many days of observation?

c) **Advantages of Formalization:**
   - Why is a mathematical model better than intuition alone?
   - What can the model do that intuition can't?
   - What can intuition do that the model can't?

d) **Teaching and Transfer:**
   - Could the vendor teach someone using the mathematical model?
   - What is lost in translation from intuition to math?
   - What is gained?

---

## Problem 2A.10: Your Personal Model ⭐⭐

**Project:** Build a model of YOUR daily decision-making.

**Choose ONE behavior to track for 7 days:**
- Sleep time vs. next-day alertness
- Study time vs. understanding
- Exercise vs. mood
- Screen time vs. productivity
- Social time vs. happiness

**Questions:**

a) **Data Collection:**
   - Design a data collection sheet
   - What variables will you measure?
   - How will you quantify them?
   - What controls do you need?

b) **Build Your Model:**
   - After collecting data, use least squares to find relationship
   - Outcome = a + b × Predictor
   - Show all calculations

c) **Interpret YOUR Model:**
   - What does your slope mean?
   - Is the relationship strong? (R²)
   - What factors does the model miss?

d) **Test Predictions:**
   - Use your model to predict tomorrow's outcome
   - Did it work? Why or why not?
   - How would you improve the model?

e) **Reflection:**
   - Did the model reveal anything surprising?
   - Does quantifying behavior change behavior?
   - What did you learn about yourself?

---

## Coding Challenge C1: Least Squares from Scratch ⭐⭐

**Task:** Implement least squares regression without using libraries.

**Requirements:**
1. Write a function that takes x and y data
2. Calculate mean of x and y
3. Calculate slope and intercept
4. Return equation and R²
5. Plot data and fitted line

**Starter Template:**
```python
def least_squares(x, y):
    # Your implementation here
    # Calculate means
    # Calculate slope
    # Calculate intercept
    # Calculate R²
    return slope, intercept, r_squared

# Test on Rajesh's data
temperature = [35, 33, 30, 28, 36, 29, 26, 37]
sales = [450, 520, 580, 720, 480, 650, 780, 440]

slope, intercept, r2 = least_squares(temperature, sales)
print(f"Sales = {intercept:.2f} + {slope:.2f} × Temperature")
print(f"R² = {r2:.4f}")
```

---

## Coding Challenge C2: Interactive Model Explorer ⭐⭐⭐

**Task:** Create an interactive tool to explore model sensitivity.

**Requirements:**
1. Load data (e.g., temperature vs. sales)
2. Show scatter plot
3. Allow user to adjust slope and intercept manually (sliders)
4. Display RSS (residual sum of squares) in real-time
5. Show optimal values from least squares
6. Demonstrate why least squares minimizes RSS

**Bonus:**
- Add animation showing RSS changing as parameters adjust
- Show residual plot updating in real-time
- Compare manual fit vs. optimal fit

---

## Summary: Key Concepts Practiced

**Mathematical Skills:**
- ✅ Least squares method (calculating slope and intercept)
- ✅ Linear regression interpretation
- ✅ R² calculation and interpretation
- ✅ Residual analysis
- ✅ Prediction and validation

**Conceptual Understanding:**
- ✅ "All models are wrong, but some are useful"
- ✅ Model assumptions and limitations
- ✅ When models work vs. when they fail
- ✅ From intuition to mathematical precision
- ✅ Balancing simplicity and accuracy

**Real-World Applications:**
- ✅ Business optimization (Rajesh, Kamala)
- ✅ Personal decision-making (study time, commute)
- ✅ Traditional knowledge (Babulal's monsoon prediction)
- ✅ Data-driven planning

---

*Problems designed by Dr. Alok Patel for The Pattern Hunters*  
*Chapter 2: From Guesswork to Models*
