"use client";

export default function Pillars() {
  const pillars = [
    {
      title: "Pasión",
      subtitle: "Lo que amas + En lo que eres bueno",
      icon: "💖",
      gradient: "from-pink to-pink/70",
      description: "Cuando combinas lo que amas con tus talentos naturales, nace tu pasión verdadera.",
    },
    {
      title: "Misión",
      subtitle: "Lo que amas + Lo que el mundo necesita",
      icon: "🎯",
      gradient: "from-purple to-purple/70",
      description: "Tu misión surge cuando tus deseos se alinean con las necesidades del mundo.",
    },
    {
      title: "Vocación",
      subtitle: "Lo que el mundo necesita + Por lo que te pagan",
      icon: "🌟",
      gradient: "from-blue to-blue-light",
      description: "Tu vocación conecta el impacto que quieres crear con valor económico real.",
    },
    {
      title: "Profesión",
      subtitle: "En lo que eres bueno + Por lo que te pagan",
      icon: "💼",
      gradient: "from-teal-light to-teal-light/70",
      description: "Tu profesión es donde tus habilidades se convierten en valor monetizable.",
    },
  ];

  return (
    <section className="py-20 px-4 relative overflow-hidden">
      {/* Decorative Background */}
      <div className="absolute inset-0 bg-gradient-to-br from-gray-50 to-white"></div>
      
      <div className="max-w-7xl mx-auto relative z-10">
        {/* Section Header */}
        <div className="text-center mb-16">
          <h2 className="text-4xl md:text-5xl font-dm-sans font-bold text-navy-dark mb-4">
            Los Cuatro Pilares del Ikigai
          </h2>
          <p className="text-xl text-teal-dark font-open-sans max-w-2xl mx-auto">
            Cada intersección revela una parte esencial de tu propósito
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
        <div className="max-w-3xl mx-auto bg-gradient-to-r from-navy-dark to-teal-dark rounded-3xl p-10 text-center shadow-2xl">
          <div className="text-5xl mb-4">✨💎✨</div>
          <h3 className="text-3xl font-dm-sans font-bold text-white mb-4">
            Tu Ikigai Está en el Centro
          </h3>
          <p className="text-white/90 font-open-sans text-lg leading-relaxed mb-6">
            Cuando descubres la intersección perfecta de estos cuatro pilares, encuentras tu <strong className="text-teal-light">IKIGAI</strong>—tu propósito único para transformar el mundo.
          </p>
          <div className="bg-white/20 backdrop-blur-sm rounded-2xl p-6 border border-white/30">
            <p className="text-white font-open-sans italic text-base">
              "Porque somos la obra maestra de Dios. Él nos creó de nuevo en Cristo Jesús, <br />
              para que hagamos las cosas buenas que preparó para nosotros tiempo atrás."
              <br />
              <strong className="text-teal-light">- Efesios 2:10</strong>
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

