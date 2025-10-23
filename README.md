# 🎯 Discover Your Ikigai - Interactive Web App

An immersive, gamified web application to help people discover their Ikigai (生き甲斐) - their reason for being. Built with Flask backend, Next.js landing page, Clerk authentication, and beautiful UI with community impact tracking.

## 🌟 **NUEVO**: Ahora con Landing Page Profesional

Este proyecto incluye:
- 🎨 **Landing Page Next.js**: Diseño moderno con Tailwind CSS
- 🔐 **Autenticación con Clerk**: Sistema de registro/login profesional
- 🌍 **Multiidioma**: Español e Inglés
- 🚀 **Listo para Producción**: Deploy en Vercel con un click

📖 **[VER GUÍA DE DEPLOYMENT →](QUICKSTART_DEPLOYMENT.md)**

## ✨ Features

### Backend (Flask)
- **🎮 Gamified Experience**: Interactive, timed exercises with progress tracking
- **⏱️ Smart Timers**: Countdown timers for each reflection phase (5-2 minutes)
- **🎨 Modern UI/UX**: Beautiful design using Surfing Digital's brand colors
- **📊 Progress Tracking**: Visual progress bar and step indicators
- **💾 Data Persistence**: All responses saved to database
- **🌍 Community Impact**: See how many people have discovered their Ikigai
- **📱 Responsive Design**: Works perfectly on all devices
- **🔄 Multi-step Flow**: 9-step guided journey through self-discovery
- **📄 PDF Export**: Download your complete Ikigai with visual diagram
- **🤖 AI Analysis**: Optional OpenAI integration for personalized insights

### Frontend (Next.js Landing Page)
- **🎯 Beautiful Landing**: Professional marketing page with animations
- **🔐 Clerk Auth**: Secure authentication system
- **🌍 Bilingual**: Switch between Spanish and English
- **⚡ Fast**: Optimized with Next.js 16 and Turbopack
- **🎨 Tailwind CSS**: Modern, responsive design
- **📱 Mobile-First**: Perfect on all screen sizes

## 🎨 Design System

The app uses Surfing Digital's color palette:
- Navy: `#001639`, `#003453`
- Teal: `#00586A`, `#0BB7B7`
- Blue: `#0056A0`, `#009FD5`
- Pink: `#ED4A6D`
- Purple: `#9D80B9`
- Accent colors for different sections

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js 18+ and npm
- Git

### Local Development

#### Backend (Flask)

1. **Navigate to the project root**
   ```bash
   cd "/Users/edwinmoreno/Documents/Surfing D/Código/Ikigai"
   ```

2. **Install Python dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Start Flask server** (puerto 5001 para evitar conflicto con AirPlay)
   ```bash
   python3 -m flask run --port 5001
   ```

4. **Backend running at**: `http://localhost:5001`

#### Frontend (Next.js Landing Page)

1. **Navigate to landing page**
   ```bash
   cd landing-page
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Configure environment variables**
   - Copia `env.example.txt` como `.env.local`
   - Añade tus Clerk API keys desde https://dashboard.clerk.com

4. **Start development server**
   ```bash
   npm run dev
   ```

5. **Landing page running at**: `http://localhost:3000`

### 🚀 Quick Start Both Apps

Usa el script incluido:
```bash
./start-all.sh
```

## 📦 Deployment to Production

### 🎯 OPCIÓN FÁCIL: Usa la Guía Rápida

```bash
cat QUICKSTART_DEPLOYMENT.md
```

O lee la guía completa:
```bash
cat DEPLOYMENT.md
```

### Resumen:
1. Sube a GitHub
2. Deploy Backend (Flask) en Vercel
3. Deploy Frontend (Next.js) en Vercel
4. Configura variables de entorno
5. ¡Listo! 🎉

**Tiempo estimado**: 10-15 minutos

## 📖 User Journey

### The 9-Step Discovery Process

1. **What You Love** (5 minutes) - List up to 10 things you love doing
2. **What You're Good At** (3 minutes) - Identify up to 10 skills/talents
3. **What You Can Be Paid For** (3 minutes) - List up to 10 monetizable skills
4. **What The World Needs** (3 minutes) - Note up to 10 problems you care about
5. **Your Passion** (2 minutes) - Find overlaps between love + good at (up to 5)
6. **Your Mission** (2 minutes) - Find overlaps between love + world needs (up to 5)
7. **Your Vocation** (2 minutes) - Find overlaps between world needs + paid for (up to 5)
8. **Your Profession** (2 minutes) - Find overlaps between good at + paid for (up to 5)
9. **Your Ikigai** (3 minutes) - Synthesize 2-5 words that capture your essence

## 🗄️ Project Structure

```
Ikigai/
├── app.py                    # Main Flask application
├── helpers.py                # Helper functions
├── project.db                # SQLite database (local)
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel deployment config
├── env.example.txt          # Environment variables template
├── README.md                # This file
├── DEPLOYMENT.md            # Full deployment guide
├── QUICKSTART_DEPLOYMENT.md # Quick deployment guide (10 min)
├── start-all.sh             # Script to run both apps
├── static/
│   ├── styles.css           # Surfing Digital design system
│   ├── ikigai.js            # Frontend JavaScript
│   ├── intro.mp3            # Audio assets
│   └── outro.wav
├── templates/               # Flask templates
│   ├── about.html          # Introduction to Ikigai
│   ├── exercise.html       # Main interactive exercise
│   ├── results.html        # Results with PDF download
│   ├── impact.html         # Community statistics
│   ├── share.html          # Social sharing
│   ├── thanks.html         # Completion page
│   └── layout.html         # Base template
└── landing-page/           # Next.js landing page
    ├── app/
    │   ├── page.tsx        # Landing page
    │   ├── layout.tsx      # Root layout with Clerk
    │   ├── globals.css     # Global styles
    │   ├── sign-in/        # Clerk sign-in page
    │   ├── sign-up/        # Clerk sign-up page
    │   └── start-exercise/ # Redirect handler
    ├── components/
    │   ├── Hero.tsx        # Hero section
    │   ├── Features.tsx    # Features showcase
    │   ├── HowItWorks.tsx  # Process explanation
    │   ├── CTA.tsx         # Call to action
    │   └── LanguageSelector.tsx
    ├── contexts/
    │   └── LanguageContext.tsx
    ├── lib/
    │   └── translations.ts  # ES/EN translations
    ├── middleware.ts        # Clerk authentication
    ├── package.json
    ├── tailwind.config.ts
    └── next.config.mjs
```

## 🗃️ Database Schema

### `ikigai_responses` table

```sql
CREATE TABLE ikigai_responses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    love TEXT,          -- What you love (comma-separated)
    good TEXT,          -- What you're good at
    paid TEXT,          -- What you can be paid for
    needs TEXT,         -- What the world needs
    passion TEXT,       -- Passion intersections
    mission TEXT,       -- Mission intersections
    vocation TEXT,      -- Vocation intersections
    ikigai TEXT,        -- Final Ikigai statement
    timestamp INTEGER DEFAULT CURRENT_TIMESTAMP
);
```

## 🎯 Key Features Explained

### Interactive Timers
- Each step has a countdown timer
- Visual warnings when time is running low
- Auto-advance when time expires (optional continue)

### Dynamic Input System
- Start with 1 input field
- Add more inputs as needed (up to limit)
- Smooth animations for new inputs
- Color-coded by category

### Progress Tracking
- Visual progress bar at top
- Step indicator (Step X of 9)
- Smooth transitions between steps

### Data Collection
- All inputs stored as JSON arrays
- Converted to comma-separated strings for database
- Preserved for display in results

## 🔧 Tech Stack

### Backend
- **Flask** 3.0.0 - Python web framework
- **SQLite** / **PostgreSQL** - Database
- **CS50 Library** - Database helpers
- **OpenAI API** - AI analysis (optional)
- **html2canvas + jsPDF** - PDF generation

### Frontend
- **Next.js** 16.0.0 - React framework
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Clerk** - Authentication
- **React Context** - State management

### Deployment
- **Vercel** - Hosting (Backend + Frontend)
- **GitHub** - Version control
- **PostgreSQL** - Production database (recommended)

## 🔐 Environment Variables

### Backend (.env)
```bash
OPENAI_API_KEY=sk-...           # Optional for AI features
SECRET_KEY=your-secret-key       # For Flask sessions
FLASK_ENV=production            # Production mode
DATABASE_URL=postgresql://...   # Optional for PostgreSQL
```

### Frontend (landing-page/.env.local)
```bash
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
NEXT_PUBLIC_FLASK_URL=https://your-backend.vercel.app
```

Ver `env.example.txt` para más detalles.

## ✅ Recent Updates

- [x] Landing page con Next.js y Tailwind CSS
- [x] Autenticación con Clerk
- [x] Soporte multiidioma (ES/EN)
- [x] PDF export con diagrama visual
- [x] AI analysis con OpenAI
- [x] Deployment guides para Vercel
- [x] Mejoras en visualización de resultados
- [x] Sistema de listas mejorado

## 🔮 Future Enhancements

- [ ] Email results to users
- [ ] Progress saving (resume later)
- [ ] Analytics dashboard
- [ ] Social sharing with custom images
- [ ] Guided meditation/reflection audio
- [ ] Mobile app version
- [ ] Community features
- [ ] Ikigai coach AI assistant

## 🤝 Contributing

This project was created as part of CS50 and enhanced with modern UX/UI principles. Contributions are welcome!

## 📝 License

This project is for educational purposes. Feel free to use and modify.

## 🙏 Acknowledgments

- **CS50 Harvard** - Original inspiration
- **Surfing Digital** - Design system and brand colors
- **Ikigai Philosophy** - Japanese concept of purpose
- **Community** - All users who discover their purpose

## 📧 Contact

For questions or feedback about this project, please reach out through the repository.

---

**Made with ❤️ for those seeking their purpose** | *生き甲斐を見つけよう*
# Deployment optimizado para Vercel
