# 🚀 Guía de Deployment a Producción

## 📋 Índice

1. [Prerequisitos](#prerequisitos)
2. [Configuración de GitHub](#github)
3. [Deployment del Backend (Flask)](#backend-flask)
4. [Deployment del Frontend (Next.js)](#frontend-nextjs)
5. [Variables de Entorno](#variables-de-entorno)
6. [Post-Deployment](#post-deployment)

---

## 🔧 Prerequisitos

Antes de empezar, asegúrate de tener:

- ✅ Cuenta en [GitHub](https://github.com)
- ✅ Cuenta en [Vercel](https://vercel.com)
- ✅ Git instalado en tu computadora
- ✅ [Clerk Account](https://clerk.com) (para autenticación)
- ✅ (Opcional) [OpenAI API Key](https://platform.openai.com) (para funciones de IA)

---

## 📦 1. Configuración de GitHub

### Paso 1.1: Inicializar Git (si no lo has hecho)

```bash
cd "/Users/edwinmoreno/Documents/Surfing D/Código/Ikigai"
git init
```

### Paso 1.2: Crear repositorio en GitHub

1. Ve a [GitHub](https://github.com/new)
2. Crea un nuevo repositorio llamado `ikigai-app`
3. **NO** marques "Initialize with README" (ya tienes archivos)
4. Click en "Create repository"

### Paso 1.3: Conectar tu proyecto a GitHub

```bash
# Agrega todos los archivos
git add .

# Haz tu primer commit
git commit -m "Initial commit: Ikigai App with Flask backend and Next.js landing page"

# Conecta con GitHub (reemplaza TU_USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/ikigai-app.git

# Sube los cambios
git branch -M main
git push -u origin main
```

**✅ TODO 1 COMPLETADO**: Tu código ahora está en GitHub

---

## 🐍 2. Deployment del Backend (Flask) en Vercel

### Paso 2.1: Preparar la aplicación Flask

Tu app ya está lista con estos archivos:
- ✅ `vercel.json` - Configuración de Vercel
- ✅ `requirements.txt` - Dependencias de Python
- ✅ `app.py` - Aplicación principal

### Paso 2.2: Deploy en Vercel

1. **Ve a [Vercel](https://vercel.com/new)**
2. **Importa tu repositorio de GitHub**:
   - Click en "Import Project"
   - Selecciona tu repositorio `ikigai-app`
   - Click en "Import"

3. **Configura el proyecto**:
   ```
   Framework Preset: Other
   Root Directory: ./
   ```

4. **Configura las Variables de Entorno** (click en "Environment Variables"):
   ```
   OPENAI_API_KEY = tu_key_de_openai (opcional)
   SECRET_KEY = un_string_aleatorio_muy_largo_y_seguro
   FLASK_ENV = production
   ```

5. **Deploy**:
   - Click en "Deploy"
   - Espera 2-3 minutos
   - ¡Tu backend estará en línea! 🎉

6. **Guarda la URL**:
   - Vercel te dará una URL como: `https://ikigai-app.vercel.app`
   - **Guarda esta URL**, la necesitarás para el frontend

**✅ TODO 2 COMPLETADO**: Backend en producción

---

## 🎨 3. Deployment del Frontend (Next.js) en Vercel

### Paso 3.1: Crear proyecto separado en Vercel

1. **Ve a [Vercel](https://vercel.com/new)** nuevamente
2. **Importa el MISMO repositorio**
3. **Esta vez configura**:
   ```
   Framework Preset: Next.js
   Root Directory: landing-page
   ```

### Paso 3.2: Configurar Variables de Entorno

Click en "Environment Variables" y añade:

```
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY = pk_test_TU_KEY_DE_CLERK
CLERK_SECRET_KEY = sk_test_TU_KEY_SECRETO_DE_CLERK
NEXT_PUBLIC_FLASK_URL = https://ikigai-app.vercel.app
```

**⚠️ IMPORTANTE**: 
- Reemplaza `https://ikigai-app.vercel.app` con la URL real de tu backend
- Obtén las keys de Clerk en [dashboard.clerk.com](https://dashboard.clerk.com)

### Paso 3.3: Deploy

1. Click en "Deploy"
2. Espera 1-2 minutos
3. ¡Tu landing page estará en línea! 🎉

**URL del landing page**: `https://ikigai-landing.vercel.app` (o similar)

**✅ TODO 3 COMPLETADO**: Frontend en producción

---

## 🔐 4. Variables de Entorno - Resumen Completo

### Backend (Flask en Vercel)

```env
OPENAI_API_KEY=sk-...tu_key_de_openai
SECRET_KEY=genera_uno_aleatorio_de_32_caracteres_minimo
FLASK_ENV=production
```

### Frontend (Next.js en Vercel)

```env
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
NEXT_PUBLIC_FLASK_URL=https://tu-backend.vercel.app
```

### ¿Dónde obtener las keys?

- **OpenAI**: [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- **Clerk**: [dashboard.clerk.com](https://dashboard.clerk.com) → Tu aplicación → API Keys
- **SECRET_KEY**: Genera uno con:
  ```bash
  python3 -c "import secrets; print(secrets.token_hex(32))"
  ```

---

## 🎯 5. Configuración Post-Deployment

### 5.1: Configurar Clerk para Producción

1. Ve a [Clerk Dashboard](https://dashboard.clerk.com)
2. En tu aplicación, ve a **"Paths"**
3. Actualiza las URLs:
   ```
   Sign in URL: /sign-in
   Sign up URL: /sign-up
   After sign in: https://tu-backend.vercel.app/exercise
   After sign up: https://tu-backend.vercel.app/exercise
   ```

### 5.2: Configurar CORS en Flask (si es necesario)

Si tienes problemas de CORS, agrega a tu `app.py`:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["https://tu-landing.vercel.app"])
```

Y añade a `requirements.txt`:
```
flask-cors==4.0.0
```

### 5.3: Base de Datos en Producción

**Opción A: SQLite (Simple, para empezar)**
- Vercel creará automáticamente `project.db`
- ⚠️ Los datos se borrarán con cada deploy

**Opción B: PostgreSQL (Recomendado para producción)**

1. Crea una base de datos gratis en [Supabase](https://supabase.com) o [Neon](https://neon.tech)
2. Obtén la `DATABASE_URL`
3. Añádela como variable de entorno en Vercel:
   ```
   DATABASE_URL=postgresql://usuario:password@host:5432/database
   ```

---

## ✅ 6. Verificación Final

### Checklist de Deployment

- [ ] ✅ Código en GitHub
- [ ] ✅ Backend Flask deployado en Vercel
- [ ] ✅ Frontend Next.js deployado en Vercel
- [ ] ✅ Variables de entorno configuradas
- [ ] ✅ Clerk configurado con URLs de producción
- [ ] ✅ Probado el flujo completo:
  - [ ] Landing page carga correctamente
  - [ ] Botón "Desbloquea tus Superpoderes" funciona
  - [ ] Registro/Login con Clerk funciona
  - [ ] Redirige al ejercicio de Flask
  - [ ] Ejercicio funciona correctamente
  - [ ] Resultados se muestran bien
  - [ ] PDF se descarga correctamente

### URLs Finales

```
🌐 Landing Page: https://ikigai-landing.vercel.app
🐍 Backend API: https://ikigai-app.vercel.app
🔐 Clerk Auth: https://clerk.com
```

---

## 🆘 Troubleshooting

### Error: "Module not found"
- Verifica que todas las dependencias estén en `requirements.txt` (Flask)
- Verifica que todas las dependencias estén en `package.json` (Next.js)
- Re-deploy después de actualizar

### Error: "Environment variable not found"
- Revisa que todas las variables estén en la configuración de Vercel
- Las variables deben estar sin comillas
- Re-deploy después de añadir variables

### Error: CORS
- Añade `flask-cors` como se muestra arriba
- Configura los orígenes correctamente

### La base de datos se borra
- Cambia a PostgreSQL para persistencia
- SQLite en Vercel es efímero

---

## 🔄 Actualizar en Producción

Cada vez que hagas cambios:

```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

Vercel **automáticamente** desplegará los cambios. 🎉

---

## 📱 URLs de Referencia

- 📚 [Documentación de Vercel](https://vercel.com/docs)
- 🐍 [Deploy Flask en Vercel](https://vercel.com/docs/frameworks/flask)
- ⚡ [Deploy Next.js en Vercel](https://vercel.com/docs/frameworks/nextjs)
- 🔐 [Documentación de Clerk](https://clerk.com/docs)

---

## 🎉 ¡Felicidades!

Tu aplicación Ikigai ahora está en producción y disponible para el mundo. 🌍✨

**Comparte tu landing page**: `https://tu-landing.vercel.app`

---

**Creado con 💙 por Surfing Digital**


