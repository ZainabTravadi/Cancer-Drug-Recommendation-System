
import React from 'react';

const HeroSection = () => {
  const handleSubmit = () => {

  // ✅ Navigate 
  window.location.hash = "upload";
};
const handleLearnMore = () => {

  // ✅ Navigate 
  window.location.hash = "faq";
};

  return (
    <section className="min-h-screen flex items-center justify-center relative overflow-hidden bg-cyber-gradient">
      {/* Animated background elements */}
      <div className="absolute inset-0">
        <div className="absolute top-20 left-10 w-72 h-72 bg-violet-500/10 rounded-full blur-3xl animate-float"></div>
        <div className="absolute bottom-20 right-10 w-96 h-96 bg-pink-500/10 rounded-full blur-3xl animate-float" style={{animationDelay: '-3s'}}></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-cyan-500/10 rounded-full blur-3xl animate-float" style={{animationDelay: '-1.5s'}}></div>
      </div>

      <div className="max-w-6xl mx-auto px-6 text-center relative z-10">
        <div className="animate-fade-in-up">
          <h1 className="text-6xl md:text-8xl font-bold mb-6 text-glow">
            <span className="bg-gradient-to-r from-violet-400 via-pink-400 to-cyan-400 bg-clip-text text-transparent">
              Cancer Drug
            </span>
            <br />
            <span className="text-white">Recommendations</span>
          </h1>
          
          <p className="text-xl md:text-2xl text-slate-300 mb-8 max-w-3xl mx-auto leading-relaxed">
            Advanced AI-powered analysis of genomic data to provide personalized cancer treatment recommendations with unprecedented accuracy.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
            <button className="neon-button animate-glow-pulse group" onClick={handleSubmit}>
              <span className="flex items-center gap-2">
                📊 Upload Report & Get Recommendations
                <svg className="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </span>
            </button>
            
            <button className="bg-transparent border-2 border-violet-500/50 text-violet-100 font-semibold py-3 px-8 rounded-lg hover:bg-violet-500 transition-all duration-300" onClick={handleLearnMore}>
              Learn More
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
