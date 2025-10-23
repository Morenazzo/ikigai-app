# 🤖 Configuración de IA para Ikigai

Este documento explica cómo configurar las funciones de Inteligencia Artificial en tu aplicación Ikigai.

## 🔑 Obtener tu API Key de OpenAI

1. Ve a [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Inicia sesión o crea una cuenta
3. Click en "Create new secret key"
4. Copia tu API key (empieza con `sk-...`)
5. ⚠️ **IMPORTANTE**: Guarda esta key en un lugar seguro, no podrás verla de nuevo

## ⚙️ Configurar la API Key en tu proyecto

### Opción 1: Usando archivo .env (Recomendado)

1. Abre el archivo `.env` en el directorio del proyecto
2. Reemplaza `your-openai-api-key-here` con tu API key:

```bash
OPENAI_API_KEY=sk-tu-api-key-aqui
```

3. Guarda el archivo
4. Reinicia el servidor Flask

### Opción 2: Variable de entorno del sistema

```bash
export OPENAI_API_KEY="sk-tu-api-key-aqui"
```

## ✨ Funciones de IA Disponibles

### 1. Sugerencias en Pasos de Intersección (Pasos 5-8)

**Ubicación**: Pasos de Pasión, Misión, Vocación y Profesión

**Función**: Botón "✨ Obtener Sugerencias con IA"

**Qué hace**: Analiza tus respuestas de las categorías base y sugiere elementos que se repiten o complementan.

**Control del usuario**: Las sugerencias se llenan automáticamente pero SIEMPRE puedes editarlas o ignorarlas.

### 2. Sugerencias de Ikigai (Paso 9)

**Ubicación**: Paso final de definición del Ikigai

**Función**: Botón "✨ Sugerencias de Ikigai con IA"

**Qué hace**: Sintetiza todas tus respuestas anteriores en 2-5 palabras clave poderosas que capturan tu propósito.

**Control del usuario**: Puedes modificar las palabras sugeridas completamente.

### 3. Análisis Completo en Resultados

**Ubicación**: Página de Resultados

**Función**: Botón "✨ Obtener Análisis Completo con IA"

**Qué hace**: 
- Valida tu Ikigai descubierto
- Identifica tus fortalezas clave
- Señala posibles desafíos
- Proporciona 3 pasos concretos siguientes
- Mensaje inspirador personalizado

### 4. Preguntas a la IA

**Ubicación**: Página de Resultados (debajo del análisis)

**Función**: Campo de texto "💬 Pregúntale a la IA sobre tu Ikigai"

**Qué hace**: Responde cualquier pregunta específica sobre tu Ikigai usando todo tu contexto.

**Ejemplos de preguntas**:
- "¿Cómo puedo empezar a vivir mi Ikigai?"
- "¿Qué carreras se alinean con mi Ikigai?"
- "¿Cómo puedo monetizar mi Ikigai?"
- "¿Qué habilidades debería desarrollar?"

## 💰 Costos

- **Modelo usado**: GPT-4o-mini
- **Costo aproximado por sugerencia**: $0.001 - $0.003 USD
- **Costo aproximado por análisis completo**: $0.005 - $0.01 USD
- **Total por usuario completo**: ~$0.05 USD

Los costos son muy bajos. Con $5 USD puedes hacer aproximadamente 100 análisis completos.

## 🔒 Seguridad

1. ✅ El archivo `.env` está en `.gitignore` - tu API key NO se sube a Git
2. ✅ La API key se valida en el backend - no se expone al frontend
3. ✅ Si no hay API key, las funciones de IA simplemente se deshabilitan
4. ⚠️ **NUNCA** compartas tu API key públicamente

## 🧪 Probar sin API Key

Si quieres probar la aplicación sin IA:
- La aplicación funciona completamente sin configurar OpenAI
- Los botones de IA simplemente no aparecerán o mostrarán un mensaje
- Todas las demás funciones siguen operando normalmente

## 🐛 Solución de Problemas

### "AI features are not enabled"
- Verifica que tu API key esté correctamente en `.env`
- Asegúrate que no tenga espacios adicionales
- Reinicia el servidor Flask

### "Failed to generate suggestions"
- Verifica que tengas créditos en tu cuenta de OpenAI
- Revisa los logs del servidor para más detalles
- Intenta de nuevo - puede ser un error temporal

### "Rate limit exceeded"
- OpenAI tiene límites de requests por minuto
- Espera unos segundos e intenta de nuevo
- Considera actualizar tu plan en OpenAI

## 📊 Monitoreo de Uso

Puedes ver tu uso de API en:
[https://platform.openai.com/usage](https://platform.openai.com/usage)

## 🎯 Mejores Prácticas

1. **Usa las sugerencias como inspiración**: La IA es muy buena, pero TÚ conoces mejor tu propósito
2. **Edita libremente**: Todas las sugerencias son editables
3. **Haz preguntas específicas**: Mientras más específica la pregunta, mejor la respuesta
4. **Itera**: Puedes pedir análisis múltiples veces y hacer varias preguntas

## 📝 Notas Técnicas

- **Temperatura de IA**: 0.7-0.8 (balance entre creatividad y coherencia)
- **Tokens máximos**: 150-1000 dependiendo de la función
- **Timeout**: 30 segundos por request
- **Reintentos**: No automáticos - el usuario decide si reintentar

---

¿Preguntas? ¿Sugerencias? ¡Disfruta descubriendo tu Ikigai con el poder de la IA! 🚀✨


