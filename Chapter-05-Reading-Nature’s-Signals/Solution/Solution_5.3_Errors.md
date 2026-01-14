# Solution 5.3: Type I and Type II Errors

## Question (a): 2×2 Decision Table

|  | **Reality A: No Effect** | **Reality B: Real Effect** |
|---|---|---|
| **Decision 1: Conclude "No Effect"** | Correct Decision (True Negative) | Type II Error (False Negative) |
| **Decision 2: Conclude "Effect Exists"** | Type I Error (False Positive) | Correct Decision (True Positive) |

---

## Question (b): Error Labels and Definitions

### Correct Decisions (2 cells)

**Cell: Reality A + Decision 1**
- **Reality:** Collar does NOT affect movement
- **Decision:** Conclude no effect
- **Result:** ✅ Correct - True Negative

**Cell: Reality B + Decision 2**
- **Reality:** Collar DOES affect movement
- **Decision:** Conclude effect exists
- **Result:** ✅ Correct - True Positive

### Type I Error (α = False Positive)

**Cell: Reality A + Decision 2**
- **Reality:** Collar does NOT affect movement
- **Decision:** Conclude effect exists
- **Result:** ❌ Type I Error - False alarm, "crying wolf"
- **Probability:** α = 0.05 (5%)

### Type II Error (β = False Negative)

**Cell: Reality B + Decision 1**
- **Reality:** Collar DOES affect movement
- **Decision:** Conclude no effect
- **Result:** ❌ Type II Error - Missed detection
- **Probability:** β = 0.30 (30% in this study)
- **Power:** 1 - β = 0.70 (70%)

---

## Question (c): Practical Consequences

### Type I Error Consequence (False Positive)

**What happens:**
- Conclude collar affects movement when it actually doesn't
- Abandon a perfectly good collar design unnecessarily
- Invest resources redesigning collar when current one is fine

**Conservation impact:**
- **Wasted resources:** Money and time spent on unnecessary redesign
- **Delayed deployment:** Fewer leopards tracked while redesigning
- **Opportunity cost:** Could have used resources for other conservation needs
- **Minimal harm to leopards:** Current collar is actually fine

**Severity:** MODERATE - Wastes resources but doesn't harm leopards

---

### Type II Error Consequence (False Negative)

**What happens:**
- Conclude collar is fine when it actually affects movement
- Continue using collar that disturbs natural behavior
- Collect biased/invalid data on leopard ecology

**Conservation impact:**
- **Biased research:** Movement data doesn't reflect natural behavior
- **Wrong conservation decisions:** Plans based on flawed data
- **Welfare concerns:** Leopards stressed/hindered by collar
- **Scientific integrity:** Published research based on artifact not reality
- **Policy implications:** Government makes wrong habitat decisions

**Severity:** HIGH - Directly harms leopards and invalidates research

---

## Question (d): Which Error is More Serious?

**Answer: Type II Error (False Negative) is more serious in this context**

**Reasoning:**

### Type II Error is Worse Because:

**1. Animal Welfare**
- Directly harms leopards by using problematic collar
- Causes ongoing stress/movement restriction
- Affects 100% of collared animals

**2. Scientific Validity**
- All data collected is biased/invalid
- Cannot correct published papers retroactively
- Other researchers may use flawed data

**3. Conservation Effectiveness**
- Decisions based on bad data lead to poor outcomes
- May choose wrong habitat corridors
- Resources misallocated based on artifact

**4. Ongoing vs One-time Cost**
- Type I: One-time cost of redesign
- Type II: Continuous harm as long as collar used

### Type I Error is More Acceptable Because:

**1. Precautionary Principle**
- Better safe than sorry when animal welfare involved
- Can always test new design
- Reversible decision

**2. Limited Immediate Harm**
- No leopards harmed by being cautious
- Just delayed data collection

**3. Science Self-Corrects**
- Future studies might reveal collar was fine
- Can resume using original design if validated

### Risk-Benefit Trade-off:
- Type I: Waste money/time (recoverable)
- Type II: Harm animals + invalid science (not recoverable)

**Verdict:** In wildlife research, prioritize avoiding harm to animals (minimize Type II error), even at cost of some false alarms (accept higher Type I error rate).

---

## Question (e): Expected Outcomes in 100 Studies

**Given:**
- α = 0.05 (5% Type I error rate)
- Power = 0.70 → β = 0.30 (30% Type II error rate)
- **True state:** Collar has NO effect (Reality A)

### If Reality A is True (No Effect):

**Expected outcomes over 100 studies:**

**Correct conclusion "no effect":**
- Probability: 1 - α = 0.95
- **Expected: 95 studies** ✅

**Incorrect conclusion "effect exists" (Type I error):**
- Probability: α = 0.05
- **Expected: 5 studies** ❌

### Breakdown:
```
100 studies where collar truly has no effect
├── 95 studies: Correctly conclude "no effect" (True Negative)
└── 5 studies: Incorrectly conclude "effect exists" (False Positive)
```

### Important Note:

The power (70%) and Type II error (30%) are **NOT relevant** here because:
- Power applies only when **real effect exists** (Reality B)
- We specified Reality A (no effect)
- Type II error cannot occur when H₀ is actually true

**If Reality B were true instead (collar does affect movement):**
```
100 studies where collar truly affects movement
├── 70 studies: Correctly conclude "effect exists" (True Positive - POWER)
└── 30 studies: Incorrectly conclude "no effect" (False Negative - Type II)
```

---

## Key Concepts Summary

### Type I Error (α = False Positive)
- **Definition:** Reject H₀ when H₀ is actually true
- **Common name:** "Crying wolf"
- **Typically set at:** α = 0.05 (5%)
- **Consequence:** False alarm, wasted resources

### Type II Error (β = False Negative)
- **Definition:** Fail to reject H₀ when H₁ is actually true
- **Common name:** "Missing the wolf"
- **Related to:** Power = 1 - β
- **Consequence:** Miss real effect, incorrect conclusion

### Power (1 - β = True Positive Rate)
- **Definition:** Probability of correctly detecting real effect
- **Influenced by:** Sample size, effect size, α level, variability
- **Typical target:** 80% (β = 0.20)
- **This study:** 70% (β = 0.30) - slightly underpowered

### Trade-offs:
- **Decrease α → Increase β** (more conservative, less power)
- **Increase sample size → Decrease both α and β** (better all around)
- **Larger effect → Easier to detect** (decreases β)

### Context Matters:
- **Medicine:** Type II very serious (miss disease)
- **Screening:** Type I acceptable (false alarm better than missed diagnosis)
- **Wildlife:** Type II serious (harm animals, invalid research)
- **Fundamental research:** Balance both errors

---

## Common Mistakes

**Mistake 1:** "5% p-value means 5% chance of being wrong"
- **Wrong:** α = probability of Type I error IF H₀ true, not probability H₀ is true

**Mistake 2:** "Non-significant means no effect"
- **Wrong:** Could be Type II error (real effect but insufficient power)

**Mistake 3:** "Significant means important"
- **Wrong:** Statistical significance ≠ practical significance

**Mistake 4:** Focusing only on Type I error
- **Wrong:** Type II error equally important, depends on context

---

*Solution for The Pattern Hunters - Chapter 5, Problem 5.3*
