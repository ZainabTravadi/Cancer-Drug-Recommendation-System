
import React, { useEffect, useState } from 'react';
import { Card } from '@/components/ui/card';

const DrugRecommendationsSection = () => {
  const [loading, setLoading] = useState(true);

  // Simulate loading delay (e.g., fetching or processing data)
  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 2000); // 2.5 seconds
    return () => clearTimeout(timer);
  }, []);
  const recommendations = [
    {
      id: 1,
      name: "Pembrolizumab (Keytruda)",
      ic50: "0.12 nM",
      confidence: 94,
      description: "PD-1 inhibitor that enhances immune system response against cancer cells. Highly effective for tumors with high PD-L1 expression.",
      mechanism: "Immune checkpoint inhibitor",
      sideEffects: "Mild to moderate immune-related adverse events",
      clinicalTrial: "Phase III KEYNOTE-189"
    },
    {
      id: 2,
      name: "Trastuzumab (Herceptin)",
      ic50: "0.08 nM",
      confidence: 91,
      description: "Monoclonal antibody targeting HER2 protein overexpressed in certain breast cancers. Blocks growth signals.",
      mechanism: "HER2 receptor antagonist",
      sideEffects: "Cardiotoxicity, infusion reactions",
      clinicalTrial: "Phase III HERA study"
    },
    {
      id: 3,
      name: "Osimertinib (Tagrisso)",
      ic50: "0.15 nM",
      confidence: 88,
      description: "Third-generation EGFR tyrosine kinase inhibitor effective against T790M resistance mutations in NSCLC.",
      mechanism: "EGFR tyrosine kinase inhibitor",
      sideEffects: "Diarrhea, rash, nail toxicity",
      clinicalTrial: "Phase III FLAURA study"
    },
    {
      id: 4,
      name: "Olaparib (Lynparza)",
      ic50: "0.22 nM",
      confidence: 85,
      description: "PARP inhibitor particularly effective in BRCA-mutated cancers. Prevents DNA repair in cancer cells.",
      mechanism: "PARP enzyme inhibitor",
      sideEffects: "Nausea, fatigue, anemia",
      clinicalTrial: "Phase III OlympiAD"
    },
    {
      id: 5,
      name: "Bevacizumab (Avastin)",
      ic50: "0.35 nM",
      confidence: 82,
      description: "Anti-angiogenic therapy that inhibits VEGF, preventing formation of new blood vessels that feed tumors.",
      mechanism: "VEGF-A inhibitor",
      sideEffects: "Hypertension, bleeding risk",
      clinicalTrial: "Phase III AVAiL study"
    }
  ];

  const getConfidenceColor = (confidence: number) => {
    if (confidence >= 90) return "text-green-400";
    if (confidence >= 80) return "text-yellow-400";
    return "text-orange-400";
  };

  const getConfidenceBg = (confidence: number) => {
    if (confidence >= 90) return "bg-green-500/20 border-green-500/30";
    if (confidence >= 80) return "bg-yellow-500/20 border-yellow-500/30";
    return "bg-orange-500/20 border-orange-500/30";
  };

  if (loading) {
  return (
    <section className="min-h-screen flex flex-col justify-center items-center bg-slate-900 text-white">
      <div className="custom-loader mb-6" />
      <p className="text-xl text-violet-300 animate-pulse">
        Analyzing your genomic data...
      </p>

      <style>{`
        .custom-loader {
          width: 64px;
          height: 64px;
          border: 5px solid transparent;
          border-top: 5px solid #8b5cf6; /* violet-500 */
          border-right: 5px solid #ec4899; /* pink-500 */
          border-radius: 50%;
          animation: spin 1s linear infinite, glow 1.5s ease-in-out infinite alternate;
        }

        @keyframes spin {
          to { transform: rotate(360deg); }
        }

        @keyframes glow {
          0% {
            box-shadow: 0 0 10px #8b5cf6, 0 0 20px #ec4899;
          }
          100% {
            box-shadow: 0 0 20px #8b5cf6, 0 0 30px #ec4899;
          }
        }
      `}</style>
    </section>
  );
}


  return (
    <section id="recommendations" className="py-20 bg-slate-900">
      <div className="max-w-7xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-glow">
            <span className="bg-gradient-to-r from-cyan-400 to-violet-400 bg-clip-text text-transparent">
              AI-Powered Recommendations
            </span>
          </h2>
          <p className="text-xl text-slate-300 max-w-3xl mx-auto">
            Top 5 personalized drug recommendations based on your genomic profile and cancer type analysis
          </p>
        </div>

        <div className="grid gap-6">
          {recommendations.map((drug, index) => (
            <Card key={drug.id} className="cyber-card hover:scale-[1.02] transition-all duration-300">
              <div className="flex flex-col lg:flex-row lg:items-center gap-6">
                {/* Rank Badge */}
                <div className="flex-shrink-0">
                  <div className="w-16 h-16 bg-gradient-to-r from-violet-500 to-pink-500 rounded-full flex items-center justify-center text-2xl font-bold text-white">
                    #{index + 1}
                  </div>
                </div>

                {/* Drug Information */}
                <div className="flex-grow space-y-4">
                  <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
                    <h3 className="text-2xl font-bold text-white">{drug.name}</h3>
                    <div className="flex gap-4">
                      <div className={`px-3 py-1 rounded-full border ${getConfidenceBg(drug.confidence)}`}>
                        <span className={`text-sm font-semibold ${getConfidenceColor(drug.confidence)}`}>
                          {drug.confidence}% Confidence
                        </span>
                      </div>
                      <div className="px-3 py-1 rounded-full bg-blue-500/20 border border-blue-500/30">
                        <span className="text-sm font-semibold text-blue-400">
                          IC50: {drug.ic50}
                        </span>
                      </div>
                    </div>
                  </div>

                  <p className="text-slate-300 leading-relaxed">{drug.description}</p>

                  <div className="grid md:grid-cols-3 gap-4">
                    <div className="bg-slate-700/30 rounded-lg p-4">
                      <h4 className="font-semibold text-cyan-300 mb-1">Mechanism</h4>
                      <p className="text-sm text-slate-300">{drug.mechanism}</p>
                    </div>
                    <div className="bg-slate-700/30 rounded-lg p-4">
                      <h4 className="font-semibold text-yellow-300 mb-1">Side Effects</h4>
                      <p className="text-sm text-slate-300">{drug.sideEffects}</p>
                    </div>
                    <div className="bg-slate-700/30 rounded-lg p-4">
                      <h4 className="font-semibold text-green-300 mb-1">Clinical Evidence</h4>
                      <p className="text-sm text-slate-300">{drug.clinicalTrial}</p>
                    </div>
                  </div>
                </div>

                {/* Action Button */}
                <div className="flex-shrink-0">
                  <button className="bg-gradient-to-r from-violet-500/20 to-pink-500/20 border border-violet-500/30 text-violet-300 px-6 py-2 rounded-lg hover:bg-gradient-to-r hover:from-violet-500/30 hover:to-pink-500/30 transition-all duration-300">
                    View Details
                  </button>
                </div>
              </div>
            </Card>
          ))}
        </div>

        <div className="text-center mt-12">
          <button className="neon-button">
            📄 Download Detailed Report (PDF)
          </button>
        </div>
      </div>
    </section>
  );
};

export default DrugRecommendationsSection;
