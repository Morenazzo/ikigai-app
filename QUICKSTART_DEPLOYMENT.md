# 🚀 QUICKSTART: Subir a Producción en 10 Minutos

## 📋 Lo que VAS A HACER TÚ (Pasos Manuales)

### PASO 1: Subir a GitHub (5 minutos)

```bash
# 1. Ve al directorio de tu proyecto
cd "/Users/edwinmoreno/Documents/Surfing D/Código/Ikigai"

# 2. Inicializa Git (si no lo has hecho)
git init

# 3. Agrega todos los archivos
git add .

# 4. Haz el commit inicial
git commit -m "Initial commit: Ikigai App"
```

**AHORA EN GITHUB.COM:**
1. Ve a https://github.com/new
2. Nombre del repo: `ikigai-app`
3. Déjalo PÚBLICO o PRIVADO (como prefieras)
4. NO marques "Initialize with README"
5. Click "Create repository"

**VUELVE A LA TERMINAL:**
```bash
# 5. Conecta con GitHub (CAMBIA "TU_USUARIO" por tu usuario real)
git remote add origin https://github.com/TU_USUARIO/ikigai-app.git

# 6. Sube todo
git branch -M main
git push -u origin main
```

**✅ LISTO - Código en GitHub**

---

## PASO 2: Deploy del Backend Flask (2 minutos)

### EN VERCEL.COM:

1. Ve a https://vercel.com/new
2. Conecta tu cuenta de GitHub (si no lo has hecho)
3. Click en "Import Project"
4. Busca y selecciona `ikigai-app`
5. **Configuración**:
   - Framework Preset: **Other**
   - Root Directory: **`./`** (raíz)

6. **Environment Variables** (Click en Add):
   ```
   SECRET_KEY = pega_aquí_un_string_aleatorio_largo
   FLASK_ENV = production
   ```

   **Para generar SECRET_KEY**, ejecuta en tu terminal:
   ```bash
   python3 -c "import secrets; print(secrets.token_hex(32))"
   ```
   Copia el resultado y pégalo como valor de SECRET_KEY.

   **OPCIONAL** (solo si quieres usar IA):
   ```
   OPENAI_API_KEY = tu_api_key_de_openai
   ```

7. Click **"Deploy"**
8. Espera 2-3 minutos ⏱️
9. **GUARDA LA URL** que te da Vercel (ej: `https://ikigai-app-abc123.vercel.app`)

**✅ LISTO - Backend en línea**

---

## PASO 3: Obtener Keys de Clerk (3 minutos)

### EN CLERK.COM:

1. Ve a https://dashboard.clerk.com
2. Si no tienes cuenta, créala (es gratis)
3. Crea una nueva aplicación:
   - Name: "Ikigai App"
   - Click "Create application"

4. **COPIA ESTAS DOS KEYS** (las necesitarás):
   - `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY` (empieza con `pk_test_...`)
   - `CLERK_SECRET_KEY` (empieza con `sk_test_...`)

5. **Configura las rutas** en Clerk:
   - Ve a **"Paths"** en el menú izquierdo
   - **After sign in redirect URL**: 
     ```
     https://TU-BACKEND-VERCEL.vercel.app/exercise
     ```
     (reemplaza con tu URL real del paso 2)
   
   - **After sign up redirect URL**: (la misma)
     ```
     https://TU-BACKEND-VERCEL.vercel.app/exercise
     ```

**✅ LISTO - Clerk configurado**

---

## PASO 4: Deploy del Frontend Next.js (2 minutos)

### DE VUELTA EN VERCEL.COM:

1. Ve a https://vercel.com/new OTRA VEZ
2. Import el MISMO repositorio `ikigai-app`
3. **Configuración** (DIFERENTE esta vez):
   - Framework Preset: **Next.js**
   - Root Directory: **`landing-page`** (importante!)

4. **Environment Variables**:
   ```
   NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY = pk_test_... (del paso 3)
   CLERK_SECRET_KEY = sk_test_... (del paso 3)
   NEXT_PUBLIC_FLASK_URL = https://tu-backend.vercel.app (del paso 2)
   ```

5. Click **"Deploy"**
6. Espera 1-2 minutos ⏱️

**✅ LISTO - Frontend en línea**

---

## 🎉 ¡TERMINASTE!

### Tus URLs finales:

```
🌐 Landing Page (compártela con el mundo):
https://ikigai-landing-abc123.vercel.app

🐍 Backend API:
https://ikigai-app-abc123.vercel.app

📊 Dashboard de Vercel:
https://vercel.com/dashboard
```

### Prueba el flujo completo:

1. ✅ Abre tu landing page
2. ✅ Click en "Desbloquea tus Superpoderes"
3. ✅ Regístrate con Clerk
4. ✅ Deberías ir al ejercicio de Flask
5. ✅ Completa el ejercicio
6. ✅ Ve tus resultados
7. ✅ Descarga el PDF

---

## 🔄 Para actualizar después:

```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

Vercel detectará automáticamente los cambios y re-deployará. 🎉

---

## 🆘 ¿Problemas?

### "Command failed: git push"
- Ejecuta primero:
  ```bash
  git config user.name "Tu Nombre"
  git config user.email "tu@email.com"
  ```

### "Repository not found"
- Verifica que la URL de GitHub sea correcta
- Asegúrate de estar logueado en GitHub

### "Build failed" en Vercel
- Revisa los logs en Vercel
- Verifica que todas las variables de entorno estén configuradas
- Re-deploy después de corregir

### Landing page no redirige al ejercicio
- Verifica que `NEXT_PUBLIC_FLASK_URL` tenga la URL correcta del backend
- Asegúrate de que Clerk tenga las rutas configuradas correctamente

---

## 📝 Checklist Final

- [ ] Código en GitHub
- [ ] Backend deployado (Flask)
- [ ] Frontend deployado (Next.js)
- [ ] Clerk configurado con las URLs de producción
- [ ] Variables de entorno configuradas
- [ ] Flujo completo probado

---

**¿Todo listo? ¡Comparte tu landing page con el mundo! 🌍✨**

Cualquier problema, revisa el archivo `DEPLOYMENT.md` para más detalles.


