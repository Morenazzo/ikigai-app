"use client";

interface CTAButtonProps {
  text: string;
  onClick?: () => void;
  icon?: string;
  variant?: 'primary' | 'secondary';
  className?: string;
}

export default function CTAButton({ 
  text, 
  onClick, 
  icon = "🚀", 
  variant = 'primary',
  className = '' 
}: CTAButtonProps) {
  
  const handleClick = () => {
    if (onClick) {
      onClick();
    } else {
      // Por defecto, redirigir al ejercicio
      window.location.href = 'http://localhost:5001/exercise';
    }
  };

  if (variant === 'secondary') {
    return (
      <button
        onClick={handleClick}
        className={`px-8 py-4 border-2 border-navy-dark text-navy-dark rounded-full font-dm-sans font-bold text-lg hover:bg-navy-dark hover:text-white transition-all duration-300 ${className}`}
      >
        {text}
      </button>
    );
  }

  return (
    <button
      onClick={handleClick}
      className={`group relative px-10 py-5 bg-gradient-to-r from-teal-light to-blue-light text-white rounded-full font-dm-sans font-bold text-lg shadow-2xl hover:shadow-teal-light/50 transition-all duration-300 hover:scale-105 animate-pulse-glow ${className}`}
    >
      <span className="flex items-center gap-3">
        {icon && <span className="text-2xl group-hover:rotate-12 transition-transform duration-300">{icon}</span>}
        <span>{text}</span>
      </span>
    </button>
  );
}

