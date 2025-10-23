"use client";

export default function Features() {
  const features = [
    {
      icon: "💖",
      title: "Lo que AMAS",
      description: "Los deseos más profundos de tu corazón",
      color: "from-pink to-pink/70",
      bgColor: "bg-pink/5",
      borderColor: "border-pink",
    },
    {
      icon: "⚡",
      title: "En lo que eres BUENO",
      description: "Tus superpoderes naturales",
      color: "from-blue to-blue-light",
      bgColor: "bg-blue/5",
      borderColor: "border-blue",
    },
    {
      icon: "💎",
      title: "Por lo que te pueden PAGAR",
      description: "Tu contribución valiosa",
      color: "from-teal-light to-teal-light/70",
      bgColor: "bg-teal-light/5",
      borderColor: "border-teal-light",
    },
    {
      icon: "🌍",
      title: "Lo que el mundo NECESITA",
      description: "Tu misión divina",
      color: "from-purple to-purple/70",
      bgColor: "bg-purple/5",
      borderColor: "border-purple",
    },
  ];

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
            ¿Qué es Ikigai?
          </h2>
          <p className="text-xl text-teal-dark font-open-sans max-w-2xl mx-auto">
            La intersección de tus dones divinos
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
        <div className="max-w-3xl mx-auto bg-white/80 backdrop-blur-sm rounded-3xl p-8 shadow-2xl">
          <div className="text-center mb-8">
            <h3 className="text-2xl font-dm-sans font-bold text-navy-dark mb-4">
              Tu Mapa del Tesoro Personal
            </h3>
            <p className="text-teal-dark font-open-sans">
              <strong>Ikigai</strong> (生き甲斐) combina <em>"iki"</em> (vida) y <em>"gai"</em> (valor). Es el <strong className="text-pink">tesoro</strong> que Dios incrustó en tu ADN—tu contribución única al mundo.
            </p>
          </div>

          {/* Ikigai Diagram Placeholder - You can replace with actual image */}
          <div className="relative aspect-video bg-gradient-to-br from-navy-dark to-teal-dark rounded-2xl overflow-hidden">
            <img 
              src="https://imageio.forbes.com/blogs-images/chrismyers/files/2018/02/ikigai-1.png?format=png&width=500" 
              alt="Diagrama Ikigai"
              className="w-full h-full object-contain p-4"
            />
          </div>

          {/* Bottom Quote */}
          <div className="mt-8 p-6 bg-gradient-to-r from-pink/10 to-teal-light/10 rounded-2xl border-l-4 border-teal-light">
            <p className="text-center font-open-sans text-navy-dark leading-relaxed">
              <strong className="text-teal-light text-lg">✨ Donde estos cuatro convergen,</strong>
              <br />
              encontrarás tu <strong className="text-pink text-lg">Ikigai</strong>—
              <br />
              <span className="text-teal-dark">tu propósito dado por Dios para impactar millones de vidas.</span>
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

