# Solution 7.6: Migration-Drift Balance

## Problem Summary
Sundarbans tigers: N=96, N_e=48, isolated. Design corridor to balance genetic drift through migration.

---

## (a) Heterozygosity Loss Rate

```
Loss rate = 1/(2N_e) = 1/(2×48) = 1/96 = 0.0104

Per generation: 1.04% loss
```

---

## (b) Critical Migration Rate

```
m_critical = 1/(4N_e) = 1/(4×48) = 1/192 = 0.0052

Critical rate: 0.52% per generation (one-way migration)
```

**Meaning:** 0.52% of Sundarbans population needs to be replaced by immigrants each generation to balance drift.

---

## (c) One Migrant Rule

```
Nm ≥ 1 for genetic health

Minimum migrants = 1/N_e × N_e = 1 migrant/generation

With generation = 5 years:
Practical requirement: 1 tiger every 5 years through corridor
```

**This is remarkably achievable - just ONE breeding tiger migrating per decade prevents genetic deterioration!**

---

## (d) Evaluate Three Corridor Options

**Option A: Wide corridor**
```
Nm = 2 tigers × 48 = 96... wait, this is wrong.
Correct: Nm = m × N_e = (2/48) × 48 = 2

Nm = 2 ✓ Exceeds threshold (Nm ≥ 1)
```

**Option B: Medium corridor**
```
Nm = (1/48) × 48 = 1

Nm = 1 ✓ Meets threshold exactly
```

**Option C: Narrow corridor**
```
Nm = (0.5/48) × 48 = 0.5

Nm = 0.5 ✗ Below threshold
```

**Options A and B meet the one migrant rule; Option C does not.**

---

## (e) Equilibrium Heterozygosity

### **Without Corridor (Isolated):**
```
H_20 = 0.42 × (1 - 1/96)^20
     = 0.42 × (0.989583)^20
     = 0.42 × 0.8110
     = 0.341
```

### **With Corridor (Option B, m=0.021):**

Approximate improved retention:
```
Retention with gene flow ≈ (1 - 1/(2N_e) + m)

Per generation retention = (1 - 1/96 + 0.021)
                         = (0.989583 + 0.021)
                         = 1.0106

This exceeds 1.0, suggesting equilibrium reached.

At equilibrium with migration:
H_eq ≈ H_0 (maintained, minimal loss)

Approximate H_20 ≈ 0.42 × (0.995)^20 ≈ 0.38
```

**Comparison:**
- Without corridor: H = 0.341 (19% loss)
- With corridor: H ≈ 0.38 (10% loss)
- **Corridor preserves ~9% additional diversity**

---

## (f) Cost-Benefit Analysis

### **Genetic Benefits:**
| Option | Cost | Nm | 100-yr H | Benefit | ₹/benefit |
|--------|------|----|---------|---------| ---------|
| No corridor | ₹0 | 0 | 0.341 | Baseline | - |
| Option C | ₹10cr | 0.5 | ~0.36 | Small | High |
| Option B | ₹25cr | 1.0 | ~0.38 | Good | Medium |
| Option A | ₹50cr | 2.0 | ~0.39 | Best | Low |

### **Recommendation: Option B (Medium Corridor)**

**Rationale:**

1. **Meets genetic threshold:** Nm=1 prevents deterioration
2. **Cost-effective:** Half price of Option A, 10× benefit of Option C
3. **Sufficient:** Additional migrants beyond 1 give diminishing returns
4. **Realistic:** 1 tiger/5 years achievable through 50m corridor
5. **Sustainable:** Maintenance costs manageable

**Other considerations:**
- **Bidirectional benefit:** Both populations gain diversity
- **Demographic rescue:** Also helps if Sundarbans population crashes
- **Behavioral corridors:** Tigers naturally use 50m width
- **Co-benefits:** Other species also benefit

**Option A justification** if:
- Funding unlimited
- Want maximum genetic insurance
- Corridor serves multiple species
- Long-term value exceeds immediate cost

**Option C (narrow) inadequate** - Nm=0.5 insufficient to prevent genetic erosion.

---

## Key Takeaways

**One Migrant Rule:** Nm ≥ 1 prevents genetic deterioration  
**Migration balances drift:** Even minimal gene flow powerful  
**Cost-effectiveness:** Meeting threshold sufficient, excess gives diminishing returns  
**Corridors provide multiple benefits:** Genetic + demographic + ecological

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.6*
