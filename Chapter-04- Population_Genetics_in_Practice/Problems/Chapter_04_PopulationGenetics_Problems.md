# Chapter 4: Population Genetics in Practice - From Theory to Application Problems

## Practice Problems for "The Pattern Hunters"
**Chapter 4: Population Genetics in Practice**

---

## Problem Set Overview

**Total Problems:** 10  
**Difficulty Distribution:**
- ⭐ Easy (3 problems): 4.1, 4.2, 4.3
- ⭐⭐ Moderate (4 problems): 4.4, 4.5, 4.6, 4.7
- ⭐⭐⭐ Hard (3 problems): 4.8, 4.9, 4.10

**Topics Covered:**
1. Hardy-Weinberg equilibrium calculations
2. Allele frequency determination from phenotype data
3. Selection coefficients and fitness calculations
4. ABO blood group analysis (multi-allele systems)
5. Sickle cell and balancing selection
6. Conservation genetics applications
7. Genetic counseling and risk assessment
8. Multi-locus selection and epistasis
9. Population stratification and admixture
10. Comprehensive genetic rescue program design

---

## ⭐ Problem 4.1: Hardy-Weinberg Basics with Sickle Cell Trait (Easy)

**Learning Objective:** Apply Hardy-Weinberg principles to calculate genotype frequencies and understand carrier frequencies

### Problem Statement

Dr. Meena Patel is conducting a genetic survey in a tribal village in Odisha where malaria is endemic. She is studying the sickle cell gene, which has two alleles:
- **A allele:** Normal hemoglobin
- **S allele:** Sickle cell hemoglobin

In a sample of 500 newborns, she finds that 4 babies (0.8%) have sickle cell disease (SS genotype).

**Background:** Individuals with SS have sickle cell disease, AS individuals have sickle cell trait (usually healthy with malaria protection), and AA individuals have normal hemoglobin.

### Questions

**(a)** Using the Hardy-Weinberg equation, calculate the frequency of the S allele (q) in this population. Show your work step-by-step.

**(b)** Calculate the frequency of the A allele (p).

**(c)** Calculate the expected frequencies of all three genotypes (AA, AS, SS) in this population.

**(d)** In the sample of 500 newborns, how many are expected to:
- Have sickle cell disease (SS)?
- Be carriers with sickle cell trait (AS)?
- Have normal hemoglobin (AA)?

**(e)** Two parents who are both carriers (AS) are planning to have children. What is the probability that:
- Their first child will have sickle cell disease?
- Their first child will be a carrier?
- Their first child will have normal hemoglobin?
- All three of their children will be unaffected (AA or AS)?

**(f)** Dr. Patel observes that the actual number of AS individuals (carriers) in her sample is 95, while the Hardy-Weinberg prediction is different. Calculate the expected number of AS carriers and discuss whether this population appears to be in Hardy-Weinberg equilibrium.

---

## ⭐ Problem 4.2: Calculating Allele Frequencies from Phenotype Data (Easy)

**Learning Objective:** Master the technique of working backward from phenotypes to allele frequencies

### Problem Statement

A biology teacher in Bhubaneswar is teaching genetics using tongue-rolling ability as an example. Tongue rolling is controlled by a single gene with two alleles:
- **R allele (dominant):** Can roll tongue
- **r allele (recessive):** Cannot roll tongue

In a class survey of 120 students:
- **81 students can roll their tongues** (RR or Rr genotypes)
- **39 students cannot roll their tongues** (rr genotype)

### Questions

**(a)** Calculate the frequency of the r allele using the Hardy-Weinberg principle. Show all steps clearly.

**(b)** Calculate the frequency of the R allele.

**(c)** Using these allele frequencies, calculate the expected number of students with each genotype (RR, Rr, rr) in this class of 120.

**(d)** What proportion of the tongue-rollers (those who can roll their tongues) are expected to be heterozygous (Rr)? Express as both a fraction and a percentage.

**(e)** A student who can roll their tongue (but doesn't know their genotype) marries someone who cannot roll their tongue. They have 4 children. 
- If the tongue-roller is RR, what's the probability all 4 children can roll their tongues?
- If the tongue-roller is Rr, what's the probability exactly 2 out of 4 children can roll their tongues?
- Given that tongue-rollers in this population have the genotype frequencies you calculated above, what's the overall probability this couple's first child will be a tongue-roller?

**(f)** The teacher wants to estimate how many students in the entire school (800 students) are likely to be heterozygous carriers (Rr). Provide this estimate with your reasoning.

---

## ⭐ Problem 4.3: ABO Blood Groups - Introduction to Multi-Allele Systems (Easy)

**Learning Objective:** Understand how Hardy-Weinberg extends to systems with more than two alleles

### Problem Statement

A blood donation camp at a college in Cuttack collects data from 400 donors and finds the following blood type distribution:

- **Type O:** 180 donors (45%)
- **Type A:** 160 donors (40%)
- **Type B:** 48 donors (12%)
- **Type AB:** 12 donors (3%)

**Background:** The ABO system has three alleles (A, B, O), where A and B are codominant and both are dominant over O.
- Type O = OO genotype only
- Type A = AA or AO genotypes
- Type B = BB or BO genotypes
- Type AB = AB genotype only

### Questions

**(a)** Calculate the frequency of the O allele (r) using the Type O blood group frequency. Show your calculation.

**(b)** The frequency of Type AB donors provides a direct relationship to allele frequencies: Type AB frequency = 2pq, where p = frequency of A allele and q = frequency of B allele.

Using this information along with the constraint that p + q + r = 1, calculate the frequencies of:
- A allele (p)
- B allele (q)
- O allele (r)

[Hint: You'll need to solve a quadratic equation using p + q = 1 - r and 2pq = 0.03]

**(c)** Using your calculated allele frequencies, determine the expected genotype frequencies for all six possible genotypes: AA, AO, BB, BO, OO, AB.

**(d)** Calculate the expected number of donors with each phenotype (blood type) based on your genotype frequencies. Compare these to the observed numbers. Does this population appear to be in Hardy-Weinberg equilibrium?

**(e)** In this population, what is the probability that a randomly chosen person is:
- A carrier of the O allele (has AO or BO genotype)?
- Homozygous at this locus (AA, BB, or OO)?

**(f)** If a Type A woman (but you don't know if she's AA or AO) marries a Type B man (but you don't know if he's BB or BO), what is the probability their child could have Type O blood? Use the population allele frequencies to calculate the likelihood each parent is a carrier of O.

---

## ⭐⭐ Problem 4.4: Selection Coefficients and Balanced Polymorphism (Moderate)

**Learning Objective:** Calculate fitness values and selection coefficients, and understand how heterozygote advantage maintains genetic variation

### Problem Statement

Researchers studying sickle cell genetics in a malaria-endemic region of Chhattisgarh measure survival rates to adulthood for different hemoglobin genotypes:

**Survival data from 1,000 births tracked over 20 years:**
- **AA genotype:** 650 survived to adulthood out of 720 born (90.3% survival)
- **AS genotype:** 245 survived to adulthood out of 250 born (98.0% survival)
- **SS genotype:** 12 survived to adulthood out of 30 born (40.0% survival)

**Current allele frequencies in adults:**
- A allele frequency (p) = 0.85
- S allele frequency (q) = 0.15

### Questions

**(a)** Calculate the relative fitness (w) for each genotype, using AS (the genotype with highest survival) as the reference with w = 1.0.

**(b)** Calculate the selection coefficient (s) against each genotype using the formula: s = 1 - w

What do these selection coefficients tell you about the strength of selection acting on each genotype?

**(c)** The average population fitness (W̄) can be calculated as:
```
W̄ = p²w(AA) + 2pqw(AS) + q²w(SS)
```

Calculate the average population fitness using:
- Current allele frequencies (p = 0.85, q = 0.15)
- The fitness values you calculated in part (a)

**(d)** For a balanced polymorphism with heterozygote advantage, the equilibrium frequency of the S allele can be approximated by:
```
q_equilibrium = s(AA) / [s(AA) + s(SS)]
```

Where s(AA) and s(SS) are the selection coefficients against AA and SS respectively.

Calculate the predicted equilibrium frequency of the S allele. How does this compare to the observed frequency of 0.15?

**(e)** If malaria were completely eliminated from this region through public health interventions:
- How would the fitness values change? (Assume AS and AA would have equal fitness of 1.0, while SS remains at 0.4)
- What would happen to the S allele frequency over time?
- Calculate the new selection coefficient against SS in the absence of malaria.
- Estimate the S allele frequency after 10 generations using the approximation: Δq ≈ -sq²(1-q) for recessive deleterious alleles.

**(f)** In the current situation with malaria present, calculate:
- In a population of 10,000 adults, how many individuals are expected to be AS carriers?
- How many AS individuals avoid severe malaria that would otherwise affect AA individuals?
- Explain why this is an example of "balancing selection."

---

## ⭐⭐ Problem 4.5: Conservation Genetics - Asiatic Lion Genetic Diversity (Moderate)

**Learning Objective:** Apply population genetics principles to real conservation scenarios and understand effective population size

### Problem Statement

The Asiatic lion (*Panthera leo persica*) population in Gir Forest has made a remarkable recovery, but genetic analysis reveals concerning patterns:

**Population data:**
- **Current total population:** 650 lions
- **Breeding adults:** Approximately 180 lions (90 males, 90 females)
- **Observed heterozygosity:** H = 0.35
- **African lion heterozygosity (reference):** H = 0.62
- **Historical Gir population (1900):** Fewer than 20 individuals

**Genetic analysis of a neutral microsatellite locus:**
- Allele A: frequency = 0.70
- Allele B: frequency = 0.30

### Questions

**(a)** Calculate the effective population size (N_e) for the Asiatic lion using:
```
N_e = (4 × N_males × N_females) / (N_males + N_females)
```

How does this compare to the census population size of 650? What does this ratio (N_e/N_census) tell you?

**(b)** For the microsatellite locus with alleles A and B at frequencies 0.70 and 0.30:
- Calculate the expected heterozygosity under Hardy-Weinberg equilibrium: H_exp = 2pq
- The observed heterozygosity is 0.32. Calculate the inbreeding coefficient (F) using:
```
F = (H_exp - H_obs) / H_exp
```
- What does this inbreeding coefficient indicate about the mating structure of this population?

**(c)** The rate of heterozygosity loss per generation due to genetic drift is:
```
ΔH/H = 1/(2N_e)
```

Calculate:
- The proportion of heterozygosity lost per generation
- The expected heterozygosity after 10 generations: H_t = H_0(1 - 1/(2N_e))^t
- How many generations until heterozygosity drops to 0.30 (a critical threshold)?

**(d)** Compare the genetic diversity between Asiatic and African lions:
- Calculate the percentage reduction in heterozygosity: [(H_African - H_Asiatic)/H_African] × 100
- This reduction is primarily due to the population bottleneck in 1900. If the bottleneck reduced the population to 15 individuals for one generation, estimate how much heterozygosity was lost during that single generation.

**(e)** **Conservation management scenarios:** Evaluate three proposed strategies:

**Strategy 1: Status Quo**
- Maintain current N_e = 180
- No intervention
- Project heterozygosity after 20 generations

**Strategy 2: Habitat Expansion**
- Increase breeding population to 240 individuals (120 males, 120 females)
- Calculate new N_e
- Project heterozygosity after 20 generations

**Strategy 3: Establish Second Population**
- Translocate 50 lions to create a new population
- Original Gir population: N_e = 140
- New population: N_e = 40
- Calculate combined heterozygosity preservation (treat as metapopulation)

Which strategy best preserves genetic diversity over 20 generations?

**(f)** **Genetic rescue consideration:** Wildlife managers consider introducing lions from an African population to increase genetic diversity.

- If 5 African lions (with H = 0.62) are introduced and successfully breed with Gir lions, estimate the heterozygosity in the next generation using: H_new ≈ (N_Gir × H_Gir + N_African × H_African)/(N_Gir + N_African)
- What are the potential risks and benefits of this genetic rescue approach?
- What percentage of African ancestry would you recommend to balance genetic diversity gains against potential outbreeding depression?

---

## ⭐⭐ Problem 4.6: Genetic Counseling and Risk Assessment (Moderate)

**Learning Objective:** Apply population genetics to medical genetics and calculate complex inheritance probabilities

### Problem Statement

Rajesh and Priya, a couple from Bhubaneswar, are planning to have children. They visit a genetic counselor because:
- **Rajesh's younger brother** has cystic fibrosis (CF), an autosomal recessive disorder
- **Priya has no family history** of CF

**Population data for their community:**
- CF incidence: 1 in 2,500 births have CF
- The population is in Hardy-Weinberg equilibrium for this gene

### Questions

**(a)** Calculate the frequency of the CF allele (f) in the population using the disease incidence. Show your work.

**(b)** Calculate the carrier frequency (heterozygotes) in the general population using 2pq.

**(c)** **Determine Rajesh's carrier probability:**

Since Rajesh's brother has CF (ff genotype), both of Rajesh's parents must be carriers (Ff).

Rajesh's possible genotypes given his parents are both Ff:
- FF: 1/4 probability
- Ff: 2/4 probability  
- ff: 1/4 probability

However, we know Rajesh does NOT have CF (he's not ff). Using conditional probability, what is the probability that Rajesh is a carrier (Ff)?

**(d)** **Determine Priya's carrier probability:**

Priya has no family history of CF. Using the population carrier frequency from part (b), what is the probability that Priya is a carrier?

**(e)** Calculate the probability that:
- Both Rajesh AND Priya are carriers
- If both are carriers, their child will have CF
- Their first child will have CF (combining all probabilities)

**(f)** The couple has a daughter who is healthy (does not have CF). They are now planning a second child. 

- Does the fact that their first child is healthy change the probability that Rajesh is a carrier? Explain using Bayesian reasoning.
- What is the probability their second child will have CF, given that their first child is healthy?

**(g)** **Extended scenario:** If CF carrier screening test is available with 95% sensitivity and 98% specificity:

- Rajesh tests positive for being a carrier. Given his family history, calculate the probability he is truly a carrier using Bayes' theorem.
- Priya tests negative. Calculate the probability she is truly not a carrier.
- With these test results, recalculate the probability their child will have CF.

---

## ⭐⭐ Problem 4.7: Population Subdivision and Wahlund Effect (Moderate)

**Learning Objective:** Understand how population structure affects genotype frequencies and detect deviations from Hardy-Weinberg equilibrium

### Problem Statement

A genetic survey studies the MN blood group system (a simple codominant two-allele system) across different regions of India. The researchers sample three populations:

**Population 1 - North India (Punjab):** 1,000 individuals
- MM: 490 individuals
- MN: 420 individuals  
- NN: 90 individuals

**Population 2 - South India (Tamil Nadu):** 1,000 individuals
- MM: 160 individuals
- MN: 480 individuals
- NN: 360 individuals

**Population 3 - Combined Urban Sample (Mumbai):** 2,000 individuals sampled from a cosmopolitan city with migrants from both regions in equal proportions
- MM: 330 individuals
- MN: 940 individuals
- NN: 730 individuals

### Questions

**(a)** For each of the three populations, calculate:
- M allele frequency (p)
- N allele frequency (q)
- Expected genotype frequencies under Hardy-Weinberg: p² (MM), 2pq (MN), q² (NN)
- Expected numbers for each genotype

**(b)** For each population, perform a chi-square test for Hardy-Weinberg equilibrium:
```
χ² = Σ[(Observed - Expected)²/Expected]
```

With 1 degree of freedom, the critical value at p = 0.05 is 3.84.

Which populations are in Hardy-Weinberg equilibrium and which are not?

**(c)** Calculate the heterozygosity for each population:
- Observed heterozygosity (H_obs): proportion of MN individuals
- Expected heterozygosity (H_exp): 2pq
- For populations not in equilibrium, is there a heterozygote excess or deficiency?

**(d)** **Understanding Population 3 (Mumbai):**

The Mumbai sample appears to be a mixture of North and South populations. Calculate what you would expect if you randomly mixed equal numbers from Population 1 and Population 2:

- Average M allele frequency in the mixed population
- Expected genotype frequencies if the mixture was fully random (Hardy-Weinberg)
- Compare to the observed Mumbai data

**(e)** The **Wahlund effect** predicts that when you combine two populations with different allele frequencies, you get a heterozygote deficiency. 

Calculate the expected heterozygote frequency under:
- **Scenario A:** Complete random mating (all as one population) - use the average allele frequencies
- **Scenario B:** No interbreeding between North/South groups (population subdivision) - calculate weighted average of heterozygosity within each subpopulation

Compare these to the observed heterozygosity in Mumbai. What do the data suggest about mating patterns in this urban population?

**(f)** Calculate the inbreeding coefficient (F_ST) that would explain the heterozygote deficiency in Mumbai:
```
F_ST = (H_exp - H_obs) / H_exp
```

Where H_exp is calculated using the combined allele frequencies.

What does this F_ST value tell you about population structure?

**(g)** **Application to conservation:** Explain why conservation programs should:
- Maintain genetic monitoring of subpopulations separately
- Be cautious about interpreting allele frequencies in mixed samples
- Consider population structure when designing breeding programs

Use specific numbers from this problem to illustrate your points.

---

## ⭐⭐⭐ Problem 4.8: Multi-Locus Selection and Epistasis (Hard)

**Learning Objective:** Analyze complex selection scenarios involving multiple genes and understand epistatic interactions

### Problem Statement

In a population from tribal Odisha, two genes provide protection against malaria through different mechanisms:

**Gene 1 - Hemoglobin (HbS locus):**
- A allele (normal): frequency p₁ = 0.85
- S allele (sickle): frequency q₁ = 0.15

**Gene 2 - G6PD (X-linked):**
- D allele (normal): frequency p₂ = 0.80 (in males)
- d allele (deficient): frequency q₂ = 0.20 (in males)

**Note:** G6PD deficiency is X-linked, so males have one copy and females have two.

### Fitness values in malaria-endemic conditions:

**For Hemoglobin genotypes (both sexes):**
- AA: w = 0.85 (susceptible to malaria)
- AS: w = 1.00 (protected, no disease)
- SS: w = 0.30 (sickle cell disease)

**For G6PD genotypes:**
- Males DD: w = 0.90 (susceptible to malaria)
- Males Dd (not applicable - males are hemizygous)
- Males dd: w = 0.95 (protected, minimal disease cost)

- Females DD: w = 0.90 (susceptible to malaria)
- Females Dd: w = 0.95 (partial protection)
- Females dd: w = 0.85 (protected but disease symptoms)

**Epistatic interaction:** Individuals with BOTH protective variants (AS genotype AND G6PD deficiency) have synergistic protection:
- Combined fitness multiplier = 1.15 (better than either alone)

### Questions

**(a)** **Single locus analysis:**

For the HbS locus alone:
- Calculate current genotype frequencies (AA, AS, SS) using Hardy-Weinberg
- Calculate mean population fitness at this locus
- Using the selection coefficients, predict the equilibrium S allele frequency:
```
q_eq = s_AA / (s_AA + s_SS)
```
Is the population at equilibrium?

**(b)** **X-linked analysis for G6PD:**

Calculate genotype frequencies and mean fitness separately for:
- Males (hemizygous): Only DD or dd
- Females: DD, Dd, dd

What is the overall mean fitness for the population at the G6PD locus?

**(c)** **Two-locus genotype frequencies:**

Assuming the two loci are on different chromosomes (independent), calculate the frequency of each combined genotype in the population. For example:
- AA/DD males: p₁² × p₂
- AS/dd males: 2p₁q₁ × q₂
- (and so on for all combinations)

Create a table showing frequencies of all relevant two-locus genotypes.

**(d)** **Epistasis analysis:**

Individuals with AS and G6PD deficiency have enhanced protection. Calculate:
- Frequency of AS/dd males (both protections)
- Frequency of AS/dd females (both protections)
- Their combined fitness considering epistasis (1.00 × 0.95 × 1.15)

What proportion of the population benefits from this epistatic interaction?

**(e)** **Comparative advantage:**

Calculate the relative fitness advantage of different protective strategies:
- Only HbS protection (AS genotype, G6PD normal)
- Only G6PD protection (AA genotype, G6PD deficient)
- Both protections (AS genotype, G6PD deficient)
- No protection (AA genotype, G6PD normal)

Express each as a percentage survival advantage over the no-protection baseline.

**(f)** **Evolutionary dynamics:**

If malaria is eliminated:
- How would fitness values change for each genotype combination?
- Which alleles would be selected against?
- Predict the direction and relative rate of change for:
  - S allele frequency
  - d allele frequency (remember this is X-linked, so change occurs differently in males vs females)

**(g)** **Population health implications:**

In a population of 10,000 individuals (5,000 males, 5,000 females):
- How many individuals carry at least one protective variant?
- How many suffer from disease symptoms (SS or dd females)?
- What is the population-level trade-off between malaria protection and genetic disease burden?

**(h)** **Medical screening recommendations:**

Design a screening and counseling program that addresses:
- Which couples are at highest risk for children with severe phenotypes?
- What is the probability that two carriers (AS male and Dd female) have a child with both SS and dd genotypes?
- Should the program screen for one gene, both genes, or different strategies for different subpopulations?

---

## ⭐⭐⭐ Problem 4.9: Population Admixture and Ancestry Estimation (Hard)

**Learning Objective:** Model population mixing, admixture dynamics, and use genetics to infer population history

### Problem Statement

Researchers are studying genetic variation in an urban population in Kolkata with complex demographic history. The city has received migrants from three distinct source populations over the past 200 years:

**Source Population 1 - Bengal (indigenous):** 
- A allele: p = 0.30
- B allele: q = 0.25  
- O allele: r = 0.45

**Source Population 2 - North India:**
- A allele: p = 0.25
- B allele: q = 0.10
- O allele: r = 0.65

**Source Population 3 - East Asia (historical trade/migration):**
- A allele: p = 0.20
- B allele: q = 0.20
- O allele: r = 0.60

**Current Kolkata urban sample (n = 3,000):**
- Type O: 1,650 (55%)
- Type A: 840 (28%)
- Type B: 420 (14%)
- Type AB: 90 (3%)

### Questions

**(a)** Calculate allele frequencies in the current Kolkata population using the ABO blood group data. Use the method from Problem 4.3:
- First calculate r (O allele frequency) from Type O percentage
- Then solve for p and q using Type AB frequency and the constraint p + q + r = 1

**(b)** **Admixture proportions:**

Let's denote the admixture proportions as:
- α = proportion from Bengal
- β = proportion from North India  
- γ = proportion from East Asia

Where α + β + γ = 1

The allele frequencies in the admixed population should equal:
```
p_Kolkata = α × p_Bengal + β × p_North + γ × p_East
q_Kolkata = α × q_Bengal + β × q_North + γ × q_East
r_Kolkata = α × r_Bengal + β × r_North + γ × r_East
```

Using your calculated allele frequencies from part (a) and assuming the East Asian contribution is small (γ = 0.05), solve for α and β.

**(c)** **Hardy-Weinberg testing in admixed population:**

Calculate expected genotype frequencies for the Kolkata population:
- Use your allele frequencies from part (a)
- Calculate expected numbers for all genotypes
- Perform chi-square test for Hardy-Weinberg equilibrium

Is the population in equilibrium? If not, what does this suggest about mating patterns or recent admixture?

**(d)** **Temporal dynamics of admixture:**

Assume the current admixture proportions (α, β, γ from part b) were established through migration 200 years ago (approximately 8 generations, assuming 25 years per generation).

If migration stopped 200 years ago and random mating occurred since then:
- Would allele frequencies have changed? Why or why not?
- Would genotype frequencies have changed? Calculate the expected approach to Hardy-Weinberg over 8 generations if there was initial disequilibrium.

**(e)** **Continuous migration model:**

Now assume instead that migration has been continuous at a rate of 2% per generation from North India:
- Calculate the change in allele frequencies per generation using: Δp = m(p_migrants - p_residents)
- Where m = 0.02 (migration rate)
- Starting from Bengal baseline, project allele frequencies after 8 generations
- Compare to your observed frequencies - does continuous or historical admixture better explain the data?

**(f)** **Linkage disequilibrium and admixture mapping:**

In recently admixed populations, different genomic regions show different ancestry proportions due to recombination breaking up ancestry blocks.

If two genetic markers 20 cM apart (recombination rate r = 0.20) show:
- Marker 1: 70% Bengal ancestry, 25% North India, 5% East Asia
- Marker 2: 65% Bengal ancestry, 30% North India, 5% East Asia

Calculate the decay of ancestry correlation over 8 generations using:
```
D_t = D_0 × (1-r)^t
```

Does this match expectation for 8 generations of random mating?

**(g)** **Application to personalized medicine:**

Different source populations have different disease risk alleles. A drug-metabolizing enzyme has allele frequencies:
- Fast metabolizer (F): Bengal = 0.40, North India = 0.60, East Asia = 0.30
- Slow metabolizer (S): (the complement)

Using the admixture proportions you calculated:
- What proportion of Kolkata population are slow metabolizers (SS)?
- How does this compare to each source population?
- Design a pharmacogenetic dosing strategy that accounts for population structure.

**(h)** **Conservation genetics parallel:**

Explain how these admixture principles apply to:
- Genetic rescue programs that introduce new individuals into isolated populations
- Detecting hybridization between endangered species and domestic relatives
- Managing genetic diversity in captive breeding programs

Use specific numerical examples from this problem to illustrate each application.

---

## ⭐⭐⭐ Problem 4.10: Comprehensive Genetic Rescue Program Design (Hard)

**Learning Objective:** Integrate all population genetics concepts to design and evaluate a complete conservation genetics intervention

### Problem Statement

You are the lead geneticist for a comprehensive rescue program for the **Nilgiri Tahr** (*Nilgiritragus hylocrius*), an endangered mountain ungulate endemic to the Western Ghats.

**Current Population Status:**

| Population | Location | N_census | N_e | H_obs | Isolation | Threats |
|------------|----------|----------|-----|-------|-----------|---------|
| **Pop A** | Eravikulam NP | 750 | 180 | 0.42 | Moderate | Tourism, Climate |
| **Pop B** | Mukurthi NP | 180 | 45 | 0.35 | High | Habitat loss |
| **Pop C** | Grass Hills | 85 | 22 | 0.28 | Very High | Poaching |
| **Pop D** | Silent Valley | 45 | 12 | 0.22 | Extreme | Fragmentation |

**Historical baseline (1950s):** Estimated 3,000 animals, H ≈ 0.58

**Biological parameters:**
- Generation time: 6 years
- Reproductive rate: 0.8 offspring per female per year
- Sex ratio: 1:1 at birth, but breeding ratio typically 1 male : 3 females

**Available genetic data from microsatellite analysis:**

**Population A (Eravikulam) - Marker locus 1:**
- Allele A1: 0.35
- Allele A2: 0.40
- Allele A3: 0.20
- Allele A4: 0.05

**Population B (Mukurthi) - Same locus:**
- Allele A1: 0.55
- Allele A2: 0.30
- Allele A3: 0.15
- Allele A4: 0.00 (lost)

**Budget:** ₹50 crores over 10 years

### Questions

#### **Part A: Population Genetic Assessment**

**(a.1)** For each population, calculate:
- Rate of heterozygosity loss per generation: ΔH = 1/(2N_e)
- Projected heterozygosity after 10 years (assuming 10 years ≈ 1.67 generations): H_t = H_0(1 - 1/(2N_e))^t
- Time (in years) until H drops below critical threshold of 0.20

**(a.2)** Calculate the inbreeding coefficient (F) for each population:
- Expected H under Hardy-Weinberg for the microsatellite locus: H_exp = 1 - Σp_i²
- Use F = (H_exp - H_obs)/H_exp

What does the increasing F across populations A→D tell you?

**(a.3)** Compare allelic richness between Pop A and Pop B:
- Population A has 4 alleles; Population B has lost A4
- Calculate the probability that Pop B will lose another allele (A3) in the next 5 generations using: P(loss) ≈ e^(-2N_e×p) for rare alleles
- What is the conservation significance of losing rare alleles?

**(a.4)** Calculate the overall metapopulation effective size treating all four populations as connected via occasional dispersal:
- Harmonic mean: 1/N_e_total = (1/4) × [1/N_e_A + 1/N_e_B + 1/N_e_C + 1/N_e_D]
- Compare to the sum of individual N_e values
- What does this tell you about the importance of small populations in overall genetic diversity?

#### **Part B: Intervention Strategy Design**

**(b.1)** **Genetic rescue through translocation:**

**Option 1:** Move animals from Pop A (largest, most diverse) to smaller populations
- Move 10 animals from A to B
- Move 10 animals from A to C  
- Move 10 animals from A to D

Calculate for each recipient population:
- New N_e (assuming translocated animals breed successfully)
- Expected heterozygosity after translocation: H_new ≈ (N_old × H_old + N_new × H_donor)/(N_old + N_new)
- Projected H after 10 years with this new starting point

**Option 2:** Circular genetic rescue
- Move 5 animals: A→B, B→C, C→D, D→A

Calculate the effect on genetic diversity using migration-drift balance:
- Effective migration rate (Nm) for each population pair
- Equilibrium F_ST between populations: F_ST ≈ 1/(4Nm + 1)

Which option better preserves overall genetic diversity?

**(b.2)** **Habitat corridor establishment:**

Two corridor proposals:
- **Corridor 1:** Connect A↔B (50 km, moderate terrain) - Cost ₹15 crores, enables 2 migrants/generation
- **Corridor 2:** Connect C↔D (30 km, difficult terrain) - Cost ₹18 crores, enables 1 migrant/generation

For each corridor:
- Calculate Nm (number of migrants × effective population size)
- Apply the "one migrant per generation" rule: does it prevent differentiation?
- Calculate F_ST reduction: Compare F_ST with and without gene flow

Which corridor provides better genetic cost-effectiveness (genetic benefit per crore spent)?

**(b.3)** **Captive breeding program:**

Establish a captive population by removing 20 animals from Pop A:
- Calculate the N_e of the captive population if managed optimally (equal sex ratio, all breed)
- Project heterozygosity in captive population over 10 years
- Calculate genetic contribution: If captive-bred animals are reintroduced (10 animals every 3 years), what is the effect on wild population N_e?

Compare costs:
- Captive facility: ₹20 crores (10-year operation)
- Genetic benefit: increased N_e and H in reintroduction populations

**(b.4)** **Assisted gene flow using reproductive technologies:**

If artificial insemination is feasible (cost: ₹2 crores to establish, ₹50,000 per procedure):
- 20 females in Pops C and D artificially inseminated with genetic material from Pop A males
- No physical translocation needed
- Calculate effective increase in gene flow
- Compare genetic benefit vs. cost to physical translocation

#### **Part C: Population Viability Modeling**

**(c.1)** **Demographic-genetic extinction risk:**

For Population D (most vulnerable):
- Calculate demographic stochasticity risk: σ_N/N = 1/√N
- Calculate genetic stochasticity: ΔH = 1/(2N_e)
- Which poses greater immediate risk?

If Population D declines by 5% per year due to habitat loss:
- Project census size over 10 years
- Project N_e over 10 years (assuming N_e/N ratio remains constant)
- At what year does N_e drop below minimum viable size (N_e = 50)?

**(c.2)** **Extinction vortex modeling:**

Population D faces multiple threats:
1. Demographic: Small population, low recruitment
2. Genetic: Inbreeding depression (fitness declines 5% for every 0.05 increase in F)
3. Environmental: Drought every 5 years reduces population by 15%

Model the interaction:
- Starting: N = 45, F = 0.25, fitness = 0.875 (already depressed)
- Each generation: Calculate new F, new fitness, demographic growth adjusted by fitness
- Include stochastic drought events
- Project 10 generations (60 years)

At what generation does N drop below 20 (quasi-extinction threshold)?

**(c.3)** **Genetic rescue impact on extinction risk:**

Repeat the Population D extinction vortex model with genetic rescue intervention (10 immigrants from Pop A in year 0):
- Recalculate starting H and F after immigration
- Reset fitness (reduced inbreeding depression)
- Re-run 10-generation projection

By how many years does genetic rescue delay extinction? Calculate the "value" of each additional year of population persistence.

#### **Part D: Integrated Decision Framework**

**(d.1)** **Multi-criteria optimization:**

You must allocate ₹50 crores among:
1. Corridor 1 (A↔B): ₹15 crores
2. Corridor 2 (C↔D): ₹18 crores
3. Captive breeding: ₹20 crores
4. Translocation program: ₹5 crores per event (can do multiple)
5. Habitat protection Pop D: ₹12 crores (prevents decline)
6. Assisted reproduction: ₹2 crores setup + ₹0.05 crores × number of procedures

Design an optimal allocation that:
- Maximizes total metapopulation H in 10 years (calculated as weighted average across populations)
- Prevents extinction of Population D
- Increases overall N_e above 300
- Stays within budget

Show your allocation table with projected outcomes for each metric.

**(d.2)** **Sensitivity analysis:**

For your proposed strategy, analyze sensitivity to:
- Corridor effectiveness (what if gene flow is 50% less than projected?)
- Translocation success (what if only 60% of translocated animals survive?)
- Cost overruns (what if actual costs are 25% higher?)
- Climate change (what if habitat carrying capacity declines 2% per year?)

Identify the parameter your strategy is most vulnerable to and propose adaptive management solutions.

**(d.3)** **Monitoring and adaptive management:**

Design a 10-year monitoring program:

**Genetic monitoring:**
- Which populations to sample? How many individuals?
- How frequently? (year 0, 3, 6, 10?)
- Which markers? (microsatellites? SNPs? whole genome?)
- What metrics to track? (H, F, N_e, allelic richness, F_ST)

**Decision triggers for adaptive management:**
- If H in Pop D drops below ____, do ____
- If F in any population exceeds ____, do ____
- If genetic differentiation (F_ST) exceeds ____, do ____
- If allelic richness declines by ____%, do ____

Define specific numeric thresholds and corresponding management actions.

**(d.4)** **Long-term sustainability (50-year horizon):**

Project the metapopulation genetics over 50 years (8-9 generations) under:
- **Scenario A:** Your proposed intervention implemented successfully
- **Scenario B:** Status quo (no intervention)
- **Scenario C:** Climate change drives 30% habitat loss by year 50

For each scenario, calculate:
- Total metapopulation size and N_e in year 50
- Average H across populations
- Probability of losing at least one population (assume P(extinction) ≈ 1 when N_e < 25 for >2 generations)
- Adaptive potential (measured by allelic richness and H)

Which scenario ensures long-term viability (>90% probability of persistence for 100 years)?

#### **Part E: Executive Summary**

**(e)** Write a comprehensive report for the Ministry of Environment (500-600 words) that includes:

**Section 1: Current Genetic Crisis (quantified)**
- Overall genetic health score
- Most threatened populations
- Projected timeline to critical thresholds

**Section 2: Recommended Strategy**
- Priority interventions (ranked 1-4)
- Budget allocation with justification
- Expected genetic outcomes (specific H and N_e targets)

**Section 3: Implementation Plan**
- Year-by-year actions
- Resource requirements
- Success metrics

**Section 4: Risk Mitigation**
- Identified risks with probability and impact
- Contingency plans
- Adaptive management triggers

**Section 5: Long-term Vision**
- 50-year goals (quantitative)
- Sustainability plan
- Research and monitoring needs

Use specific calculations from your analysis to support every recommendation. This document will determine conservation funding for the species.

---

## Summary of Problems

| Problem | Difficulty | Main Topic | Key Skills |
|---------|-----------|------------|-----------|
| 4.1 | ⭐ Easy | Hardy-Weinberg basics | Allele freq calc, genotype prediction |
| 4.2 | ⭐ Easy | Phenotype to genotype | Backward calculation, probability |
| 4.3 | ⭐ Easy | Multi-allele systems | ABO blood groups, 3-allele HWE |
| 4.4 | ⭐⭐ Moderate | Selection coefficients | Fitness, balanced polymorphism |
| 4.5 | ⭐⭐ Moderate | Conservation genetics | Effective pop size, heterozygosity loss |
| 4.6 | ⭐⭐ Moderate | Genetic counseling | Risk assessment, conditional probability |
| 4.7 | ⭐⭐ Moderate | Population structure | Wahlund effect, F-statistics |
| 4.8 | ⭐⭐⭐ Hard | Multi-locus selection | Epistasis, X-linkage, complex fitness |
| 4.9 | ⭐⭐⭐ Hard | Population admixture | Ancestry estimation, migration models |
| 4.10 | ⭐⭐⭐ Hard | Comprehensive rescue | Integration of all concepts |

---

**Total Coverage:**
- ✅ Hardy-Weinberg equilibrium calculations
- ✅ Single and multi-allele systems
- ✅ Selection coefficients and fitness
- ✅ Balancing selection and heterozygote advantage
- ✅ Effective population size
- ✅ Heterozygosity and inbreeding
- ✅ Conservation genetics applications
- ✅ Genetic counseling and medical genetics
- ✅ Population structure and admixture
- ✅ Epistasis and multi-locus interactions
- ✅ X-linked inheritance
- ✅ Genetic rescue program design
- ✅ Real Indian examples throughout

---

*Problems created for "The Pattern Hunters" by Dr. Alok Patel*  
*Chapter 4: Population Genetics in Practice - From Theory to Application*
