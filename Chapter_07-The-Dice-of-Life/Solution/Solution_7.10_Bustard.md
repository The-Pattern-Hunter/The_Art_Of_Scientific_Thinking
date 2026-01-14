# Solution 7.10: Great Indian Bustard - Comprehensive Case Study

## Problem Summary
Most critically endangered bird: 128 individuals across 4 fragmented populations. ₹100 crore budget. Design comprehensive conservation strategy.

---

## PART A: Population Viability Analysis

### (a.1) Harmonic Mean Across Metapopulation

**Treating separately (current reality):**
```
Each population evolves independently
Total genetic drift ≈ average of individual drifts
```

**If connected (hypothetical):**
```
Harmonic mean = 4 / (1/46 + 1/9 + 1/6 + 1/3)
              = 4 / (0.0217 + 0.111 + 0.167 + 0.333)
              = 4 / 0.633
              = 6.3

Treating as one population: N_e = 6.3
Treating as separate: Average N_e ≈ 16
```

**It matters enormously!** Fragmentation makes genetic situation 2-3× worse.

### (a.2) Population-Specific Projections

**Rajasthan (N_e=46, H=0.38):**
```
Loss rate = 1/92 = 0.011 (1.1% per generation)
H_10 = 0.38 × (1-1/92)^10 = 0.38 × 0.896 = 0.340
```

**Gujarat (N_e=9, H=0.22):**
```
Loss rate = 1/18 = 0.056 (5.6% per generation!)
H_10 = 0.22 × (1-1/18)^10 = 0.22 × 0.578 = 0.127
Below threshold!
```

**Maharashtra (N_e=6, H=0.18):**
```
Loss rate = 1/12 = 0.083 (8.3% per generation)
H_10 = 0.18 × (1-1/12)^10 = 0.18 × 0.387 = 0.070
FAR below threshold!
```

**Karnataka (N_e=3, H=0.12):**
```
Loss rate = 1/6 = 0.167 (16.7% per generation!)
H_10 = 0.12 × (1-1/6)^10 = 0.12 × 0.162 = 0.019
Genetic extinction imminent!
```

### (a.3) Time to Critical Threshold (H=0.15)

**Gujarat:**
```
0.15 = 0.22 × (1-1/18)^t
t = ln(0.682) / ln(0.944) = 6.6 generations (26 years)
```

**Maharashtra:**
```
0.15 = 0.18 × (1-1/12)^t
t = ln(0.833) / ln(0.917) = 2.1 generations (8 years!)
```

**Karnataka:**
```
Already below threshold (H=0.12 < 0.15)
Immediate crisis!
```

---

## PART B: Intervention Design

### (b.1) Captive Breeding Program

**Founder selection strategy:**

Maximize diversity while managing risk:
- **Rajasthan:** 15 founders (largest, most diverse)
- **Gujarat:** 8 founders (moderate, preserve unique alleles)
- **Maharashtra:** 5 founders (smaller, urgent)
- **Karnataka:** 2 founders (critically small, high risk)
- **Total:** 30 individuals

**Breeding protocol to minimize N_e loss:**
- Equalize family sizes (each pair contributes equally)
- Avoid breeding siblings
- Genetic management software (minimize inbreeding)
- Target N_e ≥ 20 in captivity

**Expected N_e:**
```
With 30 individuals, equal family sizes:
N_e ≈ N - 1 = 29 (if perfectly managed)
Realistic: N_e ≈ 20 (accounting for unequal reproduction)
```

**Project captive H after 5 generations:**
```
Starting H ≈ weighted average = 0.32
H_5 = 0.32 × (1-1/40)^5 = 0.32 × 0.882 = 0.282
```

### (b.2) Habitat Corridors

**Option A: Major corridor (Rajasthan-Gujarat)**
```
Combined: N_census = 110, N_e ≈ 65
Gene flow: 1-2 birds/generation
Nm = 2 ✓ Good genetic connection
Cost: ₹40 crores
Benefit: Rescues Gujarat, stabilizes both
```

**Option B: Three minor corridors**
```
Gujarat-Maharashtra: Nm ≈ 0.4
Maharashtra-Karnataka: Nm ≈ 0.3
Karnataka-Rajasthan: Nm ≈ 0.5
Total cost: ₹36 crores
Benefit: Connects all, but each link weak (Nm < 1)
```

**Comparison:**
- **Option A:** Strong single connection, proven effective
- **Option B:** Broader network, but individual links insufficient

**Recommendation: Option A** - Stronger genetic impact, focuses on two viable populations.

### (b.3) Translocation Program

**Scenario 1: Rajasthan → Gujarat (4 birds)**
```
Gujarat: N_e = 9 → 13 (44% increase)
Rajasthan: N_e = 46 → 42 (minimal impact)

Gujarat H_10: 0.22 × (1-1/26)^10 = 0.188 (vs 0.127 baseline)
Benefit: 0.061 improvement
```

**Scenario 2: Rajasthan → All small (2 birds each to Gujarat, Maharashtra, Karnataka)**
```
Gujarat: N_e = 9 → 11
Maharashtra: N_e = 6 → 8
Karnataka: N_e = 3 → 5
Rajasthan: N_e = 46 → 40

Total benefit ≈ 0.08 (across all populations)
```

**Scenario 2 provides greater total genetic benefit** by improving multiple populations.

---

## PART C: Integrated Management Strategy

### (c.1) Budget Allocation

| Investment | Cost (₹ Crores) | Genetic Benefit | Priority |
|------------|----------------|-----------------|----------|
| Captive breeding | 30 | 0.05 (insurance) | Essential |
| Major corridor (A) | 40 | 0.08 (Gujarat rescue) | High |
| Translocation (2×3) | 15 | 0.08 (3 pops) | High |
| Habitat protection (2 sites) | 20 | 0.03 (sustain) | Medium |
| **TOTAL** | **105** | - | **Over budget!** |

**Adjusted allocation (within ₹100 crores):**

| Investment | Cost | Rationale |
|------------|------|-----------|
| Captive breeding | ₹30cr | Non-negotiable (insurance) |
| Major corridor | ₹40cr | Highest single benefit |
| Translocation (2 events) | ₹10cr | Cost-effective boost |
| Habitat protection (Rajasthan) | ₹10cr | Protect core population |
| Power line mitigation | ₹8cr | Reduce mortality |
| **TOTAL** | **₹98cr** | ✓ Within budget |

**Expected genetic outcomes (10 years):**
- **Rajasthan:** H = 0.36 (stable, protected)
- **Gujarat:** H = 0.20 (improved with corridor/translocation)
- **Maharashtra:** H = 0.14 (critical, needs follow-up)
- **Karnataka:** H = 0.08 (likely extirpation)
- **Captive:** H = 0.28 (insurance population)

### (c.2) Risk Analysis

**Genetic risks (all HIGH):**
- Inbreeding accumulation: 2-3% per generation in small pops
- Loss of adaptive potential: Already lost 60% original diversity
- Genetic swamping: Translocation could homogenize populations

**Mitigation:** Genetic monitoring, pedigree tracking, diverse founders

**Demographic risks (HIGH-MEDIUM):**
- Allee effects: Fewer males → reduced breeding success
- Catastrophic events: Drought can kill 20% in one year
- Human conflict: Power lines kill 10-15% annually

**Mitigation:** Power line markers, habitat protection, captive population

**Management risks (MEDIUM):**
- Budget cuts: Phase interventions, front-load essential work
- Political changes: Long-term MoU, multi-state coordination
- Technical failures: Redundancy in captive facilities, backup plans

### (c.3) Monitoring Protocol

**Genetic monitoring (every 3 years):**
- Heterozygosity (microsatellites)
- Effective population size (genetic + demographic)
- Inbreeding coefficient
- Allelic richness
- Pedigree tracking
- Population structure (FST)

**Demographic monitoring (annual):**
- Census counts (all populations)
- Breeding success (clutch size, fledging rate)
- Survival rates (chick, juvenile, adult)
- Habitat quality (grassland extent, disturbance)

**Decision triggers:**
- **H <0.15 in any population:** Immediate genetic rescue
- **N_e <5:** Urgent translocation or captive removal
- **Breeding success <0.5 chicks/pair:** Investigate causes
- **Mortality >20% annually:** Emergency intervention

---

## PART D: Executive Summary for Ministry

### Current Genetic Status

The Great Indian Bustard faces imminent genetic extinction despite 128 individuals remaining. **Quantitative assessment:**

- **Overall effective population:** Harmonic mean N_e = 6.3 (fragmentation makes 128 birds genetically equivalent to 6-7 random breeders)
- **Genetic diversity:** Current H = 0.38 (Gujarat), 0.22 (Rajasthan), 0.18 (Maharashtra), 0.12 (Karnataka) - representing **60% loss** from historical baseline (H = 0.68)
- **Most at-risk populations:** Maharashtra (8 years to critical threshold), Karnataka (already below threshold)

**Comparison to baseline:** Current diversity = 40% of 1960s levels. This is comparable to cheetah bottleneck (most genetically depauperate bird in India).

### Recommended Actions (Priority Ranked)

**1. Establish captive breeding program (₹30 crores) - ESSENTIAL**
- 30 founders from all populations
- Target N_e ≥ 20
- Insurance against wild extinction
- Timeline: Year 1

**2. Build Rajasthan-Gujarat corridor (₹40 crores) - HIGH PRIORITY**
- Rescues Gujarat population (26 years to threshold)
- Creates viable meta-population (combined N_e = 65)
- Enables natural gene flow
- Timeline: Years 1-3

**3. Implement translocation program (₹10 crores) - HIGH PRIORITY**
- Transfer 2 birds from Rajasthan to each small population
- Increases N_e by 30-60% in recipients
- Provides immediate genetic boost
- Timeline: Years 2-4

**4. Habitat protection - Rajasthan core (₹10 crores) - MEDIUM PRIORITY**
- Protect largest population (70% of total)
- Ensure breeding habitat security
- Foundation for recovery
- Timeline: Years 1-10

**5. Power line mitigation (₹8 crores) - MEDIUM PRIORITY**
- Reduces mortality 10-15% → 5%
- Demographic benefit supports genetic health
- Multiple sites
- Timeline: Years 2-5

**Budget: ₹98 crores (within ₹100 crore allocation)**

### Long-Term Viability Projections

**25-year realistic outcome (with full intervention):**
- **Rajasthan:** 100-120 birds, H = 0.34 (stable, core population)
- **Gujarat:** 30-40 birds, H = 0.22 (improved with corridor)
- **Maharashtra:** 15-20 birds, H = 0.16 (marginally viable)
- **Karnataka:** 0-5 birds, H = 0.10 (likely extirpation)
- **Captive:** 100+ birds, H = 0.26 (insurance)
- **Total wild:** 145-185 birds

**Best-case scenario (full funding + optimal conditions):**
- Metapopulation of 250+ birds
- H maintained >0.30 across populations
- Self-sustaining without ongoing genetic rescue

**Worst-case scenario (business as usual, no intervention):**
- Maharashtra extinct by 2033 (8 years)
- Karnataka extinct by 2028 (3 years)
- Gujarat critically inbred by 2051
- Rajasthan slowly declining
- Total population <80 by 2050, genetic extinction inevitable

### Call to Action

**Why immediate action is essential:**
Current trajectory leads to genetic extinction within 25-50 years despite demographic presence. **We have an 8-year window** to prevent Maharashtra extirpation and establish viable captive insurance.

**What happens if we wait 5 years:**
- Maharashtra likely extinct (below rescue threshold)
- Karnataka extinct (too small)
- 20-30% additional diversity lost
- Intervention cost doubles (emergency rescue more expensive)

**Measurable 10-year goals:**
1. **Genetic:** Maintain H >0.30 in Rajasthan, >0.20 in Gujarat
2. **Demographic:** Achieve 180+ wild birds, 100+ captive
3. **Connectivity:** Functional Raj-Gujarat corridor (≥1 migrant/year)
4. **Viability:** No population extinct; all N_e >8

**The Great Indian Bustard is India's most genetically imperiled bird. Action within 2 years determines whether this species survives the century.**

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.10*
*Most comprehensive conservation genetics problem in textbook*
