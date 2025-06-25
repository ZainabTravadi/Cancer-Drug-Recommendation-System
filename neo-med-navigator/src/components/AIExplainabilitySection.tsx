
import React, { useState } from 'react';
import { Card } from '@/components/ui/card';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';

const AIExplainabilitySection = () => {
  const [expandedSection, setExpandedSection] = useState<string | null>(null);

  const explainabilityData = [
    {
      id: "genomic-analysis",
      title: "Genomic Profile Analysis",
      icon: "🧬",
      description: "How your genetic data influenced the recommendations",
      details: [
        {
          factor: "BRCA1/2 Mutations",
          impact: "High",
          explanation: "Detected pathogenic variants in BRCA1 (c.5266dupC) increase sensitivity to PARP inhibitors like Olaparib by 340%",
          confidence: 96
        },
        {
          factor: "HER2 Expression",
          impact: "High", 
          explanation: "Overexpression of HER2 protein (3+ by IHC) makes Trastuzumab highly effective with 85% response rate",
          confidence: 94
        },
        {
          factor: "PD-L1 Status",
          impact: "Medium",
          explanation: "PD-L1 expression level of 65% suggests strong response to immune checkpoint inhibitors",
          confidence: 89
        }
      ]
    },
    {
      id: "pathway-analysis", 
      title: "Molecular Pathway Impact",
      icon: "🔬",
      description: "Critical pathways affected by identified mutations",
      details: [
        {
          factor: "DNA Repair Pathway",
          impact: "Critical",
          explanation: "Homologous recombination deficiency score of 42 indicates synthetic lethality with PARP inhibition",
          confidence: 92
        },
        {
          factor: "EGFR Signaling",
          impact: "Medium",
          explanation: "Wild-type EGFR with no resistance mutations supports TKI therapy effectiveness",
          confidence: 87
        },
        {
          factor: "Angiogenesis",
          impact: "Medium",
          explanation: "VEGF pathway activation score suggests anti-angiogenic therapy benefits",
          confidence: 83
        }
      ]
    },
    {
      id: "drug-interactions",
      title: "Drug Interaction Predictions", 
      icon: "⚗️",
      description: "AI-predicted drug synergies and contraindications",
      details: [
        {
          factor: "Pembrolizumab + Chemotherapy",
          impact: "Synergistic",
          explanation: "Combination therapy shows 23% improvement in progression-free survival vs monotherapy",
          confidence: 91
        },
        {
          factor: "Olaparib + Bevacizumab",
          impact: "Additive",
          explanation: "Dual targeting of DNA repair and angiogenesis pathways shows enhanced efficacy",
          confidence: 86
        },
        {
          factor: "CYP2D6 Polymorphisms",
          impact: "Caution",
          explanation: "Poor metabolizer genotype may require dose adjustments for certain agents",
          confidence: 78
        }
      ]
    }
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

        <div className="mt-12 text-center">
          <div className="bg-slate-800/50 rounded-xl p-6 border border-violet-500/20">
            <h3 className="text-xl font-bold text-violet-300 mb-3">Model Performance Metrics</h3>
            <div className="grid md:grid-cols-4 gap-4">
              <div className="text-center">
                <div className="text-2xl font-bold text-green-400">94.2%</div>
                <div className="text-sm text-slate-400">Accuracy</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-blue-400">91.8%</div>
                <div className="text-sm text-slate-400">Precision</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-yellow-400">89.5%</div>
                <div className="text-sm text-slate-400">Recall</div>
              </div>
              <div className="text-center">
                <div className="text-2xl font-bold text-pink-400">0.87</div>
                <div className="text-sm text-slate-400">F1-Score</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default AIExplainabilitySection;
