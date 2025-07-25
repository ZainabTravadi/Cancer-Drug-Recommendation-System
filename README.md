# 🧬 ChemoChoice: *Personalized Cancer Drug Recommendation System*  

**Empowering precision oncology with Data Science**  

---

## 📝 **Description**  
**ChemoChoice** is a genomic analysis tool that recommends personalized cancer therapies based on tumor mutations, drug mechanisms, and clinical evidence. It solves the critical challenge of **drug selection in precision oncology** by:  
- 🔍 Analyzing patient genomic profiles (e.g., EGFR/BRAF mutations).  
- 💊 Matching drugs with **FDA-approved** or **investigational** therapies.  
- 📊 Prioritizing options by **IC50 potency**, **confidence scores**, and **side effects**.  

*Sample use case*:  
> *"For a lung cancer patient with EGFR T790M mutation, ChemoChoice recommends Osimertinib (IC50: 0.15 nM, 94% confidence) with FLAURA Phase III trial evidence."*  

---

## ⚙️ **Installation**  

### Prerequisites  
- Python 3.9+  
- `pip` or `conda`  

### Steps  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/ZainabTravadi/Cancer-Drug.git  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
   *(See [`requirements.txt`](requirements.txt) for full list)*  

---

## 🚀 **Usage**  

### Input Format  
Upload genomic data in `sample.txt` format provided in the repository (Here's an example):
```
PatientID,Gene,MutationType,Chromosome,Position,Reference,Alternate
P101,TP53,Missense,17,7579472,G,A
P101,BRCA1,Nonsense,17,41276045,C,T
P102,EGFR,L858R,7,55259515,C,T
P102,ALK,EML4-ALK Fusion,2,29443623,G,GGCT
P103,BRAF,V600E,7,140453136,A,T
P103,PD-L1,Overexpression,9,54393964,C,G
P104,HER2,Amplification,17,37880992,C,T
P104,VEGFR,Overexpression,6,43724098,A,G
P105,PD-1,Overexpression,2,24184905,G,A
P106,MTOR,Splice_Site,1,11106521,C,T
P107,BTK,Point_Mutation,X,101347650,T,C
P108,CD19,CD19+ B-cells,16,28945619,G,A
```

### Run the System  
For interactive UI (Navigate to neo-med-navigator folder, then run):  
```powershell 
npm run dev  
```  
To use backend API (Navigate to backend folder, then run):  
```powershell
uvicorn api:app --reload 
``` 
Or (If uvicorn is not in your system's path)
``` 
python -m uvicorn main:app --reload  
```  

---

## ✨ **Features**  
- 🎯 **Mutation-Driven Matching**: Filters drugs by gene targets (e.g., *ALK fusions → Crizotinib*).  
- 📉 **IC50 Ranking**: Sorts drugs by potency (lower IC50 = stronger effect).  
- 🏥 **Clinical Evidence**: Links to trials (e.g., *CHECKMATE-067 for Nivolumab*).  
- ⚠️ **Side Effect Warnings**: Flags toxicities (e.g., *cardiotoxicity for Trastuzumab*).  
- 🔄 **Investigational Options**: Suggests trials for resistant cases (e.g., *Merestinib for MET exon 14 skip*).  

---

## 🛠️ **Technologies Used**  
| Category       | Tools/Libraries                                                                 |  
|----------------|---------------------------------------------------------------------------------|  
| **Core**       | `Python`, `numpy`, `pandas`                                                     |  
| **ML**         | `scikit-learn`, `torch`, `torch-geometric`, `shap`, `captum`                    |  
| **Chem**       | `rdkit`, `networkx`                                                             |  
| **UI**         | `React`, `Tailwind CSS`, `shadcn/ui`, `lucide-react`                            |   
| **Deployment** | `fastapi`, `uvicorn`, `vite`                                                    |  
---

## 🤝 **Contributing**  
We welcome contributions! Here’s how:  
1. 🐛 **Report bugs**: Open an issue with steps to reproduce.  
2. 💡 **Suggest features**: Propose new drug databases or algorithms.  
3. 🛠️ **Code**: Submit PRs for:  
   - Improved mutation-drug matching logic.  
   - Integration with genomics APIs (e.g., COSMIC).  

---

## 📜 **License**  
**MIT License**  
- ✅ Modify, distribute, and use freely.  
- 📝 Attribution required.  
- 🔄 Changes/contributions must be open-sourced.  

---

## 📧 **Contact**  
For questions:  
📩 **Email**: [zainabtravadi421@gmail.com](mailto:zainabtravadi421@gmail.com) 
🔗 **LinkedIn**: [Zainab Travadi](https://www.linkedin.com/in/zainab-travadi-119a83373/)

---  

**Made with ❤️ for precision oncology**  

---
