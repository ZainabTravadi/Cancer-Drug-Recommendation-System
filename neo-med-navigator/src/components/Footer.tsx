
import React from 'react';

const Footer = () => {
  return (
    <footer className="bg-slate-950 border-t border-violet-500/20 py-12">
      <div className="max-w-6xl mx-auto px-6">
        <div className="grid md:grid-cols-4 gap-8">
          <div className="col-span-1">
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-8 h-8 bg-gradient-to-r from-violet-500 to-pink-500 rounded-lg"></div>
              <span className="text-xl font-bold text-white">CancerAI</span>
            </div>
            <p className="text-slate-400 mb-4">
              Advanced AI-powered cancer drug recommendations based on genomic analysis.
            </p>
            <div className="flex space-x-4">
              <div className="w-8 h-8 bg-violet-500/20 rounded-lg flex items-center justify-center text-violet-400 hover:bg-violet-500/30 cursor-pointer transition-colors">
                🐦
              </div>
              <div className="w-8 h-8 bg-violet-500/20 rounded-lg flex items-center justify-center text-violet-400 hover:bg-violet-500/30 cursor-pointer transition-colors">
                💼
              </div>
              <div className="w-8 h-8 bg-violet-500/20 rounded-lg flex items-center justify-center text-violet-400 hover:bg-violet-500/30 cursor-pointer transition-colors">
                📧
              </div>
            </div>
          </div>

          <div>
            <h4 className="font-semibold text-white mb-4">Platform</h4>
            <ul className="space-y-2 text-slate-400">
              <li><a href="#" className="hover:text-violet-400 transition-colors">How it Works</a></li>
              <li><a href="#" className="hover:text-violet-400 transition-colors">Supported Cancers</a></li>
              <li><a href="#" className="hover:text-violet-400 transition-colors">Clinical Evidence</a></li>
              <li><a href="#" className="hover:text-violet-400 transition-colors">API Access</a></li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold text-white mb-4">Resources</h4>
            <ul className="space-y-2 text-slate-400">
              <li><a href="#" className="hover:text-violet-400 transition-colors">Documentation</a></li>
              <li><a href="#" className="hover:text-violet-400 transition-colors">Research Papers</a></li>
              <li><a href="#" className="hover:text-violet-400 transition-colors">Case Studies</a></li>
              <li><a href="#" className="hover:text-violet-400 transition-colors">Webinars</a></li>
            </ul>
          </div>

          <div>
            <h4 className="font-semibold text-white mb-4">Support</h4>
            <ul className="space-y-2 text-slate-400">
              <li><a href="#" className="hover:text-violet-400 transition-colors">Help Center</a></li>
              <li><a href="#" className="hover:text-violet-400 transition-colors">Contact Us</a></li>
              <li><a href="#" className="hover:text-violet-400 transition-colors">Privacy Policy</a></li>
              <li><a href="#" className="hover:text-violet-400 transition-colors">Terms of Service</a></li>
            </ul>
          </div>
        </div>

        <div className="border-t border-slate-800 mt-8 pt-8 flex flex-col sm:flex-row justify-between items-center">
          <p className="text-slate-400 text-sm">
            © 2024 CancerAI. All rights reserved. Not for direct clinical use.
          </p>
          <div className="flex items-center space-x-4 mt-4 sm:mt-0">
            <span className="text-xs text-slate-500">Powered by</span>
            <div className="flex items-center space-x-2">
              <div className="w-4 h-4 bg-gradient-to-r from-violet-500 to-pink-500 rounded"></div>
              <span className="text-xs text-slate-400">Advanced AI Research</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
