"use client";

import { useEffect } from 'react';
import { useUser } from '@clerk/nextjs';
import { useRouter } from 'next/navigation';
import { useLanguage } from '@/contexts/LanguageContext';

export default function StartExercise() {
  const { isLoaded, isSignedIn, user } = useUser();
  const { language } = useLanguage();
  const router = useRouter();

  useEffect(() => {
    if (isLoaded) {
      if (!isSignedIn) {
        // Si no está autenticado, redirigir a sign-up
        router.push('/sign-up');
      } else {
        // Usuario autenticado, redirigir a Flask con idioma
        const flaskUrl = process.env.NEXT_PUBLIC_FLASK_URL || 'http://localhost:5001';
        window.location.href = `${flaskUrl}/exercise?lang=${language}`;
      }
    }
  }, [isLoaded, isSignedIn, router, language]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-navy-dark via-teal-dark to-blue">
      <div className="text-center">
        {/* Loading Spinner */}
        <div className="relative w-24 h-24 mx-auto mb-6">
          <div className="absolute inset-0 border-4 border-teal-light/30 rounded-full"></div>
          <div className="absolute inset-0 border-4 border-teal-light border-t-transparent rounded-full animate-spin"></div>
        </div>
        
        {/* Loading Text */}
        <h2 className="text-2xl font-dm-sans font-bold text-white mb-2">
          {!isLoaded ? 'Cargando...' : !isSignedIn ? 'Redirigiendo a registro...' : '¡Preparando tu viaje!'}
        </h2>
        <p className="text-white/70 font-open-sans">
          {!isLoaded ? 'Un momento por favor' : !isSignedIn ? 'Te llevaremos al registro' : 'Iniciando ejercicio de Ikigai...'}
        </p>
        
        {/* Ikigai Symbol */}
        <div className="mt-8 text-6xl animate-pulse">
          ✨
        </div>
      </div>
    </div>
  );
}

