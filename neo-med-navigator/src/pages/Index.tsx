
import React from 'react';
import Navbar from '@/components/Navbar';
import HeroSection from '@/components/HeroSection';
import DataUploadSection from '@/components/DataUploadSection';
import DrugRecommendationsSection from '@/components/DrugRecommendationsSection';
import AIExplainabilitySection from '@/components/AIExplainabilitySection';
import FAQSection from '@/components/FAQSection';
import Footer from '@/components/Footer';

const Index = () => {
  return (
    <div className="min-h-screen bg-slate-900">
      <Navbar />
      <HeroSection />
      <DataUploadSection />
      <DrugRecommendationsSection />
      <AIExplainabilitySection />
      <FAQSection />
      <Footer />
    </div>
  );
};

export default Index;
