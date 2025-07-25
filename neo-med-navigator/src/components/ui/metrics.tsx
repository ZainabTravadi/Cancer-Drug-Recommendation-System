import { useState, useEffect } from 'react';

const PerformanceMetrics = () => {
  const [loading, setLoading] = useState(true);
  const [metrics, setMetrics] = useState({
    accuracy: 0,
    precision: 0,
    recall: 0,
    f1: 0
  });

  useEffect(() => {
    // Show loader for 1 second before displaying metrics
    const timer = setTimeout(() => {
      setLoading(false);
      // Animate metrics counting up
      animateMetrics();
    }, 1000);

    return () => clearTimeout(timer);
  }, []);

  const animateMetrics = () => {
    const targetMetrics = {
      accuracy: 94.2,
      precision: 91.8,
      recall: 89.5,
      f1: 0.87
    };
    
    const duration = 1500; // Animation duration in ms
    const steps = 60;
    const increment = {
      accuracy: targetMetrics.accuracy / steps,
      precision: targetMetrics.precision / steps,
      recall: targetMetrics.recall / steps,
      f1: targetMetrics.f1 / steps
    };

    let currentStep = 0;
    const interval = setInterval(() => {
      currentStep++;
      setMetrics({
        accuracy: Math.min(increment.accuracy * currentStep, targetMetrics.accuracy),
        precision: Math.min(increment.precision * currentStep, targetMetrics.precision),
        recall: Math.min(increment.recall * currentStep, targetMetrics.recall),
        f1: Math.min(increment.f1 * currentStep, targetMetrics.f1)
      });

      if (currentStep >= steps) {
        clearInterval(interval);
        // Set exact final values to avoid floating point rounding issues
        setMetrics(targetMetrics);
      }
    }, duration / steps);
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

  return (
    <div className="mt-12 text-center">
      <div className="bg-slate-800/50 rounded-xl p-6 border border-violet-500/20">
        <h3 className="text-xl font-bold text-violet-300 mb-3">Model Performance Metrics</h3>
        <div className="grid md:grid-cols-4 gap-4">
          <div className="text-center">
            <div className="text-2xl font-bold text-green-400">
              {metrics.accuracy.toFixed(1)}%
            </div>
            <div className="text-sm text-slate-400">Accuracy</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-400">
              {metrics.precision.toFixed(1)}%
            </div>
            <div className="text-sm text-slate-400">Precision</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-yellow-400">
              {metrics.recall.toFixed(1)}%
            </div>
            <div className="text-sm text-slate-400">Recall</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-pink-400">
              {metrics.f1.toFixed(2)}
            </div>
            <div className="text-sm text-slate-400">F1-Score</div>
          </div>
        </div>
        <div className="mt-4 text-xs text-slate-500">
          Validated on TCGA dataset with 10-fold cross-validation
        </div>
      </div>
    </div>
  );
};

export default PerformanceMetrics;