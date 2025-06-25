
import React from 'react';

const Navbar = () => {
  return (
    <nav className="fixed top-0 w-full z-50 glass-effect">
      <div className="max-w-7xl mx-auto px-6 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <div className="w-8 h-8 bg-gradient-to-r from-violet-500 to-pink-500 rounded-lg"></div>
            <span className="text-xl font-bold text-white">CancerAI</span>
          </div>
          
          <div className="hidden md:flex items-center space-x-8">
            <a href="#upload" className="text-slate-300 hover:text-violet-400 transition-colors">Upload Data</a>
            <a href="#recommendations" className="text-slate-300 hover:text-violet-400 transition-colors">Recommendations</a>
            <a href="#explainability" className="text-slate-300 hover:text-violet-400 transition-colors">AI Insights</a>
            <a href="#faq" className="text-slate-300 hover:text-violet-400 transition-colors">FAQ</a>
          </div>

          <button className="md:hidden text-white">
            <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
