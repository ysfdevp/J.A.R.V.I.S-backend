# 🤖 Jarvis Web — AI Assistant with Glassmorphic UI

A modern web-based AI assistant built with **React**, **FastAPI**, and **Glassmorphism UI** with smooth animations.

![Architecture](https://img.shields.io/badge/React-19-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green) ![Vite](https://img.shields.io/badge/Vite-8+-purple) ![Vercel](https://img.shields.io/badge/Deploy-Vercel-black)

## 🎯 What's Inside

- **Frontend**: React + Vite + Framer Motion (hosted on Vercel)
- **Backend**: Python FastAPI + Uvicorn (hosted on Render/Railway/Fly.io)
- **Tools**: Web search, weather, file management, code execution, and more
- **UI**: Glassmorphism design with animated chat interface

## 🚀 Quick Start

### **Local Development**

1. **Backend** (Terminal 1):
   ```bash
   cd backend
   python -m uvicorn app:app --reload --port 8000
   ```

2. **Frontend** (Terminal 2):
   ```bash
   cd frontend
   npm run dev
   ```

3. Open `http://localhost:5173` in your browser

### **Deploy to Vercel**

See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) for step-by-step instructions to deploy:
- Backend to Render/Railway/Fly.io
- Frontend to Vercel

## 📁 Project Structure

```
JUST A RATHER VERY INTELLIGENT SYSTEM/
├── backend/                  # Python FastAPI server
│   ├── app.py               # Main API with tool endpoints
│   ├── requirements.txt      # Python dependencies
│   └── vercel.json          # Vercel config
├── frontend/                 # React + Vite web UI
│   ├── src/
│   │   ├── App.jsx          # Main app with chat interface
│   │   ├── App.css          # Glassmorphism styles
│   │   └── main.jsx         # React entry point
│   ├── .env                 # Local API URL
│   ├── .env.production      # Production API URL
│   ├── vercel.json          # Vercel deployment config
│   └── package.json
├── actions/                  # Existing AI action modules
├── agent/                    # Agent logic & task queues
├── config/                   # API keys configuration
├── core/                     # System prompts
├── memory/                   # Memory management
├── main.py                   # Original Jarvis CLI
├── DEPLOYMENT_GUIDE.md       # Full deployment instructions
└── README.md                 # This file
```

## 🛠️ Available Tools

Access these via the web UI:

- **Web Search** — Search the web using Gemini + DuckDuckGo
- **Weather Report** — Get real-time weather for any city
- **Open App** — Launch applications
- **Browser Control** — Automate web browsing
- **File Controller** — Manage files and folders
- **Computer Settings** — Control volume, brightness, etc.
- *And many more...*

## 🎨 UI Features

- **Glassmorphism Design**: Frosted glass effect with backdrop blur
- **Smooth Animations**: Framer Motion for message transitions
- **Responsive Layout**: Works on desktop, tablet, mobile
- **Dark Theme**: Eye-friendly dark mode with accent colors
- **Tool Selector**: Choose which action to perform

## 🔧 Configuration

### Backend API URL
- **Local**: `http://localhost:8000` (in [.env](frontend/.env))
- **Production**: Set in [.env.production](frontend/.env.production) and Vercel env vars

### API Keys
Add your API keys to `config/api_keys.json`:
```json
{
  "gemini_api_key": "your-google-gemini-api-key"
}
```

## 🌍 API Endpoints

- `GET /` — Health check
- `POST /api/tool` — Call an action tool

### Example Request:
```bash
curl -X POST http://localhost:8000/api/tool \
  -H "Content-Type: application/json" \
  -d '{"name": "web_search", "parameters": {"query": "python programming"}}'
```

## 📝 Dependencies

### Backend
- `fastapi` — Web framework
- `uvicorn` — ASGI server
- `pydantic` — Data validation
- (+ all existing Jarvis dependencies)

### Frontend
- `react` — UI library
- `vite` — Build tool
- `framer-motion` — Animations
- `axios` — HTTP client

## 📚 Deployment

**Full guide**: [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)

**Quick summary**:
1. Deploy backend to Render/Railway/Fly.io
2. Update frontend `.env.production` with backend URL
3. Deploy frontend to Vercel
4. Share your Vercel URL!

## 🐛 Troubleshooting

**Backend won't start?**
```bash
pip install -r backend/requirements.txt
python -m uvicorn app:app --reload --port 8000
```

**Frontend can't connect to backend?**
- Check backend is running: `curl http://localhost:8000/`
- Verify `.env` or `.env.production` has correct API URL
- Check browser console for CORS errors

**Tools not working?**
- Some tools are Windows-only (desktop_control, computer_control)
- Test with web_search or weather_report first

## 🎓 Learn More

- [Vite Docs](https://vitejs.dev/)
- [React Docs](https://react.dev/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Framer Motion](https://www.framer.com/motion/)
- [Vercel Deployment](https://vercel.com/docs)

## 📄 License

MIT

---

**Ready to deploy?** Follow [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md) 🚀
