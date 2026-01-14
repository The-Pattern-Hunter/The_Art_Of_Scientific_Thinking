# Solution 7.4: Heterozygosity Loss in Small Populations

## Problem Summary
Manipur Brow-antlered Deer: N=260, N_e=65, H_0=0.45, generation=5 years. Project diversity loss over 100 years (20 generations).

---

## Question (a): Loss Rate Per Generation

```
Loss rate = 1 / (2N_e) = 1 / (2×65) = 1/130 = 0.00769

Per generation loss: 0.769%
```

---

## Question (b): Heterozygosity After 20 Generations

```
H_t = H_0 × (1 - 1/(2N_e))^t
H_20 = 0.45 × (1 - 1/130)^20
     = 0.45 × (0.992308)^20
     = 0.45 × 0.8558
     = 0.385
```

**Result: H_20 = 0.385**

---

## Question (c): Percentage Loss

```
Percentage loss = (H_0 - H_20) / H_0 × 100%
                = (0.45 - 0.385) / 0.45 × 100%
                = 0.065 / 0.45 × 100%
                = 14.4%
```

**14.4% of genetic diversity lost over 100 years**

---

## Question (d): Compare Three Scenarios

### **Scenario 1: Status Quo (N_e=65)**
Already calculated: H_20 = 0.385

### **Scenario 2: Population Doubling (N_e=130)**
```
H_20 = 0.45 × (1 - 1/260)^20
     = 0.45 × (0.996154)^20
     = 0.45 × 0.9255
     = 0.416
```

### **Scenario 3: Genetic Rescue (N_e=90)**
```
H_20 = 0.45 × (1 - 1/180)^20
     = 0.45 × (0.994444)^20
     = 0.45 × 0.8943
     = 0.402
```

### **Comparison:**

| Scenario | N_e | H_20 | Loss | Improvement |
|----------|-----|------|------|-------------|
| Status Quo | 65 | 0.385 | 14.4% | Baseline |
| Doubling | 130 | 0.416 | 7.5% | +6.9% preserved |
| Rescue | 90 | 0.402 | 10.7% | +3.7% preserved |

**Scenario 2 (doubling) preserves most diversity: 6.9% additional retention**

---

## Question (e): Time to Critical Threshold

**Threshold:** H = 0.35  
**Starting:** H_0 = 0.45  
**Scenario 1:** N_e = 65

**Solve for t:**
```
0.35 = 0.45 × (1 - 1/130)^t
0.35/0.45 = (0.992308)^t
0.7778 = (0.992308)^t

Taking natural log both sides:
ln(0.7778) = t × ln(0.992308)
-0.2513 = t × (-0.007715)
t = 32.6 generations
```

**Result: ~33 generations (165 years)**

**Urgency:** Falls below threshold in 165 years without intervention

---

## Question (f): Recommendation

**Recommend: Scenario 2 (Population Doubling)**

**Rationale:**

1. **Best genetic outcome:** Preserves 92.5% diversity (vs 85.6% status quo)
2. **Exceeds threshold:** H=0.416 stays well above H=0.35
3. **Long-term viability:** Slower ongoing loss (0.38% vs 0.77% per generation)
4. **Sustainable:** Doubles effective breeders through habitat/management

**Implementation:** Focus on increasing breeding individuals through:
- Habitat expansion
- Reducing human disturbance during breeding
- Protecting breeding females and territories
- Possibly supplementing from captive breeding

Genetic rescue (Scenario 3) useful but less effective than doubling effective population.

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.4*
