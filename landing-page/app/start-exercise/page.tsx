"use client";

import { useEffect } from 'react';
import { useUser, useAuth } from '@clerk/nextjs';
import { useRouter } from 'next/navigation';

// Disable static rendering for this page
export const dynamic = 'force-dynamic';

export default function StartExercise() {
  const { isLoaded, isSignedIn, user } = useUser();
  const { getToken } = useAuth();
  const router = useRouter();
  
  // Get language from localStorage or default to 'es'
  const getLanguage = () => {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('ikigai-language') || 'es';
    }
    return 'es';
  };

  useEffect(() => {
    const redirectToFlask = async () => {
      if (isLoaded) {
        if (!isSignedIn) {
          // Si no está autenticado, redirigir a sign-up
          router.push('/sign-up');
        } else {
          // Usuario autenticado, obtener token y redirigir a Flask
          try {
            const token = await getToken();
            const language = getLanguage();
            const flaskUrl = process.env.NEXT_PUBLIC_FLASK_URL || 'http://localhost:5001';
            
            // Create form to POST to Flask with token
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = `${flaskUrl}/auth/clerk-callback`;
            
            // Add token
            const tokenInput = document.createElement('input');
            tokenInput.type = 'hidden';
            tokenInput.name = 'clerk_token';
            tokenInput.value = token || '';
            form.appendChild(tokenInput);
            
            // Add language
            const langInput = document.createElement('input');
            langInput.type = 'hidden';
            langInput.name = 'lang';
            langInput.value = language;
            form.appendChild(langInput);
            
            // Add user email
            const emailInput = document.createElement('input');
            emailInput.type = 'hidden';
            emailInput.name = 'email';
            emailInput.value = user?.primaryEmailAddress?.emailAddress || '';
            form.appendChild(emailInput);
            
            document.body.appendChild(form);
            form.submit();
          } catch (error) {
            console.error('Error getting Clerk token:', error);
            // Fallback: redirect without token
            const language = getLanguage();
            const flaskUrl = process.env.NEXT_PUBLIC_FLASK_URL || 'http://localhost:5001';
            window.location.href = `${flaskUrl}/exercise?lang=${language}`;
          }
        }
      }
    };
    
    redirectToFlask();
  }, [isLoaded, isSignedIn, user, router, getToken]);

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
