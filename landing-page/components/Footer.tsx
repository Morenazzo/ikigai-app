"use client";

export default function Footer() {
  return (
    <footer className="bg-gradient-to-br from-navy-dark via-navy-light to-teal-dark text-white py-12 px-4">
      <div className="max-w-7xl mx-auto">
        {/* Main Footer Content */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
          {/* Brand Section */}
          <div>
            <div className="flex items-center gap-3 mb-4">
              <div className="text-4xl">🌊</div>
              <div>
                <h3 className="font-dm-sans font-bold text-xl text-teal-light">Surfing Digital</h3>
                <p className="text-sm text-white/70 font-open-sans">Surfeando la era digital</p>
              </div>
            </div>
            <p className="text-white/80 font-open-sans text-sm leading-relaxed">
              Ayudando a las personas a descubrir su propósito divino y desbloquear sus superpoderes únicos.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-dm-sans font-bold text-lg mb-4 text-teal-light">Navegación Rápida</h4>
            <ul className="space-y-2 font-open-sans">
              <li>
                <a href="#" className="text-white/80 hover:text-teal-light transition-colors duration-200 text-sm">
                  ¿Qué es Ikigai?
                </a>
              </li>
              <li>
                <a href="#how-it-works" className="text-white/80 hover:text-teal-light transition-colors duration-200 text-sm">
                  Cómo Funciona
                </a>
              </li>
              <li>
                <a href="http://localhost:5000/exercise" className="text-white/80 hover:text-teal-light transition-colors duration-200 text-sm">
                  Comenzar Ahora
                </a>
              </li>
              <li>
                <a href="http://localhost:5000/impact" className="text-white/80 hover:text-teal-light transition-colors duration-200 text-sm">
                  Impacto Comunitario
                </a>
              </li>
            </ul>
          </div>

          {/* Contact & Social */}
          <div>
            <h4 className="font-dm-sans font-bold text-lg mb-4 text-teal-light">Conéctate</h4>
            <p className="text-white/80 font-open-sans text-sm mb-4">
              ¿Preguntas o comentarios sobre este proyecto?
            </p>
            <div className="flex gap-4">
              <a 
                href="https://surfing.digital" 
                target="_blank"
                rel="noopener noreferrer"
                className="w-10 h-10 bg-white/10 hover:bg-teal-light rounded-full flex items-center justify-center transition-all duration-300 hover:scale-110"
              >
                <span className="text-xl">🌐</span>
              </a>
              <a 
                href="#"
                className="w-10 h-10 bg-white/10 hover:bg-teal-light rounded-full flex items-center justify-center transition-all duration-300 hover:scale-110"
              >
                <span className="text-xl">📧</span>
              </a>
            </div>
          </div>
        </div>

        {/* Divider */}
        <div className="border-t border-white/20 pt-8">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            {/* Copyright */}
            <p className="text-white/60 font-open-sans text-sm text-center md:text-left">
              © 2025 Surfing Digital. Hecho con ❤️ para aquellos que buscan su propósito.
            </p>

            {/* Credits */}
            <div className="text-white/60 font-open-sans text-sm text-center md:text-right">
              <p>生き甲斐を見つけよう (Encuentra tu Ikigai)</p>
            </div>
          </div>
        </div>

        {/* Inspirational Quote */}
        <div className="mt-8 p-6 bg-white/5 backdrop-blur-sm rounded-2xl border border-white/10 text-center">
          <p className="text-white/90 font-open-sans italic text-sm leading-relaxed">
            "Porque somos la obra maestra de Dios. Él nos creó de nuevo en Cristo Jesús,<br />
            para que hagamos las cosas buenas que preparó para nosotros tiempo atrás."
          </p>
          <p className="text-teal-light font-dm-sans font-bold mt-2 text-sm">
            - Efesios 2:10
          </p>
        </div>
      </div>
    </footer>
  );
}

