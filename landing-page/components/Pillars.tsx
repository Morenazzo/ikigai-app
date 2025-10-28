"use client";

import { useLanguage } from '@/contexts/LanguageContext';

export default function Pillars() {
  const { t } = useLanguage();
  
  const icons = ["💖", "🎯", "🌟", "💼"];
  const gradients = [
    "from-pink to-pink/70",
    "from-purple to-purple/70",
    "from-blue to-blue-light",
    "from-teal-light to-teal-light/70",
  ];
  
  const pillars = t.pillars.items.map((item, index) => ({
    ...item,
    icon: icons[index],
    gradient: gradients[index],
  }));

  return (
    <section className="py-20 px-4 relative overflow-hidden">
      {/* Decorative Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-gray-50 to-white"></div>
      
      <div className="max-w-7xl mx-auto relative z-10">
        {/* Section Header */}
        <div className="text-center mb-16 px-4">
          <h2 className="text-3xl md:text-5xl font-dm-sans font-bold text-navy-dark mb-4">
            {t.pillars.title}
          </h2>
          <p className="text-lg md:text-xl text-teal-dark font-open-sans max-w-2xl mx-auto">
            {t.pillars.subtitle}
          </p>
        </div>

        {/* Pillars Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-5xl mx-auto mb-12">
          {pillars.map((pillar, index) => (
            <div
              key={index}
              className="relative bg-white rounded-3xl p-8 shadow-xl card-hover overflow-hidden"
            >
              {/* Gradient Background */}
              <div className={`absolute top-0 left-0 w-32 h-32 bg-gradient-to-br ${pillar.gradient} opacity-10 rounded-br-full`}></div>
              
              {/* Icon Circle */}
              <div className={`w-20 h-20 mb-6 bg-gradient-to-br ${pillar.gradient} rounded-full flex items-center justify-center text-4xl shadow-lg relative z-10`}>
                {pillar.icon}
              </div>

              {/* Title */}
              <h3 className={`text-2xl font-dm-sans font-bold mb-2 bg-gradient-to-r ${pillar.gradient} text-transparent bg-clip-text`}>
                {pillar.title}
              </h3>

              {/* Subtitle */}
              <p className="text-sm text-teal-dark font-open-sans font-semibold mb-4">
                {pillar.subtitle}
              </p>

              {/* Description */}
              <p className="text-navy-light font-open-sans leading-relaxed">
                {pillar.description}
              </p>

              {/* Decorative Corner */}
              <div className={`absolute bottom-0 right-0 w-24 h-24 bg-gradient-to-tl ${pillar.gradient} opacity-5 rounded-tl-full`}></div>
            </div>
          ))}
        </div>

        {/* Central Message */}
        <div className="max-w-3xl mx-auto bg-gradient-to-r from-navy-dark to-teal-dark rounded-3xl p-6 md:p-10 text-center shadow-2xl">
          <div className="text-5xl mb-4">✨💎✨</div>
          <h3 className="text-2xl md:text-3xl font-dm-sans font-bold text-white mb-4">
            {t.pillars.centerTitle}
          </h3>
          <p className="text-white/90 font-open-sans text-base md:text-lg leading-relaxed mb-6">
            {t.pillars.centerDescription}
          </p>
          <div className="bg-white/20 backdrop-blur-sm rounded-2xl p-4 md:p-6 border border-white/30">
            <p className="text-white font-open-sans italic text-sm md:text-base">
              {t.pillars.quote}
              <br />
              <strong className="text-teal-light">{t.pillars.quoteSource}</strong>
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

