# Chapter 2 Datasets - Complete Guide

## 🎯 Set A: Core Chapter Examples (Existing)

**Purpose:** Direct support for chapter narrative (Rajesh, Kamala, study hours)

| File | Rows | Purpose | Chapter Section |
|------|------|---------|----------------|
| `rajesh_weekly_sales.csv` | 7 | First model building | §2.3 - Toy Example 1 |
| `study_scores.csv` | 7 | Personal application | §2.3 - Toy Example 2 |
| `rajesh_two_weeks.csv` | 14 | Extended fitting | §2.4 - Least squares |
| `kamala_pricing.csv` | 5 | Multi-factor model | §2.2 - Optimization |
| `rajesh_week3_validation.csv` | 7 | Model validation | §2.5 - Testing models |
| `rajesh_complete_data.csv` | 20 | Full complexity | §2.6 - Multi-variable |

**Pedagogical Flow:**
1. Start simple (temperature → sales)
2. Add complexity (multiple factors)
3. Validate models (test predictions)
4. Compare approaches (which model is best?)

---

## 🔬 Set B: Extended Biological Applications (New)

**Purpose:** Apply chapter concepts to real biological systems

| File | Rows | Application | Biological Context |
|------|------|-------------|-------------------|
| `chapter_02_rice_yields.csv` | 8 | Agriculture | Multi-variable crop modeling |
| `chapter_02_mosquito_population.csv` | 36 | Public health | Growth models (exponential → logistic) |
| `chapter_02_bird_migration.csv` | 10 | Climate change | Phenology and temperature |
| `chapter_02_enzyme_kinetics.csv` | 21 | Biochemistry | Michaelis-Menten kinetics |
| `chapter_02_tree_growth.csv` | 10 | Ecology | Model selection challenge |
| `chapter_02_antibiotic_resistance.csv` | 6 | Medicine | Epidemiological trends |
| `chapter_02_predator_prey_timeseries.csv` | 24 | Conservation | Population dynamics |
| `chapter_02_asiatic_lion_population.csv` | 14 | Conservation | Population viability |
| `chapter_02_sir_outbreak_example.csv` | 31 | Public health | Disease modeling |

**Pedagogical Flow:**
1. Apply chapter methods to biology
2. Practice model building independently
3. Compare alternative models
4. Address real conservation/health questions

---

## 📖 How to Use Both Sets

### **For Instructors:**

**Week 1-2: Core Chapter Content (Set A)**
- Teach with Rajesh/Kamala examples
- Build intuition with familiar contexts
- Master least squares method
- Use provided datasets for in-class work

**Week 3-4: Biological Applications (Set B)**
- Assign as homework/projects
- Students apply methods independently
- Emphasize biological interpretation
- Prepare for Chapters 3-10

### **For Self-Learners:**

**Phase 1: Master the Basics (Set A)**
1. Read Chapter 2 
2. Work through Rajesh examples
3. Complete study scores exercise
4. Understand Kamala's optimization

**Phase 2: Apply to Biology (Set B)**
1. Choose biological problem of interest
2. Apply modeling methods learned
3. Compare your models
4. Think critically about limitations

### **For Students:**

**Assignment Structure:**
- **Required:** All Set A problems (graded)
- **Choose 2-3 from Set B:** Based on interest (project)
- **Final:** Bring own data and model it

---

## 🔄 Dataset Mapping

### Core Concept → Biological Application

| Core Example (Set A) | Biological Extension (Set B) | Learning Bridge |
|---------------------|---------------------------|----------------|
| Rajesh tea sales vs temperature | Rice yield vs fertilizer/rain | Simple → multi-variable |
| Study hours vs test score | Tree height vs age | Single predictor basics |
| Kamala pricing optimization | Enzyme kinetics (Vmax/Km) | Optimization principles |
| Rajesh validation data | Model comparison (rice/tree) | Testing predictions |
| Complete multi-factor | Predator-prey dynamics | Complex interactions |

---

## 📂 Recommended Repository Structure

```
Chapter-02-From-Guesswork-to-Models/
│
├── README.md
├── problems.md
│
├── data/
│   ├── core/                          # Set A - Chapter examples
│   │   ├── rajesh_weekly_sales.csv
│   │   ├── study_scores.csv
│   │   ├── rajesh_two_weeks.csv
│   │   ├── kamala_pricing.csv
│   │   ├── rajesh_week3_validation.csv
│   │   └── rajesh_complete_data.csv
│   │
│   ├── extended/                      # Set B - Biological applications
│   │   ├── chapter_02_rice_yields.csv
│   │   ├── chapter_02_mosquito_population.csv
│   │   ├── chapter_02_bird_migration.csv
│   │   ├── chapter_02_enzyme_kinetics.csv
│   │   ├── chapter_02_tree_growth.csv
│   │   ├── chapter_02_antibiotic_resistance.csv
│   │   ├── chapter_02_predator_prey_timeseries.csv
│   │   ├── chapter_02_asiatic_lion_population.csv
│   │   └── chapter_02_sir_outbreak_example.csv
│   │
│   └── README.md                      # This file
│
├── solutions/
│   ├── core_examples_solutions.md     # For Set A
│   └── extended_problems_solutions.md # For Set B
│
└── code/
    ├── rajesh_tea_model.py
    ├── least_squares_demo.py
    └── biological_applications.ipynb
```

---

## 🎓 Learning Pathway

### **Beginner Path** (2-3 weeks)
1. ✅ Chapter 2 reading
2. ✅ Work through Rajesh examples (Set A)
3. ✅ Complete study scores problem
4. ✅ Try 1-2 biological problems (Set B)
5. ✅ Reflect on process

### **Intermediate Path** (1-2 weeks)
1. ✅ Quick review of core concepts
2. ✅ Work through all Set B problems
3. ✅ Compare models systematically
4. ✅ Choose best model with justification

### **Advanced Path** (1 week)
1. ✅ Use core concepts as reference
2. ✅ Complete Set B independently
3. ✅ Bring own data and model it
4. ✅ Write up methods and results formally

---

## 💡 Teaching Tips

### **Using Set A (Core Examples):**

**Advantages:**
- ✅ Familiar context (tea stalls, studying)
- ✅ Builds intuition first
- ✅ Matches chapter narrative exactly
- ✅ Small datasets (easy to calculate by hand)
- ✅ Clear patterns (good for beginners)

**Best For:**
- First introduction to modeling
- In-class demonstrations
- Building confidence
- Teaching least squares mechanics

### **Using Set B (Biological Applications):**

**Advantages:**
- ✅ Real scientific context
- ✅ Realistic complexity
- ✅ Motivates biology students
- ✅ Bridges to later chapters
- ✅ Project-worthy depth

**Best For:**
- Homework assignments
- Independent projects
- Biological interpretation practice
- Model comparison exercises
- Transition to Chapters 3-10

---

## 🔧 Technical Notes

### **Set A Characteristics:**
- Small sample sizes (7-20 points)
- Strong linear relationships
- Minimal noise
- Hand-calculable
- Perfect for teaching mechanics

### **Set B Characteristics:**
- Realistic sample sizes (6-36 points)
- Moderate noise
- Some non-linear relationships
- Requires software (Python/R)
- Good for realistic practice

---

## 📝 Problem Set Recommendations

### **Core Problems (Using Set A):**

**Problem 2.1:** Build Rajesh's temperature-sales model
- Use: `rajesh_weekly_sales.csv`
- Calculate least squares by hand
- Interpret slope and intercept

**Problem 2.2:** Personal study model
- Use: `study_scores.csv`
- Predict your next test score
- Discuss limitations

**Problem 2.3:** Validate the model
- Use: `rajesh_week3_validation.csv`
- Test predictions
- Analyze residuals

**Problem 2.4:** Multi-factor modeling
- Use: `rajesh_complete_data.csv`
- Compare: temperature-only vs multi-variable
- Which model is better?

### **Extended Problems (Using Set B):**

**Problem 2.5:** Agricultural optimization
- Use: `chapter_02_rice_yields.csv`
- Build multi-variable model
- Optimize fertilizer/rainfall

**Problem 2.6:** Growth model comparison
- Use: `chapter_02_mosquito_population.csv`
- Compare exponential vs logistic
- When does logistic outperform?

**Problem 2.7:** Climate change phenology
- Use: `chapter_02_bird_migration.csv`
- Model temperature effects
- Predict future arrival dates

**Problem 2.8:** Model selection challenge
- Use: `chapter_02_tree_growth.csv`
- Try 4 different models
- Choose best with AIC

**Problem 2.9:** Disease dynamics
- Use: `chapter_02_sir_outbreak_example.csv`
- Understand SIR framework
- Evaluate interventions

**Problem 2.10:** Conservation genetics
- Use: `chapter_02_asiatic_lion_population.csv`
- Project population trajectory
- Assess genetic risks

---

## 🎯 Assessment Rubric

### **For Core Problems (Set A):**
- ✅ Correct calculations (40%)
- ✅ Proper interpretation (30%)
- ✅ Understanding of limitations (20%)
- ✅ Clear presentation (10%)

### **For Extended Problems (Set B):**
- ✅ Model implementation (25%)
- ✅ Biological interpretation (30%)
- ✅ Model comparison (25%)
- ✅ Critical analysis (20%)

---

## 🤔 Common Questions

**Q: Should I use both sets?**
A: Yes! Set A for learning mechanics, Set B for applying to biology.

**Q: Can I skip Set A if I know the math?**
A: Recommended to at least review - it builds the conceptual foundation.

**Q: Which Set B problems should I start with?**
A: Rice yields or bird migration - most similar to Set A.

**Q: Are these datasets real?**
A: Set A is pedagogical (simplified). Set B is simulated but based on real parameters.

**Q: Can I use my own data?**
A: Absolutely! That's the ultimate goal of Chapter 2.

---

## 📚 Related Chapters

**Builds On:**
- Chapter 1: Pattern recognition

**Prepares For:**
- Chapter 3: Population genetics models
- Chapter 4: Application to evolution
- Chapter 5: Statistical testing
- Chapter 6: Differential equations
- Chapters 7-10: Specific biological applications

---

## 🌟 Success Stories

> "I started with Rajesh's tea stall, then modeled my own garden's tomato yields. The concepts clicked when I applied them to something I care about!" - Biology student

> "Set A taught me the mechanics. Set B showed me why I should care. Now I see models everywhere in biology." - Undergraduate researcher

> "My class uses Set A for lectures, Set B for projects. Students love bringing their own data by the end!" - Professor

---

## 📧 Feedback Welcome

Found these datasets useful? Have suggestions? Open an issue or discussion!

Want to contribute your own biological dataset following these principles? We'd love to see it!

---

**Bottom Line:**
- **Set A** = Master the concepts (required)
- **Set B** = Apply to biology (highly recommended)
- **Both together** = Complete understanding

Happy modeling! 📊🔬

---

*Last updated: January 2026*
*Version: 1.0*
