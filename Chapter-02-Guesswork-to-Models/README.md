# Chapter 2 - Datasets
## From Guesswork to Models: The Art of Scientific Thinking

This folder contains all datasets used in Chapter 2 problems and solutions.

---

## 📁 Dataset Collections

Chapter 2 provides **two complementary sets** of datasets for different learning stages:

### **Core Examples** (Follow chapter narrative)
Simple, hand-calculable datasets that build modeling intuition through Rajesh's tea stall and Kamala's vegetable pricing stories.

### **Extended Applications** (Apply to biology)
Realistic biological datasets for independent practice applying modeling techniques to real-world problems.

---

## 📊 Core Example Datasets

These directly support the chapter narrative and can be calculated by hand.

| File | Rows | Used In | Context |
|------|------|---------|---------|
| `rajesh_weekly_sales.csv` | 7 | Problem 2.1 | Temperature vs sales (first model) |
| `study_scores.csv` | 7 | Problem 2.2 | Study hours vs test scores |
| `rajesh_two_weeks.csv` | 14 | Problem 2.3 | Extended least squares |
| `kamala_pricing.csv` | 5 | Problem 2.4 | Optimization problem |
| `rajesh_week3_validation.csv` | 7 | Problem 2.5 | Model validation |
| `rajesh_complete_data.csv` | 20 | Problem 2.6 | Multi-variable modeling |

**Start here** if you're new to mathematical modeling!

---

## 🔬 Extended Biological Datasets

Apply chapter concepts to real biological systems with realistic complexity.

| # | File | Rows | Application | Model Type |
|---|------|------|-------------|------------|
| 1 | `chapter_02_rice_yields.csv` | 8 | Agriculture | Multi-variable regression |
| 2 | `chapter_02_mosquito_population.csv` | 36 | Public health | Exponential/Logistic growth |
| 3 | `chapter_02_bird_migration.csv` | 10 | Climate change | Temperature trends |
| 4 | `chapter_02_enzyme_kinetics.csv` | 21 | Biochemistry | Michaelis-Menten |
| 5 | `chapter_02_tree_growth.csv` | 10 | Ecology | Model selection |
| 6 | `chapter_02_tea_stall_weather.csv` | 14 | Business | Categorical regression |
| 7 | `chapter_02_antibiotic_resistance.csv` | 6 | Medicine | Epidemiological trends |
| 8 | `chapter_02_predator_prey_timeseries.csv` | 24 | Conservation | Population dynamics |
| 9 | `chapter_02_asiatic_lion_population.csv` | 14 | Conservation | Population viability |
| 10 | `chapter_02_sir_outbreak_example.csv` | 31 | Public health | Disease modeling |

---

## 📖 Detailed Dataset Descriptions

### Core Example Datasets

#### 1. `rajesh_weekly_sales.csv`

**Description:** Rajesh's tea stall sales for one week (Chapter opening example)

**Columns:**
- `Day` (string): Day of week (Mon, Tue, Wed, Thu, Fri, Sat, Sun)
- `Temperature` (float): Daily temperature in °C
- `Sales` (int): Daily sales in rupees (₹)

**Sample Data:**
```csv
Day,Temperature,Sales
Mon,35,450
Tue,33,520
Wed,30,580
```

**Use Case:** Building your first linear model, understanding slope and intercept, negative correlation

**Key Pattern:** As temperature increases, sales decrease (people drink less hot tea)

---

#### 2. `study_scores.csv`

**Description:** Student study hours and corresponding test scores

**Columns:**
- `StudyHours` (int): Hours studied before test
- `TestScore` (int): Score achieved (out of 100)

**Sample Data:**
```csv
StudyHours,TestScore
2,65
3,70
4,75
```

**Use Case:** Personal application of modeling, understanding model interpretation

**Key Pattern:** Linear relationship with diminishing returns at high study hours

---

#### 3. `rajesh_two_weeks.csv`

**Description:** Extended dataset combining Week 1 and Week 2 for more robust fitting

**Columns:**
- `Day` (string): Day identifier (W1-Mon, W1-Tue, ..., W2-Mon, ...)
- `Temperature` (float): Daily temperature in °C
- `Sales` (int): Daily sales in rupees (₹)

**Use Case:** Demonstrating how more data improves model reliability

---

#### 4. `kamala_pricing.csv`

**Description:** Kamala's vegetable pricing strategy throughout the day

**Columns:**
- `Time` (string): Time of day (7 AM, 10 AM, 1 PM, 4 PM, 7 PM)
- `Price` (int): Price per kg in rupees (₹/kg)
- `DemandFactor` (float): Customer demand multiplier
- `QualityFactor` (float): Freshness/quality factor

**Sample Data:**
```csv
Time,Price,DemandFactor,QualityFactor
7 AM,40,1.2,1.0
10 AM,38,1.0,0.95
1 PM,35,1.0,0.9
```

**Use Case:** Multi-factor optimization, business decision modeling

---

#### 5. `rajesh_week3_validation.csv`

**Description:** Week 3 data for model validation and error analysis

**Columns:**
- `Day` (string): Day of week
- `Temperature` (float): Daily temperature in °C
- `ActualSales` (int): Actual sales in rupees (₹)
- `Weather` (string): Weather condition (Sunny, Cloudy, Light Rain, Heavy Rain)

**Use Case:** Testing predictions, residual analysis, discovering model limitations

---

#### 6. `rajesh_complete_data.csv`

**Description:** Complete 20-day dataset with all variables for comprehensive modeling

**Columns:**
- `Day` (int): Day number (1-20)
- `Temperature` (float): Daily temperature in °C
- `DayOfWeek` (int): Day of week (1=Monday, 7=Sunday)
- `Weather` (int): Weather code (0=Sunny, 1=Cloudy, 2=Rainy)
- `Sales` (int): Daily sales in rupees (₹)

**Use Case:** Comparing simple vs. multi-variable models, feature importance

---

### Extended Biological Datasets

#### 1. `chapter_02_rice_yields.csv`

**Problem:** Rice Yield Model  
**Rows:** 8 (years 2016-2023)  
**Columns:** 4

**Variables:**
- `Year`: Year of observation
- `Fertilizer_kg_per_hectare`: Fertilizer application rate (kg/ha)
- `Rainfall_mm`: Total seasonal rainfall (mm)
- `Yield_tonnes_per_hectare`: Rice yield (tonnes/ha)

**Usage:** Multi-variable regression, model comparison, agricultural optimization

**Source:** Based on typical Punjab rice farming patterns

**Key Question:** How do fertilizer and rainfall interact to determine yield?

---

#### 2. `chapter_02_mosquito_population.csv`

**Problem:** Population Growth Modeling  
**Rows:** 36 (daily observations)  
**Columns:** 8

**Variables:**
- `Day`: Day number (0-35)
- `Population_Count`: Estimated mosquito count
- `Weather`: Weather condition
- `Temperature_C`: Daily temperature (°C)
- `Humidity_Percent`: Relative humidity (%)
- `Notes`: Observation notes

**Usage:** Exponential vs. logistic growth comparison, carrying capacity identification, intervention timing

**Pattern:** Clear transition from exponential (days 0-15) to logistic growth (days 15-35)

**Key Question:** When does exponential growth break down and why?

---

#### 3. `chapter_02_bird_migration.csv`

**Problem:** Climate Change Phenology  
**Rows:** 10 (years 2014-2023)  
**Columns:** 8

**Variables:**
- `Year`: Year of observation
- `Arrival_Day_of_Year`: Day when first birds arrive (1-365)
- `Arrival_Date`: Actual calendar date
- `Departure_Temperature_C`: Temperature at departure location (°C)
- `Departure_Location_Latitude`: Latitude of departure site
- `Flight_Duration_Days`: Migration duration (days)
- `Number_of_Birds`: Flock size
- `Weather_Conditions`: Weather during migration

**Species:** Siberian Crane (*Leucogeranus leucogeranus*) migrating to Bharatpur Bird Sanctuary

**Usage:** Temperature-phenology relationships, climate trend analysis, prediction of future arrival dates

**Key Question:** How is climate change affecting migration timing?

---

#### 4. `chapter_02_enzyme_kinetics.csv`

**Problem:** Michaelis-Menten Model  
**Rows:** 21 (7 concentrations × 3 replicates)  
**Columns:** 6

**Variables:**
- `Substrate_Concentration_mM`: Substrate concentration (mM)
- `Velocity_umol_per_min`: Reaction velocity (μmol/min)
- `Replicate`: Replicate number (1-3)
- `Temperature_C`: Reaction temperature (37°C)
- `pH`: Reaction pH (7.0)
- `Enzyme_Concentration_ug_per_mL`: Enzyme concentration (μg/mL)

**Enzyme:** Amylase (digestive enzyme that breaks down starch)

**Usage:** Non-linear curve fitting, Vmax and Km estimation, Lineweaver-Burk transformation

**Expected Parameters:** Vmax ≈ 10.1 μmol/min, Km ≈ 2.0 mM

**Key Question:** How does substrate concentration affect reaction rate?

---

#### 5. `chapter_02_tree_growth.csv`

**Problem:** Model Selection Challenge  
**Rows:** 10 (ages 5-50 years)  
**Columns:** 7

**Variables:**
- `Age_years`: Tree age (years)
- `Height_meters`: Tree height (m)
- `DBH_cm`: Diameter at breast height (cm)
- `Crown_Width_m`: Crown width (m)
- `Location`: Plot location in Western Ghats
- `Species`: *Tectona grandis* (Teak)
- `Health_Status`: Tree health assessment

**Usage:** Compare linear, exponential, logistic, and power law models; AIC-based model selection

**Pattern:** Clear logistic growth with asymptote near 30 meters

**Key Question:** Which mathematical model best describes tree growth?

---

#### 6. `chapter_02_tea_stall_weather.csv`

**Problem:** Categorical Predictors  
**Rows:** 14 (2 weeks)  
**Columns:** 8

**Variables:**
- `Day`: Day number
- `Day_of_Week`: Weekday name
- `Weather`: Weather condition (Sunny/Cloudy/Rainy)
- `Customers`: Number of customers
- `Temperature_C`: Temperature (°C)
- `Rainfall_mm`: Rainfall amount (mm)
- `Holiday`: Yes/No
- `Time_Open_Hours`: Hours stall was open

**Usage:** Handling categorical variables, multiple predictor types, business optimization

**Pattern:** Weather categories have strong effects beyond just temperature

---

#### 7. `chapter_02_antibiotic_resistance.csv`

**Problem:** Epidemiological Modeling  
**Rows:** 6 (years 2018-2023)  
**Columns:** 8

**Variables:**
- `Year`: Year
- `Resistant_Percentage`: % of resistant infections
- `Total_Infections_Tested`: Sample size
- `Resistant_Cases`: Absolute number of resistant cases
- `Antibiotic_Usage_DDD_per_1000`: Antibiotic usage metric
- `Hospital_Beds`: Number of hospital beds
- `ICU_Beds`: Number of ICU beds
- `Notes`: Context information

**Usage:** Model comparison (linear vs. exponential vs. logistic), intervention effect analysis

**Pattern:** Accelerating resistance through 2021, intervention effect visible 2022+

**Key Question:** Which model best predicts future resistance trends?

---

#### 8. `chapter_02_predator_prey_timeseries.csv`

**Problem:** Population Dynamics  
**Rows:** 24 (quarterly 2018-2023)  
**Columns:** 8

**Variables:**
- `Year`, `Month`: Time identifiers
- `Chital_Count`: Chital/spotted deer population (prey)
- `Tiger_Count`: Tiger population (predator)
- `Habitat_Quality_Index`: Habitat quality (0-1)
- `Rainfall_mm`: Quarterly rainfall
- `Poaching_Incidents`: Poaching events
- `Tourist_Visits`: Tourism pressure

**Location:** Kanha National Park, Madhya Pradesh

**Usage:** Lotka-Volterra dynamics, equilibrium analysis, parameter estimation

**Pattern:** Oscillating populations with predator lagging prey by ~1 quarter

---

#### 9. `chapter_02_asiatic_lion_population.csv`

**Problem:** Population Viability Analysis  
**Rows:** 14 (years 2010-2023)  
**Columns:** 13

**Variables:**
- `Year`: Year
- `Total_Population`: Total census count
- `Males`, `Females`, `Cubs`: Demographic breakdown
- `Sub_Adults`, `Adults`: Age structure
- `Territory_km2`: Protected area size (1412 km²)
- `Genetic_Diversity_He`: Expected heterozygosity
- `Effective_Population_Size`: Ne (genetic)
- `Mortality_Events`: Number of deaths
- `Disease_Outbreaks`: Disease events
- `Human_Conflict_Deaths`: Human-wildlife conflict

**Location:** Gir Forest National Park, Gujarat

**Usage:** PVA modeling, stochastic projection, genetic diversity assessment, extinction risk

**Pattern:** Steady population growth but declining genetic diversity

**Key Question:** Can the population persist long-term given genetic constraints?

---

#### 10. `chapter_02_sir_outbreak_example.csv`

**Problem:** Disease Outbreak Modeling  
**Rows:** 31 (days 0-30)  
**Columns:** 8

**Variables:**
- `Day`: Day of outbreak
- `Susceptible`, `Infected`, `Recovered`: SIR compartments
- `New_Cases`: Daily new infections
- `Cumulative_Cases`: Total cases
- `R_effective`: Time-varying reproduction number
- `Intervention_Active`: Whether control measures active

**Parameters:** β = 0.5/day (baseline), γ = 0.1/day, N = 5000 students

**Usage:** SIR model validation, R₀ calculation, intervention effect analysis

**Pattern:** Intervention on day 10 flattens curve, R_effective drops below 1

**Key Question:** How effective are different intervention strategies?

---

## 🔍 Data Characteristics

### Temperature Range (Tea Stall Data)
- **Minimum:** 25°C (cool monsoon day)
- **Maximum:** 38°C (peak summer)
- **Mean:** ~31°C
- **Context:** Typical Odisha summer temperatures

### Sales Patterns
- **Minimum:** ₹326 (very hot day, 40°C)
- **Maximum:** ₹784 (cool rainy day, 25°C)
- **Mean:** ~₹594
- **Correlation:** Strong negative with temperature (r ≈ -0.85)

### Weather Distribution
- **Sunny:** ~50% (Weather = 0)
- **Cloudy:** ~30% (Weather = 1)
- **Rainy:** ~20% (Weather = 2)

### Day of Week Effects
- **Weekdays:** Variable, work-pattern driven
- **Saturday:** Higher (market day effect)
- **Sunday:** Highest (leisure time)

---

## 💾 Loading Data

### Python (Pandas - Recommended)

```python
import pandas as pd

# Load dataset
df = pd.read_csv('chapter_02_rice_yields.csv')

# View first rows
print(df.head())

# Access columns
fertilizer = df['Fertilizer_kg_per_hectare']
yields = df['Yield_tonnes_per_hectare']

# Basic statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())
```

### Python (NumPy - For arrays)

```python
import numpy as np

# Load data (skip header)
data = np.loadtxt('chapter_02_rice_yields.csv', 
                  delimiter=',', 
                  skiprows=1,
                  usecols=(1, 3))  # Fertilizer and Yield

fertilizer = data[:, 0]
yields = data[:, 1]
```

### R

```r
# Load dataset
df <- read.csv('chapter_02_rice_yields.csv')

# View structure
str(df)
head(df)
summary(df)

# Access columns
fertilizer <- df$Fertilizer_kg_per_hectare
yields <- df$Yield_tonnes_per_hectare

# Check for NAs
sum(is.na(df))
```

---

## 📈 Quick Visualization Examples

### Python

```python
import matplotlib.pyplot as plt

# Simple scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Fertilizer_kg_per_hectare'], 
            df['Yield_tonnes_per_hectare'],
            s=100, alpha=0.6, edgecolors='black')
plt.xlabel('Fertilizer (kg/ha)', fontsize=12)
plt.ylabel('Yield (tonnes/ha)', fontsize=12)
plt.title('Rice Yield vs Fertilizer Application', fontsize=14)
plt.grid(True, alpha=0.3)
plt.show()

# Multiple subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Fertilizer effect
axes[0].scatter(df['Fertilizer_kg_per_hectare'], df['Yield_tonnes_per_hectare'])
axes[0].set_title('Fertilizer Effect')
axes[0].set_xlabel('Fertilizer (kg/ha)')
axes[0].set_ylabel('Yield (tonnes/ha)')

# Rainfall effect
axes[1].scatter(df['Rainfall_mm'], df['Yield_tonnes_per_hectare'], color='blue')
axes[1].set_title('Rainfall Effect')
axes[1].set_xlabel('Rainfall (mm)')
axes[1].set_ylabel('Yield (tonnes/ha)')

plt.tight_layout()
plt.show()
```

### R

```r
# Simple scatter plot
plot(df$Fertilizer_kg_per_hectare, df$Yield_tonnes_per_hectare,
     xlab = "Fertilizer (kg/ha)",
     ylab = "Yield (tonnes/ha)",
     main = "Rice Yield vs Fertilizer",
     pch = 19, col = "darkgreen", cex = 1.5)
grid()

# Add trend line
abline(lm(Yield_tonnes_per_hectare ~ Fertilizer_kg_per_hectare, data = df),
       col = "red", lwd = 2, lty = 2)
```

---

## 🔧 Data Preprocessing Tips

### Handle Missing Values

```python
# Check for missing values
print(df.isnull().sum())

# Drop rows with any missing values
df_clean = df.dropna()

# Fill missing values with mean
df['Sales'].fillna(df['Sales'].mean(), inplace=True)

# Fill with forward fill (time series)
df['Sales'].fillna(method='ffill', inplace=True)
```

### Normalize/Standardize Data

```python
from sklearn.preprocessing import StandardScaler

# Standardize (mean=0, std=1)
scaler = StandardScaler()
df['Temperature_normalized'] = scaler.fit_transform(df[['Temperature']])

# Min-max scaling (0-1 range)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df['Temperature_scaled'] = scaler.fit_transform(df[['Temperature']])
```

### Create Derived Features

```python
# Temperature categories
df['TempCategory'] = pd.cut(df['Temperature'], 
                             bins=[0, 28, 33, 40],
                             labels=['Cool', 'Moderate', 'Hot'])

# Sales performance categories
df['Performance'] = pd.cut(df['Sales'],
                            bins=[0, 500, 650, 1000],
                            labels=['Low', 'Medium', 'High'])

# Interaction term
df['Temp_x_Weather'] = df['Temperature'] * df['Weather']
```

---

## 🧪 Data Validation

### Statistical Checks

```python
# Check correlations
corr_matrix = df[['Temperature', 'Sales', 'Rainfall_mm']].corr()
print(corr_matrix)

# Temperature should negatively correlate with sales
assert df['Temperature'].corr(df['Sales']) < 0, "Expected negative correlation"

# Check variance
print(f"Temperature variance: {df['Temperature'].var():.2f}")
print(f"Sales variance: {df['Sales'].var():.2f}")
```

### Data Integrity Checks

```python
# Realistic ranges
assert df['Temperature'].min() >= 20, "Temperature too low!"
assert df['Temperature'].max() <= 45, "Temperature too high!"

# Positive values
assert (df['Sales'] > 0).all(), "Sales must be positive!"

# No duplicates
assert df.duplicated().sum() == 0, "Duplicate rows found!"

# Correct data types
assert df['Temperature'].dtype in ['float64', 'int64']
assert df['Day'].dtype == 'object'  # String
```

---

## 📚 Problem-Dataset Mapping

### Core Examples

| Problem | Dataset | Focus | Difficulty |
|---------|---------|-------|-----------|
| 2.1 | rajesh_weekly_sales | First linear model | ⭐ Easy |
| 2.2 | study_scores | Personal application | ⭐ Easy |
| 2.3 | rajesh_two_weeks | Least squares calculation | ⭐⭐ Medium |
| 2.4 | kamala_pricing | Multi-factor optimization | ⭐⭐ Medium |
| 2.5 | rajesh_week3_validation | Model validation | ⭐⭐ Medium |
| 2.6 | rajesh_complete_data | Model comparison | ⭐⭐⭐ Hard |

### Extended Biological Applications

| Problem | Dataset | Model Type | Difficulty |
|---------|---------|-----------|-----------|
| 2.1 | tea_stall_weather | Categorical regression | ⭐ Easy |
| 2.2 | rice_yields | Multiple regression | ⭐⭐ Medium |
| 2.3 | mosquito_population | Exponential/Logistic | ⭐⭐ Medium |
| 2.4 | antibiotic_resistance | Model comparison | ⭐⭐⭐ Hard |
| 2.5 | bird_migration | Climate trends | ⭐⭐ Medium |
| 2.6 | predator_prey_timeseries | Lotka-Volterra | ⭐⭐⭐ Hard |
| 2.7 | sir_outbreak_example | SIR disease model | ⭐⭐⭐ Hard |
| 2.8 | enzyme_kinetics | Michaelis-Menten | ⭐⭐ Medium |
| 2.9 | asiatic_lion_population | Population viability | ⭐⭐⭐ Hard |
| 2.10 | tree_growth | Model selection | ⭐⭐⭐ Hard |

---

## 🎓 Learning Pathway

### **Beginner** (Week 1-2)
1. ✅ Start with `rajesh_weekly_sales.csv`
2. ✅ Calculate slope and intercept by hand
3. ✅ Understand model interpretation
4. ✅ Try `study_scores.csv` for personal connection
5. ✅ Move to `rajesh_two_weeks.csv` for validation

### **Intermediate** (Week 3-4)
1. ✅ Master core examples (all 6 files)
2. ✅ Try 2-3 biological datasets (rice, mosquito, bird)
3. ✅ Compare different model types
4. ✅ Practice biological interpretation

### **Advanced** (Week 5+)
1. ✅ Complete all extended biological datasets
2. ✅ Perform rigorous model comparison
3. ✅ Collect and model your own data
4. ✅ Write formal methods and results

---

## 📋 Creating Your Own Dataset

### Template Structure

```csv
Variable1,Variable2,Variable3
value1_1,value1_2,value1_3
value2_1,value2_2,value2_3
...
```

### Example: Generate Synthetic Data

```python
import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate data
n = 20
temperature = np.random.uniform(25, 38, n)
sales = 1550 - 30*temperature + np.random.normal(0, 20, n)

# Create DataFrame
df = pd.DataFrame({
    'Day': range(1, n+1),
    'Temperature': temperature.round(1),
    'Sales': sales.astype(int)
})

# Save
df.to_csv('my_tea_stall_data.csv', index=False)
print("Custom dataset created!")
```

---

## ⚠️ Data Usage Notes

### Academic Use
✅ **Free** for educational purposes  
✅ **Cite as:** Patel, A. (2026). *The Pattern Hunters* - Chapter 2 Datasets  
✅ **Modify** for your own exercises  
✅ **Share** with proper attribution

### Limitations
- Core datasets simplified for pedagogy
- Extended datasets simulated (not actual field data)
- Some values rounded for clarity
- Weather categories simplified

### Real-World Application
When working with real data:
- Collect 50+ data points when possible
- Include measurement errors
- Document data collection methods
- Account for confounding variables
- Validate models with holdout data

---

## 🔗 Additional Resources

### Code Examples
- `Chapter_02_Examples.ipynb` - Worked examples with all datasets
- `least_squares_demo.py` - Step-by-step least squares calculation
- `model_comparison.py` - Comparing different model types

### Related Documentation
- `solutions.md` - Detailed solutions for all problems
- `data_dictionary.md` - Complete variable definitions
- `Chapter_02_Dataset_Guide.md` - Comprehensive usage guide

### External Resources
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [R for Data Science](https://r4ds.had.co.nz/)

---

## 🤝 Contributing

Have suggestions or found issues?
1. Open an issue on GitHub
2. Submit a pull request
3. Join the discussion forum

Want to contribute your own biological dataset?
1. Follow our dataset structure
2. Include comprehensive documentation
3. Provide example analysis code
4. Submit for review

---

## 📧 Questions?

- **GitHub Issues:** Technical problems or bugs
- **Discussions:** General questions about usage
- **Email:** Contact author for other inquiries

---

## 📜 License

All datasets provided under **MIT License** for educational use.

See [LICENSE](../../LICENSE) for full details.

---

## 🙏 Acknowledgments

Datasets inspired by:
- Real tea stall observations in Bhubaneswar
- Published ecological and epidemiological studies
- Agricultural research from Punjab and Odisha
- Conservation data from Indian national parks

Special thanks to students and educators who provided feedback during development.

---

**Back to:** [Chapter 2 Home](../../README.md) | [Repository Home](../../../../README.md)

---

*Last Updated: January 2026*  
*Version: 2.0*  
*Datasets: 16 files (6 core + 10 extended)*
