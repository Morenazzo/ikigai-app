"use client";

import { useLanguage } from '@/contexts/LanguageContext';
import { useUser } from '@clerk/nextjs';
import { useRouter } from 'next/navigation';

export default function CTA() {
  const { t } = useLanguage();
  const { isSignedIn, isLoaded } = useUser();
  const router = useRouter();
  
  const handleStartJourney = () => {
    if (!isLoaded) return;
    
    if (isSignedIn) {
      const flaskUrl = process.env.NEXT_PUBLIC_FLASK_URL || 'http://localhost:5001';
      window.location.href = `${flaskUrl}/exercise`;
    } else {
      router.push('/start-exercise');
    }
  };

  return (
    <section className="py-20 px-4 relative overflow-hidden">
      {/* Animated Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-teal-light/20 via-pink/10 to-purple/20"></div>
      
      {/* Floating Elements */}
      <div className="absolute top-20 left-10 w-32 h-32 bg-teal-light/20 rounded-full blur-2xl animate-float"></div>
      <div className="absolute bottom-20 right-10 w-40 h-40 bg-pink/20 rounded-full blur-2xl animate-float" style={{ animationDelay: '1s' }}></div>

      <div className="max-w-5xl mx-auto relative z-10">
        <div className="bg-white/90 backdrop-blur-lg rounded-[3rem] p-12 md:p-16 shadow-2xl border-4 border-teal-light/30">
          {/* Icons */}
          <div className="text-center mb-8">
            <div className="text-6xl mb-4 animate-float">🎁</div>
            <div className="flex justify-center gap-4 text-4xl">
              <span className="animate-float" style={{ animationDelay: '0.2s' }}>✨</span>
              <span className="animate-float" style={{ animationDelay: '0.4s' }}>🦸‍♂️</span>
              <span className="animate-float" style={{ animationDelay: '0.6s' }}>💫</span>
            </div>
          </div>

          {/* Headline */}
          <h2 className="text-4xl md:text-5xl font-dm-sans font-bold text-navy-dark text-center mb-6">
            {t.cta.title1} <br />
            <span className="text-gradient from-teal-light via-blue-light to-pink bg-clip-text text-transparent">
              {t.cta.title2}
            </span>
          </h2>

          {/* Time Badge */}
          <div className="flex justify-center mb-8">
            <div className="inline-flex items-center gap-3 px-6 py-3 bg-gradient-to-r from-pink to-purple text-white rounded-full font-dm-sans font-bold shadow-lg">
              <span className="text-2xl">⏱️</span>
              <span>{t.cta.timeBadge}</span>
            </div>
          </div>

          {/* Description */}
          <p className="text-lg md:text-xl text-teal-dark text-center font-open-sans mb-8 max-w-3xl mx-auto leading-relaxed">
            {t.cta.description}
          </p>

          {/* Benefits List */}
          <div className="grid md:grid-cols-2 gap-4 mb-10 max-w-2xl mx-auto">
            {t.cta.benefits.map((benefit, index) => {
              const bgColors = ['bg-teal-light/5', 'bg-pink/5', 'bg-purple/5', 'bg-blue/5'];
              return (
                <div key={index} className={`flex items-start gap-3 ${bgColors[index]} p-4 rounded-2xl`}>
                  <div className="text-2xl mt-1">✅</div>
                  <div>
                    <h4 className="font-dm-sans font-bold text-navy-dark">{benefit.title}</h4>
                    <p className="text-sm text-teal-dark font-open-sans">{benefit.description}</p>
                  </div>
                </div>
              );
            })}
          </div>

          {/* CTA Button */}
          <div className="text-center">
            <button
              onClick={handleStartJourney}
              className="group relative px-12 py-6 bg-gradient-to-r from-teal-light via-blue-light to-blue text-white rounded-full font-dm-sans font-bold text-xl shadow-2xl hover:shadow-teal-light/50 transition-all duration-300 hover:scale-105 animate-pulse-glow"
            >
              <span className="flex items-center gap-3">
                <span className="text-3xl group-hover:rotate-12 transition-transform duration-300">🚀</span>
                <span>{t.cta.button}</span>
                <span className="text-3xl group-hover:rotate-12 transition-transform duration-300">✨</span>
              </span>
            </button>
            <p className="text-sm text-teal-dark font-open-sans mt-4">
              {t.cta.disclaimer}
            </p>
          </div>

          {/* Trust Badge */}
          <div className="mt-10 pt-8 border-t border-teal-light/20 text-center">
            <p className="text-navy-light font-open-sans text-sm italic">
              🏄‍♂️ <strong className="text-teal-dark">{t.cta.badge}</strong>
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

