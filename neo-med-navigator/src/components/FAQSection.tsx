
import React from 'react';
import { Card } from '@/components/ui/card';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';

const FAQSection = () => {
  const faqs = [
    {
      id: "accuracy",
      question: "How accurate are the AI drug recommendations?",
      answer: "Our AI model achieves 94.2% accuracy based on validation against clinical outcomes from over 50,000 cancer patients. The system is continuously updated with the latest clinical trial data and genomic research to maintain high precision in recommendations."
    },
    {
      id: "data-security",
      question: "How is my genomic data protected?",
      answer: "We employ bank-level encryption (AES-256) and comply with HIPAA, GDPR, and genomic data protection standards. Your data is processed in secure, isolated environments and is never shared with third parties. All data is automatically deleted after analysis unless you explicitly opt for storage."
    },
    {
      id: "upload-formats",
      question: "What file formats are supported for genomic data?",
      answer: "We support VCF (Variant Call Format), CSV with genomic annotations, TXT files with mutation lists, and raw sequencing data from major platforms including Illumina, Ion Torrent, and 23andMe. Maximum file size is 50MB per upload."
    },
    {
      id: "processing-time", 
      question: "How long does the analysis take?",
      answer: "Initial analysis typically completes within 5-10 minutes for standard genomic files. Complex whole-genome sequencing data may take up to 30 minutes. You'll receive real-time progress updates and can download preliminary results as they become available."
    },
    {
      id: "clinical-validation",
      question: "Are these recommendations clinically validated?",
      answer: "Yes, our recommendations are based on FDA-approved drugs and clinical trial data. However, these are AI-generated suggestions for discussion with your oncologist, not direct medical advice. Always consult with your healthcare provider before making treatment decisions."
    },
    {
      id: "cost-coverage",
      question: "Will insurance cover the recommended treatments?",
      answer: "Coverage varies by insurance provider and specific drugs. Our system includes insurance likelihood scores for each recommendation and can generate prior authorization support documents. We also provide information about patient assistance programs and clinical trial opportunities."
    },
    {
      id: "rare-cancers",
      question: "Does the system work for rare cancer types?",
      answer: "Our AI is trained on data from 200+ cancer subtypes, including many rare cancers. For ultra-rare conditions with limited data, the system uses pathway-based analysis and cross-cancer drug repositioning to provide the best possible recommendations."
    },
    {
      id: "updates",
      question: "How often are recommendations updated?",
      answer: "The AI model is retrained monthly with new clinical trial data, drug approvals, and genomic discoveries. Your stored profile is automatically re-analyzed when significant updates occur, and you'll be notified of any changes to your recommendations."
    }
  ];

  return (
    <section id="faq" className="py-20 bg-slate-900">
      <div className="max-w-4xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-glow">
            <span className="bg-gradient-to-r from-cyan-400 to-pink-400 bg-clip-text text-transparent">
              Frequently Asked Questions
            </span>
          </h2>
          <p className="text-xl text-slate-300">
            Everything you need to know about our AI cancer drug recommendation system
          </p>
        </div>

        <Card className="cyber-card">
          <Accordion type="single" collapsible className="space-y-1">
            {faqs.map((faq) => (
              <AccordionItem 
                key={faq.id} 
                value={faq.id}
                className="border border-slate-700/50 rounded-lg px-6 hover:border-violet-500/30 transition-colors"
              >
                <AccordionTrigger className="hover:no-underline py-6 text-left">
                  <span className="text-lg font-semibold text-white">{faq.question}</span>
                </AccordionTrigger>
                <AccordionContent className="pb-6">
                  <p className="text-slate-300 leading-relaxed">{faq.answer}</p>
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </Card>

        <div className="text-center mt-12">
          <div className="bg-gradient-to-r from-violet-500/10 to-pink-500/10 rounded-xl p-8 border border-violet-500/20">
            <h3 className="text-2xl font-bold text-white mb-4">Still have questions?</h3>
            <p className="text-slate-300 mb-6">
              Our team of geneticists and oncologists is here to help you understand your results
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <button className="neon-button">
                📧 Contact Support Team
              </button>
              <button className="bg-transparent border-2 border-violet-500/50 text-violet-300 font-semibold py-3 px-8 rounded-lg hover:bg-violet-500/10 transition-all duration-300">
                📞 Schedule Consultation
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FAQSection;
