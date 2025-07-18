import React, { useEffect, useState } from 'react';
import { Card } from '@/components/ui/card';

type Drug = {
  id: string | number;
  name: string;
  confidence: number;
  ic50: string | number;
  description: string;
  mechanism: string;
  side_effects: string;
  clinical_evidence: string;
};

type DrugRecommendationsSectionProps = {
  recommendations: Drug[];
};

const DrugRecommendationsSection: React.FC<DrugRecommendationsSectionProps> = ({ recommendations = [] }) => {
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (recommendations.length > 0) {
      setLoading(true);
      const timer = setTimeout(() => setLoading(false), 1500);
      return () => clearTimeout(timer);
    }
  }, [recommendations]);

  const getConfidenceColor = (confidence?: number) => {
    if (confidence === undefined) return '';
    if (confidence >= 90) return 'text-green-400';
    if (confidence >= 80) return 'text-yellow-400';
    return 'text-orange-400';
  };

  const getConfidenceBg = (confidence?: number) => {
    if (confidence === undefined) return '';
    if (confidence >= 90) return 'bg-green-500/20 border-green-500/30';
    if (confidence >= 80) return 'bg-yellow-500/20 border-yellow-500/30';
    return 'bg-orange-500/20 border-orange-500/30';
  };

  const handleDownloadPDF = () => {
    alert('📄 PDF download coming soon!');
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
            border-top: 5px solid #8b5cf6;
            border-right: 5px solid #ec4899;
            border-radius: 50%;
            animation: spin 1s linear infinite, glow 1.5s ease-in-out infinite alternate;
          }
          @keyframes spin {
            to { transform: rotate(360deg); }
          }
          @keyframes glow {
            0% { box-shadow: 0 0 10px #8b5cf6, 0 0 20px #ec4899; }
            100% { box-shadow: 0 0 20px #8b5cf6, 0 0 30px #ec4899; }
          }
        `}</style>
      </section>
    );
  }

  if (!recommendations || recommendations.length === 0) {
    return (
      <section id="recommendations" className="py-20 bg-slate-900 text-center text-white">
        <p className="text-xl text-slate-400">
          No recommendations to display yet. Please upload your genomic file and analyze data.
        </p>
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
            <Card key={drug.id || index} className="cyber-card hover:scale-[1.02] transition-all duration-300">
              <div className="flex flex-col lg:flex-row lg:items-center gap-6">
                <div className="flex-shrink-0">
                  <div className="w-16 h-16 bg-gradient-to-r from-violet-500 to-pink-500 rounded-full flex items-center justify-center text-2xl font-bold text-white">
                    #{index + 1}
                  </div>
                </div>

                <div className="flex-grow space-y-4">
                  <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
                    <h3 className="text-2xl font-bold text-white">{drug.name || 'Unnamed Drug'}</h3>
                    <div className="flex gap-4">
                      <div className={`px-3 py-1 rounded-full border ${getConfidenceBg(drug.confidence)}`}>
                        <span className={`text-sm font-semibold ${getConfidenceColor(drug.confidence)}`}>
                          {drug.confidence ?? '--'}% Confidence
                        </span>
                      </div>
                      <div className="px-3 py-1 rounded-full bg-blue-500/20 border border-blue-500/30">
                        <span className="text-sm font-semibold text-blue-400">
                          IC50: {drug.ic50 ?? '--'}
                        </span>
                      </div>
                    </div>
                  </div>

                  <p className="text-slate-300 leading-relaxed">
                    {drug.description || 'No description available.'}
                  </p>

                  <div className="grid md:grid-cols-3 gap-4">
                    <div className="bg-slate-700/30 rounded-lg p-4">
                      <h4 className="font-semibold text-cyan-300 mb-1">Mechanism</h4>
                      <p className="text-sm text-slate-300">{drug.mechanism || 'N/A'}</p>
                    </div>
                    <div className="bg-slate-700/30 rounded-lg p-4">
                      <h4 className="font-semibold text-yellow-300 mb-1">Side Effects</h4>
                      <p className="text-sm text-slate-300">{drug.side_effects || 'N/A'}</p>
                    </div>
                    <div className="bg-slate-700/30 rounded-lg p-4">
                      <h4 className="font-semibold text-green-300 mb-1">Clinical Evidence</h4>
                      <p className="text-sm text-slate-300">{drug.clinical_evidence || 'N/A'}</p>
                    </div>
                  </div>
                </div>

                <div className="flex-shrink-0">
                  <button
                    className="bg-gradient-to-r from-violet-500/20 to-pink-500/20 border border-violet-500/30 text-violet-300 px-6 py-2 rounded-lg hover:bg-gradient-to-r hover:from-violet-500/30 hover:to-pink-500/30 transition-all duration-300"
                    aria-label={`View more details about ${drug.name}`}
                  >
                    View Details
                  </button>
                </div>
              </div>
            </Card>
          ))}
        </div>

        <div className="text-center mt-12">
          <button
            className="neon-button"
            onClick={handleDownloadPDF}
            aria-label="Download full report as PDF"
          >
            📄 Download Detailed Report (PDF)
          </button>
        </div>
      </div>
    </section>
  );
};

export default DrugRecommendationsSection;
