# Chapter 2: From Guesswork to Models
## The Art of Scientific Thinking: How Observation Becomes Mathematical Prediction

**Learning Objectives:**
- Transform qualitative observations into quantitative models
- Build predictive models from data
- Understand model assumptions and limitations
- Test model predictions against reality
- Distinguish between correlation and mechanism

---

## Problem 2.1: From Tea Stall to Model ⭐

**Context:** Rajesh notices that on rainy days, his tea stall gets fewer customers. He wants to create a simple model to predict daily sales.

**Data (customers per day):**
```
Day  | Weather | Customers | Temperature (°C)
-----|---------|-----------|----------------
Mon  | Sunny   | 68        | 28
Tue  | Cloudy  | 54        | 26
Wed  | Rainy   | 32        | 24
Thu  | Sunny   | 72        | 30
Fri  | Rainy   | 28        | 22
Sat  | Sunny   | 65        | 29
Sun  | Cloudy  | 48        | 25
```

**Questions:**

a) **Qualitative Observation:** Describe the pattern you observe in words (no numbers yet).

b) **Quantitative Model:** Create a simple mathematical model:
   - Calculate average customers for each weather type
   - Express as: Customers = f(Weather)

c) **Prediction:** Using your model, predict customers for:
   - Next rainy day
   - Next sunny day
   
d) **Model Testing:** If tomorrow is rainy and you get 35 customers, does this:
   - Confirm your model?
   - Refute your model?
   - Neither? Explain your reasoning.

e) **Model Improvement:** What additional variable(s) might improve your predictions?

---

## Problem 2.2: Rice Yield Model ⭐⭐

**Context:** A farmer in Punjab tracks rice yields over 8 years.

**Data:**
```
Year | Fertilizer (kg/hectare) | Rainfall (mm) | Yield (tonnes/hectare)
-----|-------------------------|---------------|----------------------
2016 | 100                     | 1200          | 3.2
2017 | 120                     | 1100          | 3.5
2018 | 110                     | 1300          | 3.8
2019 | 130                     | 900           | 3.1
2020 | 140                     | 1250          | 4.2
2021 | 125                     | 1150          | 3.7
2022 | 150                     | 1000          | 3.4
2023 | 135                     | 1300          | 4.0
```

**Questions:**

a) **Single Variable Model:**
   - Plot Yield vs. Fertilizer
   - Calculate correlation coefficient
   - Create linear regression: Yield = a + b(Fertilizer)

b) **Alternative Model:**
   - Plot Yield vs. Rainfall
   - Which variable (fertilizer or rainfall) is a better predictor? Why?

c) **Two-Variable Model:**
   - Hypothesize how both variables affect yield
   - Propose: Yield = a + b(Fertilizer) + c(Rainfall)
   - What biological assumptions does this make?

d) **Model Limitations:**
   - What's the maximum yield this model predicts? Is this realistic?
   - What factors are missing from this model?

e) **Prediction:**
   - For 2024: Fertilizer = 145 kg/ha, Rainfall = 1200 mm
   - Predict yield using your best model
   - Give a confidence range (±X tonnes)

---

## Problem 2.3: Mosquito Population Growth ⭐⭐

**Context:** A public health worker monitors mosquito populations near a village.

**Observation:** Population seems to double every 5 days when unconstrained.

**Questions:**

a) **Exponential Model:**
   - Starting population: 100 mosquitoes
   - Write exponential growth model: N(t) = N₀ × 2^(t/5)
   - Calculate population after 10, 15, 20 days

b) **Reality Check:**
   - After 30 days, your model predicts ___ mosquitoes
   - Is this realistic? Why or why not?

c) **Improved Model (Logistic Growth):**
   - Maximum capacity: 10,000 mosquitoes
   - Model: N(t) = K/(1 + ((K-N₀)/N₀)e^(-rt))
   - Where K = 10,000, N₀ = 100, r = 0.139 (daily growth rate)
   - Calculate N(30) using this model
   - Compare to exponential model

d) **Intervention Planning:**
   - Health workers can reduce population by 50% with spraying
   - When should they spray to keep population below 5,000?
   - Use your model to determine optimal intervention time

e) **Model Assumptions:**
   - List 3 assumptions in the logistic model
   - Which assumption is most likely violated in reality?

---

## Problem 2.4: Antibiotic Resistance Model ⭐⭐⭐

**Context:** A hospital tracks antibiotic resistance in bacterial infections.

**Observations:**
- 2018: 5% of infections resistant
- 2023: 18% of infections resistant
- Resistance spreads through both reproduction and horizontal gene transfer

**Questions:**

a) **Simple Linear Model:**
   - Calculate rate of increase: (18% - 5%) / 5 years = ?
   - Predict resistance in 2028, 2033
   - When will 50% be resistant?

b) **Exponential Model:**
   - Fit exponential: R(t) = R₀ × e^(kt)
   - Calculate k from data points
   - Predict 2028, 2033 values
   - Compare to linear model

c) **Logistic Model:**
   - Assume maximum resistance = 95% (never 100% due to fitness costs)
   - Fit logistic model to data
   - Predict 2028, 2033
   - When will 50% be reached?

d) **Model Comparison:**
   - Create table comparing all three models
   - Which is most realistic? Why?
   - What does each model assume about the biology?

e) **Intervention Modeling:**
   - New antibiotic stewardship program reduces spread by 40%
   - Modify your best model to include this intervention starting 2024
   - How does this change your predictions?

f) **Critical Analysis:**
   - What factors does your model ignore?
   - How might bacterial fitness costs affect long-term predictions?
   - Why might the logistic model's asymptote be wrong?

---

## Problem 2.5: Bird Migration Timing ⭐⭐

**Context:** Ornithologists study when Siberian cranes arrive at Bharatpur Bird Sanctuary.

**Data (arrival dates):**
```
Year | Day of Year | Average Temperature (°C) at departure
-----|-------------|-------------------------------------
2014 | 285         | 8.2
2015 | 290         | 10.1
2016 | 282         | 7.5
2017 | 288         | 9.3
2018 | 280         | 6.8
2019 | 292         | 10.8
2020 | 286         | 8.9
2021 | 279         | 6.2
2022 | 291         | 10.5
2023 | 283         | 7.8
```

**Questions:**

a) **Pattern Recognition:**
   - Is there a trend over years? (Climate change effect?)
   - Plot arrival day vs. departure temperature
   - Calculate correlation

b) **Temperature-Based Model:**
   - Create model: Arrival Day = a + b(Temperature)
   - Biological interpretation: What does the slope mean?

c) **Climate Change Scenario:**
   - Temperature increasing 0.2°C per year
   - Predict arrival dates for 2024-2030
   - What biological risks does earlier/later arrival pose?

d) **Model Testing:**
   - Use 2014-2020 data to build model
   - Test predictions against 2021-2023 actual data
   - Calculate prediction error
   - Is your model useful?

e) **Alternative Mechanism:**
   - Hypothesis: Day length (photoperiod) also matters
   - How would you test if photoperiod or temperature is more important?
   - Design an experiment to distinguish these mechanisms

---

## Problem 2.6: Predator-Prey Dynamics ⭐⭐⭐

**Context:** In Kanha National Park, researchers study chital deer (prey) and tiger (predator) populations.

**Simplified Lotka-Volterra Model:**
```
Prey change: dN/dt = rN - aNP
Predator change: dP/dt = baNP - mP

Where:
N = prey population
P = predator population  
r = prey growth rate = 0.5
a = predation rate = 0.02
b = conversion efficiency = 0.1
m = predator mortality = 0.2
```

**Initial Conditions:**
- N₀ = 1000 chital
- P₀ = 50 tigers

**Questions:**

a) **Equilibrium Analysis:**
   - Set dN/dt = 0 and dP/dt = 0
   - Solve for equilibrium values N* and P*
   - What do these represent biologically?

b) **Stability:**
   - If population is at equilibrium, and a disease kills 10 tigers, will populations:
     - Return to equilibrium?
     - Diverge to extinction?
     - Oscillate forever?
   - Explain using the model

c) **Parameter Sensitivity:**
   - If habitat loss reduces prey growth rate r to 0.3, how does equilibrium change?
   - Calculate new N* and P*
   - Management implication?

d) **Model Limitations:**
   - List 5 biological realities this model ignores
   - Which omission is most serious?
   - How would you improve the model?

e) **Conservation Application:**
   - Managers want tiger population ≥ 60
   - Using your model, what minimum prey population is needed?
   - What if predation becomes more efficient (a increases to 0.025)?

---

## Problem 2.7: Disease Outbreak Model ⭐⭐⭐

**Context:** COVID-like outbreak in a college of 5000 students.

**SIR Model:**
```
S = Susceptible
I = Infected
R = Recovered (immune)

dS/dt = -βSI/N
dI/dt = βSI/N - γI
dR/dt = γI

β = transmission rate = 0.5 per day
γ = recovery rate = 0.1 per day (average 10 days to recover)
N = 5000 (total population)
```

**Initial Conditions:**
- S₀ = 4990
- I₀ = 10
- R₀ = 0

**Questions:**

a) **Basic Reproduction Number (R₀):**
   - Calculate: R₀ = β/γ
   - Interpret: What does this value mean?
   - Will outbreak occur? (Hint: R₀ > 1 → outbreak)

b) **Peak Prediction:**
   - Maximum infected occurs when dI/dt = 0
   - At peak: S = γ/β
   - Calculate: How many infected at peak?
   - On approximately which day? (requires numerical solution or estimation)

c) **Intervention Strategies:**
   
   **Strategy 1: Reduce Contact (Lockdown)**
   - Reduces β to 0.3
   - Calculate new R₀
   - How does peak change?
   
   **Strategy 2: Faster Recovery (Treatment)**
   - Increases γ to 0.2
   - Calculate new R₀
   - How does peak change?
   
   **Strategy 3: Vaccination**
   - 30% vaccinated before outbreak (move to R)
   - New S₀ = 3493, R₀ = 1500
   - Will outbreak still occur?

d) **Herd Immunity:**
   - Threshold: 1 - (1/R₀)
   - Calculate % needed for herd immunity
   - Compare to vaccination strategy above

e) **Model Extensions:**
   - How would you modify the model for:
     * Asymptomatic carriers?
     * Loss of immunity over time?
     * Heterogeneous mixing (hostel vs day scholars)?

---

## Problem 2.8: Enzyme Kinetics Model ⭐⭐

**Context:** Studying digestive enzyme (amylase) that breaks down starch.

**Michaelis-Menten Model:**
```
v = (Vmax × [S]) / (Km + [S])

Where:
v = reaction velocity
[S] = substrate concentration
Vmax = maximum velocity
Km = Michaelis constant
```

**Experimental Data:**
```
[Substrate] (mM) | Velocity (μmol/min)
-----------------|--------------------
0.5              | 2.1
1.0              | 3.8
2.0              | 5.9
5.0              | 8.3
10.0             | 9.5
20.0             | 9.9
50.0             | 10.1
```

**Questions:**

a) **Parameter Estimation:**
   - Plot velocity vs. substrate concentration
   - Estimate Vmax from the plot (what value does v approach?)
   - Estimate Km (substrate concentration at v = Vmax/2)

b) **Model Fitting:**
   - Using your estimates, calculate predicted velocities
   - Compare to observed values
   - Calculate R² (goodness of fit)

c) **Biological Interpretation:**
   - What does Vmax represent physically?
   - What does Km tell you about enzyme-substrate affinity?
   - Lower Km = higher or lower affinity?

d) **Lineweaver-Burk Plot:**
   - Transform: 1/v = (Km/Vmax)(1/[S]) + 1/Vmax
   - This is linear! Calculate 1/v and 1/[S] for all points
   - Plot and determine Vmax and Km from intercepts

e) **Inhibitor Effect:**
   - Competitive inhibitor added, Km increases to 8 mM, Vmax unchanged
   - Calculate new velocities for same substrate concentrations
   - Why does competitive inhibition increase Km but not Vmax?

---

## Problem 2.9: Population Viability Analysis ⭐⭐⭐

**Context:** Asiatic lion population in Gir Forest, Gujarat.

**Current Status:**
- Population: 674 lions (2020 census)
- Growth rate: 5% per year when below carrying capacity
- Carrying capacity: 1400 lions
- Genetic diversity concerns due to small founder population

**Deterministic Model (No Random Events):**
```
N(t+1) = N(t) + rN(t)(1 - N(t)/K)

Where:
N(t) = population at time t
r = intrinsic growth rate = 0.05
K = carrying capacity = 1400
```

**Questions:**

a) **Baseline Projection:**
   - Project population for next 50 years
   - When will population reach 1000? 1400?
   - Create a population trajectory graph

b) **Catastrophic Events:**
   - Canine distemper virus (CDV) outbreak possible
   - Probability: 5% per year
   - Effect: 30% mortality if occurs
   - How does this change 50-year projections? (Hint: Run multiple scenarios)

c) **Minimum Viable Population (MVP):**
   - For genetic diversity, need ≥ 500 individuals
   - Calculate: Probability of dropping below 500 in 50 years
   - Consider both demographic stochasticity and catastrophes

d) **Management Strategies:**
   
   **Option 1: Habitat Expansion**
   - Increase K to 2000
   - Cost: ₹50 crores
   - Calculate long-term population benefit
   
   **Option 2: Translocation**
   - Move 50 lions to new site (Kuno National Park)
   - Reduces disease risk (two separate populations)
   - Model both populations separately
   - Calculate overall extinction risk reduction

e) **Genetic Concerns:**
   - Effective population size (Ne) ≈ 170 (much less than census size)
   - Minimum Ne for long-term viability: 500
   - Is translocation genetically beneficial?
   - What's the trade-off between demographic and genetic risks?

---

## Problem 2.10: Model Selection Challenge ⭐⭐⭐

**Context:** You have data on tree growth in Western Ghats.

**Data: Tree Height (meters) vs. Age (years)**
```
Age | Height | Notes
----|--------|------
5   | 2.1    | Seedling/sapling phase
10  | 5.8    | Rapid juvenile growth
15  | 11.2   | 
20  | 16.5   | 
25  | 20.8   | Growth slowing
30  | 23.9   | 
35  | 26.1   | Approaching maturity
40  | 27.8   | 
45  | 28.9   | Near maximum height
50  | 29.5   | Mature tree
```

**Candidate Models:**

**Model 1: Linear**
```
H = a + bt
```

**Model 2: Exponential**
```
H = H₀e^(kt)
```

**Model 3: Logistic**
```
H = Hmax / (1 + e^(-k(t-t₀)))
```

**Model 4: Power Law**
```
H = at^b
```

**Questions:**

a) **Visual Assessment:**
   - Plot the data
   - Which model(s) seem visually appropriate?
   - Which can you immediately rule out? Why?

b) **Fit All Models:**
   - For each model, estimate parameters
   - Calculate R² for each
   - Calculate residual sum of squares (RSS)

c) **Biological Plausibility:**
   - For each model, extrapolate to age 100
   - Which predictions are biologically realistic?
   - Which models have unrealistic asymptotic behavior?

d) **AIC (Akaike Information Criterion):**
   - Calculate: AIC = 2k + n·ln(RSS/n)
   - Where k = number of parameters, n = number of data points
   - Which model has lowest AIC?
   - Why does AIC penalize complexity?

e) **Prediction Uncertainty:**
   - Using your best model, predict height at age 60
   - Give 95% confidence interval
   - What biological factors create uncertainty?

f) **Model Purpose:**
   - If goal is: "Interpolate missing ages" → which model?
   - If goal is: "Predict very old trees" → which model?
   - If goal is: "Understand growth physiology" → which model?
   - Explain why purpose matters for model selection

---

## Coding Challenge C1: Temperature-Sales Model ⭐

**Task:** Build an interactive model explorer for Rajesh's tea stall.

**Requirements:**
1. Load temperature-sales data
2. Fit linear regression
3. Plot with confidence intervals
4. Allow user to input temperature and predict sales
5. Visualize residuals

**Starter Code:**
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# TODO: Load data
# TODO: Perform regression
# TODO: Create interactive prediction
# TODO: Plot results with confidence bands
```

---

## Coding Challenge C2: SIR Disease Model Simulator ⭐⭐

**Task:** Create interactive SIR model with intervention options.

**Requirements:**
1. Implement SIR differential equations
2. Numerical solver (Euler method or scipy.odeint)
3. Plot S, I, R curves over time
4. Interactive sliders for β, γ, vaccination %
5. Display R₀, peak infections, total infected

**Starter Code:**
```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

def sir_model(y, t, beta, gamma, N):
    S, I, R = y
    dS = -beta * S * I / N
    dI = beta * S * I / N - gamma * I
    dR = gamma * I
    return [dS, dI, dI]

# TODO: Implement solver and visualization
# TODO: Add interactive controls
```

---

## Coding Challenge C3: Model Comparison Tool ⭐⭐⭐

**Task:** Compare multiple growth models on same dataset.

**Requirements:**
1. Implement: Linear, Exponential, Logistic, Power law models
2. Fit all to data
3. Calculate: R², AIC, prediction intervals
4. Create comparison table
5. Visualize all models with data on one plot

**Bonus:**
- Cross-validation (fit on subset, test on holdout)
- Bootstrap confidence intervals
- Residual analysis plots

---

## Summary: Key Concepts

### Model Building Process
1. **Observe** → Identify patterns
2. **Hypothesize** → Propose mechanism
3. **Formalize** → Write equations
4. **Parameterize** → Fit to data
5. **Validate** → Test predictions
6. **Refine** → Improve based on failures

### Model Types Covered
- **Linear Models:** Simplest, limited scope
- **Exponential Models:** Unbounded growth/decay
- **Logistic Models:** Growth with limits
- **Mechanistic Models:** Based on biological processes (SIR, Lotka-Volterra)
- **Empirical Models:** Fitted to data (Michaelis-Menten)

### Critical Questions for Any Model
1. What assumptions does it make?
2. What does it ignore?
3. When will it fail?
4. How sensitive to parameters?
5. Can predictions be tested?

### Remember
- **All models are wrong, but some are useful** (George Box)
- Simple models often more reliable than complex ones
- Models are tools for thinking, not truth
- Uncertainty is information, not failure
- Best model depends on your question

---

## Additional Resources

**Datasets for Practice:**
- `chapter_02_rice_yields.csv`
- `chapter_02_mosquito_population.csv`
- `chapter_02_bird_migration.csv`
- `chapter_02_enzyme_kinetics.csv`
- `chapter_02_tree_growth.csv`

**Python Notebooks:**
- `02_linear_regression_tutorial.ipynb`
- `02_sir_model_exploration.ipynb`
- `02_model_comparison_guide.ipynb`

**Further Reading:**
- Otto & Day (2007). *A Biologist's Guide to Mathematical Modeling*
- Ellner & Guckenheimer (2006). *Dynamic Models in Biology*
- Bolker (2008). *Ecological Models and Data in R*

---

*Problems designed by Dr. Alok Patel*  
*For The Pattern Hunters: The Art of Scientific Thinking*  
*Chapter 2: From Guesswork to Models*
