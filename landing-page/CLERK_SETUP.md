# 🔐 Configuración de Clerk - Autenticación

## ✅ LO QUE SE INSTALÓ

Clerk está completamente integrado en tu landing page de Next.js con:

- ✅ **@clerk/nextjs** instalado
- ✅ **ClerkProvider** envolviendo la app
- ✅ **middleware.ts** configurado con `clerkMiddleware()`
- ✅ Páginas de Sign-In y Sign-Up personalizadas
- ✅ Flujo de autenticación completo
- ✅ Localización en español

---

## 🚀 PASOS PARA ACTIVAR CLERK

### 1. Crear Cuenta en Clerk

1. **Visita:** https://clerk.com/
2. **Crea una cuenta** (gratis)
3. **Crea una aplicación** nueva
4. **Nombra tu app:** "Ikigai" o como prefieras

### 2. Obtener las API Keys

1. **En tu Clerk Dashboard**, ve a:
   ```
   API Keys → https://dashboard.clerk.com/last-active?path=api-keys
   ```

2. **Copia estas dos keys:**
   - `Publishable Key` (empieza con `pk_test_...`)
   - `Secret Key` (empieza con `sk_test_...`)

### 3. Crear Archivo .env.local

1. **En la carpeta `landing-page/`**, crea un archivo llamado `.env.local`

2. **Pega este contenido** (reemplaza con tus keys reales):

```bash
# Clerk Authentication Keys
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_TU_KEY_AQUI
CLERK_SECRET_KEY=sk_test_TU_KEY_AQUI

# Clerk URLs (Opcional - usa defaults)
NEXT_PUBLIC_CLERK_SIGN_IN_URL=/sign-in
NEXT_PUBLIC_CLERK_SIGN_UP_URL=/sign-up
NEXT_PUBLIC_CLERK_AFTER_SIGN_IN_URL=/start-exercise
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/start-exercise

# Flask Backend URL
NEXT_PUBLIC_FLASK_URL=http://localhost:5001
```

3. **Guarda el archivo**

**⚠️ IMPORTANTE:** 
- **NUNCA** subas `.env.local` a Git
- Ya está en `.gitignore` por defecto
- Solo usa tus keys reales en `.env.local`

### 4. Configurar Redirects en Clerk Dashboard

1. **Ve a:** Clerk Dashboard → Your App → Paths

2. **Configura las URLs de redirect:**
   ```
   Sign-in URL: /sign-in
   Sign-up URL: /sign-up
   After sign-in URL: /start-exercise
   After sign-up URL: /start-exercise
   ```

3. **Allowed redirect URLs** (para desarrollo):
   ```
   http://localhost:3001
   http://localhost:3001/start-exercise
   ```

### 5. Reiniciar el Servidor

```bash
# Detén el servidor actual (Ctrl+C)
# Reinicia:
npm run dev
```

---

## 🔄 FLUJO DE AUTENTICACIÓN

```
1. Usuario en Landing Page (/)
   ↓
2. Click en "Desbloquea tus Superpoderes" 🚀
   ↓
3. ¿Está autenticado?
   │
   ├─ NO → Redirige a /start-exercise
   │         ↓
   │       Detecta no autenticado
   │         ↓
   │       Redirige a /sign-up (Clerk)
   │         ↓
   │       Usuario se registra
   │         ↓
   │       Clerk redirige a /start-exercise
   │         ↓
   │       Detecta autenticado ✅
   │         ↓
   │       Redirige a Flask: http://localhost:5001/exercise
   │
   └─ SÍ → Redirige directamente a Flask
             http://localhost:5001/exercise
```

---

## 🎨 PÁGINAS CREADAS

### 1. `/sign-in` - Página de Inicio de Sesión
- Diseño personalizado con colores Surfing Digital
- Clerk SignIn component integrado
- Animaciones y branding

### 2. `/sign-up` - Página de Registro
- Diseño personalizado con colores Surfing Digital
- Clerk SignUp component integrado
- Lista de beneficios de registrarse
- Animaciones y branding

### 3. `/start-exercise` - Página Intermedia
- Detecta si el usuario está autenticado
- Si NO: redirige a `/sign-up`
- Si SÍ: redirige a Flask `/exercise`
- Loading screen con animación

---

## 📁 ARCHIVOS MODIFICADOS

### Nuevos Archivos:
```
landing-page/
├── middleware.ts                              ← 🆕 Clerk middleware
├── app/
│   ├── sign-in/[[...sign-in]]/page.tsx       ← 🆕 Página de login
│   ├── sign-up/[[...sign-up]]/page.tsx       ← 🆕 Página de registro
│   └── start-exercise/page.tsx                ← 🆕 Página intermedia
└── CLERK_SETUP.md                             ← 🆕 Esta guía
```

### Archivos Actualizados:
```
landing-page/
├── app/layout.tsx                             ← ✏️ ClerkProvider agregado
└── components/
    ├── Hero.tsx                               ← ✏️ useUser hook
    ├── CTA.tsx                                ← ✏️ useUser hook
    └── HowItWorks.tsx                         ← ✏️ useUser hook
```

---

## 🧪 PROBAR LA INTEGRACIÓN

### 1. Verifica que Clerk esté configurado:
```bash
# En landing-page/.env.local
cat .env.local
# Deberías ver tus keys de Clerk
```

### 2. Inicia el servidor:
```bash
npm run dev
```

### 3. Abre el navegador:
```
http://localhost:3001
```

### 4. Click en "Desbloquea tus Superpoderes":
- Debería llevarte a `/sign-up`
- Verás el formulario de Clerk con tu branding
- Regístrate con un email de prueba

### 5. Después del registro:
- Automáticamente te redirige a `/start-exercise`
- Verás un loading screen
- Te lleva a Flask: `http://localhost:5001/exercise`

---

## 🎯 CARACTERÍSTICAS IMPLEMENTADAS

✅ **Autenticación Completa:**
- Sign-Up (registro)
- Sign-In (inicio de sesión)
- Sign-Out (cerrar sesión)
- Sesión persistente

✅ **Protección de Rutas:**
- Landing page es pública (/)
- Sign-In y Sign-Up son públicas
- Ejercicio requiere autenticación

✅ **UX Mejorada:**
- Usuarios autenticados van directo al ejercicio
- Usuarios nuevos van a registro
- Loading states durante redirects
- Diseño con branding Surfing Digital

✅ **Integración con Flask:**
- Después de autenticarse → Flask
- URL configurable vía .env
- Funciona en desarrollo y producción

---

## 🎨 PERSONALIZACIÓN

### Cambiar Colores de Clerk:

En `app/sign-in/[[...sign-in]]/page.tsx` y `app/sign-up/[[...sign-up]]/page.tsx`:

```typescript
appearance={{
  elements: {
    formButtonPrimary: "bg-gradient-to-r from-teal-light to-blue-light",
    footerActionLink: "text-teal-light",
    // Agrega más personalizaciones aquí
  },
}}
```

### Cambiar Textos:

Edita los archivos de las páginas para cambiar:
- Títulos
- Descripciones
- Mensajes de beneficios

### Cambiar Redirects:

En `.env.local`:
```bash
NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL=/tu-ruta-personalizada
```

---

## 🔒 SEGURIDAD

### Variables de Entorno:
✅ `.env.local` está en `.gitignore`  
✅ Solo usar `NEXT_PUBLIC_*` para keys que necesitan el cliente  
✅ `CLERK_SECRET_KEY` nunca se expone al cliente  

### Middleware:
✅ Protege rutas automáticamente  
✅ Rutas públicas definidas explícitamente  
✅ Usa `clerkMiddleware()` oficial (no deprecado)  

### Sesiones:
✅ Clerk maneja sesiones automáticamente  
✅ Tokens JWT seguros  
✅ Refresh automático  

---

## 🐛 TROUBLESHOOTING

### "Invalid publishable key":
```bash
# Verifica que tu .env.local tenga las keys correctas
# Reinicia el servidor después de crear .env.local
npm run dev
```

### "Redirect loop":
```bash
# Verifica las URLs en Clerk Dashboard
# Asegúrate que coincidan con tu .env.local
```

### "Cannot read properties of undefined (reading 'isSignedIn')":
```bash
# Asegúrate que ClerkProvider esté en app/layout.tsx
# Verifica que estés usando useUser() dentro de un componente cliente
```

### Usuario no redirige después de sign-up:
```bash
# Verifica en Clerk Dashboard → Paths
# NEXT_PUBLIC_CLERK_AFTER_SIGN_UP_URL debe ser /start-exercise
```

---

## 📚 DOCUMENTACIÓN OFICIAL

- **Clerk Docs:** https://clerk.com/docs
- **Next.js Quickstart:** https://clerk.com/docs/quickstarts/nextjs
- **Clerk Components:** https://clerk.com/docs/components/overview
- **Customization:** https://clerk.com/docs/components/customization/overview

---

## 🚀 PARA PRODUCCIÓN

### 1. Obtener Production Keys:
```bash
# En Clerk Dashboard, cambia a "Production"
# Copia las production keys (no test keys)
```

### 2. Configurar en Vercel/Netlify:
```bash
# Agrega las variables de entorno en tu plataforma:
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_live_...
CLERK_SECRET_KEY=sk_live_...
NEXT_PUBLIC_FLASK_URL=https://tu-dominio-flask.com
```

### 3. Actualizar Allowed URLs en Clerk:
```
https://tu-dominio.com
https://tu-dominio.com/start-exercise
```

---

## ✨ RESULTADO FINAL

Con Clerk integrado, tu app ahora tiene:

✅ Registro de usuarios profesional  
✅ Inicio de sesión seguro  
✅ Gestión de sesiones automática  
✅ Protección de rutas  
✅ Diseño personalizado con tu branding  
✅ Experiencia de usuario premium  
✅ Listo para producción  

---

## 🎉 ¡TODO LISTO!

**Siguiente paso:**
1. Crea tu cuenta en Clerk
2. Obtén tus API keys
3. Crea `.env.local` con tus keys
4. Reinicia el servidor
5. ¡Prueba el registro!

**URL para probar:**
```
http://localhost:3001
```

**¿Preguntas?** Lee la documentación oficial de Clerk o revisa este archivo.

---

**Hecho con 🔐 siguiendo las mejores prácticas de Clerk**  
*生き甲斐を見つけよう* 🎯

