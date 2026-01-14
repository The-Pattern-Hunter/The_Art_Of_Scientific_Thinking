# Chapter 7: The Dice of Life – Probability and Genetic Drift Problems

## Practice Problems for "The Pattern Hunters"
**Chapter 7: Probability and Genetic Drift**

---

## Problem Set Overview

**Total Problems:** 10  
**Difficulty Distribution:**
- ⭐ Easy (3 problems): 7.1, 7.2, 7.3
- ⭐⭐ Moderate (4 problems): 7.4, 7.5, 7.6, 7.7
- ⭐⭐⭐ Hard (3 problems): 7.8, 7.9, 7.10

**Topics Covered:**
1. Genetic drift fundamentals and variance
2. Effective population size calculations
3. Heterozygosity loss over generations
4. Population bottlenecks and harmonic mean
5. Migration-drift balance
6. Census vs effective population size
7. Conservation genetics applications
8. Comprehensive wildlife management
9. Breeding program design
10. Multi-population dynamics

---

## ⭐ Problem 7.1: Understanding Genetic Drift Variance (Easy)

**Learning Objective:** Calculate and interpret genetic drift variance for different population sizes

### Problem Statement

A conservation biologist at the Wildlife Institute of India is studying three isolated populations of a rare butterfly species in the Western Ghats. All three populations have the same initial allele frequencies for a wing color gene:
- A allele (brown wings): frequency p = 0.6
- a allele (gray wings): frequency q = 0.4

However, the populations have different sizes:

**Population 1 (Nilgiri Hills):** N = 10 breeding individuals  
**Population 2 (Anamalai Hills):** N = 100 breeding individuals  
**Population 3 (Periyar Reserve):** N = 1,000 breeding individuals

### Questions

**(a)** Calculate the variance in allele frequency per generation for each population using the formula:
```
Variance (σ²) = pq / (2N)
```

**(b)** Calculate the standard deviation (σ) for each population. What does this tell you about the expected change in allele frequency per generation?

**(c)** After one generation, which population is MOST likely to experience a change in the A allele frequency from 0.6 to 0.7? Which is LEAST likely? Explain your reasoning.

**(d)** The biologist observes that after 5 generations:
- Population 1: A allele frequency changed from 0.6 to 0.8 (change = +0.2)
- Population 2: A allele frequency changed from 0.6 to 0.63 (change = +0.03)
- Population 3: A allele frequency changed from 0.6 to 0.61 (change = +0.01)

Are these observations consistent with your predictions? Explain why or why not.

**(e)** If you could only protect ONE population for long-term conservation, which would you choose and why? Consider genetic drift in your answer.

---

## ⭐ Problem 7.2: Census Size vs Effective Population Size (Easy)

**Learning Objective:** Understand the difference between census and effective population sizes

### Problem Statement

You are studying four different wildlife populations in India. For each population, you have data on census size (total number of individuals) and breeding structure.

**Population A: Sambar Deer Herd**
- Total population: 80 individuals
- Breeding structure: 20 adult males, 60 adult females
- All adults breed equally

**Population B: Blackbuck Herd**
- Total population: 100 individuals
- Breeding structure: 5 dominant males monopolize breeding, 45 adult females
- Subordinate males (50 individuals) do not breed

**Population C: Elephant Family Groups**
- Total population: 60 elephants
- Breeding structure: 1 dominant male, 15 adult females breeding
- Other individuals (44) are juveniles or non-breeding adults

**Population D: Tiger Territory**
- Total population: 40 tigers
- Breeding structure: 10 territorial males, 10 territorial females
- Other individuals (20) are dispersing juveniles that don't breed

### Questions

**(a)** For each population, identify:
- Census population size (N)
- Number of breeding males (N_m)
- Number of breeding females (N_f)

**(b)** Calculate the effective population size (N_e) for each population using:
```
N_e = (4 × N_m × N_f) / (N_m + N_f)
```

**(c)** Calculate the ratio N_e/N (effective size / census size) for each population. What does this ratio tell you?

**(d)** Rank the four populations from BEST to WORST genetic health based on effective population size.

**(e)** For Population B (Blackbuck), the conservation manager proposes two strategies:
- **Strategy 1:** Increase total population to 200 individuals (maintaining same breeding structure: 5 males, 45 females breeding)
- **Strategy 2:** Keep population at 100 but ensure 10 males breed (instead of 5), with 45 females

Calculate N_e for each strategy. Which strategy provides better genetic outcomes? Explain.

---

## ⭐ Problem 7.3: The Coin Flip Analogy (Easy)

**Learning Objective:** Understand genetic drift as a sampling process

### Problem Statement

Dr. Priya is teaching her students about genetic drift using a coin flip analogy. She explains:

"Imagine a population where there are two alleles (A and a) at equal frequency (50% each). Every generation, offspring inherit alleles randomly from parents - just like flipping coins."

She divides her class into three groups to simulate populations of different sizes:

**Group 1 (Small Population):**
- Flip 10 coins to represent 10 individuals (20 alleles total)
- Each "heads" = A allele, each "tails" = a allele

**Group 2 (Medium Population):**
- Flip 50 coins to represent 50 individuals (100 alleles total)

**Group 3 (Large Population):**
- Flip 500 coins to represent 500 individuals (1,000 alleles total)

After one "generation" of coin flips, the results are:

**Group 1:** 7 heads, 3 tails (70% A allele)  
**Group 2:** 27 heads, 23 tails (54% A allele)  
**Group 3:** 248 heads, 252 tails (49.6% A allele)

### Questions

**(a)** The expected frequency of A allele should be 50% if there's no drift. Calculate the deviation from expectation for each group:
```
Deviation = |Observed frequency - Expected frequency|
```

**(b)** Which group showed the LARGEST deviation from the expected 50%? Is this what you'd predict based on genetic drift theory?

**(c)** The theoretical standard deviation for a binomial process is:
```
σ = √(pq/n)  where p=q=0.5, n = number of coin flips
```

Calculate the expected standard deviation for each group. Do the observed deviations fall within one standard deviation?

**(d)** Group 1 students repeat their experiment 5 times. Their results across all 5 trials are:
- Trial 1: 70% A
- Trial 2: 40% A
- Trial 3: 60% A
- Trial 4: 50% A
- Trial 5: 30% A

What pattern do you observe? What does this tell you about the predictability of genetic drift in small populations?

**(e)** A student asks: "If we flip coins 1,000 times for a very large population, will we ALWAYS get exactly 50% heads?"

How would you answer this question? Explain the relationship between population size and predictability.

---

## ⭐⭐ Problem 7.4: Heterozygosity Loss in Small Populations (Moderate)

**Learning Objective:** Calculate genetic diversity loss over multiple generations

### Problem Statement

The Manipur Brow-antlered Deer (*Rucervus eldii eldii*) is critically endangered, found only in Keibul Lamjao National Park. The population consists of approximately 260 individuals, but genetic analysis suggests an effective population size of only N_e = 65.

A conservation geneticist needs to project the loss of genetic diversity over the next 100 years to plan interventions.

**Current genetic data:**
- Heterozygosity (H_0) = 0.45
- Effective population size (N_e) = 65
- Generation time = 5 years
- Time horizon = 100 years (20 generations)

### Questions

**(a)** Calculate the proportion of heterozygosity lost PER GENERATION using:
```
Proportion lost per generation = 1 / (2N_e)
```

**(b)** Calculate the expected heterozygosity after 20 generations using:
```
H_t = H_0 × (1 - 1/(2N_e))^t
```

**(c)** What percentage of the original genetic diversity will be lost after 100 years?

**(d)** The conservation team proposes three management scenarios:

**Scenario 1: Status Quo**
- N_e remains at 65
- Calculate H after 20 generations

**Scenario 2: Population Doubling**
- Increase N_e to 130
- Calculate H after 20 generations

**Scenario 3: Genetic Rescue**
- Bring in 5 breeding individuals from a related subspecies every 5 years (every generation)
- Assume this effectively increases N_e to 90
- Calculate H after 20 generations

Compare the three scenarios. How much additional diversity is preserved in Scenarios 2 and 3 compared to Status Quo?

**(e)** The minimum acceptable heterozygosity for long-term viability is H = 0.35. Under Scenario 1 (status quo), how many generations until the population falls below this threshold?

Use the formula and solve for t:
```
0.35 = 0.45 × (1 - 1/130)^t
```

**(f)** Based on your calculations, write a brief recommendation (3-4 sentences) for the conservation managers. Which scenario would you recommend and why?

---

## ⭐⭐ Problem 7.5: Population Bottleneck and Recovery (Moderate)

**Learning Objective:** Understand permanent genetic consequences of bottlenecks using harmonic mean

### Problem Statement

The Asiatic Lion population in Gir Forest experienced a severe bottleneck in the early 1900s. Historical records and genetic analysis provide the following population trajectory:

**Historical Population Sizes:**
- **1890:** N = 500 lions (pre-bottleneck)
- **1900:** N = 20 lions (bottleneck minimum)
- **1910:** N = 30 lions
- **1920:** N = 50 lions
- **1930:** N = 100 lions
- **1940-present:** N = 200-500 lions (fluctuating, averaging ~300)

**Genetic data:**
- Pre-bottleneck heterozygosity (estimated): H_1890 = 0.70
- Current heterozygosity (measured): H_2020 = 0.35

### Questions

**(a)** The bottleneck lasted approximately 5 generations (1900-1930). Calculate the harmonic mean effective population size during the bottleneck period:
```
Harmonic mean = n / (1/N_1 + 1/N_2 + ... + 1/N_n)

Use: N_1900 = 20, N_1910 = 30, N_1920 = 50, N_1930 = 100, N_1940 = 200
```

**(b)** Using the harmonic mean from part (a), calculate the expected heterozygosity after 5 generations of bottleneck:
```
H_5 = H_0 × (1 - 1/(2N_harmonic))^5
```

Starting from H_0 = 0.70

**(c)** After the bottleneck, the population recovered and has been averaging ~300 individuals for the past 18 generations (1940-2020). Calculate the expected current heterozygosity:
```
H_current = H_5 × (1 - 1/(2×300))^18
```

Where H_5 is your answer from part (b).

**(d)** Compare your calculated current heterozygosity to the observed value (0.35). Are they similar? What does this tell you about:
- The accuracy of population size estimates
- The lasting impact of bottlenecks
- The possibility of recovery

**(e)** A colleague suggests: "The lions are fine now - there are 500 of them! The bottleneck was over 100 years ago, so it doesn't matter anymore."

Using your calculations, write a response explaining why this statement is incorrect. Include:
- How much genetic diversity was lost during the bottleneck
- Why population recovery doesn't restore genetic diversity
- The ongoing implications for lion conservation

**(f)** Calculate what the heterozygosity would be today if there had been NO bottleneck (N = 500 continuously for 26 generations from 1890-2020):
```
H_2020 = 0.70 × (1 - 1/1000)^26
```

How does this compare to the actual current heterozygosity? What is the "permanent cost" of the bottleneck in terms of genetic diversity lost?

---

## ⭐⭐ Problem 7.6: Migration-Drift Balance (Moderate)

**Learning Objective:** Apply the one-migrant rule to design wildlife corridors

### Problem Statement

The Sundarbans Tiger Reserve in West Bengal is isolated from other tiger populations. Genetic analysis reveals:

**Current situation:**
- Census population: 96 tigers
- Effective population size: N_e = 48 (sex ratio and social structure effects)
- Current gene flow: ZERO (complete isolation)
- Heterozygosity: H = 0.42
- Generation time: 5 years

**Proposed corridor:**
A wildlife corridor could potentially connect the Sundarbans to a large, genetically diverse tiger population in central India.

### Questions

**(a)** Without any gene flow, calculate the rate of heterozygosity loss per generation:
```
Loss rate = 1 / (2N_e)
```

**(b)** Calculate the critical migration rate needed to balance genetic drift:
```
m_critical = 1 / (4N_e)
```

What does this migration rate mean in practical terms (percentage of population per generation)?

**(c)** The "one migrant rule" states that at least one effective migrant per generation (Nm ≥ 1) can prevent genetic deterioration.

Calculate the minimum number of migrants needed per generation:
```
Minimum migrants = 1 / N_e × N_e = 1 migrant
```

Given a generation time of 5 years, translate this into practical terms: How many tigers need to migrate through the corridor every 5 years?

**(d)** The corridor construction has three cost options:

**Option A: Wide corridor (100m wide)**
- Cost: ₹50 crores
- Expected migration: 2 tigers every 5 years (m = 2/48 = 0.042 per generation)

**Option B: Medium corridor (50m wide)**
- Cost: ₹25 crores
- Expected migration: 1 tiger every 5 years (m = 1/48 = 0.021 per generation)

**Option C: Narrow corridor (25m wide)**
- Cost: ₹10 crores
- Expected migration: 0.5 tigers every 5 years (m = 0.5/48 = 0.010 per generation)

For each option, calculate Nm (number of effective migrants per generation). Which options meet the "one migrant rule" threshold?

**(e)** Calculate the equilibrium heterozygosity with and without the corridor for Option B:

**Without corridor (isolated):**
Project H after 20 generations (100 years)

**With corridor (Option B):**
With gene flow, the effect of drift is reduced. Approximate the new heterozygosity retention as:
```
Improved retention = (1 - 1/(2N_e) + m)^t
```

Calculate H after 20 generations with m = 0.021

**(f)** Write a cost-benefit analysis (4-5 sentences) for the corridor project:
- Is the genetic benefit worth the cost?
- Which option would you recommend?
- What other factors should be considered?

---

## ⭐⭐ Problem 7.7: Social Structure and Effective Population Size (Moderate)

**Learning Objective:** Understand how mating systems affect genetic drift

### Problem Statement

You are comparing three elephant populations with identical census sizes but different social structures:

**Population A: "Random Mating" (Hypothetical)**
- Total: 100 elephants
- 50 breeding males, 50 breeding females
- All individuals mate with equal probability

**Population B: "Typical Structure" (Realistic)**
- Total: 100 elephants
- 10 breeding males, 40 breeding females
- 50 juveniles/non-breeding individuals

**Population C: "Extreme Hierarchy" (Highly skewed)**
- Total: 100 elephants
- 2 dominant males, 30 breeding females
- 68 juveniles/non-breeding individuals

### Questions

**(a)** Calculate N_e for each population using:
```
N_e = (4 × N_m × N_f) / (N_m + N_f)
```

**(b)** Calculate the N_e/N ratio for each population. What does this tell you about the genetic "efficiency" of each social structure?

**(c)** Calculate the variance in allele frequency per generation for each population (assume p = q = 0.5):
```
σ² = pq / (2N_e)
```

**(d)** Calculate the standard deviation (σ) for each. If the current A allele frequency is 0.50, what is the expected range of frequencies (mean ± 1σ) after one generation for each population?

**(e)** After 10 generations, calculate the expected heterozygosity loss for each population, starting from H_0 = 0.60:
```
H_10 = H_0 × (1 - 1/(2N_e))^10
```

**(f)** **Management intervention:** For Population C (extreme hierarchy), you could implement one of two strategies:

**Strategy 1: Increase census size**
- Double total population to 200 elephants
- BUT maintain the same breeding structure (2 males, 30 females breeding)
- Calculate new N_e

**Strategy 2: Improve breeding structure**
- Keep population at 100 elephants
- BUT ensure 10 males breed (instead of 2), with 30 females
- Calculate new N_e

Which strategy provides better genetic outcomes? Explain why managing breeding structure might be more important than increasing population size.

---

## ⭐⭐⭐ Problem 7.8: Multi-Population Metapopulation Dynamics (Hard)

**Learning Objective:** Analyze genetic drift in fragmented metapopulations

### Problem Statement

The Nilgiri Tahr (*Nilgiritragus hylocrius*) exists as a metapopulation across five mountain peaks in the Western Ghats. Each sub-population is isolated with rare migration events.

**Sub-population data:**

| Peak | Census Size | Effective Size | Current H | Isolation |
|------|-------------|----------------|-----------|-----------|
| **Peak A** | 400 | 200 | 0.65 | Low (2 migrants/gen from B) |
| **Peak B** | 300 | 150 | 0.62 | Moderate (1 migrant/gen from A) |
| **Peak C** | 100 | 50 | 0.48 | High (0.2 migrants/gen from D) |
| **Peak D** | 80 | 40 | 0.44 | Very high (isolated) |
| **Peak E** | 50 | 25 | 0.38 | Extreme (isolated) |

**Generation time:** 4 years  
**Planning horizon:** 50 years (12.5 generations, round to 12)

### Questions

**(a)** For each isolated sub-population (D and E), calculate the expected heterozygosity after 12 generations with NO intervention:
```
H_12 = H_0 × (1 - 1/(2N_e))^12
```

**(b)** Peak E is dangerously small. Calculate:
1. Rate of heterozygosity loss per generation
2. Expected time (in generations) until H drops below the critical threshold of 0.30
3. Convert to years

**(c)** **Scenario analysis:** The conservation team can only afford to build ONE corridor. They must choose between:

**Option 1: Connect C to D**
- Current: C receives 0.2 migrants/gen from D
- With corridor: C receives 1.5 migrants/gen from D
- Peak D (N_e = 40) connects to Peak C (N_e = 50)

**Option 2: Connect D to B**
- Current: D is isolated
- With corridor: D receives 1.0 migrant/gen from B
- Peak B (N_e = 150, H = 0.62) connects to Peak D (N_e = 40, H = 0.44)

For each option, calculate the new Nm for the recipient population. Which option provides better genetic rescue?

**(d)** **Complex calculation:** For Option 2 (connecting D to B), estimate Peak D's heterozygosity after 12 generations with gene flow.

Use the approximation:
```
With gene flow, effective retention ≈ (1 - 1/(2N_e) + m)^t

Where m = migration rate = migrants/N_e
```

For Peak D: m = 1.0/40 = 0.025

Calculate H_12 for Peak D with this gene flow.

**(e)** **Priority ranking:** You have funding for TWO interventions (corridors or population enhancements). Rank the following options by genetic benefit:

1. Connect C to D (Option 1 from part c)
2. Connect D to B (Option 2 from part c)
3. Enhance Peak E population (double N_e from 25 to 50 through captive breeding)
4. Enhance Peak D population (increase N_e from 40 to 80 through captive breeding)

For each option, calculate the "genetic benefit" as:
```
Benefit = (H_after_12_generations_with_intervention) - (H_after_12_generations_without)
```

Consider both the direct sub-population and any connected populations.

**(f)** **Comprehensive management plan:** Based on your analyses, write a prioritized 3-step management plan (150-200 words) that:
- Identifies which sub-populations are most at risk
- Recommends specific interventions (corridors or enhancements)
- Justifies your choices with quantitative genetic projections
- Addresses both short-term (12 generations) and long-term (>25 generations) viability

---

## ⭐⭐⭐ Problem 7.9: Genetic Rescue Program Design (Hard)

**Learning Objective:** Design evidence-based genetic rescue interventions

### Problem Statement

The Pygmy Hog (*Porcula salvania*), once thought extinct, was rediscovered in 1971 in Assam's grasslands. A captive breeding program was established in 1996 with only 6 founding individuals.

**Current situation (2025):**
- Captive population: 76 individuals (N_e ≈ 30)
- Wild reintroduced population: 150 individuals (N_e ≈ 60)
- Generations since founding: ~8 (generation time = 3 years)
- Current heterozygosity: H = 0.28 (extremely low)
- Estimated pre-bottleneck heterozygosity: H_original = 0.72

**Available source populations:**
You have identified three potential source populations for genetic rescue:

**Source A: Captive population in Bangalore**
- Size: 25 individuals (N_e = 15)
- Heterozygosity: H = 0.30
- Genetic distance from Assam: 8% sequence divergence
- Founded from same 1996 stock (sibling population)

**Source B: Wild population in Bhutan**
- Size: Unknown (estimated 40-80 individuals)
- Heterozygosity: H = 0.55 (estimated from DNA samples)
- Genetic distance: 12% sequence divergence
- Different subspecies (closely related)

**Source C: Museum specimens + genetic techniques**
- Historical DNA from 1950s museum specimens
- Could create synthetic genome with original diversity
- Heterozygosity: Could restore to H = 0.65
- Genetic distance: 0% (same historical population)
- High cost and technical risk

### Questions

**(a)** **Verify the bottleneck impact:** Calculate the expected current heterozygosity after 8 generations, starting from H = 0.72 with the founding bottleneck.

**Phase 1: Founding bottleneck (6 founders, N_e = 3)**
- Duration: 1 generation
```
H_1 = 0.72 × (1 - 1/6)^1
```

**Phase 2: Captive breeding (N_e = 30)**
- Duration: 7 generations
```
H_8 = H_1 × (1 - 1/60)^7
```

Does this match the observed H = 0.28? If not, what might explain the discrepancy?

**(b)** **Evaluate source populations:** For each source (A, B, C), analyze the trade-offs:

**Genetic benefit:**
- Calculate expected heterozygosity in Assam population after introducing 5 breeding individuals from each source
- Assume simple admixture: H_new = 0.9×H_Assam + 0.1×H_source (90% local, 10% immigrant genes)

**Genetic risk:**
- Outbreeding depression risk (higher with greater genetic distance)
- Score each source as Low/Moderate/High risk based on genetic distance

**Practical feasibility:**
- Score each source as Easy/Moderate/Difficult based on logistics

Create a comparison table.

**(c)** **Optimal rescue design:** If you choose Source B (Bhutan), design a genetic rescue program:

**Scenario 1: Single large introduction**
- Introduce 10 breeding individuals at once (Year 0)
- Calculate expected H after 1 generation of mixing

**Scenario 2: Repeated small introductions**
- Introduce 2 breeding individuals every 2 generations (5 times over 10 years)
- Calculate expected H after 5 introductions

Which scenario provides better long-term genetic benefit? Consider both immediate diversity gain and ongoing drift effects.

**(d)** **Calculate rescue effectiveness:** After genetic rescue with Source B (10 individuals introduced), project the population trajectory for 20 generations:

**Without rescue (baseline):**
- N_e = 60, H_0 = 0.28
- Calculate H_20

**With rescue (improved):**
- Assume rescue increases both H (to H_new from part b) and N_e (to 75 due to immigration)
- Calculate H_20 with improved starting point

Calculate the "genetic benefit" as the difference in heterozygosity after 20 generations.

**(e)** **Economic analysis:** Each source has different costs:

- **Source A:** ₹20 lakhs (easy domestic transfer)
- **Source B:** ₹80 lakhs (international permit, capture, transport)
- **Source C:** ₹5 crores (cutting-edge genetic technology)

Calculate "genetic benefit per crore" for each source:
```
Benefit per crore = (Genetic benefit from part d) / (Cost in crores)
```

Which provides the best return on investment?

**(f)** **Risk assessment:** Genetic rescue can fail. For Source B, list and quantify three potential risks:

1. **Outbreeding depression:** Probability and potential impact
2. **Disease introduction:** Risk and mitigation strategies
3. **Behavioral incompatibility:** Likelihood and consequences

Would you still recommend genetic rescue given these risks? Write a risk-benefit analysis (200 words).

**(g)** **Long-term monitoring plan:** Design a genetic monitoring program to evaluate rescue success:

- What metrics would you measure? (at least 5)
- How frequently? (measurement schedule)
- What would indicate success vs. failure?
- At what point would you implement a second rescue attempt?

---

## ⭐⭐⭐ Problem 7.10: Comprehensive Conservation Genetics Case Study (Hard)

**Learning Objective:** Integrate all genetic drift concepts to solve a complex conservation challenge

### Problem Statement

You are the Chief Conservation Geneticist for the Ministry of Environment, Forest and Climate Change. You must prepare a comprehensive report on the genetic viability of India's Great Indian Bustard (*Ardeotis nigriceps*), one of the world's most critically endangered birds.

**Current Status (2025):**
- **Total wild population:** 128 individuals
- **Distribution:** Fragmented across 4 states

**Population breakdown:**

| Location | Census | N_e | H | Isolation | Threats |
|----------|---------|-----|---|-----------|---------|
| **Rajasthan (Desert NP)** | 92 | 46 | 0.38 | Moderate | Power lines, habitat loss |
| **Gujarat (Kachchh)** | 18 | 9 | 0.22 | High | Feral dogs, disturbance |
| **Maharashtra (Solapur)** | 12 | 6 | 0.18 | Very high | Agriculture expansion |
| **Karnataka (scattered)** | 6 | 3 | 0.12 | Extreme | Critically fragmented |

**Biological parameters:**
- Generation time: 4 years
- Breeding system: Lek mating (few males breed)
- Clutch size: 1-2 eggs
- Historical population (1960s): ~2,000 birds (estimated H_0 = 0.68)

**Available conservation budget:** ₹100 crores over 10 years

### Questions

#### **Part A: Population Viability Analysis**

**(a.1)** Calculate the harmonic mean effective population size across the entire metapopulation. Does treating them as separate populations vs. one connected population matter?

**(a.2)** For each location, calculate:
- Rate of heterozygosity loss per generation
- Expected H after 10 generations (40 years) with NO intervention
- Probability of dropping below critical threshold H = 0.15

**(a.3)** Calculate the expected time to extinction for the three smallest populations (Gujarat, Maharashtra, Karnataka) using:
```
Approximate generations to critical threshold = 
log(H_critical / H_current) / log(1 - 1/(2N_e))
```

Where H_critical = 0.15

#### **Part B: Intervention Design**

**(b.1)** **Captive breeding program:** You can establish a breeding facility with capacity for 30 individuals. Design the breeding strategy:

- Which populations should contribute founders?
- How many from each? (Consider genetic diversity and risk)
- What breeding protocol minimizes N_e loss?
- Calculate expected N_e of captive population
- Project captive population H after 5 generations

**(b.2)** **Habitat corridors:** You can build ONE major corridor OR THREE minor corridors:

**Option A: Major corridor**
- Connect Rajasthan to Gujarat (92 + 18 = 110 total, effective N_e ≈ 65)
- Cost: ₹40 crores
- Expected gene flow: 1-2 birds per generation

**Option B: Three minor corridors**
- Connect Gujarat-Maharashtra, Maharashtra-Karnataka, Karnataka-Rajasthan
- Cost: ₹12 crores each (₹36 crores total)
- Expected gene flow: 0.3-0.5 birds per generation each

Calculate Nm for each option. Which provides better genetic outcomes?

**(b.3)** **Translocation program:** Move birds between populations to increase N_e:

**Scenario 1:** Move 4 birds from Rajasthan to Gujarat
- Calculate new N_e for both populations
- Calculate genetic benefit (change in H after 10 generations)

**Scenario 2:** Move 2 birds from Rajasthan to each small population
- Calculate new N_e for all populations
- Calculate total genetic benefit across all populations

Which scenario provides greater benefit?

#### **Part C: Integrated Management Strategy**

**(c.1)** **Budget allocation:** You have ₹100 crores to allocate among:

1. Captive breeding facility: ₹30 crores (fixed cost)
2. Major corridor: ₹40 crores OR Minor corridors: ₹36 crores
3. Translocation program: ₹5 crores per translocation event
4. Habitat protection: ₹10 crores per site
5. Power line mitigation: ₹8 crores (prevents mortality)

Design an optimal allocation that:
- Maximizes genetic benefit (measure as total H preserved)
- Addresses immediate extinction risks
- Provides long-term viability
- Stays within budget

Create a budget table showing your allocation and expected genetic outcomes for each investment.

**(c.2)** **Risk analysis:** For your proposed strategy, identify:

**Genetic risks:**
- Inbreeding accumulation rate
- Loss of adaptive potential
- Genetic swamping in small populations

**Demographic risks:**
- Allee effects at low density
- Catastrophic events (disease, drought)
- Human-wildlife conflict

**Management risks:**
- Budget cuts
- Political changes
- Technical failures

Quantify each risk as Low/Medium/High and propose mitigation measures.

**(c.3)** **Monitoring protocol:** Design a 10-year monitoring program:

**Genetic monitoring:**
- Parameters to measure (at least 6)
- Sampling frequency and locations
- Laboratory analyses required
- Decision triggers for adaptive management

**Demographic monitoring:**
- Population counts and breeding success
- Survival rates by age class
- Habitat quality assessments

**Success criteria:**
Define quantitative thresholds for:
- Genetic health (H, N_e, inbreeding)
- Population viability (size, growth rate)
- Metapopulation connectivity (gene flow)

#### **Part D: Final Report**

**(d)** Write a comprehensive executive summary (300-400 words) for the Ministry that includes:

**Current genetic status:**
- Quantitative assessment of genetic health
- Comparison to historical baseline
- Identification of most at-risk populations

**Recommended actions:**
- Priority interventions (ranked 1-5)
- Budget allocation with justification
- Timeline for implementation
- Expected outcomes (with numbers)

**Long-term viability:**
- Projection for 25 years (realistic outcome)
- Best-case scenario (with full intervention)
- Worst-case scenario (business as usual)
- Critical decision points and contingencies

**Call to action:**
- Why immediate action is essential
- What happens if we wait 5 years
- Measurable goals for next 10 years

Use specific numbers from your calculations to support every major point. This is the document that will determine whether the Great Indian Bustard receives conservation funding.

---

## Summary of Problems

| Problem | Difficulty | Main Topic | Key Skills |
|---------|-----------|------------|-----------|
| 7.1 | ⭐ Easy | Drift variance | Calculation, interpretation |
| 7.2 | ⭐ Easy | Effective pop size | N_e formula, ratios |
| 7.3 | ⭐ Easy | Coin flip analogy | Sampling, probability |
| 7.4 | ⭐⭐ Moderate | Heterozygosity loss | Multi-generation projection |
| 7.5 | ⭐⭐ Moderate | Bottlenecks | Harmonic mean, permanent damage |
| 7.6 | ⭐⭐ Moderate | Migration-drift | One migrant rule, corridors |
| 7.7 | ⭐⭐ Moderate | Social structure | Mating systems, N_e effects |
| 7.8 | ⭐⭐⭐ Hard | Metapopulations | Multi-population dynamics |
| 7.9 | ⭐⭐⭐ Hard | Genetic rescue | Source evaluation, program design |
| 7.10 | ⭐⭐⭐ Hard | Comprehensive | Integration of all concepts |

---

**Total Coverage:**
- ✅ Genetic drift variance and standard deviation
- ✅ Effective population size (multiple contexts)
- ✅ Heterozygosity loss calculations
- ✅ Population bottlenecks and harmonic mean
- ✅ Migration-drift balance and corridors
- ✅ Social structure effects on N_e
- ✅ Metapopulation genetics
- ✅ Genetic rescue program design
- ✅ Conservation decision-making
- ✅ Real Indian wildlife examples

---

*Problems created for "The Pattern Hunters" by Dr. Alok Patel*  
*Chapter 7: The Dice of Life - Probability and Genetic Drift*
