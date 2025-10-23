# 🚀 Instrucciones para Correr la Landing Page

## ✅ Lo que se creó

Se ha creado una **landing page moderna y profesional** con Next.js que incluye:

- ✨ Diseño premium usando la paleta de colores de Surfing Digital
- 🎨 Tipografías DM Sans y Open Sans
- 📱 Responsive design (móvil, tablet, desktop)
- 🎭 Animaciones y efectos visuales elegantes
- 🔗 Integración perfecta con tu app Flask de Ikigai
- 💎 6 componentes modulares (Hero, Features, HowItWorks, Pillars, CTA, Footer)

## 📍 Arquitectura del Proyecto

```
Ikigai/
├── landing-page/           ← Nueva landing page (Next.js)
│   ├── app/
│   ├── components/
│   └── package.json
│
└── app.py                  ← Tu app Flask existente
```

## 🎯 Flujo de Usuario

1. **Landing Page** (`http://localhost:3000`) - Usuario ve la presentación profesional
2. **Click en CTA** → Botones "Desbloquea tus Superpoderes" / "Comenzar"
3. **Redirige a Flask** (`http://localhost:5000/exercise`) - Ejercicio interactivo

## 🚀 Pasos para Ejecutar

### 1️⃣ Instalar Dependencias de Next.js

```bash
cd "/Users/edwinmoreno/Documents/Surfing D/Código/Ikigai/landing-page"
npm install
```

### 2️⃣ Ejecutar Landing Page (Next.js)

En una terminal:
```bash
cd "/Users/edwinmoreno/Documents/Surfing D/Código/Ikigai/landing-page"
npm run dev
```

La landing page estará en: **http://localhost:3000**

### 3️⃣ Ejecutar App Flask (en otra terminal)

En una segunda terminal:
```bash
cd "/Users/edwinmoreno/Documents/Surfing D/Código/Ikigai"
python3 -m flask run
```

La app Flask estará en: **http://localhost:5000**

### 4️⃣ Probar el Flujo Completo

1. Abre http://localhost:3000 (landing page)
2. Click en cualquier botón CTA
3. Serás redirigido a http://localhost:5000/exercise
4. ¡Completa tu Ikigai! 🎉

## 🎨 Paleta de Colores Implementada

Todos los colores de Surfing Digital están configurados:

- **Navy**: `#001639`, `#003453` - Headers, texto principal
- **Teal**: `#00586A`, `#0BB7B7` - Acentos, gradientes
- **Blue**: `#0056A0`, `#009FD5` - CTAs, enlaces
- **Pink**: `#ED4A6D` - Destacados, superpoderes
- **Purple**: `#9D80B9` - Elementos secundarios
- **Peach**: `#FFD08D` - Toques cálidos

## 📝 Tipografías Implementadas

- **DM Sans Bold** - Títulos y headlines
- **DM Sans Regular** - Subtítulos
- **Open Sans Light** - Cuerpo de texto

## 🔧 Personalización Rápida

### Cambiar el Copy
Edita los componentes en `landing-page/components/`:
- `Hero.tsx` - Mensaje principal
- `Features.tsx` - Características
- `CTA.tsx` - Call to actions

### Cambiar Colores
Edita `landing-page/tailwind.config.ts`

### Cambiar URL del Backend
En todos los componentes con botones, busca:
```typescript
window.location.href = 'http://localhost:5000/exercise';
```

## 📦 Comandos Útiles

```bash
# Instalar dependencias
npm install

# Desarrollo (hot reload)
npm run dev

# Build para producción
npm run build

# Ejecutar producción
npm start

# Linting
npm run lint
```

## 🌟 Características de Marketing

La landing page incluye:

✅ **Hero Impactante**: Mensaje claro del valor único
✅ **Social Proof**: Estadísticas (25 min, 9 pasos)
✅ **Beneficios Claros**: Los 4 elementos del Ikigai
✅ **Proceso Transparente**: Explicación del viaje de 9 pasos
✅ **CTAs Múltiples**: Varios puntos de conversión
✅ **Trust Signals**: Citas bíblicas, diseño profesional
✅ **Urgencia Sutil**: "Menos de 25 minutos"
✅ **Sin Fricción**: "Sin registro • Gratis • Inmediato"

## 🚢 Deploy (Opcional)

### Vercel (Recomendado para Next.js)
```bash
cd landing-page
npx vercel
```

### Para la App Flask
Puedes usar Railway, Render, o cualquier servicio de hosting Python.

## 🎯 Próximos Pasos Sugeridos

1. ✅ **Prueba el flujo completo** - Landing → Flask
2. 📸 **Captura screenshots** para redes sociales
3. 🎨 **Ajusta el copy** si quieres personalizar más
4. 🚀 **Deploy** a producción cuando estés listo
5. 📊 **Añade analytics** (Google Analytics, Plausible)

## ❓ Solución de Problemas

**Error: Cannot find module 'next'**
```bash
cd landing-page && npm install
```

**Puerto 3000 ya en uso**
```bash
npm run dev -- -p 3001  # Usar otro puerto
```

**Flask no corre**
```bash
pip3 install -r requirements.txt
python3 -m flask run
```

## 💡 Tips de UX/UI Aplicados

✅ Jerarquía visual clara (tamaños de texto, colores)
✅ Espaciado consistente (usando Tailwind spacing)
✅ Animaciones sutiles (no invasivas)
✅ Contraste adecuado (accesibilidad)
✅ CTA visibles y claros
✅ Responsive en todos los breakpoints
✅ Loading states y transiciones suaves
✅ Gradientes modernos
✅ Iconos y emojis para engagement
✅ Storytelling (origen de superhéroe, tesoro divino)

---

**¡Tu landing page está lista! 🎉**

Cualquier duda, revisa el README.md dentro de la carpeta `landing-page/`.

**Hecho con ❤️ usando el brand system de Surfing Digital**

