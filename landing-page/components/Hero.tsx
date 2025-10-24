"use client";

import { useLanguage } from '@/contexts/LanguageContext';
import { useUser } from '@clerk/nextjs';
import { useRouter } from 'next/navigation';

export default function Hero() {
  const { t, language } = useLanguage();
  const { isSignedIn, isLoaded } = useUser();
  const router = useRouter();
  
  const handleStartJourney = () => {
    // Si está cargando, esperar
    if (!isLoaded) return;
    
    // Si ya está autenticado, ir directo al ejercicio con el idioma
    if (isSignedIn) {
      const flaskUrl = process.env.NEXT_PUBLIC_FLASK_URL || 'http://localhost:5001';
      window.location.href = `${flaskUrl}/exercise?lang=${language}`;
    } else {
      // Si no está autenticado, ir a la página intermedia que redirige a sign-up
      router.push('/start-exercise');
    }
  };

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden px-4 py-20">
      {/* Animated Background Elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-teal-light opacity-20 rounded-full blur-3xl animate-float"></div>
        <div className="absolute -bottom-40 -left-40 w-96 h-96 bg-pink opacity-20 rounded-full blur-3xl animate-float" style={{ animationDelay: '1s' }}></div>
        <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-purple opacity-10 rounded-full blur-3xl animate-float" style={{ animationDelay: '2s' }}></div>
      </div>

      {/* Content */}
      <div className="relative z-10 max-w-6xl mx-auto text-center">
        {/* Badge */}
        <div className="inline-flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-teal-light to-blue-light text-white rounded-full font-dm-sans font-bold text-sm mb-8 animate-pulse-glow">
          <span className="text-2xl">✨</span>
          <span>{t.hero.badge}</span>
          <span className="text-2xl">✨</span>
        </div>

        {/* Main Headline */}
        <h1 className="text-5xl md:text-7xl font-dm-sans font-bold mb-6 leading-tight">
          <span className="text-navy-dark">{t.hero.title.line1}</span>
          <br />
          <span className="text-gradient from-teal-light via-blue-light to-pink text-transparent bg-clip-text">
            {t.hero.title.line2}
          </span>
          <br />
          <span className="text-navy-dark">{t.hero.title.line3}</span>
        </h1>

        {/* Subtitle */}
        <p className="text-xl md:text-2xl text-teal-dark mb-4 font-open-sans max-w-3xl mx-auto leading-relaxed">
          {t.hero.subtitle}
        </p>

        <p className="text-lg md:text-xl text-navy-light mb-10 font-open-sans max-w-2xl mx-auto opacity-90">
          {t.hero.description} 🦸‍♂️
        </p>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-12">
          <button
            onClick={handleStartJourney}
            className="group relative px-10 py-5 bg-gradient-to-r from-teal-light to-blue-light text-white rounded-full font-dm-sans font-bold text-lg shadow-2xl hover:shadow-teal-light/50 transition-all duration-300 hover:scale-105 animate-pulse-glow"
          >
            <span className="flex items-center gap-3">
              <span className="text-2xl">🚀</span>
              <span>{t.hero.ctaPrimary}</span>
            </span>
          </button>
          
          <a
            href="#how-it-works"
            className="px-8 py-4 border-2 border-navy-dark text-navy-dark rounded-full font-dm-sans font-bold text-lg hover:bg-navy-dark hover:text-white transition-all duration-300"
          >
            {t.hero.ctaSecondary}
          </a>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
          <div className="bg-white/80 backdrop-blur-sm rounded-2xl p-6 shadow-lg card-hover">
            <div className="text-4xl mb-2">⏱️</div>
            <div className="text-3xl font-dm-sans font-bold text-navy-dark mb-1">{t.hero.stats.time}</div>
            <div className="text-sm font-open-sans text-teal-dark">{t.hero.stats.timeLabel}</div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-sm rounded-2xl p-6 shadow-lg card-hover">
            <div className="text-4xl mb-2">🎯</div>
            <div className="text-3xl font-dm-sans font-bold text-navy-dark mb-1">{t.hero.stats.steps}</div>
            <div className="text-sm font-open-sans text-teal-dark">{t.hero.stats.stepsLabel}</div>
          </div>
          
          <div className="bg-white/80 backdrop-blur-sm rounded-2xl p-6 shadow-lg card-hover">
            <div className="text-4xl mb-2">💎</div>
            <div className="text-3xl font-dm-sans font-bold text-navy-dark mb-1">{t.hero.stats.treasure}</div>
            <div className="text-sm font-open-sans text-teal-dark">{t.hero.stats.treasureLabel}</div>
          </div>
        </div>

        {/* Scroll Indicator - moved outside stats grid */}
        <div className="mt-16 flex justify-center animate-bounce">
          <svg className="w-8 h-8 text-navy-dark" fill="none" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
          </svg>
        </div>
      </div>
    </section>
  );
}

