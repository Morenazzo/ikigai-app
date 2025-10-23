"use client";

import { useLanguage } from '@/contexts/LanguageContext';

export default function LanguageSelector() {
  const { language, setLanguage } = useLanguage();

  return (
    <div className="fixed top-6 right-6 z-50 flex gap-2 bg-white/90 backdrop-blur-sm rounded-full p-2 shadow-lg border border-gray-200">
      {/* Bandera de USA */}
      <button
        onClick={() => setLanguage('en')}
        className={`relative w-12 h-12 rounded-full overflow-hidden transition-all duration-300 ${
          language === 'en' 
            ? 'ring-4 ring-blue scale-110 shadow-xl' 
            : 'hover:scale-105 opacity-70 hover:opacity-100'
        }`}
        title="English"
        aria-label="Switch to English"
      >
        <div className="w-full h-full flex items-center justify-center text-3xl bg-white">
          🇺🇸
        </div>
        {language === 'en' && (
          <div className="absolute inset-0 bg-blue/10 pointer-events-none"></div>
        )}
      </button>

      {/* Bandera de México */}
      <button
        onClick={() => setLanguage('es')}
        className={`relative w-12 h-12 rounded-full overflow-hidden transition-all duration-300 ${
          language === 'es' 
            ? 'ring-4 ring-teal-light scale-110 shadow-xl' 
            : 'hover:scale-105 opacity-70 hover:opacity-100'
        }`}
        title="Español"
        aria-label="Cambiar a Español"
      >
        <div className="w-full h-full flex items-center justify-center text-3xl bg-white">
          🇲🇽
        </div>
        {language === 'es' && (
          <div className="absolute inset-0 bg-teal-light/10 pointer-events-none"></div>
        )}
      </button>
    </div>
  );
}

