# 🎯 Ikigai Landing Page - Next.js

Landing page moderna para la aplicación Ikigai, diseñada con Next.js 14, TypeScript y Tailwind CSS.

## ✨ Características

- **🎨 Diseño Moderno**: Utiliza la paleta de colores y tipografías de Surfing Digital
- **📱 Responsive**: Funciona perfectamente en todos los dispositivos
- **⚡ Rendimiento Optimizado**: Next.js 14 con App Router
- **🎭 Animaciones Suaves**: Transiciones y efectos visuales elegantes
- **💎 Componentes Modulares**: Arquitectura limpia y reutilizable

## 🎨 Brand System

### Colores Surfing Digital
- **Navy**: `#001639`, `#003453`
- **Teal**: `#00586A`, `#0BB7B7`
- **Blue**: `#0056A0`, `#009FD5`
- **Pink**: `#ED4A6D`
- **Purple**: `#9D80B9`
- **Peach**: `#FFD08D`

### Tipografías
- **DM Sans**: Bold & Regular (Headers, títulos)
- **Open Sans**: Light & Regular (Body text, párrafos)

## 🚀 Instalación

1. **Instalar dependencias**
   ```bash
   cd landing-page
   npm install
   ```

2. **Ejecutar en modo desarrollo**
   ```bash
   npm run dev
   ```

3. **Abrir en navegador**
   ```
   http://localhost:3000
   ```

## 📦 Estructura del Proyecto

```
landing-page/
├── app/
│   ├── globals.css          # Estilos globales y fuentes
│   ├── layout.tsx           # Layout principal
│   └── page.tsx             # Página principal
├── components/
│   ├── Hero.tsx             # Sección hero principal
│   ├── Features.tsx         # Características del Ikigai
│   ├── HowItWorks.tsx       # Proceso de 9 pasos
│   ├── Pillars.tsx          # Los 4 pilares
│   ├── CTA.tsx              # Call to action final
│   └── Footer.tsx           # Pie de página
├── package.json
├── tailwind.config.ts       # Configuración Tailwind
├── tsconfig.json
└── next.config.mjs
```

## 🔗 Integración con Flask

La landing page está diseñada para trabajar junto con la aplicación Flask principal:

- **Landing Page (Next.js)**: `http://localhost:3000` - Página de presentación
- **App Flask**: `http://localhost:5000` - Aplicación interactiva de Ikigai

### Flujo de Usuario

1. Usuario visita la landing page (Next.js en puerto 3000)
2. Hace clic en "Comenzar" / "Desbloquea tus Superpoderes"
3. Es redirigido a `http://localhost:5000/exercise` (Flask)
4. Completa el ejercicio interactivo de Ikigai

## 🛠️ Scripts Disponibles

```bash
# Desarrollo
npm run dev

# Build para producción
npm run build

# Ejecutar build de producción
npm start

# Linting
npm run lint
```

## 🌟 Componentes Principales

### Hero
Sección principal con:
- Título impactante con gradientes
- CTAs prominentes
- Estadísticas clave (25 min, 9 pasos, 1 tesoro)
- Elementos animados de fondo

### Features
Presenta los 4 elementos del Ikigai:
- Lo que amas 💖
- En lo que eres bueno ⚡
- Por lo que te pueden pagar 💎
- Lo que el mundo necesita 🌍

### HowItWorks
Explica el proceso de 9 pasos con:
- Timeline visual
- Tiempos de cada paso
- Descripción de cada fase

### Pillars
Los 4 pilares del Ikigai:
- Pasión (Amor + Talento)
- Misión (Amor + Necesidad)
- Vocación (Necesidad + Pago)
- Profesión (Talento + Pago)

### CTA
Call to action final con:
- Beneficios destacados
- Garantías (sin registro, gratis)
- Botón principal animado

### Footer
Información de contacto y enlaces

## 🎯 Optimizaciones

- **Tailwind CSS**: Utilidad first para estilos eficientes
- **TypeScript**: Type safety en todo el proyecto
- **Next.js 14**: App Router para mejor rendimiento
- **Lazy Loading**: Componentes se cargan eficientemente
- **SEO Optimizado**: Metadatos configurados

## 🚀 Deploy

### Vercel (Recomendado)
```bash
vercel
```

### Otros proveedores
```bash
npm run build
npm start
```

## 📝 Personalización

### Cambiar colores
Edita `tailwind.config.ts` para ajustar la paleta de colores.

### Cambiar tipografías
Edita `app/globals.css` para cambiar las fuentes de Google Fonts.

### Modificar contenido
Los componentes en `components/` contienen todo el copy y pueden editarse fácilmente.

## 🤝 Integración

Para conectar con tu backend:

1. Cambia las URLs en los botones CTA:
   ```typescript
   window.location.href = 'TU_URL_BACKEND/exercise';
   ```

2. O usa variables de entorno:
   ```typescript
   const API_URL = process.env.NEXT_PUBLIC_API_URL;
   window.location.href = `${API_URL}/exercise`;
   ```

## 📄 Licencia

Este proyecto es parte de la aplicación Ikigai de Surfing Digital.

---

**Hecho con ❤️ por Surfing Digital** | 生き甲斐を見つけよう

