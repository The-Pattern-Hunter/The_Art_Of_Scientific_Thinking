# Solution 7.5: Population Bottleneck and Recovery

## Problem Summary
Asiatic Lions: Severe bottleneck 1900-1930 (N: 500→20→100), recovered to 200-500. Measure permanent genetic damage.

---

## Question (a): Harmonic Mean

**Bottleneck generations (5 total):**
```
N: 20, 30, 50, 100, 200

Harmonic mean = 5 / (1/20 + 1/30 + 1/50 + 1/100 + 1/200)
              = 5 / (0.0500 + 0.0333 + 0.0200 + 0.0100 + 0.0050)
              = 5 / 0.1183
              = 42.3
```

**Result: N_e(harmonic) = 42.3**

**Key insight:** Harmonic mean (42.3) heavily weighted by smallest value (20), not arithmetic mean (80).

---

## Question (b): Heterozygosity After Bottleneck

```
H_5 = H_0 × (1 - 1/(2N_harmonic))^5
    = 0.70 × (1 - 1/84.6)^5
    = 0.70 × (0.988178)^5
    = 0.70 × 0.9421
    = 0.659
```

**Loss during bottleneck:** 4.1% (from 0.70 to 0.659)

---

## Question (c): Current Heterozygosity (After Recovery)

**Post-bottleneck (N_e=300, 18 generations):**
```
H_current = H_5 × (1 - 1/600)^18
          = 0.659 × (0.998333)^18
          = 0.659 × 0.9703
          = 0.639
```

**Predicted current: H = 0.639**

---

## Question (d): Compare to Observed (H=0.35)

**Predicted:** 0.639  
**Observed:** 0.35  
**Discrepancy:** Large (45% lower than predicted!)

**Possible explanations:**

1. **Effective population overestimated:** Actual N_e likely much smaller than 300 census average
2. **Additional bottlenecks:** Other population crashes not in historical record
3. **Social structure:** Lion prides reduce N_e below census (few breeding males)
4. **Inbreeding:** Close relatives forced to breed, accelerating loss

**What this tells us:**
- Bottleneck impact **worse than simple model**
- Population counting insufficient
- Social dynamics reduce genetic health
- Recovery in numbers ≠ genetic recovery

---

## Question (e): Response to Colleague

**Statement:** "Lions are fine now - 500 of them! Bottleneck was 100 years ago."

**Response:**

"This is incorrect for three critical reasons supported by our calculations:

**1. Permanent genetic loss during bottleneck:**
The harmonic mean effective size was only 42 individuals over 5 generations. We lost diversity that can NEVER be recovered naturally. Our calculations show the bottleneck alone cost 4% of genetic diversity permanently.

**2. No genetic recovery with population growth:**
Increasing from 100 to 500 lions doesn't restore lost alleles. Once an allele is lost through drift, it's gone forever unless reintroduced. The lions recovered demographically but remained genetically impoverished.

**3. Ongoing diversity loss:**
Even at 500 census (maybe N_e=150-200), we continue losing 0.25-0.33% diversity per generation. The observed heterozygosity (0.35) is 50% lower than pre-bottleneck (0.70), meaning lions have lost HALF their genetic toolkit. This makes them vulnerable to disease, reduces fertility, and limits adaptive potential."

---

## Question (f): No-Bottleneck Scenario

**Hypothetical:** N=500 continuously for 26 generations (1890-2020)

```
H_2020 = 0.70 × (1 - 1/1000)^26
       = 0.70 × (0.999)^26
       = 0.70 × 0.9743
       = 0.682
```

**Comparison:**
- **Without bottleneck:** H = 0.682 (only 2.6% loss)
- **With bottleneck (predicted):** H = 0.639 (8.7% loss)
- **With bottleneck (observed):** H = 0.35 (50% loss!)

**Permanent cost of bottleneck:**
```
Minimum genetic cost: 0.682 - 0.639 = 0.043 (6.3% additional loss)
Actual genetic cost: 0.682 - 0.35 = 0.332 (47.4% additional loss!)
```

**The bottleneck cost Asiatic lions ~47% of genetic diversity that would have been retained without it - damage that persists over a century later.**

---

## Key Takeaways

**Harmonic mean < Arithmetic mean** when values variable  
**Bottlenecks create permanent damage** - no demographic recovery  
**Social structure reduces N_e** below census significantly  
**One generation at N=20 ≈ Five generations at N=100** in genetic impact

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.5*
