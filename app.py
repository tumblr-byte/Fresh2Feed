import React, { useState } from 'react';
import { Upload, Video, AlertCircle, CheckCircle, Download, Info, Camera, Shield, Loader2 } from 'lucide-react';

export default function CivicLens() {
  const [uploadedFile, setUploadedFile] = useState(null);
  const [processing, setProcessing] = useState(false);
  const [processComplete, setProcessComplete] = useState(false);
  const [violatorDetected, setViolatorDetected] = useState(false);
  const [violatorCount, setViolatorCount] = useState(0);
  const [showAlert, setShowAlert] = useState(false);
  const [videoPreview, setVideoPreview] = useState(null);

  const handleFileUpload = (e) => {
    const file = e.target.files[0];
    if (file && file.type.startsWith('video/')) {
      setUploadedFile(file);
      setVideoPreview(URL.createObjectURL(file));
      setProcessComplete(false);
      setViolatorDetected(false);
      setShowAlert(false);
    }
  };

  const processVideo = () => {
    setProcessing(true);
    setProcessComplete(false);
    
    // Simulate video processing
    setTimeout(() => {
      setProcessing(false);
      setProcessComplete(true);
      
      // Simulate violator detection (50% chance for demo)
      const detected = Math.random() > 0.5;
      setViolatorDetected(detected);
      
      if (detected) {
        const count = Math.floor(Math.random() * 3) + 1;
        setViolatorCount(count);
        setShowAlert(true);
      }
    }, 5000);
  };

  const downloadProcessedVideo = () => {
    // In real implementation, this would download the processed video
    alert('Processed video with annotations would be downloaded here');
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900">
      {/* Alert Popup */}
      {showAlert && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl shadow-2xl max-w-md w-full animate-bounce">
            <div className="bg-red-500 text-white p-6 rounded-t-2xl">
              <div className="flex items-center gap-3">
                <AlertCircle className="w-8 h-8" />
                <h3 className="text-2xl font-bold">Violator Detected!</h3>
              </div>
            </div>
            <div className="p-6">
              <p className="text-gray-700 text-lg mb-4">
                We detected {violatorCount} person(s) with waste in the frame.
              </p>
              <p className="text-gray-600 mb-6">
                Images have been saved in the 'violators' folder for review.
              </p>
              <button
                onClick={() => setShowAlert(false)}
                className="w-full bg-red-500 hover:bg-red-600 text-white font-semibold py-3 rounded-lg transition-colors"
              >
                Acknowledge
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Header */}
      <header className="bg-black bg-opacity-30 backdrop-blur-md border-b border-white border-opacity-10">
        <div className="max-w-7xl mx-auto px-6 py-6">
          <div className="flex items-center gap-4">
            <div className="bg-gradient-to-br from-blue-500 to-cyan-500 p-3 rounded-xl shadow-lg">
              <Camera className="w-8 h-8 text-white" />
            </div>
            <div>
              <h1 className="text-4xl font-bold text-white tracking-tight">CivicLens</h1>
              <p className="text-blue-200 text-sm">AI-Powered Littering Detection System</p>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-6 py-12">
        {/* Info Banner */}
        <div className="bg-blue-500 bg-opacity-20 backdrop-blur-md border border-blue-400 border-opacity-30 rounded-2xl p-6 mb-8">
          <div className="flex items-start gap-4">
            <Info className="w-6 h-6 text-blue-300 flex-shrink-0 mt-1" />
            <div className="text-blue-100">
              <h3 className="font-semibold text-lg mb-2">How CivicLens Works</h3>
              <p className="text-sm leading-relaxed mb-3">
                This system detects littering violations by tracking persons who are already present in the frame holding waste - not those entering the frame with waste already in hand.
              </p>
              <ul className="space-y-1 text-sm">
                <li>• Identifies waste and persons in real-time</li>
                <li>• Tracks hand proximity to waste items</li>
                <li>• Flags violators when waste is dropped outside dustbins</li>
                <li>• Captures evidence with bounding boxes and annotations</li>
              </ul>
            </div>
          </div>
        </div>

        {/* Upload Section */}
        <div className="grid lg:grid-cols-2 gap-8 mb-8">
          {/* Upload Card */}
          <div className="bg-white bg-opacity-10 backdrop-blur-md rounded-2xl p-8 border border-white border-opacity-20 shadow-2xl">
            <h2 className="text-2xl font-bold text-white mb-6 flex items-center gap-3">
              <Upload className="w-7 h-7 text-cyan-400" />
              Upload Video
            </h2>
            
            <div className="mb-6">
              <label className="block w-full">
                <div className={`border-3 border-dashed rounded-xl p-12 text-center cursor-pointer transition-all ${
                  uploadedFile 
                    ? 'border-green-400 bg-green-500 bg-opacity-10' 
                    : 'border-blue-400 hover:border-cyan-400 hover:bg-blue-500 hover:bg-opacity-10'
                }`}>
                  <input
                    type="file"
                    accept="video/*"
                    onChange={handleFileUpload}
                    className="hidden"
                  />
                  {uploadedFile ? (
                    <div className="space-y-3">
                      <CheckCircle className="w-16 h-16 text-green-400 mx-auto" />
                      <p className="text-white font-semibold text-lg">{uploadedFile.name}</p>
                      <p className="text-green-300 text-sm">Ready to process</p>
                    </div>
                  ) : (
                    <div className="space-y-3">
                      <Video className="w-16 h-16 text-blue-400 mx-auto" />
                      <p className="text-white font-semibold">Click to upload video</p>
                      <p className="text-blue-300 text-sm">or drag and drop</p>
                    </div>
                  )}
                </div>
              </label>
            </div>

            {/* Requirements */}
            <div className="bg-yellow-500 bg-opacity-20 border border-yellow-400 border-opacity-30 rounded-xl p-4">
              <h4 className="font-semibold text-yellow-200 mb-2 flex items-center gap-2">
                <AlertCircle className="w-5 h-5" />
                Video Requirements
              </h4>
              <ul className="text-yellow-100 text-sm space-y-1">
                <li>• Duration: Maximum 10 seconds</li>
                <li>• Quality: Clean, well-lit footage</li>
                <li>• Framing: Close-up (not too close, not too far)</li>
                <li>• Content: Clear view of persons and waste items</li>
              </ul>
            </div>

            {uploadedFile && !processing && !processComplete && (
              <button
                onClick={processVideo}
                className="w-full mt-6 bg-gradient-to-r from-blue-500 to-cyan-500 hover:from-blue-600 hover:to-cyan-600 text-white font-bold py-4 rounded-xl shadow-lg transition-all transform hover:scale-105"
              >
                Start Processing
              </button>
            )}

            {processing && (
              <div className="mt-6 bg-blue-500 bg-opacity-20 border border-blue-400 border-opacity-30 rounded-xl p-6 text-center">
                <Loader2 className="w-12 h-12 text-blue-400 mx-auto mb-3 animate-spin" />
                <p className="text-white font-semibold">Processing video...</p>
                <p className="text-blue-300 text-sm mt-2">Analyzing frames and detecting violations</p>
              </div>
            )}

            {processComplete && (
              <div className="mt-6 space-y-4">
                <div className={`border rounded-xl p-6 ${
                  violatorDetected 
                    ? 'bg-red-500 bg-opacity-20 border-red-400' 
                    : 'bg-green-500 bg-opacity-20 border-green-400'
                } border-opacity-30`}>
                  <div className="flex items-center gap-3 mb-3">
                    {violatorDetected ? (
                      <>
                        <AlertCircle className="w-8 h-8 text-red-400" />
                        <h3 className="text-xl font-bold text-red-200">Violations Detected</h3>
                      </>
                    ) : (
                      <>
                        <CheckCircle className="w-8 h-8 text-green-400" />
                        <h3 className="text-xl font-bold text-green-200">No Violations</h3>
                      </>
                    )}
                  </div>
                  <p className={violatorDetected ? 'text-red-200' : 'text-green-200'}>
                    {violatorDetected 
                      ? `${violatorCount} violator(s) identified and saved`
                      : 'Video processed successfully with no violations'}
                  </p>
                </div>

                <button
                  onClick={downloadProcessedVideo}
                  className="w-full bg-gradient-to-r from-green-500 to-emerald-500 hover:from-green-600 hover:to-emerald-600 text-white font-bold py-4 rounded-xl shadow-lg transition-all transform hover:scale-105 flex items-center justify-center gap-2"
                >
                  <Download className="w-5 h-5" />
                  Download Annotated Video
                </button>
              </div>
            )}
          </div>

          {/* Preview Card */}
          <div className="bg-white bg-opacity-10 backdrop-blur-md rounded-2xl p-8 border border-white border-opacity-20 shadow-2xl">
            <h2 className="text-2xl font-bold text-white mb-6 flex items-center gap-3">
              <Video className="w-7 h-7 text-cyan-400" />
              Video Preview
            </h2>
            
            {videoPreview ? (
              <div className="rounded-xl overflow-hidden bg-black shadow-lg">
                <video
                  src={videoPreview}
                  controls
                  className="w-full"
                  style={{ maxHeight: '400px' }}
                >
                  Your browser does not support video playback.
                </video>
              </div>
            ) : (
              <div className="border-2 border-dashed border-gray-600 rounded-xl p-16 text-center bg-black bg-opacity-30">
                <Video className="w-20 h-20 text-gray-500 mx-auto mb-4" />
                <p className="text-gray-400">No video uploaded</p>
              </div>
            )}

            {processComplete && (
              <div className="mt-6 bg-gradient-to-r from-purple-500 to-pink-500 bg-opacity-20 border border-purple-400 border-opacity-30 rounded-xl p-6">
                <h4 className="font-semibold text-purple-200 mb-3 flex items-center gap-2">
                  <Shield className="w-5 h-5" />
                  Processing Summary
                </h4>
                <div className="space-y-2 text-sm">
                  <div className="flex justify-between text-purple-100">
                    <span>Frames Analyzed:</span>
                    <span className="font-semibold">250</span>
                  </div>
                  <div className="flex justify-between text-purple-100">
                    <span>Persons Tracked:</span>
                    <span className="font-semibold">3</span>
                  </div>
                  <div className="flex justify-between text-purple-100">
                    <span>Waste Items Detected:</span>
                    <span className="font-semibold">5</span>
                  </div>
                  <div className="flex justify-between text-purple-100">
                    <span>Violators Identified:</span>
                    <span className="font-semibold text-red-300">{violatorCount}</span>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Features Section */}
        <div className="grid md:grid-cols-3 gap-6">
          <div className="bg-white bg-opacity-10 backdrop-blur-md rounded-xl p-6 border border-white border-opacity-20">
            <div className="bg-blue-500 w-12 h-12 rounded-lg flex items-center justify-center mb-4">
              <Camera className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-lg font-bold text-white mb-2">Real-time Detection</h3>
            <p className="text-blue-200 text-sm">Advanced AI tracks persons and waste items frame-by-frame</p>
          </div>

          <div className="bg-white bg-opacity-10 backdrop-blur-md rounded-xl p-6 border border-white border-opacity-20">
            <div className="bg-purple-500 w-12 h-12 rounded-lg flex items-center justify-center mb-4">
              <Shield className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-lg font-bold text-white mb-2">Evidence Capture</h3>
            <p className="text-blue-200 text-sm">Automatically saves violator images with bounding boxes</p>
          </div>

          <div className="bg-white bg-opacity-10 backdrop-blur-md rounded-xl p-6 border border-white border-opacity-20">
            <div className="bg-green-500 w-12 h-12 rounded-lg flex items-center justify-center mb-4">
              <Download className="w-6 h-6 text-white" />
            </div>
            <h3 className="text-lg font-bold text-white mb-2">Annotated Output</h3>
            <p className="text-blue-200 text-sm">Download processed videos with complete visual annotations</p>
          </div>
        </div>
      </main>

      {/* Footer */}
      <footer className="mt-16 bg-black bg-opacity-30 backdrop-blur-md border-t border-white border-opacity-10 py-6">
        <div className="max-w-7xl mx-auto px-6 text-center">
          <p className="text-blue-200 text-sm">
            CivicLens © 2025 - Powered by AI • Protecting Our Environment
          </p>
        </div>
      </footer>
    </div>
  );
}