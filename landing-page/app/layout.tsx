import type { Metadata } from "next";
import { ClerkProvider } from "@clerk/nextjs";
import { esES } from "@clerk/localizations";
import "./globals.css";

export const metadata: Metadata = {
  title: "Descubre tu Ikigai | Surfing Digital",
  description: "Descubre tu propósito divino - Tu tesoro dado por Dios para impactar millones de vidas",
  keywords: "ikigai, propósito de vida, superpoderes, vocación, misión, pasión",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ClerkProvider localization={esES}>
      <html lang="es">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  );
}

