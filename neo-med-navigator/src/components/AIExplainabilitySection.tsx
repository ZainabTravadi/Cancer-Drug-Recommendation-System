
import React, { useState } from 'react';
import { Card } from '@/components/ui/card';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';
import PerformanceMetrics from './ui/metrics';

const AIExplainabilitySection = () => {
  const [expandedSection, setExpandedSection] = useState<string | null>(null);

  const explainabilityData = [
    {
      id: "genomic-analysis",
      title: "Genomic Profile Analysis",
      icon: "🧬",
      description: "How genetic markers influence drug effectiveness",
      details: [
        {
          factor: "EGFR T790M Mutation",
          impact: "High",
          explanation: "Presence of T790M mutation increases sensitivity to Osimertinib by 78% compared to wild-type EGFR",
          confidence: 97,
          relatedDrugs: [1, 13, 27]
        },
        {
          factor: "BRCA1/2 Pathogenic Variants", 
          impact: "High",
          explanation: "Germline BRCA mutations confer 92% response rate to PARP inhibitors like Olaparib",
          confidence: 95,
          relatedDrugs: [2, 47, 48, 49]
        },
        {
          factor: "HER2 Amplification",
          impact: "Critical",
          explanation: "HER2 3+ overexpression by IHC makes Trastuzumab first-line therapy with 89% response rate",
          confidence: 98,
          relatedDrugs: [4, 11, 37, 38]
        }
      ]
    },
    {
      id: "pathway-activity", 
      title: "Pathway Activation Analysis",
      icon: "🔄",
      description: "Key signaling pathways affecting treatment options",
      details: [
        {
          factor: "MAPK Pathway Activation",
          impact: "High",
          explanation: "BRAF V600E mutation drives constitutive MAPK signaling, making Dabrafenib/Trametinib combination 85% effective",
          confidence: 93,
          relatedDrugs: [5, 6, 34, 35, 36]
        },
        {
          factor: "PD-1/PD-L1 Axis",
          impact: "Moderate",
          explanation: "Tumor proportion score ≥50% predicts 62% response rate to Pembrolizumab monotherapy",
          confidence: 88,
          relatedDrugs: [7, 8, 51, 52]
        },
        {
          factor: "Angiogenesis Signaling",
          impact: "Moderate",
          explanation: "VEGF pathway activation score of 7.2 suggests benefit from Axitinib or Cabozantinib",
          confidence: 82,
          relatedDrugs: [12, 14, 19, 29]
        }
      ]
    },
    {
      id: "drug-mechanisms",
      title: "Drug Mechanism Insights", 
      icon: "⚗️",
      description: "Key pharmacological factors influencing recommendations",
      details: [
        {
          factor: "Blood-Brain Barrier Penetration",
          impact: "Critical",
          explanation: "Alectinib and Lorlatinib show 10x greater CNS penetration than 1st-gen ALK inhibitors for brain metastases",
          confidence: 94,
          relatedDrugs: [31, 32]
        },
        {
          factor: "Resistance Mutation Coverage",
          impact: "High",
          explanation: "Ponatinib and Asciminib maintain activity against T315I gatekeeper mutation in BCR-ABL",
          confidence: 91,
          relatedDrugs: [44, 30]
        },
        {
          factor: "ADC Payload Efficiency",
          impact: "High",
          explanation: "Trastuzumab deruxtecan demonstrates 8:1 drug-to-antibody ratio with membrane-permeable payload",
          confidence: 89,
          relatedDrugs: [57]
        }
      ]
    },
    {
      id: "clinical-context",
      title: "Clinical Considerations",
      icon: "🏥",
      description: "Patient-specific factors affecting treatment selection",
      details: [
        {
          factor: "Prior Treatment History",
          impact: "High",
          explanation: "Progressed on 1st-line EGFR TKI increases likelihood of T790M-mediated resistance (68% prevalence)",
          confidence: 90,
          relatedDrugs: [1, 27]
        },
        {
          factor: "Comorbidity Profile",
          impact: "Moderate",
          explanation: "Pre-existing cardiac conditions may contraindicate HER2 therapies with cardiotoxicity risk",
          confidence: 85,
          relatedDrugs: [4, 38]
        },
        {
          factor: "Biomarker Dynamics",
          impact: "Emerging",
          explanation: "On-treatment ctDNA clearance by cycle 2 predicts 89% PFS at 12 months with PARP inhibitors",
          confidence: 78,
          relatedDrugs: [2, 47, 48, 49]
        }
      ]
    },
];

  const getImpactColor = (impact: string) => {
    switch (impact.toLowerCase()) {
      case 'critical':
      case 'high':
        return 'text-red-400 bg-red-500/20 border-red-500/30';
      case 'synergistic':
      case 'medium':
        return 'text-yellow-400 bg-yellow-500/20 border-yellow-500/30';
      case 'additive':
        return 'text-green-400 bg-green-500/20 border-green-500/30';
      case 'caution':
        return 'text-orange-400 bg-orange-500/20 border-orange-500/30';
      default:
        return 'text-blue-400 bg-blue-500/20 border-blue-500/30';
    }
  };

  return (
    <section id="explainability" className="py-20 bg-dark-gradient">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-glow">
            <span className="bg-gradient-to-r from-pink-400 to-cyan-400 bg-clip-text text-transparent">
              AI Explainability
            </span>
          </h2>
          <p className="text-xl text-slate-300 max-w-3xl mx-auto">
            Understand how our AI arrived at these recommendations with transparent, evidence-based insights
          </p>
        </div>

        <div className="space-y-6">
          {explainabilityData.map((section) => (
            <Card key={section.id} className="cyber-card">
              <Accordion type="single" collapsible>
                <AccordionItem value={section.id} className="border-none">
                  <AccordionTrigger className="hover:no-underline py-6">
                    <div className="flex items-center gap-4 text-left">
                      <div className="text-3xl">{section.icon}</div>
                      <div>
                        <h3 className="text-2xl font-bold text-white mb-2">{section.title}</h3>
                        <p className="text-slate-300">{section.description}</p>
                      </div>
                    </div>
                  </AccordionTrigger>
                  
                  <AccordionContent className="pt-4">
                    <div className="space-y-4">
                      {section.details.map((detail, index) => (
                        <div key={index} className="bg-slate-700/30 rounded-lg p-4 border border-slate-600/30">
                          <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4 mb-3">
                            <h4 className="font-semibold text-lg text-white">{detail.factor}</h4>
                            <div className="flex gap-3">
                              <span className={`px-3 py-1 rounded-full border text-sm font-semibold ${getImpactColor(detail.impact)}`}>
                                {detail.impact} Impact
                              </span>
                              <span className="px-3 py-1 rounded-full bg-violet-500/20 border border-violet-500/30 text-violet-400 text-sm font-semibold">
                                {detail.confidence}% Confidence
                              </span>
                            </div>
                          </div>
                          <p className="text-slate-300 leading-relaxed">{detail.explanation}</p>
                        </div>
                      ))}
                    </div>
                  </AccordionContent>
                </AccordionItem>
              </Accordion>
            </Card>
          ))}
        </div>

        <PerformanceMetrics />
      </div>
    </section>
  );
};

export default AIExplainabilitySection;
