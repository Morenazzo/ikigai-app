"use client";

import { useLanguage } from '@/contexts/LanguageContext';
import { useUser } from '@clerk/nextjs';
import { useRouter } from 'next/navigation';

export default function HowItWorks() {
  const { t, language } = useLanguage();
  const { isSignedIn, isLoaded } = useUser();
  const router = useRouter();
  
  const icons = ["💖", "⚡", "💎", "🌍", "🎯", "✨"];
  const colors = ["pink", "blue", "teal-light", "purple", "blue-light", "teal-light"];
  const stepNumbers = ["1", "2", "3", "4", "5-8", "9"];
  
  const steps = t.howItWorks.steps.map((step, index) => ({
    step: stepNumbers[index],
    title: step.title,
    time: step.time,
    description: step.description,
    icon: icons[index],
    color: colors[index],
  }));

  return (
    <section id="how-it-works" className="py-20 px-4 bg-gradient-to-br from-navy-dark via-navy-light to-teal-dark">
      <div className="max-w-7xl mx-auto">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-dm-sans font-bold text-white mb-4">
            {t.howItWorks.title}
          </h2>
          <p className="text-xl text-teal-light font-open-sans max-w-2xl mx-auto">
            {t.howItWorks.subtitle}
          </p>
        </div>

        {/* Steps Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {steps.map((step, index) => (
            <div
              key={index}
              className="relative bg-white/10 backdrop-blur-sm rounded-2xl p-8 border border-white/20 hover:bg-white/20 transition-all duration-300 group card-hover"
            >
              {/* Step Number Badge */}
              <div className="absolute -top-4 -right-4 w-12 h-12 bg-gradient-to-br from-teal-light to-blue-light rounded-full flex items-center justify-center text-white font-dm-sans font-bold text-lg shadow-lg">
                {step.step}
              </div>

              {/* Icon */}
              <div className="text-5xl mb-4 transform group-hover:scale-110 transition-transform duration-300">
                {step.icon}
              </div>

              {/* Title */}
              <h3 className="text-xl font-dm-sans font-bold text-white mb-2">
                {step.title}
              </h3>

              {/* Time Badge */}
              <div className="inline-block px-4 py-1 bg-white/20 rounded-full text-teal-light font-dm-sans text-sm font-bold mb-4">
                ⏱️ {step.time}
              </div>

              {/* Description */}
              <p className="text-sm font-open-sans text-white/80 leading-relaxed">
                {step.description}
              </p>
            </div>
          ))}
        </div>

        {/* Bottom CTA */}
        <div className="mt-16 text-center">
          <div className="inline-block bg-white/10 backdrop-blur-sm rounded-3xl p-8 border border-white/20">
            <div className="text-4xl mb-4">🎁✨🦸‍♂️</div>
            <h3 className="text-2xl font-dm-sans font-bold text-white mb-4">
              {t.howItWorks.ctaTitle}
            </h3>
            <p className="text-white/80 font-open-sans mb-6 max-w-xl mx-auto">
              {t.howItWorks.ctaDescription}
            </p>
            <button
              onClick={() => {
                if (!isLoaded) return;
                if (isSignedIn) {
                  const flaskUrl = process.env.NEXT_PUBLIC_FLASK_URL || 'http://localhost:5001';
                  window.location.href = `${flaskUrl}/exercise?lang=${language}`;
                } else {
                  router.push('/start-exercise');
                }
              }}
              className="px-10 py-5 bg-gradient-to-r from-pink to-purple text-white rounded-full font-dm-sans font-bold text-lg shadow-2xl hover:shadow-pink/50 transition-all duration-300 hover:scale-105"
            >
              🚀 {t.howItWorks.ctaButton}
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}

