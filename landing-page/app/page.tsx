"use client";

import { useState, useEffect } from 'react';
import { LanguageProvider } from '@/contexts/LanguageContext';
import LanguageSelector from '@/components/LanguageSelector';
import Hero from '@/components/Hero';
import Features from '@/components/Features';
import HowItWorks from '@/components/HowItWorks';
import Pillars from '@/components/Pillars';
import CTA from '@/components/CTA';
import Footer from '@/components/Footer';

export default function Home() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  return (
    <LanguageProvider>
      <main className="min-h-screen">
        <LanguageSelector />
        <Hero />
        <Features />
        <HowItWorks />
        <Pillars />
        <CTA />
        <Footer />
      </main>
    </LanguageProvider>
  );
}

