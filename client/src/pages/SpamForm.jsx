import { useState } from "react";
import axios from "axios";

export default function SpamForm() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const checkSpam = async () => {
    try {
      setLoading(true);
      setResult("");

      const res = await axios.post(
        `${import.meta.env.VITE_BACKEND_URL}/predict`,
        {
          message,
        }
      );

      setResult(res.data.prediction);
    } catch (error) {
      setResult("Error occurred",error);
    } finally {
      setLoading(false);
    }
  };


  const clearAll = () => {
    setMessage("");
    setResult("");
    setLoading(false);
  };

  const isSpam = result === "Spam";

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 via-white to-purple-50">

      <div className="w-full max-w-xl bg-white shadow-2xl rounded-2xl p-8 border border-gray-100">

       
        <h1 className="text-3xl font-bold text-center text-gray-800 mb-2">
          Spam Email Detector
        </h1>
        <p className="text-center text-gray-500 mb-6">
          Check whether your message is spam or not using AI
        </p>

      
        <textarea
          className="w-full h-40 p-4 border rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-400 resize-none"
          placeholder="Paste your email or message here..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />

      
        <div className="flex gap-3 mt-5">
          
          
          <button
            onClick={checkSpam}
            disabled={!message || loading}
            className="flex-1 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 text-white font-semibold py-3 rounded-xl transition duration-300"
          >
            {loading ? "Checking..." : "Check Spam"}
          </button>

         
          <button
            onClick={clearAll}
            className="flex-1 bg-gray-200 hover:bg-gray-300 text-gray-700 font-semibold py-3 rounded-xl transition duration-300"
          >
            Clear
          </button>

        </div>

        
        {result && (
          <div
            className={`mt-6 text-center p-4 rounded-xl font-semibold text-lg ${
              isSpam
                ? "bg-red-100 text-red-700 border border-red-300"
                : "bg-green-100 text-green-700 border border-green-300"
            }`}
          >
            {isSpam ? "Spam Email Detected" : "Not Spam Email"}
          </div>
        )}

      </div>
    </div>
  );
}