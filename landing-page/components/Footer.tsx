"use client";

import { useLanguage } from '@/contexts/LanguageContext';

export default function Footer() {
  const { t } = useLanguage();
  
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
              {t.footer.brandDescription}
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-dm-sans font-bold text-lg mb-4 text-teal-light">{t.footer.quickLinks}</h4>
            <ul className="space-y-2 font-open-sans">
              <li>
                <a href="#" className="text-white/80 hover:text-teal-light transition-colors duration-200 text-sm">
                  {t.footer.links.whatIsIkigai}
                </a>
              </li>
              <li>
                <a href="#how-it-works" className="text-white/80 hover:text-teal-light transition-colors duration-200 text-sm">
                  {t.footer.links.howItWorks}
                </a>
              </li>
              <li>
                <a href="http://localhost:5000/exercise" className="text-white/80 hover:text-teal-light transition-colors duration-200 text-sm">
                  {t.footer.links.startNow}
                </a>
              </li>
              <li>
                <a href="http://localhost:5000/impact" className="text-white/80 hover:text-teal-light transition-colors duration-200 text-sm">
                  {t.footer.links.impact}
                </a>
              </li>
            </ul>
          </div>

          {/* Contact & Social */}
          <div>
            <h4 className="font-dm-sans font-bold text-lg mb-4 text-teal-light">{t.footer.connect}</h4>
            <p className="text-white/80 font-open-sans text-sm mb-4">
              {t.footer.contactText}
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
              {t.footer.copyright}
            </p>

            {/* Credits */}
            <div className="text-white/60 font-open-sans text-sm text-center md:text-right">
              <p>{t.footer.findYourIkigai}</p>
            </div>
          </div>
        </div>

        {/* Inspirational Quote */}
        <div className="mt-8 p-4 md:p-6 bg-white/5 backdrop-blur-sm rounded-2xl border border-white/10 text-center">
          <p className="text-white/90 font-open-sans italic text-xs md:text-sm leading-relaxed">
            {t.pillars.quote}
          </p>
          <p className="text-teal-light font-dm-sans font-bold mt-2 text-sm">
            {t.pillars.quoteSource}
          </p>
        </div>
      </div>
    </footer>
  );
}

