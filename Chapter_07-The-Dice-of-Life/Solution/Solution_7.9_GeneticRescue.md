# Solution 7.9: Genetic Rescue Program Design

## Problem Summary
Pygmy Hog: 6 founders (1996), now 76 captive + 150 wild, H=0.28 (vs H_original=0.72). Design genetic rescue.

---

## (a) Verify Bottleneck Impact

**Phase 1: Founding (N_e=3, 1 generation):**
```
H_1 = 0.72 × (1-1/6)^1 = 0.72 × 0.833 = 0.60
```

**Phase 2: Captive breeding (N_e=30, 7 generations):**
```
H_8 = 0.60 × (1-1/60)^7
    = 0.60 × (0.983)^7
    = 0.60 × 0.891
    = 0.535
```

**Predicted: 0.535**  
**Observed: 0.28**  
**Discrepancy: Large (48% lower!)**

**Possible explanations:**
1. Founders more inbred than estimated (effective N_e < 3)
2. Captive breeding less effective (actual N_e < 30)
3. Additional bottlenecks during breeding program
4. Selection against less fit genotypes

**Conclusion:** Bottleneck impact worse than simple model predicts. Actual N_e likely half of estimates.

---

## (b) Evaluate Source Populations

### **Source A: Bangalore Captive**

**Genetic benefit:**
```
H_new = 0.9×0.28 + 0.1×0.30 = 0.252 + 0.030 = 0.282
Gain: 0.002 (minimal)
```

**Risk:** Low (8% divergence, same stock)  
**Feasibility:** Easy (domestic transfer)  
**Assessment:** Little benefit - sibling population, same problem

### **Source B: Bhutan Wild**

**Genetic benefit:**
```
H_new = 0.9×0.28 + 0.1×0.55 = 0.252 + 0.055 = 0.307
Gain: 0.027 (moderate)
```

**Risk:** Moderate (12% divergence, different subspecies)  
**Feasibility:** Difficult (international, wild capture)  
**Assessment:** Good benefit, manageable risk

### **Source C: Museum Genomics**

**Genetic benefit:**
```
H_new = 0.9×0.28 + 0.1×0.65 = 0.252 + 0.065 = 0.317
Gain: 0.037 (highest)
```

**Risk:** High (technical failure, unknown viability)  
**Feasibility:** Very difficult (experimental technology)  
**Assessment:** Best genetic benefit but risky and expensive

### **Comparison Table:**

| Source | H_new | Gain | Risk | Feasibility | Cost |
|--------|-------|------|------|-------------|------|
| A | 0.282 | 0.002 | Low | Easy | ₹20L |
| B | 0.307 | 0.027 | Moderate | Difficult | ₹80L |
| C | 0.317 | 0.037 | High | Very difficult | ₹500L |

---

## (c) Rescue Design (Source B)

### **Scenario 1: Single Large Introduction (10 individuals, Year 0)**

**Immediate gain:**
```
H_new = 0.9×0.28 + 0.1×0.55 = 0.307
```

**After 10 generations (no more migration):**
```
Assume N_e increases to 70 (immigration + mixing)
H_10 = 0.307 × (1-1/140)^10 = 0.307 × 0.931 = 0.286
```

### **Scenario 2: Repeated Small Introductions (2 per 2 gen, 5 times)**

**Year 0:** H = 0.28  
**Year 6 (3 gen later, first intro):** H ≈ 0.28 × 0.96 = 0.269, then boost to 0.28  
**Year 12:** Similar, H maintained ~0.28-0.29  
**After 10 generations:** H ≈ 0.29

**Comparison:**
- **Scenario 1:** Higher initial boost, then declines to 0.286
- **Scenario 2:** Sustained support, maintains ~0.29

**Recommendation: Scenario 2 (repeated)** - Provides ongoing gene flow, more sustainable.

---

## (d) 20-Generation Projection

**Without rescue (N_e=60, H_0=0.28):**
```
H_20 = 0.28 × (1-1/120)^20 = 0.28 × 0.847 = 0.237
```

**With rescue (N_e=75, H_0=0.307):**
```
H_20 = 0.307 × (1-1/150)^20 = 0.307 × 0.875 = 0.269
```

**Genetic benefit: 0.269 - 0.237 = 0.032 (3.2% additional retention)**

---

## (e) Economic Analysis

**Calculate benefit per crore:**

**Source A:** 0.002 / 0.20 = 0.010 per crore  
**Source B:** 0.032 / 0.80 = 0.040 per crore ⭐ **Best ROI**  
**Source C:** 0.037 / 5.00 = 0.007 per crore

**Source B provides best return on investment despite higher absolute cost.**

---

## (f) Risk-Benefit Analysis (Source B)

### **Risks:**

**1. Outbreeding depression (15% probability, moderate impact)**
- First generation hybrids may have reduced fitness
- Mitigation: Monitor F1 survival/reproduction closely
- Usually resolves by F2 generation

**2. Disease introduction (5% probability, severe impact)**
- Bhutan hogs might carry novel pathogens
- Mitigation: Quarantine 6 months, full veterinary screening
- Biosecurity protocols

**3. Behavioral incompatibility (10% probability, low impact)**
- Bhutan hogs may have different social behaviors
- Mitigation: Gradual introduction, monitor integration
- Past translocation experience

### **Risk-Benefit Assessment:**

**Quantified risks:**
```
Expected cost of failure = Σ(Probability × Impact)
≈ 0.15×0.3 + 0.05×0.8 + 0.10×0.2 = 0.045 + 0.040 + 0.020 = 0.105

Expected benefit = 0.032 (genetic gain)
Net expected benefit = 0.032 - 0.105×0.032 = 0.029
```

**Recommendation: Proceed with caution**

Genetic rescue justified because:
1. Net positive benefit expected
2. Without rescue, population approaches genetic extinction
3. Risks manageable with proper protocols
4. Alternative (do nothing) guarantees genetic erosion

**Implement with:**
- Extensive health screening
- Gradual introduction protocol
- Intensive monitoring program
- Contingency plans

---

## (g) Monitoring Plan

**Metrics (measure every 2 years):**
1. Heterozygosity (microsatellites, 15 loci)
2. Allelic richness (number of alleles per locus)
3. Inbreeding coefficient (F)
4. Effective population size (N_e, genetic estimate)
5. Reproductive success (offspring per female)
6. Survival rates (by age class)

**Success indicators:**
- H stable or increasing (≥0.28)
- N_e >60
- Reproductive success normal (1.5 offspring/female)
- No disease outbreaks

**Failure indicators:**
- H declining despite rescue
- Increased mortality in F1
- Disease outbreak
- Reproductive incompatibility

**Decision triggers:**
- If H <0.25 by Year 10: Implement second rescue
- If survival <70% in F1: Halt further introductions, investigate
- If successful: Expand to 10 immigrants by Year 15

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.9*
