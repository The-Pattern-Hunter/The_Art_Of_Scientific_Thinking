# Chapter 2 Datasets
## From Guesswork to Models

This folder contains all CSV datasets for Chapter 2 practice problems.

---

## Dataset Descriptions

### 1. `chapter_02_rice_yields.csv`
**Problem:** 2.2 - Rice Yield Model  
**Rows:** 8 (2016-2023)  
**Columns:** 4

**Variables:**
- `Year`: Year of observation
- `Fertilizer_kg_per_hectare`: Fertilizer application rate (kg/ha)
- `Rainfall_mm`: Total seasonal rainfall (mm)
- `Yield_tonnes_per_hectare`: Rice yield (tonnes/ha)

**Usage:** Multi-variable regression, model comparison, prediction

**Source:** Simulated data based on typical Punjab rice farming patterns

---

### 2. `chapter_02_mosquito_population.csv`
**Problem:** 2.3 - Mosquito Population Growth  
**Rows:** 36 (daily observations)  
**Columns:** 8

**Variables:**
- `Day`: Day number (0-35)
- `Population_Count`: Estimated mosquito count
- `Weather`: Weather condition
- `Temperature_C`: Daily temperature (°C)
- `Humidity_Percent`: Relative humidity (%)
- `Notes`: Observation notes

**Usage:** Exponential vs. logistic growth, carrying capacity, intervention timing

**Pattern:** Shows transition from exponential to logistic growth near carrying capacity

---

### 3. `chapter_02_bird_migration.csv`
**Problem:** 2.5 - Bird Migration Timing  
**Rows:** 10 (2014-2023)  
**Columns:** 8

**Variables:**
- `Year`: Year of observation
- `Arrival_Day_of_Year`: Day of year when first birds arrive (1-365)
- `Arrival_Date`: Actual date
- `Departure_Temperature_C`: Temperature at departure location (°C)
- `Departure_Location_Latitude`: Latitude of departure site
- `Flight_Duration_Days`: Migration duration
- `Number_of_Birds`: Flock size
- `Weather_Conditions`: Weather during migration

**Usage:** Climate change effects, temperature-phenology relationships, trend analysis

**Species:** Siberian Crane (*Leucogeranus leucogeranus*) to Bharatpur, Rajasthan

---

### 4. `chapter_02_enzyme_kinetics.csv`
**Problem:** 2.8 - Enzyme Kinetics Model  
**Rows:** 21 (7 substrate concentrations × 3 replicates)  
**Columns:** 6

**Variables:**
- `Substrate_Concentration_mM`: Substrate concentration (mM)
- `Velocity_umol_per_min`: Reaction velocity (μmol/min)
- `Replicate`: Replicate number (1-3)
- `Temperature_C`: Reaction temperature (°C)
- `pH`: Reaction pH
- `Enzyme_Concentration_ug_per_mL`: Enzyme concentration (μg/mL)

**Usage:** Michaelis-Menten model fitting, parameter estimation, Lineweaver-Burk plot

**Enzyme:** Amylase (starch digestion)

**Parameters:** Vmax ≈ 10.1 μmol/min, Km ≈ 2.0 mM

---

### 5. `chapter_02_tree_growth.csv`
**Problem:** 2.10 - Model Selection Challenge  
**Rows:** 10 (5-50 years)  
**Columns:** 7

**Variables:**
- `Age_years`: Tree age (years)
- `Height_meters`: Tree height (m)
- `DBH_cm`: Diameter at breast height (cm)
- `Crown_Width_m`: Crown width (m)
- `Location`: Plot location
- `Species`: Tree species (Latin name)
- `Health_Status`: Tree health assessment

**Usage:** Compare linear, exponential, logistic, and power law models

**Species:** Teak (*Tectona grandis*) from Western Ghats

**Pattern:** Logistic growth with asymptote near 30 meters

---

### 6. `chapter_02_tea_stall_weather.csv`
**Problem:** 2.1 - From Tea Stall to Model  
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

**Usage:** Qualitative to quantitative transformation, categorical predictors, simple regression

**Pattern:** Weather strongly affects customer numbers, temperature has additional effect

---

### 7. `chapter_02_antibiotic_resistance.csv`
**Problem:** 2.4 - Antibiotic Resistance Model  
**Rows:** 6 (2018-2023)  
**Columns:** 8

**Variables:**
- `Year`: Year
- `Resistant_Percentage`: Percentage of resistant infections
- `Total_Infections_Tested`: Sample size
- `Resistant_Cases`: Absolute number of resistant cases
- `Antibiotic_Usage_DDD_per_1000`: Antibiotic usage (Defined Daily Dose per 1000 patient-days)
- `Hospital_Beds`: Number of hospital beds
- `ICU_Beds`: Number of ICU beds
- `Notes`: Context notes

**Usage:** Model comparison (linear, exponential, logistic), intervention modeling

**Pattern:** Accelerating resistance spread, intervention effect visible in 2022

---

### 8. `chapter_02_predator_prey_timeseries.csv`
**Problem:** 2.6 - Predator-Prey Dynamics  
**Rows:** 24 (quarterly data 2018-2023)  
**Columns:** 8

**Variables:**
- `Year`: Year
- `Month`: Month (1, 4, 7, 10 for quarterly)
- `Chital_Count`: Chital (spotted deer) population estimate
- `Tiger_Count`: Tiger population estimate
- `Habitat_Quality_Index`: Habitat quality (0-1)
- `Rainfall_mm`: Rainfall that month (mm)
- `Poaching_Incidents`: Number of poaching events
- `Tourist_Visits`: Number of tourist visits

**Usage:** Lotka-Volterra model fitting, equilibrium analysis, parameter estimation

**Location:** Kanha National Park, Madhya Pradesh

**Pattern:** Oscillating populations with predator lagging prey

---

### 9. `chapter_02_asiatic_lion_population.csv`
**Problem:** 2.9 - Population Viability Analysis  
**Rows:** 14 (2010-2023)  
**Columns:** 13

**Variables:**
- `Year`: Year
- `Total_Population`: Total lion count
- `Males`, `Females`, `Cubs`: Demographic breakdown
- `Sub_Adults`, `Adults`: Age class breakdown
- `Territory_km2`: Protected area size (km²)
- `Genetic_Diversity_He`: Expected heterozygosity
- `Effective_Population_Size`: Ne (genetic effective size)
- `Mortality_Events`: Number of deaths
- `Disease_Outbreaks`: Number of disease events
- `Human_Conflict_Deaths`: Deaths from human-wildlife conflict

**Usage:** PVA modeling, stochastic projection, genetic analysis, extinction risk

**Location:** Gir Forest National Park, Gujarat

**Pattern:** Steady growth with genetic diversity concerns

---

### 10. `chapter_02_sir_outbreak_example.csv`
**Problem:** 2.7 - Disease Outbreak Model  
**Rows:** 31 (daily data for 30 days)  
**Columns:** 8

**Variables:**
- `Day`: Day of outbreak (0-30)
- `Susceptible`: Number of susceptible individuals
- `Infected`: Number of infected individuals
- `Recovered`: Number of recovered individuals
- `New_Cases`: New cases that day
- `Cumulative_Cases`: Total cases to date
- `R_effective`: Effective reproduction number
- `Intervention_Active`: Whether intervention is active (Yes/No)

**Usage:** SIR model validation, intervention effect analysis, R₀ calculation

**Parameters:** β = 0.5/day (pre-intervention), γ = 0.1/day, N = 5000

**Pattern:** Shows intervention effect starting day 10, flattening the curve

---

## Loading Data in Python

### Basic Loading
```python
import pandas as pd

# Load a dataset
df = pd.read_csv('chapter_02_rice_yields.csv')

# Display first few rows
print(df.head())

# Get basic info
print(df.info())
print(df.describe())
```

### Common Operations
```python
# Select columns
fertilizer = df['Fertilizer_kg_per_hectare']
yield_data = df['Yield_tonnes_per_hectare']

# Filter rows
high_rain = df[df['Rainfall_mm'] > 1200]

# Calculate statistics
mean_yield = df['Yield_tonnes_per_hectare'].mean()
std_yield = df['Yield_tonnes_per_hectare'].std()

# Create new columns
df['Yield_per_Fertilizer'] = df['Yield_tonnes_per_hectare'] / df['Fertilizer_kg_per_hectare']
```

### Plotting
```python
import matplotlib.pyplot as plt

# Simple scatter plot
plt.scatter(df['Fertilizer_kg_per_hectare'], df['Yield_tonnes_per_hectare'])
plt.xlabel('Fertilizer (kg/ha)')
plt.ylabel('Yield (tonnes/ha)')
plt.title('Rice Yield vs Fertilizer')
plt.show()
```

---

## Loading Data in R

### Basic Loading
```r
# Load a dataset
df <- read.csv('chapter_02_rice_yields.csv')

# Display first few rows
head(df)

# Get summary statistics
summary(df)
str(df)
```

### Common Operations
```r
# Select columns
fertilizer <- df$Fertilizer_kg_per_hectare
yield_data <- df$Yield_tonnes_per_hectare

# Filter rows
high_rain <- df[df$Rainfall_mm > 1200, ]

# Calculate statistics
mean_yield <- mean(df$Yield_tonnes_per_hectare)
sd_yield <- sd(df$Yield_tonnes_per_hectare)
```

### Plotting
```r
# Simple scatter plot
plot(df$Fertilizer_kg_per_hectare, df$Yield_tonnes_per_hectare,
     xlab = "Fertilizer (kg/ha)",
     ylab = "Yield (tonnes/ha)",
     main = "Rice Yield vs Fertilizer",
     pch = 19)
```

---

## Data Quality Notes

### Realistic Features
- **Noise:** All datasets include realistic measurement error
- **Missing patterns:** Some variables show expected correlations
- **Biological constraints:** Values respect biological limits
- **Temporal autocorrelation:** Time series show realistic dependencies

### Simulated vs Real
These datasets are **simulated** but based on:
- Published research parameters
- Real ecological patterns
- Typical field study designs
- Actual species biology

They are designed to teach concepts while maintaining biological realism.

---

## Problem-Dataset Mapping

| Problem | Dataset(s) | Primary Model Type |
|---------|-----------|-------------------|
| 2.1 | tea_stall_weather | Categorical regression |
| 2.2 | rice_yields | Multiple regression |
| 2.3 | mosquito_population | Exponential/Logistic |
| 2.4 | antibiotic_resistance | Model comparison |
| 2.5 | bird_migration | Linear regression, trends |
| 2.6 | predator_prey_timeseries | Lotka-Volterra |
| 2.7 | sir_outbreak_example | SIR compartmental |
| 2.8 | enzyme_kinetics | Michaelis-Menten |
| 2.9 | asiatic_lion_population | PVA, stochastic |
| 2.10 | tree_growth | Model selection |

---

## Additional Resources

### Code Examples
See `Chapter_02_Examples.ipynb` for worked examples using these datasets.

### Extended Datasets
For larger versions of these datasets with additional variables, see the `extended/` folder.

### Data Dictionary
For detailed variable definitions and units, see `data_dictionary.md`.

---

## Citation

If using these datasets in publications or presentations:

> Patel, A. (2026). The Pattern Hunters: The Art of Scientific Thinking - Chapter 2 Datasets. 
> GitHub: github.com/The-Pattern-Hunter/pattern-hunters-problems

---

## Questions or Issues?

- Open an issue on GitHub
- Check the Discussion forum
- Email: [contact information]

---

**Note:** All datasets are provided under MIT License for educational use.

*Last Updated: January 2026*  
*Version: 1.0*
