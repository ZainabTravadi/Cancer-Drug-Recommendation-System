# 🧬 Personalized Cancer Drug Treatment: Core Concepts

## 🎯 What is Personalized Cancer Treatment?

Personalized (or Precision) Cancer Treatment is a therapeutic approach that:

- Tailors drug treatments based on an individual patient’s **genetic, molecular, and cellular profile**.
- Aims to improve drug efficacy and reduce side effects by avoiding “one-size-fits-all” therapies.
- Uses data like gene expression, mutations, protein levels, and biomarkers to predict which drugs or drug combinations will work best for a specific patient.

### Key Technologies Involved:
- **Next-Generation Sequencing (NGS)** to identify mutations.
- **Transcriptomics** (gene expression levels).
- **Bioinformatics** to match profiles with drug response data.

---

## 💡 Why Is It Important?

- Two patients with the same cancer type may respond differently to the same drug.
- Personalized treatment increases survival rates and reduces unnecessary toxicity.
- It drives **precision oncology**, integrating AI, omics data, and pharmacology.

---

## 🧪 Pharmacological Metrics

---

### 1. **IC50 – Half Maximal Inhibitory Concentration**

**Definition**:
> The concentration of a drug at which 50% of the target (e.g., cancer cells) is inhibited or killed.

- It's a **dose-response metric**: lower IC50 → higher potency.
- Used to **quantify how sensitive a cell line or tumor is** to a drug.

**Interpretation**:
- **Low IC50 (<1 µM)** → Highly sensitive → Drug is very effective.
- **High IC50 (>10 µM)** → Low sensitivity → Drug less effective.

**Relevance to ML Models**:
- IC50 is often used as a **target label** in regression tasks.
- Helps train models to predict how sensitive a cancer cell is to a specific drug.

---

### 2. **AUC – Area Under the Dose-Response Curve**

**Definition**:
> AUC quantifies the total drug effect over a range of concentrations in a dose-response curve.

- Integrates the full dose-response curve, not just a single point (like IC50).
- **Lower AUC = more effective drug** (steeper and lower curve).

**Comparison with IC50**:
| IC50   | Single dose point | Measures potency |
| AUC    | Whole response curve | Measures overall sensitivity |

**Use in ML**:
- AUC can be used as an alternative or complementary label to IC50.
- Often used in classification tasks (e.g., sensitive vs resistant).

---

### 3. **Drug Synergy**

**Definition**:
> When two or more drugs work **better together** than the sum of their individual effects.

- A **synergistic drug pair** may require lower doses, reducing toxicity.
- Used in **combination therapy**, which is crucial in treating advanced cancers.

**Quantitative Models for Synergy**:
- **Bliss Independence**: Based on probabilistic independence.
- **Loewe Additivity**: Assumes drugs with the same mechanism should be additive.
- **ZIP Model (Zero Interaction Potency)**: Compares observed and expected interactions.

**Interpretation**:
- **Synergy Score > 0** → Synergistic
- **Synergy Score ≈ 0** → Additive
- **Synergy Score < 0** → Antagonistic

**Use in ML/DL**:
- Can train models to predict **synergy scores** from molecular and genomic features of two drugs + cell line.

---

## 🧬 Public Datasets Used in Research

| **GDSC**    | Genomics of Drug Sensitivity in Cancer – cell line screening data           | IC50, AUC, mutations, expression |

| **CellMiner** | NCI-60 cancer cell lines, includes gene expression + 20,000+ compounds     | IC50, AUC, RNA/protein data |

| **TCGA**     | The Cancer Genome Atlas – real patient tumor genomics + clinical outcomes  | Gene expression, survival data |

---

## 📘 Summary Table

| **IC50**    | Drug concentration at which 50% of the target is inhibited              | Regression label   |
| **AUC**     | Overall effect of drug across all concentrations                        | Regression/Ranking |
| **Synergy** | Combined drug effect greater than individual drugs                      | Classification/Ranking |
| **GDSC**    | Drug screening on cancer cell lines                                     | Source of training data |
| **CellMiner** | Cell line drug response + gene expression                             | Model fine-tuning  |
| **TCGA**    | Patient genomics and survival outcomes                                  | Model validation   |

## 🛠 How This Ties Into Your Project

- Use IC50/AUC as **ground truth labels** to predict drug effectiveness.
- Use synergy scores to build models that suggest **optimal drug pairs**.
- Use genomic data (gene expression, mutations) as **input features**.
- These metrics provide **explainable outputs** to clinicians or researchers.

## 🔗 Recommended Reading Links

- [NCBI: Pharmacogenomics Overview](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7860563/)
- [NIH: What Is Precision Medicine?](https://www.cancer.gov/about-cancer/treatment/types/precision-medicine)
- [GDSC Resource](https://www.cancerrxgene.org)
- [CellMiner](https://discover.nci.nih.gov/cellminer)
- [TCGA Data Portal](https://portal.gdc.cancer.gov)
