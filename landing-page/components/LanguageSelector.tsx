"use client";

import { useLanguage } from '@/contexts/LanguageContext';

export default function LanguageSelector() {
  const { language, setLanguage } = useLanguage();
  
  return (
    <div className="fixed top-6 right-6 z-50">
      <div className="relative inline-flex items-center bg-white/95 backdrop-blur-sm rounded-full p-1.5 shadow-xl border border-gray-200/50">
        {/* Background slider - se mueve según el idioma seleccionado */}
        <div 
          className={`absolute top-1.5 bottom-1.5 rounded-full bg-gradient-to-r from-teal-light to-blue-light shadow-lg transition-all duration-300 ease-out ${
            language === 'es' 
              ? 'left-1.5 w-[calc(50%-6px)]' 
              : 'left-[calc(50%+3px)] w-[calc(50%-6px)]'
          }`}
        />
        
        {/* Spanish button */}
        <button
          onClick={() => setLanguage('es')}
          className={`relative z-10 px-6 py-2.5 rounded-full font-dm-sans font-semibold text-sm transition-all duration-300 min-w-[100px] ${
            language === 'es'
              ? 'text-white scale-105'
              : 'text-navy/60 hover:text-navy hover:scale-105'
          }`}
          aria-label="Cambiar a Español"
        >
          Español
        </button>
        
        {/* English button */}
        <button
          onClick={() => setLanguage('en')}
          className={`relative z-10 px-6 py-2.5 rounded-full font-dm-sans font-semibold text-sm transition-all duration-300 min-w-[100px] ${
            language === 'en'
              ? 'text-white scale-105'
              : 'text-navy/60 hover:text-navy hover:scale-105'
          }`}
          aria-label="Switch to English"
        >
          English
        </button>
      </div>
    </div>
  );
}
