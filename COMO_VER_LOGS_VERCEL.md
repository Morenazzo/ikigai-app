# 🔍 Cómo Ver Logs de Vercel para Diagnosticar el Error 500

## 📋 Cambios Realizados

He simplificado la configuración para hacerla más compatible con Vercel:

### ✅ Archivos Modificados:

1. **`requirements.txt`** - Eliminadas dependencias problemáticas:
   - ❌ Removido `psycopg2-binary` (causa problemas en Vercel)
   - ❌ Removido `httpx` (no necesario)
   - ❌ Removido `pytz` (no necesario)
   - ✅ Mantenido solo lo esencial

2. **`vercel.json`** - Simplificado al mínimo:
   ```json
   {
     "version": 2,
     "builds": [{"src": "api/index.py", "use": "@vercel/python"}],
     "routes": [{"src": "/(.*)", "dest": "/api/index"}]
   }
   ```

3. **`api/index.py`** - Agregado mejor logging de errores

4. **`app.py`** - Forzar SQLite en Vercel (más confiable que PostgreSQL)

5. **Nuevos archivos:**
   - `.vercelignore` - Excluir archivos innecesarios
   - `runtime.txt` - Especificar Python 3.9
   - `/health` endpoint - Para diagnóstico

## 🚀 Pasos para Desplegar y Diagnosticar

### 1. Commit y Push de los Cambios

```bash
cd "/Users/edwinmoreno/Documents/Surfing D/Código/Ikigai"

# Ver los cambios
git status

# Agregar todos los archivos modificados
git add .

# Commit
git commit -m "Fix: Simplificar deps y config para Vercel - eliminar psycopg2"

# Push
git push origin main
```

### 2. Esperar el Deploy (2-3 minutos)

Ve a: https://vercel.com/dashboard

Verás:
- 🟡 **Building** → Compilando
- 🟢 **Ready** → Listo (si sale bien)
- 🔴 **Error** → Falló

### 3. Ver los Logs del Build

**En Vercel Dashboard:**

```
1. Click en tu proyecto
2. Click en "Deployments"
3. Click en el deployment más reciente (el de arriba)
4. Click en "Building" (la pestaña)
5. Busca errores en color rojo
```

**Busca estos errores comunes:**

```
❌ "ModuleNotFoundError: No module named 'X'"
   → Falta una dependencia en requirements.txt

❌ "ImportError: cannot import name 'X'"
   → Problema con imports

❌ "SyntaxError"
   → Error de sintaxis en el código

❌ "psycopg2.OperationalError"
   → Problema con PostgreSQL (ya lo removimos)
```

### 4. Ver los Runtime Logs (MUY IMPORTANTE)

**Para ver qué pasa cuando la función corre:**

```
1. En Vercel Dashboard → Tu proyecto
2. Click en "Logs" (en el menú izquierdo)
   O
   Click en "Functions" → "api/index" → "View Logs"

3. Intenta acceder a tu app (para generar logs)

4. Busca en los logs:
   - "❌ ERROR importing app:" → Error al importar
   - "Traceback" → Stack trace de Python
   - "Exception" → Excepciones
   - Cualquier mensaje en rojo
```

### 5. Prueba el Health Check

Una vez desplegado, visita:

```
https://tu-proyecto.vercel.app/health
```

Deberías ver algo como:
```json
{
  "status": "ok",
  "python_version": "3.9.x",
  "database": "connected",
  "vercel_env": "production",
  "modules": {
    "flask": "ok",
    "jwt": "ok",
    ...
  }
}
```

Si ves un **500 error** aquí también, entonces el problema es en la inicialización de la app.

### 6. Probar Rutas Específicas

```bash
# Health check (debe funcionar siempre)
curl https://tu-proyecto.vercel.app/health

# Exercise page (si health funciona)
curl https://tu-proyecto.vercel.app/exercise

# Results (si health funciona)
curl https://tu-proyecto.vercel.app/results
```

## 🔧 Cómo Interpretar los Logs

### Tipo 1: Error en Build Time

```
Error: Command "pip install -r requirements.txt" exited with 1
```

**Solución:** Una dependencia no se puede instalar
- Revisa `requirements.txt`
- Prueba localmente: `pip install -r requirements.txt`

### Tipo 2: Error en Import

```
❌ ERROR importing app: No module named 'jwt'
```

**Solución:** Falta dependencia
- Ya agregamos `PyJWT==2.8.0` en requirements.txt
- Verifica que esté en el archivo

### Tipo 3: Error en Runtime (Database)

```
Database error: unable to open database file
```

**Solución:** Problema con SQLite en /tmp
- Ya lo manejamos con try-catch
- La app debería funcionar sin DB

### Tipo 4: Error de Timeout

```
Task timed out after 10.00 seconds
```

**Solución:** La función tarda demasiado
- Ya removimos las llamadas API bloqueantes a Clerk
- Timeout ahora es solo para decode JWT (instantáneo)

## 📊 Dashboard de Vercel - Dónde Ver Cada Cosa

```
Vercel Dashboard
├── Overview
│   └── Ver estado general del proyecto
│
├── Deployments
│   ├── Lista de todos los deploys
│   ├── Click en uno → Ver detalles
│   │   ├── Building → Logs de compilación
│   │   ├── Functions → Logs de ejecución
│   │   └── Source → Ver el código desplegado
│   └── "···" menu → Redeploy / View Logs
│
├── Logs
│   ├── Real-time logs de todas las funciones
│   └── Filtrar por severidad: Error, Warning, Info
│
├── Functions
│   └── api/index
│       ├── Ver invocaciones
│       ├── Ver errores
│       └── View Logs → Logs específicos de esta función
│
└── Settings
    ├── Environment Variables (verifica aquí tus secrets)
    └── General → Clear Build Cache (si algo está raro)
```

## 🎯 Checklist de Verificación

Antes de pedir ayuda, verifica:

- [ ] El deploy terminó exitosamente (🟢 Ready)
- [ ] Las variables de entorno están configuradas:
  - `CLERK_SECRET_KEY`
  - `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`
  - `SECRET_KEY`
- [ ] `/health` endpoint responde (aunque sea con error, debe responder algo)
- [ ] Revisaste los logs de Build (pestaña "Building")
- [ ] Revisaste los logs de Runtime (pestaña "Functions" → "View Logs")
- [ ] Intentaste acceder a la página para generar logs

## 📝 Información que Necesito

Si sigues viendo el error 500, **copia y pégame:**

### A. De los Build Logs:
```
[COPY AQUÍ los últimos 20-30 líneas del build log]
```

### B. De los Runtime Logs (lo más importante):
```
[COPY AQUÍ cualquier error que veas cuando accedes a la página]

Especialmente busca:
- "❌ ERROR"
- "Traceback"
- "Exception"
- Cualquier línea en rojo
```

### C. El URL exacto que estás visitando:
```
https://tu-proyecto.vercel.app/ruta-exacta
```

### D. La respuesta del /health endpoint:
```
https://tu-proyecto.vercel.app/health
```

## 🔄 Si Nada Funciona: Reset Completo

```bash
# En Vercel Dashboard:
1. Settings → General → Clear Build Cache
2. Deployments → Latest → ··· → Redeploy

# O con CLI:
vercel --prod --force
```

## 🆘 Comandos Útiles de Vercel CLI

```bash
# Ver logs en tiempo real
vercel logs --follow

# Ver logs de producción
vercel logs production

# Ver logs con errores solamente
vercel logs --output errors

# Deploy forzado (limpia cache)
vercel --prod --force
```

---

**IMPORTANTE:** Los logs de Vercel son **CRUCIALES** para saber qué está fallando. Sin ver los logs, estamos a ciegas.

Por favor:
1. ✅ Haz commit y push de estos cambios
2. ✅ Espera a que el deploy termine
3. ✅ Ve al dashboard de Vercel
4. ✅ Copia los logs de Runtime (Functions → View Logs)
5. ✅ Pégalos aquí para que pueda ver el error exacto


