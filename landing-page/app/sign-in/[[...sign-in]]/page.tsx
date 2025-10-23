import { SignIn } from "@clerk/nextjs";

export default function SignInPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-navy-dark via-teal-dark to-blue px-4 py-12">
      <div className="w-full max-w-md">
        {/* Branding Header */}
        <div className="text-center mb-8">
          <div className="text-5xl mb-4 animate-float">✨</div>
          <h1 className="text-3xl font-dm-sans font-bold text-white mb-2">
            Bienvenido de Nuevo
          </h1>
          <p className="text-white/70 font-open-sans">
            Continúa tu viaje hacia el descubrimiento de tu Ikigai
          </p>
        </div>

        {/* Clerk Sign In Component */}
        <div className="flex justify-center">
          <SignIn
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

