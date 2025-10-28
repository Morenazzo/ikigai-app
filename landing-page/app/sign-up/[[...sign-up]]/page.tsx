import { SignUp } from "@clerk/nextjs";

export default function SignUpPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-navy-dark via-teal-dark to-blue px-4 py-12">
      <div className="w-full max-w-md">
        {/* Branding Header */}
        <div className="text-center mb-8">
          <div className="text-5xl mb-4 animate-float">🎁</div>
          <h1 className="text-3xl font-dm-sans font-bold text-white mb-2">
            Desbloquea tu Superpoder
          </h1>
          <p className="text-white/70 font-open-sans">
            Regístrate para descubrir tu propósito divino
          </p>
        </div>

        {/* Clerk Sign Up Component */}
        <div className="flex justify-center">
          <SignUp
            afterSignUpUrl="/start-exercise"
            redirectUrl="/start-exercise"
            appearance={{
              elements: {
                rootBox: "mx-auto",
                card: "bg-white/95 backdrop-blur-sm shadow-2xl",
                headerTitle: "font-dm-sans",
                headerSubtitle: "font-open-sans",
                socialButtonsBlockButton: "font-open-sans",
                formButtonPrimary: "bg-gradient-to-r from-teal-light to-blue-light hover:from-teal-light/90 hover:to-blue-light/90 font-dm-sans",
                formFieldLabel: "font-open-sans text-navy-dark",
                formFieldInput: "font-open-sans",
                footerActionLink: "text-teal-light hover:text-teal-light/80",
              },
            }}
          />
        </div>

        {/* Features List */}
        <div className="mt-8 bg-white/10 backdrop-blur-sm rounded-2xl p-6 border border-white/20">
          <h3 className="text-white font-dm-sans font-bold mb-4 text-center">
            ¿Por qué registrarte?
          </h3>
          <ul className="space-y-3">
            <li className="flex items-start gap-3 text-white/90 font-open-sans text-sm">
              <span className="text-teal-light text-lg">✓</span>
              <span>Guarda tu progreso y resultados</span>
            </li>
            <li className="flex items-start gap-3 text-white/90 font-open-sans text-sm">
              <span className="text-teal-light text-lg">✓</span>
              <span>Accede a tu Ikigai en cualquier momento</span>
            </li>
            <li className="flex items-start gap-3 text-white/90 font-open-sans text-sm">
              <span className="text-teal-light text-lg">✓</span>
              <span>Gana 200 Puntos Surfer al completar</span>
            </li>
          </ul>
        </div>

        {/* Bottom Link */}
        <div className="mt-8 text-center">
          <a 
            href="/"
            className="text-white/70 hover:text-white font-open-sans text-sm transition-colors duration-200"
          >
            ← Volver al inicio
          </a>
        </div>
      </div>
    </div>
  );
}

