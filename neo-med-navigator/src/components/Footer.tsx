import React from 'react';

const Footer = () => {
  // Social and Contact Links
  const socialLinks = {
    twitter: "https://twitter.com/yourusername",
    linkedin: "https://www.linkedin.com/in/zainab-travadi-119a83373/",
    github: "https://github.com/ZainabTravadi",
    email: "mailto:zainabtravadi421@gmail.com",
    resume: "https://docs.google.com/your-resume-link"
  };

  // Resources and Tools Links
  const resourceLinks = {
    documentation: "http://www.bccancer.bc.ca/health-professionals/clinical-resources/cancer-drug-manual/drug-index",
    researchPapers: "https://www.cancer.gov/about-cancer/treatment/drugs/cancer-type",
    postman: "https://www.postman.com/",
    fastapi: "https://fastapi.tiangolo.com/",
  };

  return (
    <footer className="bg-slate-950 border-t border-violet-500/20 py-12">
      <div className="max-w-6xl mx-auto px-6">
        <div className="grid md:grid-cols-4 gap-8">
          {/* Brand Section */}
          <div className="col-span-1">
            <div className="flex items-center space-x-2 mb-4">
              <div className="w-8 h-8 bg-gradient-to-r from-violet-500 to-pink-500 rounded-lg"></div>
              <span className="text-xl font-bold text-white">ChemoChoice</span>
            </div>
            <p className="text-slate-400 mb-4">
              Cancer drug recommendations based on genomic analysis.
            </p>
            <div className="flex space-x-4">
              <a href={socialLinks.twitter} target="_blank" rel="noopener noreferrer"
                className="w-8 h-8 bg-violet-500/20 rounded-lg flex items-center justify-center text-violet-400 hover:bg-violet-500/30 transition-colors"
                aria-label="Twitter">
                🐦
              </a>
              <a href={socialLinks.linkedin} target="_blank" rel="noopener noreferrer"
                className="w-8 h-8 bg-violet-500/20 rounded-lg flex items-center justify-center text-violet-400 hover:bg-violet-500/30 transition-colors"
                aria-label="LinkedIn">
                💼
              </a>
              <a href={socialLinks.email}
                className="w-8 h-8 bg-violet-500/20 rounded-lg flex items-center justify-center text-violet-400 hover:bg-violet-500/30 transition-colors"
                aria-label="Email">
                📧
              </a>
            </div>
          </div>

          {/* About Section */}
          <div>
            <h4 className="font-semibold text-white mb-4">About me</h4>
            <ul className="space-y-2 text-slate-400">
              <li>Zainab Travadi</li>
              <li>Data Scientist IN THE MAKING</li>
              <li>B Tech CSE</li>
              <li>Parul University</li>
            </ul>
          </div>

          {/* Contacts Section */}
          <div>
            <h4 className="font-semibold text-white mb-4">Contacts & Links</h4>
            <ul className="space-y-2 text-slate-400">
              <li>
                <a href={socialLinks.linkedin} target="_blank" rel="noopener noreferrer"
                  className="hover:text-violet-400 transition-colors">
                  LinkedIn
                </a>
              </li>
              <li>
                <a href={socialLinks.github} target="_blank" rel="noopener noreferrer"
                  className="hover:text-violet-400 transition-colors">
                  GitHub
                </a>
              </li>
              <li>
                <a href={socialLinks.email}
                  className="hover:text-violet-400 transition-colors">
                  Email
                </a>
              </li>
              <li>
                <a href={socialLinks.resume} target="_blank" rel="noopener noreferrer"
                  className="hover:text-violet-400 transition-colors">
                  Resume
                </a>
              </li>
            </ul>
          </div>

          {/* Resources Section */}
          <div>
            <h4 className="font-semibold text-white mb-4">Resources & Tools</h4>
            <ul className="space-y-2 text-slate-400">
              <li>
                <a href={resourceLinks.documentation} target="_blank" rel="noopener noreferrer"
                  className="hover:text-violet-400 transition-colors">
                  Documentation
                </a>
              </li>
              <li>
                <a href={resourceLinks.researchPapers} target="_blank" rel="noopener noreferrer"
                  className="hover:text-violet-400 transition-colors">
                  Research Papers
                </a>
              </li>
              <li>
                <a href={resourceLinks.postman} target="_blank" rel="noopener noreferrer"
                  className="hover:text-violet-400 transition-colors">
                  Postman
                </a>
              </li>
              <li>
                <a href={resourceLinks.fastapi} target="_blank" rel="noopener noreferrer"
                  className="hover:text-violet-400 transition-colors">
                  FastAPI
                </a>
              </li>
            </ul>
          </div>
        </div>

        {/* Footer Bottom */}
        <div className="border-t border-slate-800 mt-8 pt-8 flex flex-col sm:flex-row justify-between items-center">
          <p className="text-slate-400 text-sm">
            © 2025 ChemoChoice. All rights reserved. Not for direct clinical use.
          </p>
          <div className="flex items-center space-x-4 mt-4 sm:mt-0">
            <span className="text-xs text-slate-500">Powered by</span>
            <div className="flex items-center space-x-2">
              <div className="w-4 h-4 bg-gradient-to-r from-violet-500 to-pink-500 rounded"></div>
              <span className="text-xs text-slate-400">Advanced Research</span>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;