# Solution 5.1: Understanding P-values

## Problem Summary
Dr. Meera tests a blood pressure medication (n=50), finds mean decrease from 145 to 138 mmHg (7 mmHg reduction), with p = 0.03.

---

## Question (a): Evaluate Statements

### Statement A: "There is a 3% probability that the medication has no effect."
**❌ INCORRECT**

**Why wrong:** P-value is NOT the probability that H₀ is true. It's the probability of observing data this extreme IF H₀ is true (reverse logic).

**Correct concept:** P-value assumes H₀ is true, then calculates probability of data. It doesn't tell us probability of H₀.

---

### Statement B: "If the medication truly had no effect, we would observe a decrease this large or larger only 3% of the time by chance."
**✅ CORRECT**

**Why right:** This is the exact definition of p-value. It assumes H₀ (no effect) and asks: "How often would random chance produce a 7 mmHg decrease or more?"

**Answer:** Only 3% of the time.

---

### Statement C: "There is a 97% probability that the medication works."
**❌ INCORRECT**

**Why wrong:** Similar to Statement A. P-value doesn't give probability that medication works. Cannot calculate P(H₁ is true) from p-value alone.

**Correct concept:** P = 0.03 means data is unlikely under H₀, which provides evidence against H₀, but doesn't quantify probability of H₁.

---

### Statement D: "We have strong evidence against the hypothesis that the medication has no effect."
**✅ CORRECT**

**Why right:** P = 0.03 < 0.05 (typical threshold), meaning data is rare under H₀. This provides evidence against H₀ (no effect).

**Note:** "Strong" is debatable (p = 0.03 is moderate), but statement is essentially correct.

---

### Statement E: "The medication reduces blood pressure by 7 mmHg in all patients."
**❌ INCORRECT**

**Why wrong:** Confuses population mean with individual responses. The 7 mmHg is the average reduction; individual patients vary widely.

**Reality:** Some patients might have 0 mmHg reduction, others 15 mmHg. Mean = 7 doesn't mean everyone = 7.

---

## Question (b): Correct Interpretation

**Proper interpretation of p = 0.03:**

"If the medication truly had no effect on blood pressure, we would expect to see a mean reduction of 7 mmHg or greater in only 3% of studies of this size due to random chance alone. Since this is unlikely, we have evidence that the medication does affect blood pressure."

**Key elements:**
1. Assumes H₀ (no effect) is true
2. Calculates probability of observing our data (or more extreme)
3. Uses this low probability as evidence against H₀
4. Avoids claiming certainty about H₁

---

## Question (c): Effect of Larger Sample Size

**Answer:** P-value would likely be **SMALLER** (closer to 0)

**Reasoning:**

With larger sample size (n=500 vs n=50):
- Standard error decreases: SE = SD/√n
- SE with n=50: SE = SD/√50 = SD/7.07
- SE with n=500: SE = SD/√500 = SD/22.36
- **SE is 3.16× smaller** with larger sample

**Test statistic:**
```
t = (observed difference) / SE

Smaller SE → Larger t → Smaller p-value
```

**Numerical example:**
If SD = 15 mmHg:
- n=50: t = 7/(15/7.07) = 7/2.12 = 3.30 → p ≈ 0.002
- n=500: t = 7/(15/22.36) = 7/0.67 = 10.45 → p < 0.0001

**Larger samples detect smaller effects more reliably.**

---

## Question (d): Clinical Importance

**Information needed:**

### 1. Clinical Significance Threshold
"What reduction is medically meaningful?"
- Expert guidelines: 5 mmHg reduction clinically important
- Our 7 mmHg exceeds this threshold ✓

### 2. Individual Variability
"How consistent is the effect?"
- Confidence interval needed
- If 95% CI = [2, 12] → Most patients benefit
- If 95% CI = [-5, 19] → High variability, some harmed

### 3. Side Effects
"What are the harms?"
- If severe side effects → 7 mmHg may not be worth it
- If minimal side effects → 7 mmHg is valuable

### 4. Cost
"Is it affordable/cost-effective?"
- ₹10/month → Excellent value
- ₹10,000/month → May not be justified for 7 mmHg

### 5. Patient Baseline
"How high is their blood pressure?"
- Baseline 145 → reduction to 138 (still borderline high)
- Baseline 185 → reduction to 178 (still very high)
- Effect may be proportional

### 6. Comparison to Alternatives
"How does it compare to other treatments?"
- If standard drug reduces by 15 mmHg → This is inferior
- If standard drug reduces by 3 mmHg → This is superior

### 7. Duration of Effect
"How long does reduction last?"
- Temporary (days) → Not clinically useful
- Sustained (years) → Very valuable

### 8. Patient Compliance
"Can patients actually take it as prescribed?"
- Once daily → Good compliance expected
- Four times daily with dietary restrictions → Poor compliance likely

---

## Key Takeaways

### P-value Means:
✅ Probability of observing data this extreme IF H₀ is true  
✅ Used as evidence against H₀  
✅ Does NOT prove H₁  

### P-value Does NOT Mean:
❌ Probability that H₀ is true  
❌ Probability that H₁ is true  
❌ Effect size or clinical importance  
❌ Probability that result is due to chance  

### Statistical vs Clinical Significance:
- **Statistical:** p < 0.05 (unlikely under H₀)
- **Clinical:** Effect large enough to matter to patients
- **Both needed:** Significant AND meaningful

### Sample Size Effects:
- **Larger n** → More precision → Smaller p-values
- Can detect smaller effects
- May find trivial effects "significant"
- Always report effect size with p-value

---

## Common Mistakes

**Mistake 1:** "P = 0.03 means 97% chance the drug works"
- **Wrong:** P-value doesn't give probability of H₁

**Mistake 2:** "P = 0.03 means only 3% chance this is random"
- **Wrong:** P-value is probability of data given H₀, not probability of H₀

**Mistake 3:** "Significant p-value means large/important effect"
- **Wrong:** Can have tiny meaningless effect with p < 0.001 if n is huge

**Mistake 4:** "Non-significant means no effect"
- **Wrong:** Might have real effect but insufficient power to detect it

---

*Solution for The Pattern Hunters - Chapter 5, Problem 5.1*
