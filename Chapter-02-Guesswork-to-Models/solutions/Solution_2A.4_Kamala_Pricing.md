# Solution 2A.4: Kamala's Vegetable Pricing ⭐⭐

## Problem Summary
Analyze Kamala's dynamic pricing strategy throughout the day to understand the demand curve, revenue optimization, and practical business decisions. This example demonstrates optimization in action.

---

## Given Data

```
Time of Day | Hour | Price (₹/kg) | Kg Sold | Revenue (₹)
------------|------|--------------|---------|-------------
Morning     | 8    | 40           | 25      | 1000
Mid-Morning | 10   | 38           | 30      | 1140
Noon        | 12   | 35           | 28      | 980
Afternoon   | 14   | 32           | 35      | 1120
Evening     | 16   | 28           | 40      | 1120
Late        | 18   | 20           | 30      | 600
```

---

## Question (a): Pattern Analysis

### Describe How Price and Quantity Change Throughout the Day

**Price Pattern:**
```
8 AM:  ₹40/kg (HIGHEST)
10 AM: ₹38/kg (↓5%)
12 PM: ₹35/kg (↓8%)
2 PM:  ₹32/kg (↓9%)
4 PM:  ₹28/kg (↓13%)
6 PM:  ₹20/kg (↓29%) (LOWEST)

Total decline: From ₹40 to ₹20 = 50% reduction
```

**Pattern:** Steady, continuous price decrease throughout the day

---

**Quantity Sold Pattern:**
```
8 AM:  25 kg (baseline)
10 AM: 30 kg (+20%)
12 PM: 28 kg (-7%)
2 PM:  35 kg (+25%) (HIGHEST)
4 PM:  40 kg (+14%) (PEAK VOLUME)
6 PM:  30 kg (-25%)

Trend: Generally increasing until evening, then drops
```

**Pattern:** Volume increases as price drops (classic demand curve), peaks at evening rush

---

### Calculate Total Revenue at Each Time Point

**Revenue Calculation:**
```
Revenue = Price × Quantity
```

**Detailed Calculations:**

| Time | Price | Quantity | Calculation | Revenue |
|------|-------|----------|-------------|---------|
| Morning | ₹40 | 25 kg | 40 × 25 | ₹1,000 |
| Mid-Morning | ₹38 | 30 kg | 38 × 30 | ₹1,140 |
| Noon | ₹35 | 28 kg | 35 × 28 | ₹980 |
| Afternoon | ₹32 | 35 kg | 32 × 35 | ₹1,120 |
| Evening | ₹28 | 40 kg | 28 × 40 | ₹1,120 |
| Late | ₹20 | 30 kg | 20 × 30 | ₹600 |

---

### When is Revenue Highest? Lowest?

**Revenue Rankings:**
```
1. Mid-Morning (10 AM): ₹1,140 ← HIGHEST
2. Afternoon (2 PM):    ₹1,120 (tie)
3. Evening (4 PM):      ₹1,120 (tie)
4. Morning (8 AM):      ₹1,000
5. Noon (12 PM):        ₹980
6. Late (6 PM):         ₹600  ← LOWEST
```

**Key Insights:**

**Highest Revenue (₹1,140 at 10 AM):**
- Sweet spot between price (₹38) and volume (30 kg)
- Government employees buying lunch ingredients
- Peak purchasing power time

**Tied for 2nd (₹1,120 at 2 PM and 4 PM):**
- **2 PM:** Moderate price (₹32), good volume (35 kg)
- **4 PM:** Lower price (₹28), but high volume compensates (40 kg)
- Different strategies, same revenue!

**Lowest Revenue (₹600 at 6 PM):**
- Very low price (₹20) but can't make up with volume
- Limited customers late in day
- Tomatoes losing freshness - must sell

---

### Visual Revenue Pattern

```
Revenue (₹)
1200 |     ●(10 AM)
     |         ●────●(2,4 PM)
1000 | ●(8 AM)    
     |       
 800 |         ●(12 PM)
     |
 600 |                     ●(6 PM)
     |________________________
       8   10   12   14   16   18  Hour
```

**Pattern:** 
- Peaks at mid-morning
- Maintains high plateau through afternoon
- Crashes in late evening

---

## Question (b): Build a Model

### The Revenue Relationship

**Given:**
```
Revenue = Price × Quantity
```

**But quantity depends on price!**

This is the **demand curve** - as price changes, quantity demanded changes.

**Hypothesis:** 
```
Quantity = a + b × Price
```

Where:
- **a** = quantity at price ₹0 (theoretical maximum)
- **b** = slope (how quantity responds to price)
- We expect **b < 0** (negative) because higher price → lower quantity

---

### Use Least Squares to Find Relationship

**Data for Regression:**

| Price (x) | Quantity (y) |
|-----------|--------------|
| 40        | 25           |
| 38        | 30           |
| 35        | 28           |
| 32        | 35           |
| 28        | 40           |
| 20        | 30           |

---

**Step 1: Calculate Means**

```
Mean Price (x̄) = (40 + 38 + 35 + 32 + 28 + 20) / 6
                = 193 / 6
                = 32.17 ₹/kg

Mean Quantity (ȳ) = (25 + 30 + 28 + 35 + 40 + 30) / 6
                   = 188 / 6
                   = 31.33 kg
```

---

**Step 2: Calculate Deviations**

| Price (x) | Qty (y) | (x - x̄) | (y - ȳ) | (x - x̄)² | (x - x̄)(y - ȳ) |
|-----------|---------|----------|----------|-----------|------------------|
| 40        | 25      | 7.83     | -6.33    | 61.31     | -49.56          |
| 38        | 30      | 5.83     | -1.33    | 33.99     | -7.75           |
| 35        | 28      | 2.83     | -3.33    | 8.01      | -9.42           |
| 32        | 35      | -0.17    | 3.67     | 0.03      | -0.62           |
| 28        | 40      | -4.17    | 8.67     | 17.39     | -36.15          |
| 20        | 30      | -12.17   | -1.33    | 148.11    | 16.19           |
|**Sum**    |         | 0        | 0        | **268.84**| **-87.31**      |

---

**Step 3: Calculate Slope (b)**

```
b = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)²]
  = -87.31 / 268.84
  = -0.325 kg per ₹
```

**Interpretation:** For every ₹1 increase in price, quantity sold decreases by 0.325 kg

---

**Step 4: Calculate Intercept (a)**

```
a = ȳ - b × x̄
  = 31.33 - (-0.325) × 32.17
  = 31.33 + 10.46
  = 41.79 kg
```

---

### Final Demand Model

```
Quantity = 41.79 - 0.325 × Price
```

**Or rearranged (Inverse Demand Curve):**
```
Price = (41.79 - Quantity) / 0.325
Price = 128.6 - 3.08 × Quantity
```

---

### What Does a Negative Slope Mean?

**Negative slope (b = -0.325) is the DEMAND CURVE!**

**Economic Interpretation:**

**1. Law of Demand:**
```
Higher Price → Lower Quantity Demanded
Lower Price → Higher Quantity Demanded
```

This is fundamental economics - people buy less when things cost more!

**2. Price Elasticity:**

```
For every ₹1 increase → lose 0.325 kg sales
For every ₹10 increase → lose 3.25 kg sales

Example:
At ₹30: Predict 41.79 - 0.325(30) = 32.04 kg
At ₹40: Predict 41.79 - 0.325(40) = 28.79 kg
Difference: 3.25 kg for ₹10 increase
```

**3. Customer Behavior:**

**Psychological factors:**
- Price sensitivity (customers compare prices)
- Budget constraints (limited money)
- Perceived value (is it worth it?)
- Alternatives (other vendors, other vegetables)

**4. Market Dynamics:**

```
At ₹20 (cheap): 35 kg demanded (lots of buyers)
At ₹40 (expensive): 25 kg demanded (only committed buyers)
```

---

### Model Validation

**Test Predictions:**

| Actual Price | Actual Qty | Predicted Qty | Error |
|--------------|------------|---------------|-------|
| ₹40          | 25 kg      | 28.79 kg      | -3.79 |
| ₹38          | 30 kg      | 29.44 kg      | +0.56 |
| ₹35          | 28 kg      | 30.41 kg      | -2.41 |
| ₹32          | 35 kg      | 31.39 kg      | +3.61 |
| ₹28          | 40 kg      | 32.69 kg      | +7.31 |
| ₹20          | 30 kg      | 35.29 kg      | -5.29 |

**R² Calculation:**

```
TSS = Σ(y - ȳ)² = 260.67
RSS = Σ(residual²) = 127.85
R² = 1 - (127.85/260.67) = 0.51 (51%)
```

**Model explains 51% of variation** - moderate fit

**Why not perfect?**
- Time of day effects (not just price!)
- Quality deterioration (tomatoes wilting)
- Customer traffic patterns
- Random variation

---

## Question (c): Optimization Question

### If Kamala Starts with 100 kg, What Pricing Strategy Maximizes Revenue?

This is a **constrained optimization problem**!

**Constraints:**
- Total inventory: 100 kg
- Must sell throughout day (6 time periods)
- Tomatoes deteriorate (can't hold forever)
- Customer traffic varies by time

---

### Strategy 1: Keep High Prices All Day

**Scenario:** Price = ₹40 throughout

```
Using demand model: Q = 41.79 - 0.325(40) = 28.79 kg

If 6 equal periods:
  Total sold: 6 × 28.79 = 172.74 kg

Problem: We only have 100 kg!
  Sell out by period 3-4
  Miss afternoon/evening customers
  
Revenue: ₹40 × 100 kg = ₹4,000
```

**Issues:**
- ✗ Sell out too early
- ✗ Miss evening rush customers  
- ✗ Angry customers (out of stock)
- ✗ Lost market share

---

### Strategy 2: Drop Prices Gradually (Kamala's Strategy)

**Current strategy from data:**

```
Period 1 (8 AM):  ₹40 × 25 kg = ₹1,000 | Remaining: 75 kg
Period 2 (10 AM): ₹38 × 30 kg = ₹1,140 | Remaining: 45 kg
Period 3 (12 PM): ₹35 × 28 kg = ₹980  | Remaining: 17 kg
Period 4 (2 PM):  ₹32 × 35 kg... wait, need only 17 kg!

Adjust: Sell 17 kg at ₹32 = ₹544
Total so far: ₹3,664 for 100 kg
```

**But Kamala sells across all 6 periods. Let's calculate actual:**

```
Total sold: 25 + 30 + 28 + 35 + 40 + 30 = 188 kg

She has MORE than 100 kg! 
Either:
  (a) Restock during day, OR
  (b) Problem is theoretical exercise
```

**Let's optimize for 100 kg constraint:**

---

### Optimization Approach: Dynamic Programming

**Goal:** Maximize Σ(Price × Quantity) subject to Σ(Quantity) = 100 kg

**Strategy:** Allocate inventory to maximize revenue

**Key Insight:** Sell more at HIGH-PRICE times, less at LOW-PRICE times

---

### Optimal Allocation (Simplified)

**Revenue per kg at each time:**

```
Morning (8 AM):    ₹40/kg → Priority 1 (HIGHEST)
Mid-Morning (10):  ₹38/kg → Priority 2
Noon (12):         ₹35/kg → Priority 3
Afternoon (2):     ₹32/kg → Priority 4
Evening (4):       ₹28/kg → Priority 5
Late (6):          ₹20/kg → Priority 6 (LOWEST)
```

**Naive Strategy:** Sell everything early at high prices

**Problem:** No customers left later! Demand is time-dependent.

---

### Realistic Optimal Strategy

**Consider demand at each time:**

```
Max potential sales (from model):
8 AM:  29 kg (at ₹40)
10 AM: 29 kg (at ₹38)
12 PM: 30 kg (at ₹35)
2 PM:  31 kg (at ₹32)
4 PM:  33 kg (at ₹28)
6 PM:  35 kg (at ₹20)
```

**Optimal allocation (meeting demand at highest prices):**

```
8 AM:  Sell 20 kg at ₹40 = ₹800  (Remaining: 80)
10 AM: Sell 25 kg at ₹38 = ₹950  (Remaining: 55)
12 PM: Sell 20 kg at ₹35 = ₹700  (Remaining: 35)
2 PM:  Sell 15 kg at ₹32 = ₹480  (Remaining: 20)
4 PM:  Sell 15 kg at ₹28 = ₹420  (Remaining: 5)
6 PM:  Sell 5 kg at ₹20  = ₹100  (Remaining: 0)

Total Revenue: ₹3,450
```

---

### Should She Keep High Prices or Drop Gradually?

**Answer: DROP PRICES GRADUALLY (what Kamala does!)**

**Why?**

**1. Time-Varying Demand:**
```
Morning: Specific customer segment (office workers)
Afternoon: Different segment (housewives)
Evening: Yet another segment (late shoppers)

Can't serve all segments at one price!
```

**2. Inventory Constraint:**
```
Hold high price → unsold inventory → spoilage
Drop price → clear inventory → cash flow
```

**3. Customer Goodwill:**
```
Stock-outs anger customers
Loyal customers get served (come back)
Reputation matters for repeat business
```

**4. Perishable Goods Reality:**
```
Hour 8: Fresh tomatoes worth ₹40
Hour 18: Wilting tomatoes worth ₹20
Better ₹20 than ₹0 (total loss)!
```

**5. Competition:**
```
Rigid pricing → lose customers to flexible vendors
Dynamic pricing → capture more market segments
```

---

### Mathematical Optimum vs Practical Reality

**Pure Math Optimum:** 
```
Sell all at highest price that clears inventory
Revenue = Price × 100 kg
Maximize Price subject to demand
```

**Practical Optimum (Kamala's approach):**
```
Balance multiple objectives:
  - Revenue maximization
  - Inventory clearance
  - Customer satisfaction
  - Competitive positioning
  - Tomorrow's business
```

**Kamala's wisdom:** Gradual price reduction achieves multiple goals simultaneously!

---

## Question (d): Real-World Complications

### What Other Factors Affect Kamala's Pricing Decisions?

---

### 1. Tomato Quality (Freshness Degradation)

**Problem:** Vegetables deteriorate over time

**Impact on Pricing:**
```
8 AM:  Fresh, vibrant → Can charge ₹40
12 PM: Slightly wilted → Must drop to ₹35
6 PM:  Clearly old → Only ₹20 acceptable
```

**Not in model:** Quality decline forces price drops independent of demand

**Kamala's solution:**
- Display freshest tomatoes in morning
- Hide slightly wilted ones
- Deep discounts on aging stock

---

### 2. Competition from Nearby Vendors

**Problem:** 10 other vegetable sellers within 50 meters

**Competitive Dynamics:**

**Morning (8 AM):**
```
All vendors: ₹38-42/kg (similar)
Kamala: Can maintain ₹40 (her tomatoes are good quality)
```

**Afternoon (2 PM):**
```
Competitor 1: Drops to ₹30 (wants to sell out)
Competitor 2: Still at ₹35 (has fresh stock)
Kamala: Must match or beat to compete → ₹32
```

**Evening (6 PM):**
```
Most vendors: Sold out or gone home
Kamala: Can be flexible, ₹20 clears remaining
```

**Not in model:** Competitor pricing drives Kamala's decisions

**Strategic responses:**
- Price matching (stay competitive)
- Quality differentiation (justify premium)
- Timing (undercutprice when they're out of stock)

---

### 3. Customer Type Variation

**Problem:** Different customers have different willingness-to-pay

**Customer Segments:**

**Segment 1: Morning Office Workers**
```
Time: 7-9 AM
Characteristics:
  - High income
  - Time-constrained
  - Quality-focused
  - Price-insensitive
  
Kamala's strategy: High price (₹40), premium selection
```

**Segment 2: Housewives (Bulk Buyers)**
```
Time: 10 AM - 2 PM
Characteristics:
  - Price-sensitive
  - Buy in quantity
  - Compare prices
  - Quality-aware
  
Kamala's strategy: Moderate price (₹32-38), volume discounts
```

**Segment 3: Evening Bargain Hunters**
```
Time: 4-6 PM
Characteristics:
  - Very price-sensitive
  - Accept lower quality
  - Small quantities
  - Flexible timing
  
Kamala's strategy: Deep discount (₹20-28), clear inventory
```

**Not in model:** Customer heterogeneity drives price discrimination strategy

---

### 4. Weather and Seasonal Effects

**Weather Impact:**

**Rainy Day:**
```
Fewer customers overall
But tomato prices higher (supply disruption)
Kamala: Raise base price ₹5 across all times
```

**Hot Sunny Day:**
```
More customers (cooking at home)
Tomatoes wilt faster
Kamala: Drop prices faster, sell out earlier
```

**Seasonal Variation:**

**Winter (Nov-Feb):**
```
Peak tomato season
Abundant supply → lower wholesale cost
Kamala: Lower prices, higher volume
```

**Summer (Apr-June):**
```
Tomato scarcity
High wholesale cost
Kamala: Higher prices but lower volume
```

**Not in model:** External factors shift entire demand curve

---

### 5. Wholesale Purchase Costs

**Problem:** Kamala's costs vary daily

**Cost Dynamics:**

**Today's wholesale price: ₹18/kg**
```
Markup at different times:
  8 AM:  ₹40 - ₹18 = ₹22 profit (122% markup)
  12 PM: ₹35 - ₹18 = ₹17 profit (94% markup)
  6 PM:  ₹20 - ₹18 = ₹2 profit (11% markup)
```

**Tomorrow's wholesale: ₹25/kg (supply shortage)**
```
Now ₹20 evening price = LOSS!
Must adjust entire price schedule upward
```

**Not in model:** Cost structure determines price floor

**Kamala's rule:** Never sell below cost unless clearing spoilage

---

### 6. Bulk Purchase Negotiations

**Problem:** Large buyers want discounts

**Scenario:**
```
Restaurant owner (4 PM): "I'll buy 20 kg if you give me ₹25/kg"

Kamala's calculation:
  Current price: ₹28/kg
  Offer: ₹25/kg for 20 kg = ₹500 revenue
  Alternative: Sell piecemeal at ₹28, maybe only move 15 kg = ₹420
  
Decision: Accept! ₹500 > ₹420, and guarantees sale
```

**Not in model:** Bulk discounts and negotiation

**Trade-off:** Lower price per kg but guaranteed volume and immediate cash

---

### 7. Reputation and Customer Relationships

**Long-term Considerations:**

**Mrs. Sharma (Regular Customer):**
```
Comes every day at 8 AM
Always pays full price
Loyal for 5 years

Today: Kamala notices she looks worried, buying less

Kamala's decision: Give extra coriander free, ₹2 discount
Cost: ₹2 immediate
Benefit: Customer loyalty retained (worth ₹300/month for 12 months = ₹3,600)
```

**Not in model:** Customer lifetime value exceeds single transaction

**From book (page 63):**
> "When she notices that Mrs. Sharma, her regular customer, looks worried and is buying less than usual, Kamala quietly gives her extra coriander for free. She's not being sentimental—she's making a long-term investment in customer loyalty that any business school would applaud."

---

### 8. Cash Flow Needs

**Problem:** Kamala needs cash for tomorrow's wholesale purchase

**Scenario:**
```
3 PM: Kamala needs ₹1,500 by 6 PM to pay wholesaler tomorrow morning

Current: Sold ₹2,500 so far, ₹1,000 spent on rent/expenses
Cash on hand: ₹1,500
Need: ₹1,500 more

Remaining inventory: 35 kg

Option A: Hold ₹35/kg, sell slowly → might only move 20 kg = ₹700 (SHORT!)
Option B: Drop to ₹30/kg, sell faster → likely move all 35 kg = ₹1,050 ✓

Decision: Drop price to ensure cash flow
```

**Not in model:** Liquidity constraints affect pricing

---

### 9. Storage and Opportunity Costs

**Problem:** Unsold tomatoes = lost money

**End-of-day calculation:**

**Scenario 1: Hold out for high price**
```
6 PM: Still have 15 kg unsold at ₹28/kg
Overnight: 50% spoilage (7.5 kg lost)
Tomorrow: Sell 7.5 kg at ₹15/kg (old stock) = ₹112.50
Total from 15 kg: ₹112.50
```

**Scenario 2: Deep discount now**
```
6 PM: Drop to ₹20/kg, sell all 15 kg immediately
Revenue: ₹300
Total from 15 kg: ₹300
```

**Better to take ₹300 now than ₹112.50 tomorrow!**

**Not in model:** Opportunity cost of unsold inventory

---

### 10. Market Information Asymmetry

**Problem:** Customers don't know what other vendors charge

**Information advantage:**

**Uninformed customer:**
```
Sees ₹35/kg at Kamala's stall
Doesn't know competitors charging ₹32
Pays ₹35 (Kamala captures information rent)
```

**Informed customer (smart shopper):**
```
Checked 5 stalls
Knows ₹32 is cheapest
Kamala: Must match or lose sale
```

**Not in model:** Information economics and price transparency

**Kamala's strategy:** 
- Emphasize quality (justify premium)
- Quick, friendly service (convenience value)
- Loyal customer discounts (reward repeat business)

---

## Model Improvement Suggestions

### Enhanced Model: Multi-Factor Pricing

```
Price = Base_Price(Hour) × Quality_Factor × Competition_Adjustment × 
        Customer_Type_Factor × Weather_Factor × Cash_Flow_Urgency

Where:
  Base_Price(Hour): Time-based baseline from demand curve
  Quality_Factor: 1.0 (fresh) to 0.5 (wilting)
  Competition_Adjustment: 0.9 to 1.1 based on nearby prices
  Customer_Type_Factor: 1.2 (premium buyers) to 0.8 (bulk/bargain)
  Weather_Factor: 1.1 (rain) to 0.9 (extreme heat)
  Cash_Flow_Urgency: 1.0 (normal) to 0.8 (need cash NOW)
```

---

## Key Takeaways

### Economics Principles Demonstrated

**1. Law of Demand:**
- Downward sloping demand curve (negative relationship)
- Higher price → lower quantity

**2. Price Discrimination:**
- Charge different prices to different segments
- Morning: Premium pricing (office workers)
- Evening: Discount pricing (bargain hunters)

**3. Revenue Optimization:**
- Revenue = Price × Quantity
- Must balance both factors
- Sweet spot: ₹38 at 10 AM (₹1,140 revenue)

**4. Perishable Goods Dynamics:**
- Time pressure to sell
- Value deteriorates
- Deep discounts rational at end

**5. Dynamic Pricing:**
- Adjust in real-time
- Respond to market conditions
- Maximize across entire day

---

### Business Strategy Insights

**Kamala's Sophisticated Approach:**

**1. Market Segmentation:**
- Identifies different customer types
- Prices accordingly
- Maximizes total revenue

**2. Inventory Management:**
- Balances holding cost vs selling
- Clears stock before spoilage
- Maintains cash flow

**3. Competitive Intelligence:**
- Monitors nearby vendors
- Responds to price changes
- Differentiates on quality/service

**4. Relationship Management:**
- Invests in loyal customers
- Short-term sacrifice for long-term gain
- Customer lifetime value thinking

**5. Adaptive Optimization:**
- Not rigid formula
- Responds to daily variations
- Experience-based adjustments

---

### From Book (Pages 62-63)

> "Kamala has intuitively developed what economists call a 'dynamic optimization algorithm'—the same mathematical framework used by airlines to price tickets and by stock markets to value shares."

**This problem shows:**
- Kamala uses sophisticated math intuitively
- Mathematical models capture this wisdom
- Models also reveal limitations
- Real optimization includes factors beyond math

---

## Common Mistakes

### ❌ Mistake 1: Confusing Correlation with Causation

**Wrong:** "Low prices CAUSE high sales"

**Right:** "Low prices are ASSOCIATED with high sales, but causation is complex (time of day, quality, customers all matter)"

---

### ❌ Mistake 2: Ignoring Constraints

**Wrong:** "Optimal price is ₹40 because it's highest"

**Right:** "Optimal price balances revenue with inventory clearance, customer satisfaction, and competitive position"

---

### ❌ Mistake 3: Static Optimization

**Wrong:** "Set one price that maximizes revenue"

**Right:** "Dynamic pricing throughout day captures more value from heterogeneous customers"

---

### ❌ Mistake 4: Overconfidence in Model

**Wrong:** "Model says quantity = 41.79 - 0.325 × Price, so this always works"

**Right:** "Model explains 51% of variation; other factors (quality, competition, weather) also critical"

---

## Extensions for Advanced Students

### Extension 1: Elasticity Calculation

**Price Elasticity of Demand:**
```
ε = (ΔQ/Q) / (ΔP/P)

At ₹32 (mean price):
  Q = 31.33 kg
  ΔQ/ΔP = -0.325
  
ε = (-0.325 × 32) / 31.33 = -0.33

Interpretation: 1% price increase → 0.33% quantity decrease (inelastic)
```

---

### Extension 2: Consumer Surplus

**Calculate consumer surplus at each price point:**
```
CS = ∫[Demand Curve - Price] dQ

Measures customer benefit from transaction
Higher at lower prices
```

---

### Extension 3: Multi-Product Optimization

**Kamala sells many vegetables:**
```
Maximize: Σ(Revenue_i) subject to:
  - Space constraint
  - Capital constraint  
  - Complementary goods (onions + tomatoes bought together)
```

---

*Solution by Dr. Alok Patel for The Pattern Hunters*  
*Chapter 2: From Guesswork to Models - Set A*  
*Based on book example (pages 62-63)*
