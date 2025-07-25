
import React from 'react';
import { Card } from '@/components/ui/card';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '@/components/ui/accordion';

const FAQSection = () => {
  const faqs = [
    {
      id: "accuracy",
      question: "Is this a real medical application?",
      answer: "No, this is a demonstration project created for educational purposes only. The drug recommendations and genomic analysis shown are simulated and should not be used for actual medical decisions. Always consult with a qualified healthcare provider for medical advice."
    },
    {
      id: "data-security",
      question: "Where does the sample data come from?",
      answer: "The genomic and drug data in this project is synthesized from publicly available research datasets and clinical trial information. No real patient data is used in this demonstration. All patient IDs and genomic profiles are fictional examples."
    },
    {
      id: "upload-formats",
      question: "What file formats are supported for genomic data?",
      answer: "We support VCF (Variant Call Format), CSV with genomic annotations, TXT files with mutation lists, and raw sequencing data from major platforms including Illumina, Ion Torrent, and 23andMe. Maximum file size is 50MB per upload."
    },
    {
      id: "processing-time", 
      question: "How long does the analysis take?",
      answer: "Initial analysis typically completes within 5 minutes for standard genomic files."
    },
    {
      id: "limitations",
      question: "What are the key limitations of this demo?",
      answer: "1) No real patient data processing 2) Simplified mock algorithms 3) Static dataset 4) No HIPAA compliance needed (as it's a demo) 5) Treatment timelines/outcomes are completely simulated."
    },
    {
      id: "extension",
      question: "How could this be extended for real clinical use?",
      answer: "To make this production-ready would require: 1) Integration with real genomic pipelines 2) FDA-approved algorithms 3) HIPAA-compliant infrastructure 4) Clinician validation workflows 5) Ongoing clinical trial data integration."
    },
    {
      id: "contributing",
      question: "Can I contribute to or modify this project?",
      answer: "Yes! This is an open-source educational project."
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
              Feel free to reach out to understand the project or discuss improvements.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
  <a
    href="https://www.linkedin.com/in/zainab-travadi-119a83373" 
    target="_blank"
    rel="noopener noreferrer"
    className="neon-button">
    💼 Connect on LinkedIn
  </a>
  <a
    href="mailto:zainabtravadi421@gmail.com"
    className="bg-transparent border-2 border-violet-500/50 text-violet-300 font-semibold py-3 px-8 rounded-lg hover:bg-violet-500/10 transition-all duration-300">
    📧 Email Me
  </a>
</div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default FAQSection;
