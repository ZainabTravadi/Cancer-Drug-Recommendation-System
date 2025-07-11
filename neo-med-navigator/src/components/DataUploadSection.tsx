import React, { useState } from 'react';
import { Card } from '@/components/ui/card';
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue
} from '@/components/ui/select';

type DataUploadSectionProps = {
  setRecommendations: React.Dispatch<React.SetStateAction<any[]>>;
};

const DataUploadSection: React.FC<DataUploadSectionProps> = ({ setRecommendations }) => {
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [cancerType, setCancerType] = useState('');
  const [notes, setNotes] = useState('');
  const [dragActive, setDragActive] = useState(false);

  const cancerTypes = [
    'Breast Cancer',
    'Lung Cancer',
    'Colorectal Cancer',
    'Prostate Cancer',
    'Pancreatic Cancer',
    'Ovarian Cancer',
    'Brain Cancer',
    'Kidney Cancer'
  ];

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      if (file.size > 50 * 1024 * 1024) {
        alert('❌ File size exceeds 50MB limit.');
        return;
      }
      setUploadedFile(file);
    }
  };

  const handleDrop = (e: React.DragEvent<HTMLLabelElement>) => {
    e.preventDefault();
    setDragActive(false);
    const file = e.dataTransfer.files?.[0];
    if (file) {
      if (file.size > 50 * 1024 * 1024) {
        alert('❌ File size exceeds 50MB limit.');
        return;
      }
      setUploadedFile(file);
    }
  };

  const handleDragOver = (e: React.DragEvent<HTMLLabelElement>) => {
    e.preventDefault();
    setDragActive(true);
  };

  const handleDragLeave = () => {
    setDragActive(false);
  };

  const handleSubmit = async () => {
    if (!uploadedFile || !cancerType) {
      alert("📋 Please upload a file and select a cancer type.");
      return;
    }

    const formData = new FormData();
    formData.append("file", uploadedFile);
    formData.append("cancer_type", cancerType);
    formData.append("notes", notes);

    try {
      const response = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        console.error("❌ Backend returned error:", data);
        alert(`❌ ${data.detail || "Server error. Please try again."}`);
        return;
      }

      console.log("✅ AI Recommendations:", data);
      setRecommendations(data);

      // Scroll to recommendation section
      window.location.hash = "recommendations";
    } catch (error) {
      console.error("❌ Error uploading data:", error);
      alert("❌ Failed to connect to server. Please try again.");
    }
  };

  return (
    <section id="upload" className="py-20 bg-dark-gradient">
      <div className="max-w-6xl mx-auto px-6">
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-bold mb-6 text-glow">
            <span className="bg-gradient-to-r from-violet-400 to-pink-400 bg-clip-text text-transparent">
              Upload Your Data
            </span>
          </h2>
          <p className="text-xl text-slate-300 max-w-3xl mx-auto">
            Securely upload your genomic data and select cancer type for personalized AI analysis
          </p>
        </div>

        <div className="grid md:grid-cols-2 gap-8">
          {/* Genomic Data Upload */}
          <Card className="cyber-card">
            <h3 className="text-2xl font-bold mb-6 text-violet-300">Genomic Data File</h3>

            <div
              className={`border-2 border-dashed rounded-xl p-8 text-center transition-colors ${
                dragActive ? 'border-violet-500/70' : 'border-violet-500/30 hover:border-violet-500/50'
              }`}
            >
              <input
                type="file"
                accept=".vcf,.txt,.csv"
                onChange={handleFileUpload}
                className="hidden"
                id="genomic-upload"
                aria-label="Upload Genomic File"
              />

              <label
                htmlFor="genomic-upload"
                onDrop={handleDrop}
                onDragOver={handleDragOver}
                onDragLeave={handleDragLeave}
                className="cursor-pointer block"
              >
                <div className="mb-4">
                  <svg className="w-16 h-16 mx-auto text-violet-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"
                    />
                  </svg>
                </div>
                <p className="text-lg font-semibold text-white mb-2">
                  {uploadedFile ? uploadedFile.name : 'Drop or click to upload genomic file'}
                </p>
                <p className="text-slate-400">
                  Supports VCF, TXT, CSV formats (Max 50MB)
                </p>
              </label>
            </div>

            {uploadedFile && (
              <div className="mt-4 p-4 bg-violet-500/10 rounded-lg border border-violet-500/20">
                <div className="flex items-center justify-between">
                  <span className="text-sm text-violet-300">✓ File uploaded successfully</span>
                  <button
                    onClick={() => setUploadedFile(null)}
                    className="text-slate-400 hover:text-white"
                    aria-label="Remove uploaded file"
                  >
                    ✕
                  </button>
                </div>
              </div>
            )}
          </Card>

          {/* Cancer Type Selection */}
          <Card className="cyber-card">
            <h3 className="text-2xl font-bold mb-6 text-pink-300">Cancer Type</h3>

            <div className="space-y-6">
              <Select value={cancerType} onValueChange={setCancerType}>
                <SelectTrigger
                  className="w-full bg-slate-700/50 border-violet-500/30 text-white"
                  aria-label="Cancer Type Selector"
                >
                  <SelectValue placeholder="Select cancer type" />
                </SelectTrigger>
                <SelectContent className="bg-slate-800 border-violet-500/30">
                  {cancerTypes.map((type) => (
                    <SelectItem key={type} value={type} className="text-white hover:bg-violet-500/20">
                      {type}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>

              <div className="bg-slate-700/30 rounded-lg p-4">
                <h4 className="font-semibold text-cyan-300 mb-2">Additional Information</h4>
                <textarea
                  placeholder="Patient history, current treatments, or other relevant details..."
                  className="w-full bg-transparent border border-slate-600 rounded-lg p-3 text-white placeholder-slate-400 focus:border-violet-500 focus:outline-none"
                  rows={4}
                  aria-label="Additional information"
                  value={notes}
                  onChange={(e) => setNotes(e.target.value)}
                />
              </div>
            </div>
          </Card>
        </div>

        <div className="text-center mt-12">
          <button
            className="neon-button disabled:opacity-50 disabled:cursor-not-allowed"
            disabled={!uploadedFile || !cancerType}
            onClick={handleSubmit}
            aria-label="Analyze and Generate Recommendations"
          >
            🧬 Analyze Data & Generate Recommendations
          </button>

          {(!uploadedFile || !cancerType) && (
            <p className="text-sm text-slate-400 mt-2">
              Please upload a file and select a cancer type to proceed.
            </p>
          )}
        </div>
      </div>
    </section>
  );
};

export default DataUploadSection;
