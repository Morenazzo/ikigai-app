#!/bin/bash

# Script para desplegar los cambios a Vercel
# Uso: bash deploy-to-vercel.sh

set -e  # Exit on error

echo "🚀 DESPLEGANDO A VERCEL"
echo "======================="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo -e "${RED}❌ Error: No estás en el directorio correcto${NC}"
    echo "   Por favor corre este script desde: /Users/edwinmoreno/Documents/Surfing D/Código/Ikigai"
    exit 1
fi

echo -e "${YELLOW}📋 Verificando cambios...${NC}"
echo ""
git status --short
echo ""

# Ask for confirmation
echo -e "${YELLOW}¿Quieres hacer commit y push de estos cambios? (y/n)${NC}"
read -r response
if [[ ! "$response" =~ ^[Yy]$ ]]; then
    echo -e "${RED}❌ Deploy cancelado${NC}"
    exit 0
fi

echo ""
echo -e "${GREEN}✅ Agregando archivos...${NC}"
git add requirements.txt
git add app.py
git add api/index.py
git add vercel.json
git add .vercelignore
git add runtime.txt
git add COMO_VER_LOGS_VERCEL.md
git add SOLUCION_CRASH_VERCEL.md
git add DESPLEGAR_AHORA.md

echo -e "${GREEN}✅ Haciendo commit...${NC}"
git commit -m "Fix: Simplificar configuración para Vercel

- Eliminado psycopg2-binary (causa crashes)
- Eliminado httpx y pytz (innecesarios)
- Simplificado vercel.json
- Forzar SQLite en serverless
- Agregado endpoint /health para diagnóstico
- Agregado .vercelignore y runtime.txt
- Mejorado manejo de errores en inicialización"

echo -e "${GREEN}✅ Pushing a GitHub...${NC}"
git push origin main

echo ""
echo -e "${GREEN}✅ ¡DEPLOY INICIADO!${NC}"
echo ""
echo "🔍 Próximos pasos:"
echo ""
echo "1. Ve a: https://vercel.com/dashboard"
echo "2. Click en tu proyecto"
echo "3. Espera 2-3 minutos a que termine el build"
echo "4. Prueba el endpoint de health:"
echo "   https://TU-PROYECTO.vercel.app/health"
echo ""
echo "5. Si falla, ve los logs:"
echo "   Dashboard → Functions → api/index → View Logs"
echo ""
echo "6. Copia cualquier ERROR y pégalo en el chat"
echo ""
echo -e "${YELLOW}📖 Para más detalles, lee: COMO_VER_LOGS_VERCEL.md${NC}"
echo ""

