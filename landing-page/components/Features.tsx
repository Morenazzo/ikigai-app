"use client";

import { useLanguage } from '@/contexts/LanguageContext';

export default function Features() {
  const { t, language } = useLanguage();
  
  const features = t.features.items.map((item, index) => {
    const styles = [
      {
        icon: "💖",
        color: "from-pink to-pink/70",
        bgColor: "bg-pink/5",
        borderColor: "border-pink",
      },
      {
        icon: "⚡",
        color: "from-blue to-blue-light",
        bgColor: "bg-blue/5",
        borderColor: "border-blue",
      },
      {
        icon: "💎",
        color: "from-teal-light to-teal-light/70",
        bgColor: "bg-teal-light/5",
        borderColor: "border-teal-light",
      },
      {
        icon: "🌍",
        color: "from-purple to-purple/70",
        bgColor: "bg-purple/5",
        borderColor: "border-purple",
      },
    ];
    return {
      ...item,
      ...styles[index],
    };
  });

  return (
    <section className="py-20 px-4 relative overflow-hidden">
      {/* Background Pattern */}
      <div className="absolute inset-0 opacity-5">
        <div className="absolute inset-0" style={{
          backgroundImage: 'radial-gradient(circle, #0BB7B7 1px, transparent 1px)',
          backgroundSize: '50px 50px'
        }}></div>
      </div>

      <div className="max-w-7xl mx-auto relative z-10">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-dm-sans font-bold text-navy-dark mb-4">
            {t.features.title}
          </h2>
          <p className="text-xl text-teal-dark font-open-sans max-w-2xl mx-auto">
            {t.features.subtitle}
          </p>
        </div>

        {/* Features Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-16">
          {features.map((feature, index) => (
            <div
              key={index}
              className={`relative p-8 ${feature.bgColor} rounded-3xl border-l-4 ${feature.borderColor} card-hover group`}
              style={{ animationDelay: `${index * 0.1}s` }}
            >
              {/* Icon */}
              <div className="text-6xl mb-4 transform group-hover:scale-110 transition-transform duration-300">
                {feature.icon}
              </div>
              
              {/* Title */}
              <h3 className="text-xl font-dm-sans font-bold text-navy-dark mb-3">
                {feature.title}
              </h3>
              
              {/* Description */}
              <p className="text-sm font-open-sans text-teal-dark leading-relaxed">
                {feature.description}
              </p>

              {/* Hover Effect */}
              <div className={`absolute inset-0 bg-gradient-to-br ${feature.color} opacity-0 group-hover:opacity-5 rounded-3xl transition-opacity duration-300`}></div>
            </div>
          ))}
        </div>

        {/* Center Image/Diagram */}
        <div className="max-w-3xl mx-auto bg-white/80 backdrop-blur-sm rounded-3xl p-4 md:p-8 shadow-2xl">
          <div className="text-center mb-8">
            <h3 className="text-xl md:text-2xl font-dm-sans font-bold text-navy-dark mb-4">
              {t.features.mapTitle}
            </h3>
            <p className="text-sm md:text-base text-teal-dark font-open-sans px-2">
              {t.features.mapDescription}
            </p>
          </div>

          {/* Ikigai Diagram - Surfing Digital branded */}
          <div className="relative aspect-square max-w-md md:max-w-lg mx-auto bg-navy-dark rounded-2xl overflow-hidden shadow-2xl">
            <img 
              src={`/images/ikigai-${language}.svg`}
              alt={language === 'es' ? 'Diagrama Ikigai - Tu Razón de Ser' : 'Ikigai Diagram - Your Reason for Being'}
              className="w-full h-full object-contain p-2 md:p-4"
              loading="lazy"
            />
          </div>

          {/* Bottom Quote */}
          <div className="mt-8 p-4 md:p-6 bg-gradient-to-r from-pink/10 to-teal-light/10 rounded-2xl border-l-4 border-teal-light">
            <p className="text-center font-open-sans text-navy-dark leading-relaxed text-sm md:text-base">
              <strong className="text-teal-light text-base md:text-lg">{t.features.convergence}</strong>
              <br />
              {t.features.findIkigai}
              <br />
              <span className="text-teal-dark">{t.features.purpose}</span>
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

