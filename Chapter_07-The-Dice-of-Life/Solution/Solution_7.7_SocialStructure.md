# Solution 7.7: Social Structure and Effective Population Size

## Problem Summary
Three elephant populations (N=100) with different breeding structures. Compare genetic impacts.

---

## (a) Calculate N_e

**Population A (Random Mating):**
```
N_e = (4×50×50)/(50+50) = 10,000/100 = 100
```

**Population B (Typical):**
```
N_e = (4×10×40)/(10+40) = 1,600/50 = 32
```

**Population C (Extreme Hierarchy):**
```
N_e = (4×2×30)/(2+30) = 240/32 = 7.5
```

---

## (b) N_e/N Ratios

```
Population A: 100/100 = 1.00 (100%)
Population B: 32/100 = 0.32 (32%)
Population C: 7.5/100 = 0.075 (7.5%)
```

**Interpretation:**  
**Pop A:** Perfectly efficient (ideal)  
**Pop B:** 68% genetic loss due to structure  
**Pop C:** 92.5% genetic loss - extreme inefficiency!

---

## (c) Drift Variance

```
σ² = pq/(2N_e) = 0.25/(2N_e)

Population A: σ² = 0.25/200 = 0.00125
Population B: σ² = 0.25/64 = 0.00391 (3.1× larger)
Population C: σ² = 0.25/15 = 0.0167 (13.3× larger!)
```

---

## (d) Standard Deviations and Ranges

```
σ = √σ²

Pop A: σ = 0.0354 (3.5%), range: 0.465-0.535
Pop B: σ = 0.0625 (6.3%), range: 0.438-0.563
Pop C: σ = 0.129 (12.9%), range: 0.371-0.629
```

**Population C shows ±13% random swings per generation - extreme!**

---

## (e) Heterozygosity After 10 Generations

```
H_10 = H_0 × (1 - 1/(2N_e))^10

Pop A: H_10 = 0.60 × (1-1/200)^10 = 0.60 × 0.951 = 0.571 (4.9% loss)
Pop B: H_10 = 0.60 × (1-1/64)^10 = 0.60 × 0.852 = 0.511 (14.8% loss)
Pop C: H_10 = 0.60 × (1-1/15)^10 = 0.60 × 0.513 = 0.308 (48.7% loss!)
```

**Population C loses HALF its diversity in just 10 generations due to breeding structure.**

---

## (f) Management Interventions

### **Strategy 1: Double Census (maintain structure)**
```
New: N=200, but still 2 males, 30 females breeding

N_e = (4×2×30)/(2+30) = 240/32 = 7.5

NO CHANGE in N_e!
```

### **Strategy 2: Improve Breeding Structure**
```
Keep N=100, but 10 males (not 2), 30 females

N_e = (4×10×30)/(10+30) = 1,200/40 = 30

N_e increases from 7.5 to 30 (4× improvement!)
```

### **Comparison:**

| Strategy | N | N_e | H_10 | Improvement |
|----------|---|-----|------|-------------|
| Current | 100 | 7.5 | 0.308 | Baseline |
| Strategy 1 | 200 | 7.5 | 0.308 | 0% |
| Strategy 2 | 100 | 30 | 0.505 | +64% diversity retained! |

**Strategy 2 (improve breeding) vastly superior to Strategy 1 (increase census).**

---

## Why Breeding Structure > Population Size

**Fundamental principle:** N_e depends on NUMBER of breeders, not total population

**Strategy 1 failure:**
- Added 100 non-breeding individuals
- Same 2 males monopolize breeding
- Zero genetic benefit
- Wasted resources

**Strategy 2 success:**
- Same total population
- 5× more breeding males
- 4× higher N_e
- Massive genetic benefit

**Implementation methods:**
- Break up male dominance hierarchies
- Rotate breeding bulls
- Manage territories to reduce competition
- Translocate dominant males temporarily

**This is cheaper and more effective than doubling population!**

---

## Key Takeaways

**Social structure dramatically reduces N_e**  
**Breeding structure > census size** for genetics  
**Management can improve N_e** without increasing N  
**Behavioral interventions cost-effective**

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.7*
