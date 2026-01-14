# Solution 7.8: Multi-Population Metapopulation Dynamics

## Problem Summary
Nilgiri Tahr across 5 isolated peaks. Analyze drift, plan corridors. Budget limited to ONE corridor.

---

## (a) Isolated Populations D and E

**Peak D (N_e=40, H_0=0.44):**
```
H_12 = 0.44 × (1-1/80)^12
     = 0.44 × (0.9875)^12
     = 0.44 × 0.860
     = 0.378
```

**Peak E (N_e=25, H_0=0.38):**
```
H_12 = 0.38 × (1-1/50)^12
     = 0.38 × (0.98)^12
     = 0.38 × 0.785
     = 0.298
```

**Results:**  
Peak D: 14% loss (378→0.378)  
Peak E: 22% loss - **CRITICAL!**

---

## (b) Peak E Crisis Analysis

**1. Loss rate:**
```
Loss per generation = 1/(2×25) = 0.02 (2% per gen)
```

**2. Time to H=0.30 threshold:**
```
0.30 = 0.38 × (0.98)^t
0.789 = (0.98)^t
t = ln(0.789)/ln(0.98) = 11.8 generations
```

**3. Convert to years:**
```
11.8 generations × 4 years = 47 years
```

**Peak E will fall below critical threshold in ~50 years without intervention.**

---

## (c) Corridor Option Analysis

### **Option 1: Connect C to D**

**Current state:**  
C receives 0.2 migrants/gen from D

**With corridor:**  
C receives 1.5 migrants/gen from D

**Calculate Nm for C:**
```
Nm = 1.5 × 50 = 75... No, wrong!
Nm = m × N_e = (1.5/50) × 50 = 1.5

Current Nm = 0.2
New Nm = 1.5 ✓ Exceeds threshold
```

**Benefit:** C improves from Nm=0.2 to Nm=1.5

### **Option 2: Connect D to B**

**Current state:**  
D is isolated (Nm=0)

**With corridor:**  
D receives 1.0 migrant/gen from B (H=0.62, N_e=150)

**Calculate Nm for D:**
```
Nm = 1.0 (exactly meets threshold)
```

**Benefit:** D improves from Nm=0 to Nm=1.0  
**Plus:** B is large, diverse donor (H=0.62 > D's 0.44)

### **Comparison:**

| Option | Recipient | Current Nm | New Nm | Donor Quality |
|--------|-----------|------------|--------|---------------|
| 1 | Peak C | 0.2 | 1.5 | D: small, low H |
| 2 | Peak D | 0 | 1.0 | B: large, high H |

**Recommendation: Option 2** - Rescues completely isolated D with high-quality donor.

---

## (d) Peak D with Gene Flow

**With m=0.025 from B:**
```
Improved retention ≈ (1 - 1/(2N_e) + m)^t
                    = (1 - 1/80 + 0.025)^12
                    = (0.9875 + 0.025)^12
                    = (1.0125)^12
                    = 1.161

This suggests growth, which is unrealistic. 
Better approximation: Gene flow reduces effective loss rate.

Effective loss with migration ≈ (1/(2N_e) - m)
= 0.0125 - 0.025 = -0.0125 (net gain!)

At equilibrium: H maintained near starting point
Estimate H_12 ≈ 0.44 × 0.95 ≈ 0.42

Much better than 0.378 without corridor!
```

---

## (e) Priority Ranking

Calculate genetic benefit for each:

**Option 1: Connect C to D**
```
Benefit = H_with - H_without
C without: H_12 = 0.48 × (0.99)^12 = 0.435
C with (Nm=1.5): H_12 ≈ 0.48 × 0.97 ≈ 0.466
Benefit ≈ 0.031
```

**Option 2: Connect D to B**
```
D without: H_12 = 0.378
D with: H_12 ≈ 0.42
Benefit ≈ 0.042
```

**Option 3: Enhance Peak E (N_e: 25→50)**
```
E current: H_12 = 0.298
E enhanced: H_12 = 0.38 × (0.99)^12 = 0.344
Benefit ≈ 0.046
```

**Option 4: Enhance Peak D (N_e: 40→80)**
```
D current: H_12 = 0.378
D enhanced: H_12 = 0.44 × (0.99375)^12 = 0.408
Benefit ≈ 0.030
```

**Ranking (highest benefit first):**
1. **Option 3** (Enhance E): 0.046 benefit - **Most critical!**
2. **Option 2** (Connect D-B): 0.042 benefit
3. **Option 1** (Connect C-D): 0.031 benefit
4. **Option 4** (Enhance D): 0.030 benefit

---

## (f) Management Plan

### **Priority 1: Immediate Action - Peak E Captive Breeding**

**Rationale:** Peak E (N_e=25) critically small, 47 years to threshold. Highest genetic benefit (0.046).

**Action:** Establish captive population, double effective breeders to N_e=50. Cost moderate, prevents near-term extinction.

### **Priority 2: Medium-term - Connect D to B**

**Rationale:** Peak D isolated, would benefit from large, diverse donor (B). Second-highest benefit (0.042). Provides long-term genetic rescue.

**Action:** Build corridor between D and B. More expensive but sustainable solution. Maintains natural gene flow indefinitely.

### **Priority 3: Long-term Monitoring - Peaks A, B, C**

**Rationale:** These populations relatively stable (N_e ≥ 50, some connectivity). Lower immediate risk.

**Action:** Monitor genetic diversity, maintain existing corridors, enhance if needed.

---

**25-generation projection:**
- **Peak E:** With enhancement, H drops to ~0.31 (acceptable)
- **Peak D:** With corridor, H ~0.40 (stable)
- **Peaks A-C:** Maintain H >0.55 (healthy)

**Without intervention:**
- **Peak E:** Likely genetic extinction (<0.25) within 25 gen
- **Peak D:** Severe loss (H ~0.35), approaching critical
- **All populations:** Continued fragmentation erosion

---

*Solution for The Pattern Hunters - Chapter 7, Problem 7.8*
