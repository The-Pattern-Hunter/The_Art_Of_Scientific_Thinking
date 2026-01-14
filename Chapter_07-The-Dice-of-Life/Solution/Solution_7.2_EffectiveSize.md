# Solution 7.2: Census Size vs Effective Population Size

## Problem Summary
Four wildlife populations with identical census sizes (or similar) but different breeding structures. Need to calculate N_e and understand implications.

---

## Question (a): Identify Parameters

**Population A: Sambar Deer (Random Mating)**
- N_census = 80
- N_m = 20 breeding males
- N_f = 60 breeding females

**Population B: Blackbuck (Skewed Mating)**
- N_census = 100
- N_m = 5 breeding males (dominant only)
- N_f = 45 breeding females

**Population C: Elephants (Extreme Skew)**
- N_census = 60
- N_m = 1 breeding male (dominant)
- N_f = 15 breeding females

**Population D: Tigers (Territorial)**
- N_census = 40
- N_m = 10 breeding males
- N_f = 10 breeding females

---

## Question (b): Calculate N_e

**Formula:**
```
N_e = (4 × N_m × N_f) / (N_m + N_f)
```

**Population A: Sambar Deer**
```
N_e = (4 × 20 × 60) / (20 + 60)
    = 4800 / 80
    = 60
```

**Population B: Blackbuck**
```
N_e = (4 × 5 × 45) / (5 + 45)
    = 900 / 50
    = 18
```

**Population C: Elephants**
```
N_e = (4 × 1 × 15) / (1 + 15)
    = 60 / 16
    = 3.75
```

**Population D: Tigers**
```
N_e = (4 × 10 × 10) / (10 + 10)
    = 400 / 20
    = 20
```

**Results Summary:**
- Population A: N_e = 60
- Population B: N_e = 18
- Population C: N_e = 3.75
- Population D: N_e = 20

---

## Question (c): Calculate N_e/N Ratios

**Population A:**
```
N_e/N = 60/80 = 0.75 (75%)
```

**Population B:**
```
N_e/N = 18/100 = 0.18 (18%)
```

**Population C:**
```
N_e/N = 3.75/60 = 0.0625 (6.25%)
```

**Population D:**
```
N_e/N = 20/40 = 0.50 (50%)
```

**Interpretation:**

**High ratio (>50%):**
- Population A (75%): Most efficient genetic structure
- Population D (50%): Moderately efficient
- Breeding structure closer to ideal (equal sex ratio, random mating)

**Low ratio (<20%):**
- Population B (18%): Very inefficient
- Population C (6.25%): Extremely inefficient
- Highly skewed breeding → massive genetic loss

**What ratio tells us:**
- **Genetic "efficiency"** - how much of census population contributes genetically
- **Drift vulnerability** - low ratio = high drift despite large N
- **Management effectiveness** - population increases may not help if ratio stays low

---

## Question (d): Rank Populations (Best to Worst)

**Ranking by N_e (genetic health):**

1. **Population A: Sambar Deer** (N_e = 60) ⭐⭐⭐
   - Largest effective size
   - Best genetic health
   - Lowest drift

2. **Population D: Tigers** (N_e = 20) ⭐⭐
   - Moderate effective size
   - Decent genetic health
   - Equal sex ratio helps

3. **Population B: Blackbuck** (N_e = 18) ⭐
   - Small effective size despite 100 total
   - Poor genetic health
   - High drift risk

4. **Population C: Elephants** (N_e = 3.75) ❌
   - Critically small effective size
   - 60 elephants = 4 genetically!
   - Extreme drift, inbreeding risk

**Key Insight:** Population C (60 elephants) is genetically worse than Population D (40 tigers) despite being larger, because of extreme breeding skew.

---

## Question (e): Blackbuck Management Strategies

**Current situation:**
- N = 100, N_m = 5, N_f = 45
- N_e = 18

### **Strategy 1: Double Population (Same Structure)**

**New parameters:**
- N = 200
- N_m = 5 (still same dominant males)
- N_f = 45 (still same females breeding)

**Calculate N_e:**
```
N_e = (4 × 5 × 45) / (5 + 45)
    = 900 / 50
    = 18

NO CHANGE! Still N_e = 18
```

**Why no improvement?**
- N_e depends on NUMBER of breeders, not total population
- Added 100 non-breeding individuals
- No genetic benefit

### **Strategy 2: Improve Breeding Structure**

**New parameters:**
- N = 100 (same total)
- N_m = 10 (double breeding males)
- N_f = 45 (same)

**Calculate N_e:**
```
N_e = (4 × 10 × 45) / (10 + 45)
    = 1800 / 55
    = 32.7
```

**Improvement:** N_e increased from 18 to 32.7 (+82% increase!)

### **Comparison:**

| Strategy | N_census | N_e | N_e/N | Improvement |
|----------|----------|-----|-------|-------------|
| Current | 100 | 18 | 0.18 | Baseline |
| Strategy 1 | 200 | 18 | 0.09 | **0%** |
| Strategy 2 | 100 | 32.7 | 0.33 | **+82%** |

### **Recommendation: Strategy 2**

**Reasons:**

**1. Genetic benefit:**
- 82% increase in N_e
- Reduces drift by half
- Better long-term viability

**2. Cost-effectiveness:**
- No need to double population
- Focus on behavior/management
- Resources saved

**3. Practical implementation:**
- Break up male dominance hierarchies
- Manage territories to allow more males to breed
- Possibly translocate dominant males

**4. Long-term diversity:**
Calculate heterozygosity loss over 20 generations:
```
Strategy 1: H_20 = H_0 × (1-1/36)^20 = H_0 × 0.578 (42% loss)
Strategy 2: H_20 = H_0 × (1-1/65.4)^20 = H_0 × 0.717 (28% loss)

Strategy 2 preserves 14% MORE diversity
```

---

## Key Takeaways

### **Effective Population Size Formula:**
```
N_e = (4 × N_m × N_f) / (N_m + N_f)
```

**Key properties:**
- Maximum when N_m = N_f (equal sex ratio)
- Determined by SMALLER sex (bottleneck effect)
- If N_m << N_f: N_e ≈ 4×N_m (limited by males)

### **Why N_e ≠ N_census:**

**Factor 1: Unequal sex ratios**
- Breeding limited by rarer sex
- Extreme: 1 male + 99 females → N_e ≈ 4

**Factor 2: Variation in reproductive success**
- Only breeding individuals contribute
- Dominant males monopolize mating
- Non-breeders = genetic ghosts

**Factor 3: Social structure**
- Lekking, harems, territories
- Reduces effective breeders
- Can make N_e << N_census

### **Conservation Implications:**

**1. Census counts misleading:**
- 100 blackbuck ≠ genetically healthy
- Must know breeding structure
- Genetic monitoring essential

**2. Management strategies:**
- **Bad:** Just increase total numbers
- **Good:** Increase breeding males
- **Best:** Equalize male:female breeding ratio

**3. Genetic efficiency matters:**
- High N_e/N ratio = efficient population
- Low N_e/N ratio = management needed
- Target: N_e/N > 0.5 if possible

**4. Social disruption can help:**
- Breaking dominance hierarchies
- Rotating breeding males
- May improve genetic health

---

## Common Mistakes

**Mistake 1:** Using total population instead of breeders
- Wrong: N_e formula with N_census values
- Correct: Use only breeding males and females

**Mistake 2:** Assuming N_e ≈ N/2
- Only true for ideal random mating, equal sex ratio
- Reality: Often N_e << N/2

**Mistake 3:** Thinking bigger populations always better
- Not if breeding structure stays the same
- 1000 elephants with 1 breeding male still has N_e ≈ 4!

**Mistake 4:** Ignoring the limiting sex
- If 5 males breed with 100 females: Limited by males
- N_e ≈ 20, not 105

**Mistake 5:** Managing only population size
- Strategy 1 doubled population, zero genetic gain
- Must address breeding structure
- Behavioral management > population increase

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.2*
