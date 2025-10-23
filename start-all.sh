#!/bin/bash

# Script para iniciar ambos servidores (Landing Page + Flask App)

echo "🚀 Iniciando Ikigai - Landing Page + App"
echo ""

# Colores para la terminal
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Función para manejar Ctrl+C
cleanup() {
    echo ""
    echo "🛑 Deteniendo servidores..."
    kill $NEXT_PID $FLASK_PID 2>/dev/null
    exit 0
}

trap cleanup SIGINT SIGTERM

# Directorio base
BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Iniciar Next.js (Landing Page)
echo -e "${CYAN}📄 Iniciando Landing Page (Next.js)...${NC}"
cd "$BASE_DIR/landing-page"
npm run dev > /tmp/ikigai-nextjs.log 2>&1 &
NEXT_PID=$!
echo -e "${GREEN}✓ Landing Page corriendo en http://localhost:3000${NC}"
echo ""

# Esperar 3 segundos
sleep 3

# Iniciar Flask (App)
echo -e "${CYAN}⚡ Iniciando App Flask...${NC}"
cd "$BASE_DIR"
python3 -m flask run > /tmp/ikigai-flask.log 2>&1 &
FLASK_PID=$!
echo -e "${GREEN}✓ App Flask corriendo en http://localhost:5000${NC}"
echo ""

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${BLUE}🌊 Ikigai está listo!${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo -e "${CYAN}Landing Page:${NC} http://localhost:3000"
echo -e "${CYAN}App Flask:${NC}    http://localhost:5000"
echo ""
echo "Presiona Ctrl+C para detener ambos servidores"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📋 Logs guardados en:"
echo "  - /tmp/ikigai-nextjs.log"
echo "  - /tmp/ikigai-flask.log"
echo ""

# Mantener el script corriendo
wait

